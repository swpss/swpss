import json

import datetime
from datetime import datetime as dt

from rest_framework.test import APITestCase

from data.models import Dataset
from users.models import Account
from machines.models import Machine, MachineDetail


class TestDataApp(APITestCase):
    def setUp(self):
        self.SUCCESS = '1'
        self.ERROR = '0'

        self.data = {
            'mid': '1',
            's': 1,
            'd': 2,
            'v': 230,
            'i': 22,
            'f': 52,
            'c': 5,
            'r': 5
        }

        self.user_data = {
                'password': 'filthys3cr3t',
                'confirm_password': 'filthys3cr3t',
                'first_name': 'Anvesh',
                'last_name': 'Kumar',
                'address': 'blah blah blah',
                'phone_number': '9032197570',
                'email': 'anvesh@gmail.com',
                'location': 'IN-TG',
                'has_smart_phone': True,
                'account_type': 3
        }

        self.user = Account.objects.create_user(
            self.user_data['email'],
            self.user_data['first_name'],
            self.user_data['address'],
            self.user_data['phone_number'],
            self.user_data['location'],
            self.user_data['account_type'],
            self.user_data['has_smart_phone'],
            self.user_data['password'],
            last_name=self.user_data['last_name']
        )

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

        self.machine_details = {
            'machine_model': None,
            'farmer_email': self.user_data['email'],
            'depth_during_installation': 120,
            'm_id': '1',
            'location': 'IN-TG',
            'serial_number': 1
        }

        self.base_url = 'http://localhost:8000/api/v1'
        self.insert_url = self.base_url + '/insert/?'
        self.data_url = self.base_url + '/data'
        self.range_url = self.base_url + '/range'

        self.machine = None
        self.model = None

    def tearDown(self):
        pass

    def create_model(self):
        self.model = MachineDetail.objects.create(
                firmware=self.model_details['firmware'],
                rating_watts=self.model_details['rating_watts'],
                rating_volts=self.model_details['rating_volts'],
                rpm=self.model_details['rpm'],
                rating_low_volts=self.model_details['rating_low_volts'],
                rating_high_volts=self.model_details['rating_high_volts'],
                make=self.model_details['make'],
                model=self.model_details['model'],
                year=self.model_details['year'],
                head_low=self.model_details['head_low'],
                head_high=self.model_details['head_high'],
                number_of_stages=self.model_details['number_of_stages'],
                pump_rating=self.model_details['pump_rating'],
                model_name=self.model_details['model_name'],
                optimal_depth=self.model_details['optimal_depth'],
                total_dynamic_head=self.model_details['total_dynamic_head'],
                horse_power=self.model_details['horse_power'],
                ref_head=self.model_details['ref_head'],
                ref_head_lpm=self.model_details['ref_head_lpm']
            )

    def create_machine(self):
        model = MachineDetail.objects.all()[0]
        self.machine = Machine.objects.create(
                model=model,
                sold_by=self.user,
                bought_by=self.user,
                m_id=self.machine_details['m_id'],
                depth_during_installation=self.machine_details['depth_during_installation'],
                location=self.machine_details['location'],
                serial_number=self.machine_details['serial_number']
                )

    def update_machine(self, new_m_id):
        machine = Machine.objects.get(
                m_id=self.machine_details['m_id']
                )

        machine.m_id= new_m_id
        machine.save()

        self.machine_details['m_id'] = new_m_id

    def delete_model(self):
        MachineDetail.objects.get(
                make=self.model_details['make']
                ).delete()

    def delete_machine(self):
        Machine.objects.get(
                m_id=self.machine_details['m_id']
                ).delete()

    def create_user_account_and_login(self):
        user_creds = {
            'username': '9032197570',
            'password': 'filthys3cr3t'
        }

        auth_url = self.base_url + '/auth/'
        response = self.client.post(auth_url, user_creds)
        token = response.data
        self.client.credentials(
                HTTP_AUTHORIZATION='Token ' + token['token'])

    def construct_url(self):
        url = self.insert_url + 'mid=' + self.data['mid']
        for k, v in self.data.iteritems():
            if k != 'mid':
                url += '&' + k + '=' + str(v)
        return url

    def insert_data(self):
        query_url = self.construct_url()

        response = self.client.get(query_url)
        self.assertEquals(self.SUCCESS, response.data)

        response = self.client.get(query_url)
        self.assertEquals(self.SUCCESS, response.data)

    def test_list_datasets(self):
        self.create_model()
        self.create_machine()

        self.insert_data()

        self.create_user_account_and_login()

        query_url = self.data_url + '/' + self.data['mid'] + '/'
        response = self.client.get(query_url)

        data = response.data['results']
        self.assertEquals(len(data), 2)

    def test_update_mid_and_check_data(self):
        """
        Checks if the data before updation of phone number is being,
        returned by the API.
        """
        self.create_model()
        self.create_machine()

        self.insert_data()

        new_imsi_number = '2'
        self.update_machine(new_m_id)
        self.data['mid'] = new_m_id

        self.insert_data()

        self.create_user_account_and_login()
        query_url = self.data_url + '/' + self.data['mid'] + '/'
        response = self.client.get(query_url)

        results = json.loads(response.content)

        self.assertEquals(results['count'], 4)

    def test_data_with_range_view(self):
        """
        This method is used to test DataWithRange view,
        by passing both the start and end dates.
        """

        self.create_model()
        self.create_machine()
        self.insert_data()

        date_literal = '%Y-%m-%d'
        start_date = dt.today()
        end_date = start_date + datetime.timedelta(days=1)

        self.create_user_account_and_login()
        query_url = self.range_url + '/' + self.data['mid'] + \
                    '/?s=' + dt.strftime(start_date, date_literal) + \
                    '&e=' + dt.strftime(end_date, date_literal)

        response = self.client.get(query_url)
        results = json.loads(response.content)

        self.assertEquals(len(results), 2)
