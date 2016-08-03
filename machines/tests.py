import json

from rest_framework import status
from rest_framework.test import APIClient
from rest_framework.test import APITestCase

from machines.models import MachineDetail, Machine
from machines.serializers import MachineSerializer, MachineDetailSerializer
from users.models import Account
from users.serializers import AccountSerializer


class Helper(APIClient):
    def __init__(self):
        self.model_details = {
            'firmware': '2.3.1',
            'rating_watts': 120,
            'rating_volts': 120,
            'rpm': 120,
            'rating_low_volts': 120,
            'rating_high_volts': 120,
            'make': 'hello',
            'model': 'one',
            'year': 2012,
            'head_low': 12,
            'head_high': 15,
            'number_of_stages': 3,
            'pump_rating': 12,
            'model_name': 'pump name',
            'optimal_depth': 120,
            'total_dynamic_head': 123,
            'horse_power': 3,
            'ref_head': 50,
            'ref_head_lpm': 160
          }

        self.machine_details = None

        """
        Used to save the response when new machine/model is created
        """
        self.response_model_details = None
        self.response_machine_details = None

        self.supplier_details = {
            'password': 'filthys3cr3t',
            'confirm_password': 'filthys3cr3t',
            'first_name': 'Anvesh',
            'last_name': 'Kumar',
            'address': 'blah blah blah',
            'phone_number': '9876543210',
            'email': 'supplier@gmail.com',
            'location': 'IN-TG',
            'has_smart_phone': True,
            'account_type': 0
        }

        self.supplier_login_details = {
            'username': self.supplier_details['phone_number'],
            'password': self.supplier_details['password']
        }

        self.farmer_details = {
            'password': 'filthys3cr3t',
            'confirm_password': 'filthys3cr3t',
            'first_name': 'Anvesh',
            'last_name': 'Kumar',
            'address': 'blah blah blah',
            'phone_number': '1234567890',
            'email': 'farmer@gmail.com',
            'location': 'IN-TG',
            'has_smart_phone': True,
            'account_type': 3
        }

        self.farmer_login_details = {
            'username': self.farmer_details['phone_number'],
            'password': self.farmer_details['password']
        }

        self.api_client = APIClient()
        self.base_url = '/api/v1'
        self.auth_url = self.base_url + '/auth/'
        self.users_url = self.base_url + '/users/'
        self.models_url = self.base_url + '/models/'
        self.machines_url = self.base_url + '/machines/'

    def create_user(self, user_details):
        created_user = Account.objects.create_user(
            user_details['email'],
            user_details['first_name'],
            user_details['address'],
            user_details['phone_number'],
            user_details['location'],
            user_details['account_type'],
            user_details['has_smart_phone'],
            user_details['password'],
            last_name=user_details['last_name']
        )

        return AccountSerializer(created_user)

    def login(self, login_details):
        response = self.api_client.post(
                self.auth_url,
                login_details
                )

        if response.status_code == status.HTTP_200_OK:
            json_response = json.loads(response.content)
            token = json_response['token']
            return token

        else:
            print 'Error with user %s login' % (login_details.username)
            print response.content

    def update_auth_header(self, token=None):
        if token is not None:
            self.api_client.credentials(HTTP_AUTHORIZATION='Token ' + token)
        else:
            self.api_client.credentials()

    def create_new_model(self, model_details):
        response = self.api_client.post(
                self.models_url,
                model_details
                )

        if response.status_code == status.HTTP_201_CREATED:
            self.response_model_details = json.loads(response.content)

        return response

    def create_new_machine(self, machine_details):
        response = self.api_client.post(
                self.machines_url,
                machine_details
                )

        if response.status_code == status.HTTP_201_CREATED:
            self.response_machine_details = json.loads(response.content)

        return response

    def delete_user(self, user_details):
        user = Account.objects.get(phone_number=user_details['phone_number'])
        user.delete()

    def delete_model(self, model_details):
        model = MachineDetail.objects.get(id=model_details['id'])
        model.delete()


class TestMachine(APITestCase):
    def setUp(self):
        self.helper = Helper()

        self.res_supplier_detail = self.helper.create_user(
                self.helper.supplier_details)
        self.res_farmer_detail = self.helper.create_user(
                self.helper.farmer_details)

        self.res_model = self.create_new_model_with_query(
                self.helper.model_details)
        self.res_model = self.res_model.data

        self.helper.machine_details = {
            'machine_model': self.res_model['id'],
            'farmer_phone_number': self.helper.farmer_details['phone_number'],
            'depth_during_installation': 120,
            'm_id': '1',
            'location': 'IN-TG',
            'serial_number': 1,
            'address': 'Hyderabad'
        }

        self.supplier_token = self.helper.login(
                self.helper.supplier_login_details)
        self.farmer_token = self.helper.login(
                self.helper.farmer_login_details)

    def tearDown(self):
        self.helper.delete_user(self.helper.supplier_details)
        self.helper.delete_user(self.helper.farmer_details)

        self.delete_model(self.helper.model_details)

    def create_new_model_with_query(self, model_details):
        created_model = MachineDetail.objects.create(
                firmware=model_details['firmware'],
                rating_watts=model_details['rating_watts'],
                rating_volts=model_details['rating_volts'],
                rpm=model_details['rpm'],
                rating_low_volts=model_details['rating_low_volts'],
                rating_high_volts=model_details['rating_high_volts'],
                make=model_details['make'],
                model=model_details['model'],
                year=model_details['year'],
                head_low=model_details['head_low'],
                head_high=model_details['head_high'],
                number_of_stages=model_details['number_of_stages'],
                pump_rating=model_details['pump_rating'],
                model_name=model_details['model_name'],
                optimal_depth=model_details['optimal_depth'],
                total_dynamic_head=model_details['total_dynamic_head'],
                horse_power=model_details['horse_power'],
                ref_head=model_details['ref_head'],
                ref_head_lpm=model_details['ref_head_lpm']
                )

        if created_model is None:
            print 'New model creation failed! (line 185)'

        return MachineDetailSerializer(created_model)

    def delete_model(self, model_details):
        model = MachineDetail.objects.get(make=model_details['make'])

        try:
            model.delete()
        except:
            print 'No method delete() in model (line 193)'

    def test_creating_machine_without_auth(self):
        response = self.helper.create_new_machine(self.helper.machine_details)
        self.assertEquals(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_creating_machine_with_auth(self):
        self.helper.update_auth_header(self.supplier_token)
        response = self.helper.create_new_machine(self.helper.machine_details)
        content = json.loads(response.content)
        self.assertIn('id', content)

    def test_updating_machine_without_auth(self):
        self.helper.update_auth_header(self.supplier_token)
        response = self.helper.create_new_machine(self.helper.machine_details)

        content = json.loads(response.content)
        content['m_id'] = '2222222222'

        self.helper.update_auth_header()  # reset client credentials

        response = self.helper.api_client.put(
                self.helper.machines_url + str(content['id']) + '/',
                data=content)
        self.assertEquals(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_updating_machine_with_auth(self):
        new_m_id = '2222222222'

        self.helper.update_auth_header(self.supplier_token)
        response = self.helper.create_new_machine(self.helper.machine_details)

        content = json.loads(response.content)
        content['m_id'] = new_m_id
        content['machine_model'] = content['model']['id']
        content.pop('model')
        content['farmer_phone_number'] = content['bought_by']['phone_number']
        content.pop('bought_by')
        content.pop('sold_by')

        response = self.helper.api_client.put(
                self.helper.machines_url + str(content['id']) + '/',
                data=json.dumps(content),
                content_type='application/json')
        content = json.loads(response.content)

        self.assertEquals(new_m_id, content['m_id'])

    def test_read_machine_without_auth(self):
        response = self.helper.api_client.get(
                self.helper.machines_url)
        self.assertEquals(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_read_machine_with_auth(self):
        self.helper.update_auth_header(self.supplier_token)
        self.helper.create_new_machine(self.helper.machine_details)
        response = self.helper.api_client.get(
                self.helper.machines_url
                )
        content = json.loads(response.content)
        self.assertEquals(content['count'], 1)


class TestMachineDetail(APITestCase):
    def setUp(self):
        self.helper = Helper()

        # Only manufacturer can create, update or delete
        # a model
        self.manufacturer_details = {
            'password': 'filthys3cr3t',
            'confirm_password': 'filthys3cr3t',
            'first_name': 'Anvesh',
            'last_name': 'Kumar',
            'address': 'blah blah blah',
            'phone_number': '9876543210',
            'email': 'manufacturer@gmail.com',
            'location': 'IN-TG',
            'has_smart_phone': True,
            'account_type': 4
        }

        self.manu_login_details = {
            'username': '9876543210',
            'password': 'filthys3cr3t'
        }

        self.res_manufacturer = self.helper.create_user(
                self.manufacturer_details
                )

        self.manufacturer_token = self.helper.login(
                self.manu_login_details
                )

    def tearDown(self):
        self.helper.delete_user(self.manufacturer_details)

    def test_creating_model_without_auth(self):
        response = self.helper.create_new_model(self.helper.model_details)
        self.assertEquals(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_creating_model_with_auth(self):
        self.helper.update_auth_header(self.manufacturer_token)
        response = self.helper.create_new_model(self.helper.model_details)
        content = json.loads(response.content)
        self.assertEquals(content['make'], self.helper.model_details['make'])

    def test_updating_model_without_auth(self):
        self.helper.update_auth_header(self.manufacturer_token)

        response = self.helper.create_new_model(self.helper.model_details)
        content = json.loads(response.content)

        # reset client credentials
        self.helper.update_auth_header()

        content['make'] = 'not hello'
        u_response = self.helper.api_client.put(
                self.helper.models_url + str(content['id']) + '/',
                data=content
                )

        self.assertEquals(u_response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_updating_model_with_auth(self):
        make = 'not hello'
        self.helper.update_auth_header(self.manufacturer_token)
        response = self.helper.create_new_model(self.helper.model_details)
        content = json.loads(response.content)

        content['make'] = make
        u_response = self.helper.api_client.put(
                self.helper.models_url + str(content['id']) + '/',
                data=content
                )

        u_content = json.loads(u_response.content)
        self.assertEquals(make, u_content['make'])

    def test_read_model_without_auth(self):
        response = self.helper.api_client.get(self.helper.models_url)
        self.assertEquals(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_read_model_with_auth(self):
        self.helper.update_auth_header(self.manufacturer_token)

        created_response = self.helper.create_new_model(
                self.helper.model_details)
        self.assertEquals(
                created_response.status_code,
                status.HTTP_201_CREATED)

        response = self.helper.api_client.get(self.helper.models_url)
        content = json.loads(response.content)

        self.assertEquals(len(content), 1)
