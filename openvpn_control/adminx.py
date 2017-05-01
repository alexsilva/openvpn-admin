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


class OVPNAdmin(object):
    search_fields = (
        "country",
        'protocol',
        'port'
    )

    list_filter = (
        "country",
        'protocol',
        'port'
    )

    list_display = (
        'file',
        "country",
        'protocol',
        'port'
    )


site.register(Vpn, VPNAdmin)
site.register(Ovpn, OVPNAdmin)
