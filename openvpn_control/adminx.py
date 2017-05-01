from django.template.loader import render_to_string
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
        'port',
        'vpn_activate'
    )

    def vpn_activate(self, instance):
        """ativate vpn"""
        return render_to_string("w_buttom.html", context={
            'instance': instance
        })

    vpn_activate.short_description = "VPN"
    vpn_activate.allow_tags = True
    vpn_activate.is_column = False


site.register(Vpn, VPNAdmin)
site.register(Ovpn, OVPNAdmin)
