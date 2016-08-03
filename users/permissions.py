from rest_framework import permissions


class IsAccountOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, account):
        if request.user:
            return request.user == account


# Role based registration (Example role is supplier He can register farmer only)
class IsAllowedToRegister(permissions.BasePermission):
    def has_permission(self, request, view):
        # Check helper(users/helper.py) module for reference.
        MANUFACTURER_USER_TYPE = 4
        SUPPLIER_USER_TYPE = 0
        FARMER_USER_TYPE = 3

        if request.user and request.user.is_authenticated():
            if int(request.data['account_type']) == FARMER_USER_TYPE:
                return request.user.account_type in [SUPPLIER_USER_TYPE, MANUFACTURER_USER_TYPE]
            else:
                return request.user.account_type == MANUFACTURER_USER_TYPE
        return False



