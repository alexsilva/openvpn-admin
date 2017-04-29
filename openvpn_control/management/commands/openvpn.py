from django.core.management.base import BaseCommand, CommandError
import sh


class Command(BaseCommand):
    help = 'openvpn command control'

    def add_arguments(self, parser):
        # parser.add_argument('poll_id', nargs='+', type=int)
        pass

    def handle(self, *args, **options):
        """"""
        sh.openvpn()
