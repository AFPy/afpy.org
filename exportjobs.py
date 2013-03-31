import base64
from elementtree import ElementTree
from elementtree.ElementTree import Element, SubElement
from Products.CMFCore.utils import getToolByName


pl = app["afpy"]

catalog = getToolByName(pl, "portal_catalog")
jobs = catalog.searchResults(portal_type='AFPYJob',
                             sort_on='creation_date',
                             sort_order='reverse',)
afpyjobs = Element("jobs")

for j in jobs:
    jobobj = j.getObject()
    job = SubElement(afpyjobs, 'job')
    id = SubElement(job, 'id')
    id.text = j.id
    creator = SubElement(job, 'creator')
    creator.text = jobobj.listCreators()[0]
    creation_date = SubElement(job, 'creation_date')
    creation_date.text = str(j.created)
    review_state = SubElement(job, 'review_state')
    review_state.text = j.review_state
    url = SubElement(job, 'url')
    url.text = j.getPath()
    textdetails = SubElement(job, 'text')
    textdetails.text = jobobj.getText().decode("utf-8")
    title = SubElement(job, 'title')
    title.text = j.Title.decode("utf-8")
    company = SubElement(job, 'company')
    company.text = jobobj.company.encode("utf-8").decode("utf-8")
    desc = SubElement(job, 'description')
    desc.text = j.Description.decode("utf-8")
    source = SubElement(job, 'sourceUrl')
    source.text = jobobj.sourceUrl
    address = SubElement(job, 'adresse')
    ad = "<br>".join(jobobj.adresse)
    address.text = ad.encode("utf-8").decode("utf-8")
    remote =  SubElement(job, 'remoteUrl')
    remote.text = jobobj.remoteUrl
    contact =  SubElement(job, 'contact')
    contact.text = jobobj.contact
    email =  SubElement(job, 'email')
    email.text = jobobj.email
    phone =  SubElement(job, 'phone')
    phone.text = jobobj.phone
    #TODO: LOGO !
    logo_field = jobobj.getField('logo')
    mimetype = logo_field.getContentType(jobobj)
    if mimetype.startswith('image/'):
        logo = SubElement(job, 'logo', mimetype=mimetype, filename = logo_field.getFilename(jobobj))
        raw_image = logo_field.get(jobobj, raw=True).aq_inner
        if isinstance(raw_image.data, str):
            logo.text = base64.b64encode(raw_image.data)
        else:
            logo.text = base64.b64encode(raw_image.data.data)


output_file = open( 'jobs.xml', 'w' )
output_file.write( '<?xml version="1.0"?>' )
output_file.write( ElementTree.tostring(afpyjobs) )
output_file.close()

