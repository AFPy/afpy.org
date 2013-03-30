# -*- coding: utf-8 -*-
"""Chopeur des données de la session d'authentification"""

from Products.Five import BrowserView

class SessionDataIniView(BrowserView):
    def __call__(self, *args, **kwargs):
        props = ('cookie_name', 'cookie_lifetime', 'cookie_domain', 'mod_auth_tkt',
                 'timeout', 'refresh_interval', 'external_ticket_name', 'secure',
                 '_shared_secret', 'path'
        )

        session_plugin = self.context.acl_users.session
        out = "[authtkt]\n"
        for name in props:
            if name.startswith('_'):
                key = name[1:]
            else:
                key = name
            out += "{0} = {1}\n".format(key, getattr(session_plugin, name))
        return out