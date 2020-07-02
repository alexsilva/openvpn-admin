# openvpn-admin
Web interface written in python/django to manage vpn connections.


# INSTALL

## Not maintained [send pull requests for improvements]

``` git clone https://github.com/alexsilva/openvpn-admin.git ```

``` cd openvpn-admin ```

``` sudo apt-get install supervisor ```

``` sudo python -m pip install -r requirements.txt ```

``` python manage.py makemigrations ```

``` python manage.py migrate ```

``` python manage.py createsuperuser (after enter: admin | admin12345)```

# EXPORT SUPERVISOR CONFIG `as root`

``` python manage.py supervisor getconfig > /etc/supervisor/supervisord.conf ```

# SUPERVISOR INITIALIZATION `Supervisor must start as root user`

``` sudo service supervisor start ```


# DEFAULTS (django-environ)

``` /etc/supervisor/openvpn-admin/settings.env (Location of the environment configuration script) ```

---

``` SUPERVISOR_HTTP_SERVER_PORT == 9105 (Supervisor rpc port) ```

---

``` DJANGO_RUNSERVER_PORT == 8105 (Port of the local django admin server) ```

---

![Admin](https://github.com/alexsilva/openvpn-admin/raw/master/images/vpn.PNG)
