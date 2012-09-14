"""Definition of the Fiche Zope content type
"""

from zope.interface import implements

from Products.Archetypes import atapi
from Products.ATContentTypes.content import base
from Products.ATContentTypes.content import schemata

from afpy.contenttypes.interfaces import IFicheZope
from afpy.contenttypes.config import PROJECTNAME
from afpy.contenttypes.content.schemata import FicheZopeSchema


FicheZopeSchema['title'].storage = atapi.AnnotationStorage()
FicheZopeSchema['description'].storage = atapi.AnnotationStorage()

schemata.finalizeATCTSchema(FicheZopeSchema, moveDiscussion=False)


class FicheZope(base.ATCTContent):
    """Fiche Zope"""
    implements(IFicheZope)

    meta_type = "FicheZope"
    schema = FicheZopeSchema

    title = atapi.ATFieldProperty('title')
    description = atapi.ATFieldProperty('description')


atapi.registerType(FicheZope, PROJECTNAME)
