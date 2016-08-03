from rest_framework import permissions

from users.helper import AccountTypes


class DefaultPerms(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated()

    def has_object_permission(self, request, view, obj):
        return self.has_permission(request, view)


class ComplaintPerms(permissions.BasePermission):
    ACCOUNT_TYPES = AccountTypes.to_dict()

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return request.user.is_authenticated()

        if request.method == 'POST':
            return request.user.account_type in [
                    self.ACCOUNT_TYPES['FARMER'],
                    self.ACCOUNT_TYPES['SUPPLIER'],
                    self.ACCOUNT_TYPES['MANUFACTURER'],
                    self.ACCOUNT_TYPES['TECHNICIAN(CYBERMOTION)'],
                    self.ACCOUNT_TYPES['TECHNICIAN(CLIENT)'],
                    self.ACCOUNT_TYPES['TECHNICIAN(LOCATION)']
                    ]
        if request.method == 'PUT':
            return request.user.account_type in [
                    self.ACCOUNT_TYPES['TECHNICIAN(CYBERMOTION)'],
                    self.ACCOUNT_TYPES['TECHNICIAN(CLIENT)'],
                    self.ACCOUNT_TYPES['TECHNICIAN(LOCATION)']
                    ]

    def has_object_permission(self, request, view, obj):
        self.has_permission(request, view)
