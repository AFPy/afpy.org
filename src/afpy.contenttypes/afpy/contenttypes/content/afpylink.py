"""Definition of the AFPY Link content type
"""

from zope.interface import implements

from Products.Archetypes import atapi
from Products.ATContentTypes.content import base
from Products.ATContentTypes.content import schemata

# -*- Message Factory Imported Here -*-

from afpy.contenttypes.interfaces import IAFPYLink
from afpy.contenttypes.config import PROJECTNAME
from afpy.contenttypes.content.schemata import AFPYLinkSchema


AFPYLinkSchema['title'].storage = atapi.AnnotationStorage()
AFPYLinkSchema['description'].storage = atapi.AnnotationStorage()

schemata.finalizeATCTSchema(AFPYLinkSchema, moveDiscussion=False)


class AFPYLink(base.ATCTContent):
    """AFPY Link Content Type"""
    implements(IAFPYLink)

    meta_type = "AFPYLink"
    schema = AFPYLinkSchema

    title = atapi.ATFieldProperty('title')
    description = atapi.ATFieldProperty('description')


atapi.registerType(AFPYLink, PROJECTNAME)
