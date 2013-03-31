from elementtree import ElementTree
from Products.CMFCore.utils import getToolByName
from DateTime import DateTime
from base64 import decodestring
import transaction


def changeWorkflowState(content, state_id, acquire_permissions=False,
                        portal_workflow=None, **kw):
    """Change the workflow state of an object
    @param content: Content obj which state will be changed
    @param state_id: name of the state to put on content
    @param acquire_permissions: True->All permissions unchecked and on riles and
                                acquired
                                False->Applies new state security map
    @param portal_workflow: Provide workflow tool (optimisation) if known
    @param kw: change the values of same name of the state mapping
    @return: None
    """

    if portal_workflow is None:
        portal_workflow = getToolByName(content, 'portal_workflow')

    # Might raise IndexError if no workflow is associated to this type
    wf_def = portal_workflow.getWorkflowsFor(content)[0]
    wf_id= wf_def.getId()

    wf_state = {
        'action': None,
        'actor': None,
        'comments': "Setting state to %s" % state_id,
        'review_state': state_id,
        'time': DateTime(),
        }

    # Updating wf_state from keyword args
    for k in kw.keys():
        # Remove unknown items
        if not wf_state.has_key(k):
            del kw[k]
    if kw.has_key('review_state'):
        del kw['review_state']
    wf_state.update(kw)

    portal_workflow.setStatusOf(wf_id, content, wf_state)

    if acquire_permissions:
        # Acquire all permissions
        for permission in content.possible_permissions():
            content.manage_permission(permission, acquire=1)
    else:
        # Setting new state permissions
        wf_def.updateRoleMappingsFor(content)

    # Map changes to the catalogs
    content.reindexObject(idxs=['allowedRolesAndUsers', 'review_state'])
    return


pl = app["afpy.org"]

site = getToolByName(pl, 'portal_url').getPortalObject()
wftool = getToolByName(site, "portal_workflow")

document = ElementTree.parse('jobs.xml')
print len(document.findall('job'))
jobs_folder = pl["jobs"]
for node in document.findall('job'):
    path = node.find('url').text
    creator = node.find('creator').text
    jobid = node.find('id').text
    state = node.find('review_state').text
    id = "%s-%s"%(creator,jobid)
    if id not in jobs_folder.contentIds():
        jobs_folder.invokeFactory(type_name='AFPY Job', id=id, title=u'%s' % node.find('title').text)
        job = jobs_folder[id]
        job.processForm()
        job.setCompany(node.find('company').text.encode("utf-8"))
        logo = node.find('logo')
        if logo != None:
            job.setImage(decodestring(logo.text), mimetype=logo.attrib['mimetype'],
                          filename=logo.attrib['filename'], refresh_exif=True)
        job.setDescription(node.find('description').text.encode("utf-8"))
        job.setCreationDate(DateTime(node.find('creation_date').text))
        job.setSourceUrl(node.find('sourceUrl').text)
        job.setRemoteUrl(node.find('remoteUrl').text)
        job.setContact(node.find('contact').text)
        job.setEmail(node.find('email').text)
        job.setText(node.find('text').text)
        job.setPhone(node.find('phone').text)
        address = node.find('adresse').text
        if address:
            job.setAddress(address.split("<br>"))
        changeWorkflowState(job, state, comments="No comment")
        job.setModificationDate(DateTime(node.find('creation_date').text))
        job.reindexObject()
jobs_folder.reindexObject()
transaction.commit()


