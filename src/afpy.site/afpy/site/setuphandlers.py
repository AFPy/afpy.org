# -*- codingav  utf-8 -*-

from Products.CMFCore.utils import getToolByName
from Products.CMFPlone.utils import _createObjectByType

FOLDERS_TO_DELETE = ['events']

FOLDERS_TO_EXCLUDE = ['Members']

CONTENTS_TO_INIT = [{'id':'site',
                     'title':"Le site web de l'AFPY",
                     'type':'Folder'},
                    {'id':'association',
                     'title':"L'AFPY - Association Francophone Python",
                     'type':'Folder'}]


def setup_content(context):
    """Final content setup
    """
    if context.readDataFile(
        'afpy.site_various.txt') is None: return
    site = getToolByName(context.getSite(), 
                         'portal_url').getPortalObject()

    wftool = getToolByName(site, "portal_workflow")

    existing = set(site.objectIds())

    # Initialize some contents
    for item_page in CONTENTS_TO_INIT:
        item_page_id = item_page['id']
        if item_page_id not in existing:
            _createObjectByType(item_page['type'], site, id=item_page_id,
                                title = u'%s' % item_page['title'])
            page = site[item_page_id]
            # Publish content:
            if wftool.getInfoFor(page, 'review_state') != 'published':
                wftool.doActionFor(page, 'publish')

    # Delete useless folder:
    for f in FOLDERS_TO_DELETE:
        if f in site.objectIds():
            site.manage_delObjects(ids=[f])

    # Exclude some folder to the nav:
    for f in FOLDERS_TO_EXCLUDE:
        folder = getattr(site, f)
        folder.setExcludeFromNav(True)
        folder.reindexObject()

