# -*- coding: utf-8 -*-

import os, sys
import logging

try:
    from Products.CMFPlone.migrations import migration_util
except:
    #plone4
    from plone.app.upgrade import utils as migration_util

from Products.CMFCore.utils import getToolByName
from Products.ATContentTypes.interface.image import IATImage
from Products.ATContentTypes.content.image import ATImage
import transaction


from Products.CMFCore.utils import getToolByName
              
PROFILE =  'profile-afpy.gallery:default'
PROFILEID = 'profile-%s' % PROFILE

def log(message):
    logger = logging.getLogger('afpy.gallery.upgrades')
    logger.warn(message)

def recook_resources(context):
    """
    """
    site = getToolByName(context, 'portal_url').getPortalObject()
    jsregistry = getToolByName(site, 'portal_javascripts')
    cssregistry = getToolByName(site, 'portal_css')
    jsregistry.cookResources()
    cssregistry.cookResources()
    log('Recooked css/js')

def import_js(context):
    """
    """
    site = getToolByName(context, 'portal_url').getPortalObject()
    portal_setup = getToolByName(context, 'portal_setup')
    portal_setup.runImportStepFromProfile(PROFILEID, 'jsregistry', run_dependencies=False)
    log('Imported js')

def import_css(context):
    """
    """
    site = getToolByName(context, 'portal_url').getPortalObject()
    portal_setup = getToolByName(context, 'portal_setup')
    portal_setup.runImportStepFromProfile(PROFILEID, 'cssregistry', run_dependencies=False)
    log('Imported css')

def upgrade_1000(context):
    """
    """
    site = getToolByName(context, 'portal_url').getPortalObject()
    portal_setup = site.portal_setup
    log('v1000 applied')

