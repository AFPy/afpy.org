"""Definition of the Fiche Python content type
"""

from zope.interface import implements

from Products.Archetypes import atapi
from Products.ATContentTypes.content import base
from Products.ATContentTypes.content import schemata

from afpy.contenttypes.interfaces import IFichePython
from afpy.contenttypes.config import PROJECTNAME
from afpy.contenttypes.content.schemata import FichePythonSchema 


FichePythonSchema['title'].storage = atapi.AnnotationStorage()
FichePythonSchema['description'].storage = atapi.AnnotationStorage()

schemata.finalizeATCTSchema(FichePythonSchema, moveDiscussion=False)


class FichePython(base.ATCTContent):
    """Fiche Python AFPY"""
    implements(IFichePython)

    meta_type = "FichePython"
    schema = FichePythonSchema

    title = atapi.ATFieldProperty('title')
    description = atapi.ATFieldProperty('description')


atapi.registerType(FichePython, PROJECTNAME)
