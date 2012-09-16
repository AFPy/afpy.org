import ConfigParser
import pkg_resources
import logging
import transaction
from Products.CMFCore.utils import getToolByName

from afpy.gallery import app_config
from afpy.gallery.app_config import PRODUCT_DEPENDENCIES, EXTENSION_PROFILES
from Products.CMFPlone.utils import _createObjectByType



def publish_all(context):
    url = getToolByName(context, 'portal_url')
    site = url.getPortalObject()
    catalog = getToolByName(site, 'portal_catalog')
    wftool = getToolByName(site, 'portal_workflow')
    brains = catalog.search({
        'path': {'query':
                 '/'.join(context.getPhysicalPath())},
        'review_state': 'private',
    })

    for fp in brains:
        wftool.doActionFor(fp.getObject(), 'publish')

ALBUMS_ID = 'photos'
ALBUMS_TITLE = 'Albums'
def setupVarious(context):
    logger = logging.getLogger('afpy.gallery / setuphandler')
    cfg = pkg_resources.resource_filename(
        'afpy.gallery', 'albums.cfg'
    )
    if context.readDataFile(
        'afpy.gallery_various.txt') is None: return
    portal = getToolByName(
        context.getSite(), 'portal_url').getPortalObject()
    plone = portal.restrictedTraverse('@@plone')
    if not ALBUMS_ID in portal.objectIds():
        albums = _createObjectByType('Folder',
                                     portal,
                                     ALBUMS_ID)
        albums.processForm()
        albums.setTitle(ALBUMS_TITLE)
    else:
        albums = portal[ALBUMS_ID]
    ocfg = ConfigParser.ConfigParser()
    ocfg.readfp(open(cfg))
    for isection in ocfg.sections():
        section = dict(ocfg.items(isection))
        id = plone.normalizeString(isection)
        title = section.get('title', id)
        gtype = None
        url = None
        if not 'url' in section:
            gtype, otype = 'flickr', 'Link'
            url = (
                'http://www.flickr.com/photos'
                '/searchtags/%s' % (section['tags']
                )
            )
        else:
            url = section['url']
            if 'picasa' in url.lower():
                gtype = 'picasa'
            elif 'smugmug' in url.lower():
                gtype = 'smugmug'
        if not id in albums.objectIds():
            gal = _createObjectByType('Link', albums, id)
            gal.processForm()
        else:
            gal = albums[id]
        gal.setTitle(title)
        gal.setRemoteUrl(url)
        if gtype in ['picasa', 'flickr']:
            gal.setLayout('galleria_view')
        else:
            if gal.hasProperty('layout'):
                gal._delProperty('layout')
        logger.info('Parsed %s' % isection)
    publish_all(albums)


