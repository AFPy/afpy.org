"""Definition of the Python Howto content type
"""

from zope.interface import implements

from Products.Archetypes import atapi
from Products.ATContentTypes.content import base
from Products.ATContentTypes.content import schemata

from afpy.contenttypes.interfaces import IPythonHowto
from afpy.contenttypes.config import PROJECTNAME
from afpy.contenttypes.content.schemata import PythonHowtoSchema


PythonHowtoSchema['title'].storage = atapi.AnnotationStorage()
PythonHowtoSchema['description'].storage = atapi.AnnotationStorage()

schemata.finalizeATCTSchema(PythonHowtoSchema, moveDiscussion=False)


class PythonHowto(base.ATCTContent):
    """Python Howto"""
    implements(IPythonHowto)

    meta_type = "PythonHowto"
    schema = PythonHowtoSchema

    title = atapi.ATFieldProperty('title')
    description = atapi.ATFieldProperty('description')


atapi.registerType(PythonHowto, PROJECTNAME)
