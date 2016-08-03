from django.http import JsonResponse, HttpResponse
from django.db.models import Q
from rest_framework import viewsets, permissions, views, status
from rest_framework.response import Response
from users.helper import StatesOfIndia
from machines.models import Machine
from users.models import Account
from users.serializers import AccountSerializer
from users.permissions import IsAllowedToRegister, IsAccountOwner
from users.pagination import UserPagination

class AccountViewSet(viewsets.ModelViewSet):
    serializer_class = AccountSerializer
    pagination_class = UserPagination

    def get_queryset(self):
        SUPPLIER = 0
        OFFICERS = [1, 2]
        FARMER = 3
        MANUFACTURER = 4

        if not self.request.user.is_authenticated():
            return None
        elif self.request.user.account_type == SUPPLIER:
            sold_by = self.request.user
            ma_list = []
            machines  = Machine.objects.filter(sold_by = sold_by)
            for machine in machines:
                ma_list.append(machine.bought_by)
            queryset = ma_list    
        elif self.request.user.account_type == FARMER:
            queryset = Account.objects.filter(email=self.request.user.email)
        elif self.request.user.account_type in OFFICERS:
            queryset = Account.objects.filter(
                    location=self.request.user.location
                ).exclude(email=self.request.user.email)
        else:
            queryset = Account.objects.all()

        return queryset

    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return (permissions.IsAuthenticated(), )

        if self.request.method == 'POST':
            return (IsAllowedToRegister(), )

        if self.request.method == 'PUT':
            return (IsAccountOwner(),)

        return (
            permissions.IsAuthenticated(),
            IsAccountOwner(),
        )


class MyAccount(views.APIView):
    def get(self, request, format=None):
        if request.user.is_authenticated():
            myaccount = AccountSerializer(instance=request.user)
            return Response(data=myaccount.data)
        else:
            return Response(
                    data={
                        "detail": 'Authentication details were not provided.'},
                    status=status.HTTP_401_UNAUTHORIZED)

    def put(self, request, format=None):
        if request.user.is_authenticated():
            user = Account.objects.get(id=request.DATA['id'])

            password = request.DATA['password']
            confirm_password = request.DATA['confirm_password']

            user.first_name = request.DATA['first_name']
            user.last_name = request.DATA['last_name']
            user.email = request.DATA['email']
            user.phone_number = request.DATA['phone_number']
            user.location = request.DATA['location']
            user.address = request.DATA['address']
            user.has_smart_phone = request.DATA['has_smart_phone']

            if password and confirm_password and password == confirm_password:
                user.set_password(password)

            user.save()

            serialized = AccountSerializer(instance=user)

            return Response(data=serialized.data)

        else:
            return Response(
                    data={
                        "detail": 'Authentication details were not provided.'},
                    status=status.HTTP_401_UNAUTHORIZED)


class GetUserByEmail(views.APIView):
    def get(self, request, format=None):
        user = Account.objects.get(email=request.query_params['email'])
        serialized = AccountSerializer(instance=user)
        return Response(data=serialized.data)


class searchUser(views.APIView):
    def get(self, request, keyword, format=None):
        SUPPLIER = 0
        OFFICERS = [1, 2]
        FARMER = 3
        MANUFACTURER = 4
        keyword = str(keyword)

        if not self.request.user.is_authenticated():
            return None
        elif self.request.user.account_type == SUPPLIER:
            queryset = Account.objects.filter(
                    account_type=FARMER
                ).filter(location=self.request.user.location)
        elif self.request.user.account_type == FARMER:
            queryset = Account.objects.filter(email=self.request.user.email)
        elif self.request.user.account_type in OFFICERS:
            queryset = Account.objects.filter(
                    location=self.request.user.location
                ).exclude(email=self.request.user.email)
        else:
            queryset = Account.objects.all()

        users = queryset.filter(
                Q(first_name__contains=keyword) |
                Q(last_name__contains=keyword) |
                Q(email__contains=keyword)
            )

        serialized = AccountSerializer(users, many=True)

        return Response(data=serialized.data)
def clients(request):
    clients = Account.objects.filter(account_type=0)
    a = []
    for client in clients:
        b={
        "id":client.id,
        "name":client.first_name,
        "location":StatesOfIndia.STATES[client.location] 
        }
        a.append(b)
    return JsonResponse({"a":a})