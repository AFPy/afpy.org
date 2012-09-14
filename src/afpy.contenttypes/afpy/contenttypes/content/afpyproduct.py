"""Definition of the AFPY Product content type
"""

from zope.interface import implements

from Products.Archetypes import atapi
from Products.ATContentTypes.content import base
from Products.ATContentTypes.content import schemata

from afpy.contenttypes.interfaces import IAFPYProduct
from afpy.contenttypes.config import PROJECTNAME
from afpy.contenttypes.content.schemata import AFPYProductSchema


AFPYProductSchema['title'].storage = atapi.AnnotationStorage()
AFPYProductSchema['description'].storage = atapi.AnnotationStorage()

schemata.finalizeATCTSchema(AFPYProductSchema, moveDiscussion=False)


class AFPYProduct(base.ATCTContent):
    """AFPY Product"""
    implements(IAFPYProduct)

    meta_type = "AFPYProduct"
    schema = AFPYProductSchema

    title = atapi.ATFieldProperty('title')
    description = atapi.ATFieldProperty('description')


atapi.registerType(AFPYProduct, PROJECTNAME)
