# openvpn-admin
Web interface written in python/django to manage vpn connections.


INSTALL

``` git clone https://github.com/alexsilva/openvpn-admin.git ```

``` sudo apt-get install supervisor ```

``` sudo python -m pip install -r requirements.txt ```

EXPORT SUPERVISOR CONFIG `as root`

``` python manage.py supervisor getconfig > /etc/supervisor/supervisord.conf ```

SUPERVISOR INITIALIZATION `Supervisor must start as root user´

``` sudo service supervisor start ```


