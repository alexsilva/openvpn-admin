from django.conf.urls import url


from .views import VPNActivateView, VPNStatusView


urlpatterns = [
    url("activate/(?P<pk>\d+)", VPNActivateView.as_view(),
        name='vpn-control-activate'),

    url("status/(?P<pk>\d+)", VPNStatusView.as_view(),
        name='vpn-control-status')
]