"""Definition of the Zope Howto content type
"""

from zope.interface import implements

from Products.Archetypes import atapi
from Products.ATContentTypes.content import base
from Products.ATContentTypes.content import schemata

# -*- Message Factory Imported Here -*-

from afpy.contenttypes.interfaces import IZopeHowto
from afpy.contenttypes.config import PROJECTNAME
from afpy.contenttypes.content.schemata import ZopeHowtoSchema 


ZopeHowtoSchema['title'].storage = atapi.AnnotationStorage()
ZopeHowtoSchema['description'].storage = atapi.AnnotationStorage()

schemata.finalizeATCTSchema(ZopeHowtoSchema, moveDiscussion=False)


class ZopeHowto(base.ATCTContent):
    """Zope Howto AFPY"""
    implements(IZopeHowto)

    meta_type = "ZopeHowto"
    schema = ZopeHowtoSchema

    title = atapi.ATFieldProperty('title')
    description = atapi.ATFieldProperty('description')


atapi.registerType(ZopeHowto, PROJECTNAME)
