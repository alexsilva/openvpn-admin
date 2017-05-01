from django.db import models


class Vpn(models.Model):
    username = models.CharField("username", max_length=255)
    password = models.CharField("password", max_length=32)

    def __unicode__(self):
        return self.username


class Ovpn(models.Model):
    file = models.FileField("File (.ovpn)", help_text="configuration file")

    country = models.CharField("Country", max_length=8)
    protocol = models.CharField("Protocol", max_length=8)
    port = models.IntegerField("Port")

    vpn = models.ForeignKey(Vpn, verbose_name="VPN")

    activated = models.BooleanField('Activated', default=False)

    def __unicode__(self):
        return u"{0.file} / {0.vpn}".format(self)
