from xadmin import site

from .models import Vpn, Ovpn

site.register(Vpn)
site.register(Ovpn)
