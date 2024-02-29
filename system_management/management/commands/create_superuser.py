# yourapp/management/commands/create_superuser.py
from django.core.management.base import BaseCommand
from system_management.models import CustomUser, Voucher

class Command(BaseCommand):
    help = 'Create a superuser with a plain text password'

    def handle(self, *args, **options):
        email = 'admin@gmail.com'  
        password = 'adminpassword'  
        if not CustomUser.objects.filter(email=email).exists():
            superuser = CustomUser.objects.create_superuser(email=email)
            superuser.set_password(password)  
            superuser.save()
            self.stdout.write(self.style.SUCCESS('Superuser created successfully'))
        else:
            self.stdout.write(self.style.SUCCESS('Superuser already exists'))
