"""Definition of the AFPY Job content type
"""

from zope.interface import implements

from Products.Archetypes import atapi
from Products.ATContentTypes.content import base
from Products.ATContentTypes.content import schemata

from afpy.contenttypes.interfaces import IAFPYJob
from afpy.contenttypes.config import PROJECTNAME
from afpy.contenttypes.content.schemata import AFPYJobSchema


AFPYJobSchema['title'].storage = atapi.AnnotationStorage()
AFPYJobSchema['description'].storage = atapi.AnnotationStorage()

schemata.finalizeATCTSchema(AFPYJobSchema, moveDiscussion=False)


class AFPYJob(base.ATCTContent):
    """Job content type"""
    implements(IAFPYJob)

    meta_type = "AFPYJob"
    schema = AFPYJobSchema

    title = atapi.ATFieldProperty('title')
    description = atapi.ATFieldProperty('description')
    
    def tag(self,**kwargs):
        ''' tag wrapper '''
        return self.getField('image').tag(self, scale='medium', **kwargs)

    def Creator(self):
        ''' faked creator '''
        return self.getCompany()

atapi.registerType(AFPYJob, PROJECTNAME)
