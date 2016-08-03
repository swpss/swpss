import json

from rest_framework.test import APITestCase
from rest_framework import status
from users.models import Account
from users.serializers import AccountSerializer


class TestAccountModel(APITestCase):
    """
    Each test should be independent,
    if one test B depends on A, then do
    the following:

         def A():
           pass
         def B():
           pass
         def test_A_then_B():
           A()
           B()
    """
    def setUp(self):
        self.data = {
                'password': 'filthys3cr3t',
                'confirm_password': 'filthys3cr3t',
                'first_name': 'Anvesh',
                'last_name': 'Kumar',
                'address': 'blah blah blah',
                'phone_number': '9032197570',
                'email': 'anvesh@gmail.com',
                'location': 'IN-TG',
                'has_smart_phone': True,
                'account_type': 4
        }

        self.user = Account.objects.create_user(
            self.data['email'],
            self.data['first_name'],
            self.data['address'],
            self.data['phone_number'],
            self.data['location'],
            self.data['account_type'],
            self.data['has_smart_phone'],
            self.data['password'],
            last_name=self.data['last_name']
        )

        self.supplier_data = {
                'password': 'filthys3cr3t',
                'confirm_password': 'filthys3cr3t',
                'first_name': 'Supplier',
                'last_name': 'Reddy',
                'address': 'blah blah blah',
                'phone_number': '9132197570',
                'email': 'supplier@gmail.com',
                'location': 'IN-TG',
                'has_smart_phone': True,
                'account_type': 0
        }

        self.login_data = {
                "username": "9032197570",
                "password": "filthys3cr3t"
        }

        self.base_url = 'http://localhost:8000/'
        self.api_url = self.base_url + 'api/v1/'
        self.auth_url = self.api_url + 'auth/'
        self.users_url = self.api_url + 'users/'
        self.append_json_format = '.json'

    def tearDown(self):
        pass

    def user_login(self, login_data):
        # Returns a token of the given user(login_data)
        token_response = self.client.post(
                self.api_url + 'auth/',
                data=login_data
                )
        return json.loads(str(token_response.content))

    def update_client_credentials(self, token):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token['token'])

    def test_manufacturer_account_creation_with_model(self):
        self.assertIn(self.data['phone_number'], str(self.user))

    def test_serialization(self):
        data = self.data
        serialized = AccountSerializer(self.user)
        data.pop('password')
        data.pop('confirm_password')
        self.assertDictContainsSubset(data, serialized.data)

    def test_deserialization(self):
        data = self.data
        data['email'] = 'anveshj@gmail.com'
        data['phone_number'] = '8032197570'
        de_serialized = AccountSerializer(data=data)
        self.assertEqual(True, de_serialized.is_valid())

    def test_account_updation(self):
        data = self.data

        token = self.user_login(self.login_data)
        self.update_client_credentials(token)

        user_data_response = self.client.get(self.users_url)

        user_data = json.loads(user_data_response.content)
        user_data = user_data['results'][0]

        data['last_name'] = 'Arrabochu'

        update_response = self.client.put(
                self.users_url + str(user_data['id']) + '/',
                data=data
        )
        updated_data = json.loads(update_response.content)
        updated_data.pop('id')
        updated_data.pop('created_at')
        updated_data.pop('modified_at')

        self.assertDictContainsSubset(updated_data, data)

    def test_supplier_account_creation(self):
        data = self.supplier_data
        token = self.user_login(self.login_data)

        self.update_client_credentials(token)
        create_response = self.client.post(self.users_url, data=data)

        created_user = json.loads(str(create_response.content))
        created_user.pop('id')
        created_user.pop('created_at')
        created_user.pop('modified_at')

        self.assertDictContainsSubset(created_user, data)

    def test_supplier_creates_farmer_account(self):
        farmer_data = self.data

        farmer_data['email'] = 'farmer@gmail.com'
        farmer_data['phone_number'] = '9876543210'
        farmer_data['account_type'] = 3

        token = self.user_login(self.login_data)
        self.update_client_credentials(token)
        create_response = self.client.post(
                self.users_url,
                data=self.supplier_data
            )

        supplier_login_data = {
                "username": self.supplier_data['phone_number'],
                "password": self.supplier_data['password']
        }

        token = self.user_login(supplier_login_data)
        self.update_client_credentials(token)

        create_response = self.client.post(self.users_url, data=farmer_data)
        created_user = json.loads(str(create_response.content))

        created_user.pop('id')
        created_user.pop('created_at')
        created_user.pop('modified_at')
        self.assertDictContainsSubset(created_user, farmer_data)

    def test_user_profile(self):
        token = self.user_login(self.login_data)
        self.update_client_credentials(token)

        res_data = self.client.get(self.api_url + 'myaccount/')
        res_data = json.loads(res_data.content)

        res_data.pop('id')
        res_data.pop('created_at')
        res_data.pop('modified_at')

        self.assertDictContainsSubset(res_data, self.data)
