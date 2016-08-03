from django.db import models
from users.models import Account
from users.helper import StatesOfIndia


class MachineDetail(models.Model):

    con_model_no = models.CharField(max_length=15)
    con_hardware_version = models.CharField(max_length=15)
    con_firmware_version = models.CharField(max_length=15)
    con_enclosure_version = models.CharField(max_length=15)
    con_year = models.IntegerField()

    #controller Specs
    con_drive_capacity = models.IntegerField()
    con_open_circuit_voltage = models.FloatField()

    #mppt range
    con_mppt_min_volts = models.FloatField()
    con_mppt_max_volts = models.FloatField()
    con_max_input_current = models.FloatField()
    con_certifications = models.CharField(max_length=4, choices=(
                                            ('IPV5', 'IPV5'),
                                            ('TUV', 'TUV'),
                                            ('VEC', 'VEC'),
                                            ('UL', 'UL'),
                                            ), default='UL')

    #controller output
    con_output_voltage_range = models.CharField(max_length=10)
    con_max_output_current = models.FloatField()
    con_max_frequency = models.FloatField()

    #Pump Details
    p_model = models.CharField(max_length=15)
    p_make = models.CharField(max_length=15)
    p_year = models.IntegerField()
    p_rpm = models.FloatField()
    p_head_low = models.FloatField()
    p_head_high = models.FloatField()
    p_no_of_stages = models.FloatField()
    p_rated_voltage = models.FloatField()
    p_low_voltage = models.FloatField()
    p_rated_head = models.FloatField()
    p_max_dynamic_head = models.FloatField()
    p_outlet_diameter = models.FloatField()
    p_impeller = models.FloatField()
    p_material = models.FloatField()
    p_bee_rating = models.FloatField()

    # Motor details.
    
    horse_power = models.FloatField(default=5)
    pump_type = models.CharField(max_length=3, choices=(
                                            ('SMB', 'Submersible'),
                                            ), default='SMB')

    # Added later for LPM calculations
    ref_head = models.FloatField()
    ref_head_lpm = models.FloatField()

    def __unicode__(self):
        return self.p_make

    def get_firmare_details(self):
        return self.con_firmware_version


class Machine(models.Model):
    model = models.ForeignKey(MachineDetail, related_name='machine_detail')
    sold_by = models.ForeignKey(
            Account, blank=True,
            null=True, related_name='supplier')
    bought_by = models.ForeignKey(
            Account, blank=True,
            null=True, related_name='farmer')
    m_id = models.CharField(max_length=15, unique=True)
    latitude = models.DecimalField(
            max_digits=8, decimal_places=5,
            blank=True, null=True)
    longitude = models.DecimalField(
            max_digits=8, decimal_places=5,
            blank=True, null=True)
    location = models.CharField(
            max_length=5,
            choices=StatesOfIndia.get_state_names())
    depth_during_installation = models.FloatField(null=True)
    serial_number = models.IntegerField(unique=True)
    address = models.TextField(blank=True, null=True)

    date_of_installation = models.DateField(blank=True, null=True)
    date_of_inspection = models.DateField(blank=True, null=True)

    def __unicode__(self):
        return self.m_id
