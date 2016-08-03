from rest_framework import permissions

from .models import * 

from users.helper import AccountTypes


class IsAllowedToAlter(permissions.BasePermission):
    """
    Enforces authorization on models(MachineDetails) i.e.
    MachineDetail can be added or updated by manufacturer only.
    """

    ACCOUNT_TYPES = AccountTypes.to_dict()

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return request.user.is_authenticated()

        if request.user.is_authenticated():
            return request.user.account_type == \
                    self.ACCOUNT_TYPES['MANUFACTURER']

    def has_object_permission(self, request, view, obj):
        return self.has_permission(request, view)


class IsAllowedToSell(permissions.BasePermission):
    """
    Enforces authorization on machines i.e.
    Machine can be added or updated by supplier only.
    """

    ACCOUNT_TYPES = AccountTypes.to_dict()

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return request.user.is_authenticated()

        if request.user.is_authenticated():
            return request.user.account_type == self.ACCOUNT_TYPES['SUPPLIER']

        return False

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return request.user.is_authenticated()

        if request.user.is_authenticated():
            if request.user.account_type == self.ACCOUNT_TYPES['SUPPLIER']:
                return obj.sold_by == request.user

        return False






# class IsAllowedToView(permissions.BasePermission):
#     Supplier = 0
#     Officer = [1,2]
#     Farmer = 3
#     Manufacturer = 4
#     Technician = 5
#     def has_permission(self, request, view, obj):
#         if request.method in permissions.SAFE_METHODS:
#             return request.user.is_authenticated()

#         if request.user.is_authenticated():
#             if  request.user.account_type == Supplier:
#                 return obj.sold_by == request.user
#             elif request.user.account_type in Officer:
#                 return obj.location == request.user.location
#             elif request.user.account_type in Farmer:
#                 return obj.bought_by = request.user
#             elif    
#         return False