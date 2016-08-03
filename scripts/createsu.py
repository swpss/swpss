from users.models import Account

if Account.objects.count() == 0:
    admin = Account.objects.create_superuser(
            "Admin",
            "Hyderabad",
            "9160083701",
            "IN-TG",
            4,
            True,
            "cybermotionind519",
            )
