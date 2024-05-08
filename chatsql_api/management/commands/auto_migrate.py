from django.core.management.base import BaseCommand
from django.core.management import call_command

class AutoMigrate(BaseCommand):
    help = 'Automatically make migrations and migrate'

    def handle(self, *args, **options):
        self.stdout.write("Making migrations...")
        call_command('makemigrations', interactive=False)
        self.stdout.write("Applying migrations...")
        call_command('migrate', interactive=False)
        self.stdout.write(self.style.SUCCESS("Migrations successfully applied!"))
