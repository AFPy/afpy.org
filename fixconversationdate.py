# coding:utf-8
""" $ bin/instance run fixconversationdate.py monsite
"""

import re
import transaction
import parser
import sys
from Products.CMFCore.utils import getToolByName


instance_id = 'afpy'
if len(sys.argv) > 1:
    instance_id = sys.argv[1]
if instance_id not in app.keys():
    if instance_id != 'afpy':
        print "Le site '%s' n'existe pas. Renseignez le bon id de votre site \
contenant les forums à corriger !" % instance_id
        sys.exit(1)
    print """Vous n'avez pas de site afpy, passez en paramètre l'id de votre \
site Plone contenant les forums à corriger :
$ bin/instance run fixconversationdate.py monsite
"""
    sys.exit(2)

pl = app[instance_id]
catalog = getToolByName(pl, "portal_catalog")
conversations = catalog.searchResults(portal_type='PloneboardConversation')
for c in conversations:
    item = c.getObject()
    lastcommentdate = item.getLastCommentDate()
    if item.modified() != lastcommentdate:
        item.setModificationDate(lastcommentdate)
        catalog.indexObject(item)
transaction.commit()


#TODO: fix clear and rebuild catalog need 