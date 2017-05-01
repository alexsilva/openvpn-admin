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
    refresh_times = range(15, 61, 15)

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

    vpn_activate.short_description = """VPN<span style="margin-left: 5px" 
                                        class="badge badge-success" id="vpn-ip"></span>"""
    vpn_activate.allow_tags = True
    vpn_activate.is_column = False


site.register(Vpn, VPNAdmin)
site.register(Ovpn, OVPNAdmin)
