"""Definition of the AFPY Event content type
"""

from zope.interface import implements

from Products.Archetypes import atapi
from Products.ATContentTypes.content import base
from Products.ATContentTypes.content import schemata

from afpy.contenttypes.interfaces import IAFPYEvent
from afpy.contenttypes.config import PROJECTNAME
from afpy.contenttypes.content.schemata import AFPYEventSchema


AFPYEventSchema['title'].storage = atapi.AnnotationStorage()
AFPYEventSchema['description'].storage = atapi.AnnotationStorage()

schemata.finalizeATCTSchema(AFPYEventSchema, moveDiscussion=False)


class AFPYEvent(base.ATCTContent):
    """Event of afpy.org site"""
    implements(IAFPYEvent)

    meta_type = "AFPYEvent"
    schema = AFPYEventSchema

    title = atapi.ATFieldProperty('title')
    description = atapi.ATFieldProperty('description')


atapi.registerType(AFPYEvent, PROJECTNAME)
