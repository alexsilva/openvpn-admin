from xadmin import site

from .models import Vpn, Ovpn
from .forms import VPNForm


class VPNAdmin(object):
    form = VPNForm
    # fields = (
    #     "username",
    #     "password",
    #     "import_zip"
    # )


site.register(Vpn, VPNAdmin)
site.register(Ovpn)
