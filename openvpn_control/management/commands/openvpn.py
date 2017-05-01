import os
import re

from django.core.management.base import BaseCommand, CommandError
from openvpn_control.models import Ovpn
from django.conf import settings
import sh


class Command(BaseCommand):
    help = 'openvpn command control'
    vpn_param = "auth-user-pass"

    def add_arguments(self, parser):
        # parser.add_argument('--pk', type=int)
        pass

    def handle(self, *args, **options):
        """"""
        ovpn = Ovpn.objects.filter(activated=True)
        if ovpn.exists():
            ovpn = ovpn[0]
            auth_filepath = os.path.join(settings.BASE_DIR, "vpn{0.vpn.pk}.auth.txt".format(ovpn))
            with open(auth_filepath, "w") as auth:
                auth.write(ovpn.vpn.username + '\n')
                auth.write(ovpn.vpn.password)
            # get file content
            with open(ovpn.file.path, "r") as vpn:
                vpn_file_content = vpn.readlines()
            # change file
            for index, line in enumerate(vpn_file_content):
                if re.match(self.vpn_param + '.*', line):
                    vpn_file_content[index] = "{0.vpn_param} {1:s}\n".format(self, auth_filepath)
                    break
            # write new data
            with open(ovpn.file.path, "w") as vpn:
                vpn.write(''.join(vpn_file_content))
            # vpn activate
            sh.openvpn(ovpn.file.path)
