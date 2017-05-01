# coding=utf-8
from django.forms.widgets import Media
from xadmin.views import BaseAdminPlugin, ListAdminView


class JSHeadPlugin(BaseAdminPlugin):
    """Move o arquivo js para o head do templates
    Necessário em casos que o js precisa ser carregado antes
    """
    render_js_on_head = []

    def __init__(self, admin_view):
        super(JSHeadPlugin, self).__init__(admin_view)
        self._template = self.admin_view.base_template
        self._media = Media()

    def _init(self):
        """Configurações do plugin depois que foi marcado como ativo"""
        self.admin_view.base_template = 'openvpn/js_head_base.html'

    def init_request(self, *args, **kwargs):
        if len(self.render_js_on_head) > 0:
            self._init()
            return True
        return False

    def get_context(self, context):
        context['js_head_base'] = self._template
        context['js_head_media'] = self._media
        return context

    def get_media(self, media):
        media_js = media._js
        to_remove = []
        for js in media._js:
            if js in self.render_js_on_head:
                self._media.add_js((js,))
                to_remove.append(js)
        for js in to_remove:
            try:
                media_js.remove(js)
            except ValueError:
                pass
        return media


def register(site):
    site.register_plugin(JSHeadPlugin, ListAdminView)
