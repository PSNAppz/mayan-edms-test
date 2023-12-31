from django.core.management.base import BaseCommand

from ...models import AutoAdminSingleton


class Command(BaseCommand):
    help = 'Used to create a super user with a secure and automatic password.'

    def handle(self, *args, **options):
        AutoAdminSingleton.objects.create_autoadmin()
