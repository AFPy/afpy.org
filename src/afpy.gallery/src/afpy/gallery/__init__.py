import logging
from zope.i18nmessageid import MessageFactory
MessageFactory = afpygalleryMessageFactory = MessageFactory('afpy.gallery') 
logger = logging.getLogger('afpy.gallery')
def initialize(context):
    """Initializer called when used as a Zope 2 product.""" 
