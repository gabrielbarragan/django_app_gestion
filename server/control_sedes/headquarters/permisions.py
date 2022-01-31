from rest_framework import permissions
from headquarters.models import HeadQuarter
from users.models import Account

   
class HeadQuarterPermission(permissions.BasePermission):
    """
    Permissions check for employees from hehadquarter.
    """

    def has_permission(self, request, view):
        headquarter = Account.objects.values_list('headquarter').get(username=request.user)
        for sede in headquarter:
            whitelisted = HeadQuarter.objects.filter(pk=sede).exists()
            if whitelisted:
                return whitelisted
        return not whitelisted