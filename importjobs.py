from elementtree import ElementTree
from elementtree.ElementTree import Element, SubElement
from Products.CMFCore.utils import getToolByName


pl = app["afpy.org"]
document = ElementTree.parse('jobs.xml')
for node in document.findall('job'):
    print node.find('id').text, node.find('title').text, node.find('company').text
    #TODO : create AFPY Job into new site
