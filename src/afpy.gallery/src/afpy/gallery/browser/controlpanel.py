#!/usr/bin/env python
# -*- coding: utf-8 -*-
__docformat__ = 'restructuredtext en'

import csv
from AccessControl import getSecurityManager
import logging
import os
from AccessControl import Unauthorized

from zope.component import (
    getAdapter,
    getMultiAdapter,
    queryMultiAdapter,
    getUtility
)

from zope import component, interface, schema
from zope.publisher.interfaces import IPublishTraverse

from Products.Five import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.statusmessages.interfaces import IStatusMessage
from Products.CMFCore.utils import getToolByName

from z3c.form import form, button
from z3c.form import field

from plone.z3cform import layout
from plone.z3cform.interfaces import IFormWrapper
from plone.z3cform.templates import (
    ZopeTwoFormTemplateFactory,
)
import transaction

from afpy.gallery import MessageFactory as _

try:
    from kss.core import kssaction
    from plone.app.kss.plonekssview import PloneKSSView
except ImportError:
    class PloneKSSView:
        pass
    def kssaction(fun):
        return fun

class NullFormValidation(PloneKSSView):
    """Disable inline validation.

XXX: This horrible hack should only be a temporary solution until
we find a way to make plone.z3c.form calculate and use the form
name correctly.
"""

    @kssaction
    def validate_input(self, *args):
        return

hpath = lambda p: os.path.join(os.path.dirname(__file__), p)

class IMigrateSchema(interface.Interface):
    migrate = schema.Bool(
        title=_(u"Import from albums.cfg"), default=False)

def can_migrate(context, do_raise=True):
    has_perm = getSecurityManager().checkPermission(
        "cmf.ManagePortal", context)
    if do_raise and not has_perm:
        raise Unauthorized('unauthorized')
    return has_perm

class ConfigurationForm(form.Form):
    """."""
    ignoreContext=True
    fields = field.Fields(IMigrateSchema)
    def _getContent(self):
        pass
    def _redirect(self, msg=''):
        """ Redirect
        """
        if self.request:
            if msg:
                IStatusMessage(self.request).addStatusMessage(msg, type='info')
            self.request.response.redirect(self.context.absolute_url())
        return msg

    @button.buttonAndHandler(u'Apply')
    def handleApply(self, action):
        logger = logging.getLogger('afpy')
        portal_setup = getToolByName(
            self.context, 'portal_setup')
        portal_setup.runImportStepFromProfile(
            'profile-afpy.gallery:default', 
            'afpy_gallery_setupVarious', 
            run_dependencies=False)
        logger.info('finished')

class IImport(interface.Interface):
    """Marker interface"""

#class ISimpleFormView(IFormWrapper):
#    """."""
#layout_factory = ZopeTwoFormTemplateFactory(hpath('simpleformwrapper.pt'), form=ISimpleFormView,)
#component.provideAdapter(layout_factory)
ConfigurationFormView = layout.wrap_form(ConfigurationForm)

class Import(BrowserView):
    """."""
    interface.implements((IImport, IPublishTraverse))
    form_template = ViewPageTemplateFile('form.pt')
    def restrictedTraverse(self, *args, **kwargs):
        return self.context.restrictedTraverse(
            *args, **kwargs)
    def get_form(self, formview, iformwrapper=None, iform=None):
        """mark the form to allow template overrides"""
        context = self.context
        self.request.form['viewname'] = self.__name__
        zformv = formview(
            context, self.request).__of__(context)
        if iformwrapper:
            interface.alsoProvides(zformv, iformwrapper)
        if iform:
            interface.alsoProvides(zformv.form_instance,iform)
        return zformv

    def __call__(self):
        """."""
        can_migrate(self.context)
        zformv = self.get_form(ConfigurationFormView)
        content = zformv()
        return self.form_template(
            **{'f': content}
        )

    def _redirect(self, msg='', where=None):
        """ Redirect
        """
        if self.request:
            if msg:
                IStatusMessage(
                self.request).addStatusMessage(
                msg, type='info')
            l = self.context.absolute_url()
            if where:
                l = l + where
            self.request.response.redirect(l)
        return msg

# vim:set et sts=4 ts=4 tw=80: 
