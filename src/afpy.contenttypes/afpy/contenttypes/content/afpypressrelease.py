"""Definition of the AFPY Press Release content type
"""

from zope.interface import implements

from Products.Archetypes import atapi
from Products.ATContentTypes.content import base
from Products.ATContentTypes.content import schemata

from afpy.contenttypes.interfaces import IAFPYPressRelease
from afpy.contenttypes.config import PROJECTNAME
from afpy.contenttypes.content.schemata import AFPYPressReleaseSchema


AFPYPressReleaseSchema['title'].storage = atapi.AnnotationStorage()
AFPYPressReleaseSchema['description'].storage = atapi.AnnotationStorage()

schemata.finalizeATCTSchema(AFPYPressReleaseSchema, moveDiscussion=False)


class AFPYPressRelease(base.ATCTContent):
    """AFPY Press Release"""
    implements(IAFPYPressRelease)

    meta_type = "AFPYPressRelease"
    schema = AFPYPressReleaseSchema

    title = atapi.ATFieldProperty('title')
    description = atapi.ATFieldProperty('description')


atapi.registerType(AFPYPressRelease, PROJECTNAME)
