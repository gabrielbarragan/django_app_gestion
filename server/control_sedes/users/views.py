from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.core.mail import send_mail
from django.conf import settings
import datetime

from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from rest_framework import mixins
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from users.models import Account
from organizations.models import Organization
from headquarters.models import HeadQuarter
from timetables.models import TimeTable, Days
from users.serializer import  AccountSerializer, UserSerializerAccess, UserSerializerResponse

# Create your views here.


class UserDetail(generics.RetrieveAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    

class CreateListUSer(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):

    serializer_class = AccountSerializer
    queryset = Account.objects.all()
    permission_classes = [IsAdminUser]

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        print(*args)
        return self.create(request, *args, **kwargs)
class UserAccess(APIView):
    """View for validate access in a headquarter"""
    serializer_class = UserSerializerAccess

    def post(self, request):
        # Recuperamos las credenciales y autenticamos al usuario
        email = request.data.get('email', None)
        password = request.data.get('password', None)   
        user = authenticate(email=email, password=password)
        headquarter_post = request.data.get('headquarter', None)
        headquarter_consult=HeadQuarter.objects.filter(pk=headquarter_post).values()
        headquarter_user = Account.objects.filter(email=email).values('headquarter')
        user_name = list(Account.objects.filter(email=email).values('first_name', 'last_name'))[0]
        user_name_str = user_name['first_name']+' '+user_name['last_name']
        
        timetable_user = list(Account.objects.filter(email = email).values_list('timetables',flat = True))
        organization_consultada = list(HeadQuarter.objects.filter(pk=headquarter_post).values_list('organization',flat=True))[0]
        admin_organization = list(Organization.objects.filter(pk=organization_consultada).values_list('admin_user',flat=True))[0]
        admin_email = list(Account.objects.filter(pk=admin_organization).values_list('email', flat=True))[0]
        
        
        time_now = datetime.datetime.now()

        encontrado= 0
        #validando si la sede corresponde a alguna de las sedes a las que el usuario tiene acceso
        for sede in headquarter_user:
            if int(headquarter_post) == int(sede['headquarter']):
                encontrado+=1

        #obteniendo el id del día actual
        day_now_id=list(Days.objects.filter(day=time_now.strftime("%A")).values_list('pk', flat = True))[0]
        auth_day=0
        
        #Validando cada uno de los horarios del usuario
        for timetable in timetable_user:

            #lista con los días que el usuario tiene permitido el ingreso
            day_list_id= [day for day in list(TimeTable.objects.filter(pk = int(timetable)).values_list('days', flat = True))]

            #obteniendo hora inicial y final del respectivo horario
            timetable_start=list(TimeTable.objects.filter(pk=int(timetable)).values_list('start_time', flat = True))[0]
            timetable_end=list(TimeTable.objects.filter(pk=int(timetable)).values_list('end_time', flat = True))[0]

            #validando que el día actual esté entre los días permitidos
            if day_now_id in day_list_id:

                #validando que la hora actual esté dentro de las horas permitidas
                if time_now.time() >= timetable_start and time_now.time() <= timetable_end:
                    auth_day+=1
        #transformando la información de la sede en un dict
        for sede in headquarter_consult:
            headquarter_consult = sede
        # validando requisitos de acceso(login, sede y horarios)
        if user and encontrado >= 1 and auth_day >=1 and headquarter_consult['state']=='On':
            login(request, user)

            data_response=[{
                'access':True,
                'headquarter':headquarter_consult
            }]
            return Response(UserSerializerResponse(data_response, many=True).data,
                status=status.HTTP_200_OK)

        # Si no es correcto devolvemos un error en la petición
        data_response=[{
            'access':False,
            'headquarter':headquarter_consult
        }]
        send_email(admin_email, user_name_str, headquarter_consult['name'])
        return Response(UserSerializerResponse(data_response, many=True).data,            
            status=status.HTTP_401_UNAUTHORIZED)

def send_email(admin_email, user_complete_name, sede):
    send_mail(
    'Intento de acceso fallido',
    f'{user_complete_name} ha intentado ingresar a la sede {sede} sin éxito',
    settings.EMAIL_HOST_USER,
    [admin_email],
    fail_silently=False,
    )
