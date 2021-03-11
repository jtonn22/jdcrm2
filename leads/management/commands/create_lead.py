from django.core.management.base import BaseCommand


class Command(BaseCommand):

    # used to check the name of the arguements that you pass in to the command
    # Arguements noted within this method need to pass before the handle method below will run
    def add_arguments(self, parser):
        parser.add_argument("first_name", type=str)

    # handle method is used to handle what ever happens when you call the function
    def handle(self, *args, **options):
        print("Hello world")