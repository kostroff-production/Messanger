from django.core.management.base import BaseCommand
from backend.settings import ADMIN
from chat.models import Person


class Command(BaseCommand):
    def handle(self, *args, **options):
        if Person.objects.count() == 0:
            Person.objects.create_superuser(login=ADMIN['login'], password=ADMIN['password'])
        else:
            print('Admin accounts can only be initialized if no Person exist')
