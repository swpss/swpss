from django.db import models
from django.contrib.auth.models import AbstractBaseUser, \
        BaseUserManager, PermissionsMixin

from users.helper import AccountTypes, StatesOfIndia


class AccountManager(BaseUserManager):
    def create_user(
            self,
            email,
            first_name,
            address,
            phone_number,
            location,
            account_type,
            has_smart_phone,
            password=None,
            **kwargs
    ):
        msg = 'Account must have a valid %s.'
#        if not email:
#            raise ValueError(msg % 'email address')
        if not first_name:
            raise ValueError(msg % 'first name')
        if not address:
            raise ValueError(msg % 'address')
        if not phone_number and len(phone_number) != 10:
            raise ValueError(msg % 'phone number')
        if has_smart_phone is None:
            raise ValueError('This field cannot be None.')

        account = self.model(
                first_name=first_name,
                address=address,
                phone_number=phone_number,
                location=location,
                account_type=account_type,
                has_smart_phone=has_smart_phone,
                last_name=kwargs.get('last_name')
        )
        if email is not None:
            email = self.normalize_email(email)
            account.set_email(email)
        account.set_password(password)
        account.save()
        return account

    def create_superuser(
            self,
            first_name,
            address,
            phone_number,
            location,
            account_type,
            has_smart_phone,
            password,
            email=None,
            **kwargs
    ):
        account = self.create_user(
                email,
                first_name,
                address,
                phone_number,
                location,
                account_type,
                has_smart_phone,
                password,
                **kwargs
        )
        account.is_superuser = True
        account.is_staff = True
        account.save()

        return account


class Account(AbstractBaseUser, PermissionsMixin):
    # TODO: Add created_at and modified_at fields for this model.
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40, blank=True, null=True)

    address = models.CharField(max_length=350)
    phone_number = models.CharField(
            max_length=10,
            unique=True,
            help_text="Enter the phone number WITHOUT country code"
        )

    email = models.EmailField(unique=True, blank=True)
    location = models.CharField(
            max_length=5,
            choices=StatesOfIndia.get_state_names(),
            default='IN-TG'
        )

    has_smart_phone = models.BooleanField(default=False)
    account_type = models.IntegerField(
            choices=AccountTypes.get_account_types()
        )
    is_staff = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    client  = models.IntegerField(default=0)
    objects = AccountManager()

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = [
        'first_name',
        'address',
        'location',
        'account_type',
        'has_smart_phone',
    ]

    def __unicode__(self):
        return '{0} ({1})'.format(self.first_name, self.phone_number)

    def get_full_name(self):
        return ' '.join([self.first_name, self.last_name])

    def get_short_name(self):
        return self.first_name

    def set_email(self, email):
        self.email = email

