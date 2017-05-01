from django.http import HttpResponse
from django.views.generic import View
from django.core.management import call_command
from .models import Ovpn


class VPNActivateView(View):

    def get(self, request, pk):
        Ovpn.objects.exclude(pk=pk).update(activated=False)
        Ovpn.objects.filter(pk=pk).update(activated=True)
        call_command("supervisor", **{'ctl-command': ('restart', 'openvpn')})
        return HttpResponse("OK")
