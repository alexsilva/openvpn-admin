from django.conf import settings
from django.template.loader import render_to_string
from django.core.urlresolvers import reverse, reverse_lazy
from xadmin import site
from xadmin.views import filter_hook

from .xplugins import jshead

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
    render_js_on_head = [
        reverse_lazy('js_reverse'),
        settings.STATIC_URL + "openvpn/config.js"
    ]
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
        return render_to_string("openvpn/w_buttom.html", context={
            'instance': instance
        })

    vpn_activate.short_description = """VPN<span style="margin-left: 5px" 
                                        class="badge badge-success" id="vpn-ip"></span>"""
    vpn_activate.allow_tags = True
    vpn_activate.is_column = False

    @filter_hook
    def get_media(self):
        media = super(OVPNAdmin, self).get_media()
        media.add_js(self.render_js_on_head)
        return media


site.register(Vpn, VPNAdmin)
site.register(Ovpn, OVPNAdmin)

# plugins

jshead.register(site)
