"""Definition of the AFPY News content type
"""

from zope.interface import implements

from Products.Archetypes import atapi
from Products.ATContentTypes.content import base
from Products.ATContentTypes.content import schemata

# -*- Message Factory Imported Here -*-

from afpy.contenttypes.interfaces import IAFPYNews
from afpy.contenttypes.config import PROJECTNAME
from afpy.contenttypes.content.schemata import AFPYNewsSchema


AFPYNewsSchema['title'].storage = atapi.AnnotationStorage()
AFPYNewsSchema['description'].storage = atapi.AnnotationStorage()

schemata.finalizeATCTSchema(AFPYNewsSchema, moveDiscussion=False)


class AFPYNews(base.ATCTContent):
    """Description of the Example Type"""
    implements(IAFPYNews)

    meta_type = "AFPYNews"
    schema = AFPYNewsSchema

    title = atapi.ATFieldProperty('title')
    description = atapi.ATFieldProperty('description')


atapi.registerType(AFPYNews, PROJECTNAME)
