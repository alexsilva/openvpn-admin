from django.conf.urls import url


from .views import VPNActivateView


urlpatterns = [
    url("activate/(?P<pk>\d+)", VPNActivateView.as_view(),
        name='vpn-control-activate')
]