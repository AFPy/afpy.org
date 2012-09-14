Introduction
============

This is a full-blown functional test. The emphasis here is on testing what
the user may input and see, and the system is largely tested as a black box.
We use PloneTestCase to set up this test as well, so we have a full Plone site
to play with. We *can* inspect the state of the portal, e.g. using 
self.portal and self.folder, but it is often frowned upon since you are not
treating the system as a black box. Also, if you, for example, log in or set
roles using calls like self.setRoles(), these are not reflected in the test
browser, which runs as a separate session.

Being a doctest, we can tell a story here.

First, we must perform some setup. We use the testbrowser that is shipped
with Five, as this provides proper Zope 2 integration. Most of the 
documentation, though, is in the underlying zope.testbrower package.

    >>> from Products.Five.testbrowser import Browser
    >>> browser = Browser()
    >>> portal_url = self.portal.absolute_url()

The following is useful when writing and debugging testbrowser tests. It lets
us see all error messages in the error_log.

    >>> self.portal.error_log._ignored_exceptions = ()

With that in place, we can go to the portal front page and log in. We will
do this using the default user from PloneTestCase:

    >>> from Products.PloneTestCase.setup import portal_owner, default_password

Because add-on themes or products may remove or hide the login portlet, this test will use the login form that comes with plone.  

    >>> browser.open(portal_url + '/login_form')
    >>> browser.getControl(name='__ac_name').value = portal_owner
    >>> browser.getControl(name='__ac_password').value = default_password
    >>> browser.getControl(name='submit').click()

Here, we set the value of the fields on the login form and then simulate a
submit click.  We then ensure that we get the friendly logged-in message:

    >>> "You are now logged in" in browser.contents
    True

Finally, let's return to the front page of our site before continuing

    >>> browser.open(portal_url)

-*- extra stuff goes here -*-
The Zope Howto content type
===============================

In this section we are tesing the Zope Howto content type by performing
basic operations like adding, updadating and deleting Zope Howto content
items.

Adding a new Zope Howto content item
--------------------------------

We use the 'Add new' menu to add a new content item.

    >>> browser.getLink('Add new').click()

Then we select the type of item we want to add. In this case we select
'Zope Howto' and click the 'Add' button to get to the add form.

    >>> browser.getControl('Zope Howto').click()
    >>> browser.getControl(name='form.button.Add').click()
    >>> 'Zope Howto' in browser.contents
    True

Now we fill the form and submit it.

    >>> browser.getControl(name='title').value = 'Zope Howto Sample'
    >>> browser.getControl('Save').click()
    >>> 'Changes saved' in browser.contents
    True

And we are done! We added a new 'Zope Howto' content item to the portal.

Updating an existing Zope Howto content item
---------------------------------------

Let's click on the 'edit' tab and update the object attribute values.

    >>> browser.getLink('Edit').click()
    >>> browser.getControl(name='title').value = 'New Zope Howto Sample'
    >>> browser.getControl('Save').click()

We check that the changes were applied.

    >>> 'Changes saved' in browser.contents
    True
    >>> 'New Zope Howto Sample' in browser.contents
    True

Removing a/an Zope Howto content item
--------------------------------

If we go to the home page, we can see a tab with the 'New Zope Howto
Sample' title in the global navigation tabs.

    >>> browser.open(portal_url)
    >>> 'New Zope Howto Sample' in browser.contents
    True

Now we are going to delete the 'New Zope Howto Sample' object. First we
go to the contents tab and select the 'New Zope Howto Sample' for
deletion.

    >>> browser.getLink('Contents').click()
    >>> browser.getControl('New Zope Howto Sample').click()

We click on the 'Delete' button.

    >>> browser.getControl('Delete').click()
    >>> 'Item(s) deleted' in browser.contents
    True

So, if we go back to the home page, there is no longer a 'New Zope Howto
Sample' tab.

    >>> browser.open(portal_url)
    >>> 'New Zope Howto Sample' in browser.contents
    False

Adding a new Zope Howto content item as contributor
------------------------------------------------

Not only site managers are allowed to add Zope Howto content items, but
also site contributors.

Let's logout and then login as 'contributor', a portal member that has the
contributor role assigned.

    >>> browser.getLink('Log out').click()
    >>> browser.open(portal_url + '/login_form')
    >>> browser.getControl(name='__ac_name').value = 'contributor'
    >>> browser.getControl(name='__ac_password').value = default_password
    >>> browser.getControl(name='submit').click()
    >>> browser.open(portal_url)

We use the 'Add new' menu to add a new content item.

    >>> browser.getLink('Add new').click()

We select 'Zope Howto' and click the 'Add' button to get to the add form.

    >>> browser.getControl('Zope Howto').click()
    >>> browser.getControl(name='form.button.Add').click()
    >>> 'Zope Howto' in browser.contents
    True

Now we fill the form and submit it.

    >>> browser.getControl(name='title').value = 'Zope Howto Sample'
    >>> browser.getControl('Save').click()
    >>> 'Changes saved' in browser.contents
    True

Done! We added a new Zope Howto content item logged in as contributor.

Finally, let's login back as manager.

    >>> browser.getLink('Log out').click()
    >>> browser.open(portal_url + '/login_form')
    >>> browser.getControl(name='__ac_name').value = portal_owner
    >>> browser.getControl(name='__ac_password').value = default_password
    >>> browser.getControl(name='submit').click()
    >>> browser.open(portal_url)


The Python Howto content type
===============================

In this section we are tesing the Python Howto content type by performing
basic operations like adding, updadating and deleting Python Howto content
items.

Adding a new Python Howto content item
--------------------------------

We use the 'Add new' menu to add a new content item.

    >>> browser.getLink('Add new').click()

Then we select the type of item we want to add. In this case we select
'Python Howto' and click the 'Add' button to get to the add form.

    >>> browser.getControl('Python Howto').click()
    >>> browser.getControl(name='form.button.Add').click()
    >>> 'Python Howto' in browser.contents
    True

Now we fill the form and submit it.

    >>> browser.getControl(name='title').value = 'Python Howto Sample'
    >>> browser.getControl('Save').click()
    >>> 'Changes saved' in browser.contents
    True

And we are done! We added a new 'Python Howto' content item to the portal.

Updating an existing Python Howto content item
---------------------------------------

Let's click on the 'edit' tab and update the object attribute values.

    >>> browser.getLink('Edit').click()
    >>> browser.getControl(name='title').value = 'New Python Howto Sample'
    >>> browser.getControl('Save').click()

We check that the changes were applied.

    >>> 'Changes saved' in browser.contents
    True
    >>> 'New Python Howto Sample' in browser.contents
    True

Removing a/an Python Howto content item
--------------------------------

If we go to the home page, we can see a tab with the 'New Python Howto
Sample' title in the global navigation tabs.

    >>> browser.open(portal_url)
    >>> 'New Python Howto Sample' in browser.contents
    True

Now we are going to delete the 'New Python Howto Sample' object. First we
go to the contents tab and select the 'New Python Howto Sample' for
deletion.

    >>> browser.getLink('Contents').click()
    >>> browser.getControl('New Python Howto Sample').click()

We click on the 'Delete' button.

    >>> browser.getControl('Delete').click()
    >>> 'Item(s) deleted' in browser.contents
    True

So, if we go back to the home page, there is no longer a 'New Python Howto
Sample' tab.

    >>> browser.open(portal_url)
    >>> 'New Python Howto Sample' in browser.contents
    False

Adding a new Python Howto content item as contributor
------------------------------------------------

Not only site managers are allowed to add Python Howto content items, but
also site contributors.

Let's logout and then login as 'contributor', a portal member that has the
contributor role assigned.

    >>> browser.getLink('Log out').click()
    >>> browser.open(portal_url + '/login_form')
    >>> browser.getControl(name='__ac_name').value = 'contributor'
    >>> browser.getControl(name='__ac_password').value = default_password
    >>> browser.getControl(name='submit').click()
    >>> browser.open(portal_url)

We use the 'Add new' menu to add a new content item.

    >>> browser.getLink('Add new').click()

We select 'Python Howto' and click the 'Add' button to get to the add form.

    >>> browser.getControl('Python Howto').click()
    >>> browser.getControl(name='form.button.Add').click()
    >>> 'Python Howto' in browser.contents
    True

Now we fill the form and submit it.

    >>> browser.getControl(name='title').value = 'Python Howto Sample'
    >>> browser.getControl('Save').click()
    >>> 'Changes saved' in browser.contents
    True

Done! We added a new Python Howto content item logged in as contributor.

Finally, let's login back as manager.

    >>> browser.getLink('Log out').click()
    >>> browser.open(portal_url + '/login_form')
    >>> browser.getControl(name='__ac_name').value = portal_owner
    >>> browser.getControl(name='__ac_password').value = default_password
    >>> browser.getControl(name='submit').click()
    >>> browser.open(portal_url)


The Fiche Zope content type
===============================

In this section we are tesing the Fiche Zope content type by performing
basic operations like adding, updadating and deleting Fiche Zope content
items.

Adding a new Fiche Zope content item
--------------------------------

We use the 'Add new' menu to add a new content item.

    >>> browser.getLink('Add new').click()

Then we select the type of item we want to add. In this case we select
'Fiche Zope' and click the 'Add' button to get to the add form.

    >>> browser.getControl('Fiche Zope').click()
    >>> browser.getControl(name='form.button.Add').click()
    >>> 'Fiche Zope' in browser.contents
    True

Now we fill the form and submit it.

    >>> browser.getControl(name='title').value = 'Fiche Zope Sample'
    >>> browser.getControl('Save').click()
    >>> 'Changes saved' in browser.contents
    True

And we are done! We added a new 'Fiche Zope' content item to the portal.

Updating an existing Fiche Zope content item
---------------------------------------

Let's click on the 'edit' tab and update the object attribute values.

    >>> browser.getLink('Edit').click()
    >>> browser.getControl(name='title').value = 'New Fiche Zope Sample'
    >>> browser.getControl('Save').click()

We check that the changes were applied.

    >>> 'Changes saved' in browser.contents
    True
    >>> 'New Fiche Zope Sample' in browser.contents
    True

Removing a/an Fiche Zope content item
--------------------------------

If we go to the home page, we can see a tab with the 'New Fiche Zope
Sample' title in the global navigation tabs.

    >>> browser.open(portal_url)
    >>> 'New Fiche Zope Sample' in browser.contents
    True

Now we are going to delete the 'New Fiche Zope Sample' object. First we
go to the contents tab and select the 'New Fiche Zope Sample' for
deletion.

    >>> browser.getLink('Contents').click()
    >>> browser.getControl('New Fiche Zope Sample').click()

We click on the 'Delete' button.

    >>> browser.getControl('Delete').click()
    >>> 'Item(s) deleted' in browser.contents
    True

So, if we go back to the home page, there is no longer a 'New Fiche Zope
Sample' tab.

    >>> browser.open(portal_url)
    >>> 'New Fiche Zope Sample' in browser.contents
    False

Adding a new Fiche Zope content item as contributor
------------------------------------------------

Not only site managers are allowed to add Fiche Zope content items, but
also site contributors.

Let's logout and then login as 'contributor', a portal member that has the
contributor role assigned.

    >>> browser.getLink('Log out').click()
    >>> browser.open(portal_url + '/login_form')
    >>> browser.getControl(name='__ac_name').value = 'contributor'
    >>> browser.getControl(name='__ac_password').value = default_password
    >>> browser.getControl(name='submit').click()
    >>> browser.open(portal_url)

We use the 'Add new' menu to add a new content item.

    >>> browser.getLink('Add new').click()

We select 'Fiche Zope' and click the 'Add' button to get to the add form.

    >>> browser.getControl('Fiche Zope').click()
    >>> browser.getControl(name='form.button.Add').click()
    >>> 'Fiche Zope' in browser.contents
    True

Now we fill the form and submit it.

    >>> browser.getControl(name='title').value = 'Fiche Zope Sample'
    >>> browser.getControl('Save').click()
    >>> 'Changes saved' in browser.contents
    True

Done! We added a new Fiche Zope content item logged in as contributor.

Finally, let's login back as manager.

    >>> browser.getLink('Log out').click()
    >>> browser.open(portal_url + '/login_form')
    >>> browser.getControl(name='__ac_name').value = portal_owner
    >>> browser.getControl(name='__ac_password').value = default_password
    >>> browser.getControl(name='submit').click()
    >>> browser.open(portal_url)


The Fiche Python content type
===============================

In this section we are tesing the Fiche Python content type by performing
basic operations like adding, updadating and deleting Fiche Python content
items.

Adding a new Fiche Python content item
--------------------------------

We use the 'Add new' menu to add a new content item.

    >>> browser.getLink('Add new').click()

Then we select the type of item we want to add. In this case we select
'Fiche Python' and click the 'Add' button to get to the add form.

    >>> browser.getControl('Fiche Python').click()
    >>> browser.getControl(name='form.button.Add').click()
    >>> 'Fiche Python' in browser.contents
    True

Now we fill the form and submit it.

    >>> browser.getControl(name='title').value = 'Fiche Python Sample'
    >>> browser.getControl('Save').click()
    >>> 'Changes saved' in browser.contents
    True

And we are done! We added a new 'Fiche Python' content item to the portal.

Updating an existing Fiche Python content item
---------------------------------------

Let's click on the 'edit' tab and update the object attribute values.

    >>> browser.getLink('Edit').click()
    >>> browser.getControl(name='title').value = 'New Fiche Python Sample'
    >>> browser.getControl('Save').click()

We check that the changes were applied.

    >>> 'Changes saved' in browser.contents
    True
    >>> 'New Fiche Python Sample' in browser.contents
    True

Removing a/an Fiche Python content item
--------------------------------

If we go to the home page, we can see a tab with the 'New Fiche Python
Sample' title in the global navigation tabs.

    >>> browser.open(portal_url)
    >>> 'New Fiche Python Sample' in browser.contents
    True

Now we are going to delete the 'New Fiche Python Sample' object. First we
go to the contents tab and select the 'New Fiche Python Sample' for
deletion.

    >>> browser.getLink('Contents').click()
    >>> browser.getControl('New Fiche Python Sample').click()

We click on the 'Delete' button.

    >>> browser.getControl('Delete').click()
    >>> 'Item(s) deleted' in browser.contents
    True

So, if we go back to the home page, there is no longer a 'New Fiche Python
Sample' tab.

    >>> browser.open(portal_url)
    >>> 'New Fiche Python Sample' in browser.contents
    False

Adding a new Fiche Python content item as contributor
------------------------------------------------

Not only site managers are allowed to add Fiche Python content items, but
also site contributors.

Let's logout and then login as 'contributor', a portal member that has the
contributor role assigned.

    >>> browser.getLink('Log out').click()
    >>> browser.open(portal_url + '/login_form')
    >>> browser.getControl(name='__ac_name').value = 'contributor'
    >>> browser.getControl(name='__ac_password').value = default_password
    >>> browser.getControl(name='submit').click()
    >>> browser.open(portal_url)

We use the 'Add new' menu to add a new content item.

    >>> browser.getLink('Add new').click()

We select 'Fiche Python' and click the 'Add' button to get to the add form.

    >>> browser.getControl('Fiche Python').click()
    >>> browser.getControl(name='form.button.Add').click()
    >>> 'Fiche Python' in browser.contents
    True

Now we fill the form and submit it.

    >>> browser.getControl(name='title').value = 'Fiche Python Sample'
    >>> browser.getControl('Save').click()
    >>> 'Changes saved' in browser.contents
    True

Done! We added a new Fiche Python content item logged in as contributor.

Finally, let's login back as manager.

    >>> browser.getLink('Log out').click()
    >>> browser.open(portal_url + '/login_form')
    >>> browser.getControl(name='__ac_name').value = portal_owner
    >>> browser.getControl(name='__ac_password').value = default_password
    >>> browser.getControl(name='submit').click()
    >>> browser.open(portal_url)


The AFPY Product content type
===============================

In this section we are tesing the AFPY Product content type by performing
basic operations like adding, updadating and deleting AFPY Product content
items.

Adding a new AFPY Product content item
--------------------------------

We use the 'Add new' menu to add a new content item.

    >>> browser.getLink('Add new').click()

Then we select the type of item we want to add. In this case we select
'AFPY Product' and click the 'Add' button to get to the add form.

    >>> browser.getControl('AFPY Product').click()
    >>> browser.getControl(name='form.button.Add').click()
    >>> 'AFPY Product' in browser.contents
    True

Now we fill the form and submit it.

    >>> browser.getControl(name='title').value = 'AFPY Product Sample'
    >>> browser.getControl('Save').click()
    >>> 'Changes saved' in browser.contents
    True

And we are done! We added a new 'AFPY Product' content item to the portal.

Updating an existing AFPY Product content item
---------------------------------------

Let's click on the 'edit' tab and update the object attribute values.

    >>> browser.getLink('Edit').click()
    >>> browser.getControl(name='title').value = 'New AFPY Product Sample'
    >>> browser.getControl('Save').click()

We check that the changes were applied.

    >>> 'Changes saved' in browser.contents
    True
    >>> 'New AFPY Product Sample' in browser.contents
    True

Removing a/an AFPY Product content item
--------------------------------

If we go to the home page, we can see a tab with the 'New AFPY Product
Sample' title in the global navigation tabs.

    >>> browser.open(portal_url)
    >>> 'New AFPY Product Sample' in browser.contents
    True

Now we are going to delete the 'New AFPY Product Sample' object. First we
go to the contents tab and select the 'New AFPY Product Sample' for
deletion.

    >>> browser.getLink('Contents').click()
    >>> browser.getControl('New AFPY Product Sample').click()

We click on the 'Delete' button.

    >>> browser.getControl('Delete').click()
    >>> 'Item(s) deleted' in browser.contents
    True

So, if we go back to the home page, there is no longer a 'New AFPY Product
Sample' tab.

    >>> browser.open(portal_url)
    >>> 'New AFPY Product Sample' in browser.contents
    False

Adding a new AFPY Product content item as contributor
------------------------------------------------

Not only site managers are allowed to add AFPY Product content items, but
also site contributors.

Let's logout and then login as 'contributor', a portal member that has the
contributor role assigned.

    >>> browser.getLink('Log out').click()
    >>> browser.open(portal_url + '/login_form')
    >>> browser.getControl(name='__ac_name').value = 'contributor'
    >>> browser.getControl(name='__ac_password').value = default_password
    >>> browser.getControl(name='submit').click()
    >>> browser.open(portal_url)

We use the 'Add new' menu to add a new content item.

    >>> browser.getLink('Add new').click()

We select 'AFPY Product' and click the 'Add' button to get to the add form.

    >>> browser.getControl('AFPY Product').click()
    >>> browser.getControl(name='form.button.Add').click()
    >>> 'AFPY Product' in browser.contents
    True

Now we fill the form and submit it.

    >>> browser.getControl(name='title').value = 'AFPY Product Sample'
    >>> browser.getControl('Save').click()
    >>> 'Changes saved' in browser.contents
    True

Done! We added a new AFPY Product content item logged in as contributor.

Finally, let's login back as manager.

    >>> browser.getLink('Log out').click()
    >>> browser.open(portal_url + '/login_form')
    >>> browser.getControl(name='__ac_name').value = portal_owner
    >>> browser.getControl(name='__ac_password').value = default_password
    >>> browser.getControl(name='submit').click()
    >>> browser.open(portal_url)


The AFPY Press Release content type
===============================

In this section we are tesing the AFPY Press Release content type by performing
basic operations like adding, updadating and deleting AFPY Press Release content
items.

Adding a new AFPY Press Release content item
--------------------------------

We use the 'Add new' menu to add a new content item.

    >>> browser.getLink('Add new').click()

Then we select the type of item we want to add. In this case we select
'AFPY Press Release' and click the 'Add' button to get to the add form.

    >>> browser.getControl('AFPY Press Release').click()
    >>> browser.getControl(name='form.button.Add').click()
    >>> 'AFPY Press Release' in browser.contents
    True

Now we fill the form and submit it.

    >>> browser.getControl(name='title').value = 'AFPY Press Release Sample'
    >>> browser.getControl('Save').click()
    >>> 'Changes saved' in browser.contents
    True

And we are done! We added a new 'AFPY Press Release' content item to the portal.

Updating an existing AFPY Press Release content item
---------------------------------------

Let's click on the 'edit' tab and update the object attribute values.

    >>> browser.getLink('Edit').click()
    >>> browser.getControl(name='title').value = 'New AFPY Press Release Sample'
    >>> browser.getControl('Save').click()

We check that the changes were applied.

    >>> 'Changes saved' in browser.contents
    True
    >>> 'New AFPY Press Release Sample' in browser.contents
    True

Removing a/an AFPY Press Release content item
--------------------------------

If we go to the home page, we can see a tab with the 'New AFPY Press Release
Sample' title in the global navigation tabs.

    >>> browser.open(portal_url)
    >>> 'New AFPY Press Release Sample' in browser.contents
    True

Now we are going to delete the 'New AFPY Press Release Sample' object. First we
go to the contents tab and select the 'New AFPY Press Release Sample' for
deletion.

    >>> browser.getLink('Contents').click()
    >>> browser.getControl('New AFPY Press Release Sample').click()

We click on the 'Delete' button.

    >>> browser.getControl('Delete').click()
    >>> 'Item(s) deleted' in browser.contents
    True

So, if we go back to the home page, there is no longer a 'New AFPY Press Release
Sample' tab.

    >>> browser.open(portal_url)
    >>> 'New AFPY Press Release Sample' in browser.contents
    False

Adding a new AFPY Press Release content item as contributor
------------------------------------------------

Not only site managers are allowed to add AFPY Press Release content items, but
also site contributors.

Let's logout and then login as 'contributor', a portal member that has the
contributor role assigned.

    >>> browser.getLink('Log out').click()
    >>> browser.open(portal_url + '/login_form')
    >>> browser.getControl(name='__ac_name').value = 'contributor'
    >>> browser.getControl(name='__ac_password').value = default_password
    >>> browser.getControl(name='submit').click()
    >>> browser.open(portal_url)

We use the 'Add new' menu to add a new content item.

    >>> browser.getLink('Add new').click()

We select 'AFPY Press Release' and click the 'Add' button to get to the add form.

    >>> browser.getControl('AFPY Press Release').click()
    >>> browser.getControl(name='form.button.Add').click()
    >>> 'AFPY Press Release' in browser.contents
    True

Now we fill the form and submit it.

    >>> browser.getControl(name='title').value = 'AFPY Press Release Sample'
    >>> browser.getControl('Save').click()
    >>> 'Changes saved' in browser.contents
    True

Done! We added a new AFPY Press Release content item logged in as contributor.

Finally, let's login back as manager.

    >>> browser.getLink('Log out').click()
    >>> browser.open(portal_url + '/login_form')
    >>> browser.getControl(name='__ac_name').value = portal_owner
    >>> browser.getControl(name='__ac_password').value = default_password
    >>> browser.getControl(name='submit').click()
    >>> browser.open(portal_url)


The AFPY News content type
===============================

In this section we are tesing the AFPY News content type by performing
basic operations like adding, updadating and deleting AFPY News content
items.

Adding a new AFPY News content item
--------------------------------

We use the 'Add new' menu to add a new content item.

    >>> browser.getLink('Add new').click()

Then we select the type of item we want to add. In this case we select
'AFPY News' and click the 'Add' button to get to the add form.

    >>> browser.getControl('AFPY News').click()
    >>> browser.getControl(name='form.button.Add').click()
    >>> 'AFPY News' in browser.contents
    True

Now we fill the form and submit it.

    >>> browser.getControl(name='title').value = 'AFPY News Sample'
    >>> browser.getControl('Save').click()
    >>> 'Changes saved' in browser.contents
    True

And we are done! We added a new 'AFPY News' content item to the portal.

Updating an existing AFPY News content item
---------------------------------------

Let's click on the 'edit' tab and update the object attribute values.

    >>> browser.getLink('Edit').click()
    >>> browser.getControl(name='title').value = 'New AFPY News Sample'
    >>> browser.getControl('Save').click()

We check that the changes were applied.

    >>> 'Changes saved' in browser.contents
    True
    >>> 'New AFPY News Sample' in browser.contents
    True

Removing a/an AFPY News content item
--------------------------------

If we go to the home page, we can see a tab with the 'New AFPY News
Sample' title in the global navigation tabs.

    >>> browser.open(portal_url)
    >>> 'New AFPY News Sample' in browser.contents
    True

Now we are going to delete the 'New AFPY News Sample' object. First we
go to the contents tab and select the 'New AFPY News Sample' for
deletion.

    >>> browser.getLink('Contents').click()
    >>> browser.getControl('New AFPY News Sample').click()

We click on the 'Delete' button.

    >>> browser.getControl('Delete').click()
    >>> 'Item(s) deleted' in browser.contents
    True

So, if we go back to the home page, there is no longer a 'New AFPY News
Sample' tab.

    >>> browser.open(portal_url)
    >>> 'New AFPY News Sample' in browser.contents
    False

Adding a new AFPY News content item as contributor
------------------------------------------------

Not only site managers are allowed to add AFPY News content items, but
also site contributors.

Let's logout and then login as 'contributor', a portal member that has the
contributor role assigned.

    >>> browser.getLink('Log out').click()
    >>> browser.open(portal_url + '/login_form')
    >>> browser.getControl(name='__ac_name').value = 'contributor'
    >>> browser.getControl(name='__ac_password').value = default_password
    >>> browser.getControl(name='submit').click()
    >>> browser.open(portal_url)

We use the 'Add new' menu to add a new content item.

    >>> browser.getLink('Add new').click()

We select 'AFPY News' and click the 'Add' button to get to the add form.

    >>> browser.getControl('AFPY News').click()
    >>> browser.getControl(name='form.button.Add').click()
    >>> 'AFPY News' in browser.contents
    True

Now we fill the form and submit it.

    >>> browser.getControl(name='title').value = 'AFPY News Sample'
    >>> browser.getControl('Save').click()
    >>> 'Changes saved' in browser.contents
    True

Done! We added a new AFPY News content item logged in as contributor.

Finally, let's login back as manager.

    >>> browser.getLink('Log out').click()
    >>> browser.open(portal_url + '/login_form')
    >>> browser.getControl(name='__ac_name').value = portal_owner
    >>> browser.getControl(name='__ac_password').value = default_password
    >>> browser.getControl(name='submit').click()
    >>> browser.open(portal_url)


The AFPY Link content type
===============================

In this section we are tesing the AFPY Link content type by performing
basic operations like adding, updadating and deleting AFPY Link content
items.

Adding a new AFPY Link content item
--------------------------------

We use the 'Add new' menu to add a new content item.

    >>> browser.getLink('Add new').click()

Then we select the type of item we want to add. In this case we select
'AFPY Link' and click the 'Add' button to get to the add form.

    >>> browser.getControl('AFPY Link').click()
    >>> browser.getControl(name='form.button.Add').click()
    >>> 'AFPY Link' in browser.contents
    True

Now we fill the form and submit it.

    >>> browser.getControl(name='title').value = 'AFPY Link Sample'
    >>> browser.getControl('Save').click()
    >>> 'Changes saved' in browser.contents
    True

And we are done! We added a new 'AFPY Link' content item to the portal.

Updating an existing AFPY Link content item
---------------------------------------

Let's click on the 'edit' tab and update the object attribute values.

    >>> browser.getLink('Edit').click()
    >>> browser.getControl(name='title').value = 'New AFPY Link Sample'
    >>> browser.getControl('Save').click()

We check that the changes were applied.

    >>> 'Changes saved' in browser.contents
    True
    >>> 'New AFPY Link Sample' in browser.contents
    True

Removing a/an AFPY Link content item
--------------------------------

If we go to the home page, we can see a tab with the 'New AFPY Link
Sample' title in the global navigation tabs.

    >>> browser.open(portal_url)
    >>> 'New AFPY Link Sample' in browser.contents
    True

Now we are going to delete the 'New AFPY Link Sample' object. First we
go to the contents tab and select the 'New AFPY Link Sample' for
deletion.

    >>> browser.getLink('Contents').click()
    >>> browser.getControl('New AFPY Link Sample').click()

We click on the 'Delete' button.

    >>> browser.getControl('Delete').click()
    >>> 'Item(s) deleted' in browser.contents
    True

So, if we go back to the home page, there is no longer a 'New AFPY Link
Sample' tab.

    >>> browser.open(portal_url)
    >>> 'New AFPY Link Sample' in browser.contents
    False

Adding a new AFPY Link content item as contributor
------------------------------------------------

Not only site managers are allowed to add AFPY Link content items, but
also site contributors.

Let's logout and then login as 'contributor', a portal member that has the
contributor role assigned.

    >>> browser.getLink('Log out').click()
    >>> browser.open(portal_url + '/login_form')
    >>> browser.getControl(name='__ac_name').value = 'contributor'
    >>> browser.getControl(name='__ac_password').value = default_password
    >>> browser.getControl(name='submit').click()
    >>> browser.open(portal_url)

We use the 'Add new' menu to add a new content item.

    >>> browser.getLink('Add new').click()

We select 'AFPY Link' and click the 'Add' button to get to the add form.

    >>> browser.getControl('AFPY Link').click()
    >>> browser.getControl(name='form.button.Add').click()
    >>> 'AFPY Link' in browser.contents
    True

Now we fill the form and submit it.

    >>> browser.getControl(name='title').value = 'AFPY Link Sample'
    >>> browser.getControl('Save').click()
    >>> 'Changes saved' in browser.contents
    True

Done! We added a new AFPY Link content item logged in as contributor.

Finally, let's login back as manager.

    >>> browser.getLink('Log out').click()
    >>> browser.open(portal_url + '/login_form')
    >>> browser.getControl(name='__ac_name').value = portal_owner
    >>> browser.getControl(name='__ac_password').value = default_password
    >>> browser.getControl(name='submit').click()
    >>> browser.open(portal_url)


The AFPY Job content type
===============================

In this section we are tesing the AFPY Job content type by performing
basic operations like adding, updadating and deleting AFPY Job content
items.

Adding a new AFPY Job content item
--------------------------------

We use the 'Add new' menu to add a new content item.

    >>> browser.getLink('Add new').click()

Then we select the type of item we want to add. In this case we select
'AFPY Job' and click the 'Add' button to get to the add form.

    >>> browser.getControl('AFPY Job').click()
    >>> browser.getControl(name='form.button.Add').click()
    >>> 'AFPY Job' in browser.contents
    True

Now we fill the form and submit it.

    >>> browser.getControl(name='title').value = 'AFPY Job Sample'
    >>> browser.getControl('Save').click()
    >>> 'Changes saved' in browser.contents
    True

And we are done! We added a new 'AFPY Job' content item to the portal.

Updating an existing AFPY Job content item
---------------------------------------

Let's click on the 'edit' tab and update the object attribute values.

    >>> browser.getLink('Edit').click()
    >>> browser.getControl(name='title').value = 'New AFPY Job Sample'
    >>> browser.getControl('Save').click()

We check that the changes were applied.

    >>> 'Changes saved' in browser.contents
    True
    >>> 'New AFPY Job Sample' in browser.contents
    True

Removing a/an AFPY Job content item
--------------------------------

If we go to the home page, we can see a tab with the 'New AFPY Job
Sample' title in the global navigation tabs.

    >>> browser.open(portal_url)
    >>> 'New AFPY Job Sample' in browser.contents
    True

Now we are going to delete the 'New AFPY Job Sample' object. First we
go to the contents tab and select the 'New AFPY Job Sample' for
deletion.

    >>> browser.getLink('Contents').click()
    >>> browser.getControl('New AFPY Job Sample').click()

We click on the 'Delete' button.

    >>> browser.getControl('Delete').click()
    >>> 'Item(s) deleted' in browser.contents
    True

So, if we go back to the home page, there is no longer a 'New AFPY Job
Sample' tab.

    >>> browser.open(portal_url)
    >>> 'New AFPY Job Sample' in browser.contents
    False

Adding a new AFPY Job content item as contributor
------------------------------------------------

Not only site managers are allowed to add AFPY Job content items, but
also site contributors.

Let's logout and then login as 'contributor', a portal member that has the
contributor role assigned.

    >>> browser.getLink('Log out').click()
    >>> browser.open(portal_url + '/login_form')
    >>> browser.getControl(name='__ac_name').value = 'contributor'
    >>> browser.getControl(name='__ac_password').value = default_password
    >>> browser.getControl(name='submit').click()
    >>> browser.open(portal_url)

We use the 'Add new' menu to add a new content item.

    >>> browser.getLink('Add new').click()

We select 'AFPY Job' and click the 'Add' button to get to the add form.

    >>> browser.getControl('AFPY Job').click()
    >>> browser.getControl(name='form.button.Add').click()
    >>> 'AFPY Job' in browser.contents
    True

Now we fill the form and submit it.

    >>> browser.getControl(name='title').value = 'AFPY Job Sample'
    >>> browser.getControl('Save').click()
    >>> 'Changes saved' in browser.contents
    True

Done! We added a new AFPY Job content item logged in as contributor.

Finally, let's login back as manager.

    >>> browser.getLink('Log out').click()
    >>> browser.open(portal_url + '/login_form')
    >>> browser.getControl(name='__ac_name').value = portal_owner
    >>> browser.getControl(name='__ac_password').value = default_password
    >>> browser.getControl(name='submit').click()
    >>> browser.open(portal_url)


The AFPY Event content type
===============================

In this section we are tesing the AFPY Event content type by performing
basic operations like adding, updadating and deleting AFPY Event content
items.

Adding a new AFPY Event content item
--------------------------------

We use the 'Add new' menu to add a new content item.

    >>> browser.getLink('Add new').click()

Then we select the type of item we want to add. In this case we select
'AFPY Event' and click the 'Add' button to get to the add form.

    >>> browser.getControl('AFPY Event').click()
    >>> browser.getControl(name='form.button.Add').click()
    >>> 'AFPY Event' in browser.contents
    True

Now we fill the form and submit it.

    >>> browser.getControl(name='title').value = 'AFPY Event Sample'
    >>> browser.getControl('Save').click()
    >>> 'Changes saved' in browser.contents
    True

And we are done! We added a new 'AFPY Event' content item to the portal.

Updating an existing AFPY Event content item
---------------------------------------

Let's click on the 'edit' tab and update the object attribute values.

    >>> browser.getLink('Edit').click()
    >>> browser.getControl(name='title').value = 'New AFPY Event Sample'
    >>> browser.getControl('Save').click()

We check that the changes were applied.

    >>> 'Changes saved' in browser.contents
    True
    >>> 'New AFPY Event Sample' in browser.contents
    True

Removing a/an AFPY Event content item
--------------------------------

If we go to the home page, we can see a tab with the 'New AFPY Event
Sample' title in the global navigation tabs.

    >>> browser.open(portal_url)
    >>> 'New AFPY Event Sample' in browser.contents
    True

Now we are going to delete the 'New AFPY Event Sample' object. First we
go to the contents tab and select the 'New AFPY Event Sample' for
deletion.

    >>> browser.getLink('Contents').click()
    >>> browser.getControl('New AFPY Event Sample').click()

We click on the 'Delete' button.

    >>> browser.getControl('Delete').click()
    >>> 'Item(s) deleted' in browser.contents
    True

So, if we go back to the home page, there is no longer a 'New AFPY Event
Sample' tab.

    >>> browser.open(portal_url)
    >>> 'New AFPY Event Sample' in browser.contents
    False

Adding a new AFPY Event content item as contributor
------------------------------------------------

Not only site managers are allowed to add AFPY Event content items, but
also site contributors.

Let's logout and then login as 'contributor', a portal member that has the
contributor role assigned.

    >>> browser.getLink('Log out').click()
    >>> browser.open(portal_url + '/login_form')
    >>> browser.getControl(name='__ac_name').value = 'contributor'
    >>> browser.getControl(name='__ac_password').value = default_password
    >>> browser.getControl(name='submit').click()
    >>> browser.open(portal_url)

We use the 'Add new' menu to add a new content item.

    >>> browser.getLink('Add new').click()

We select 'AFPY Event' and click the 'Add' button to get to the add form.

    >>> browser.getControl('AFPY Event').click()
    >>> browser.getControl(name='form.button.Add').click()
    >>> 'AFPY Event' in browser.contents
    True

Now we fill the form and submit it.

    >>> browser.getControl(name='title').value = 'AFPY Event Sample'
    >>> browser.getControl('Save').click()
    >>> 'Changes saved' in browser.contents
    True

Done! We added a new AFPY Event content item logged in as contributor.

Finally, let's login back as manager.

    >>> browser.getLink('Log out').click()
    >>> browser.open(portal_url + '/login_form')
    >>> browser.getControl(name='__ac_name').value = portal_owner
    >>> browser.getControl(name='__ac_password').value = default_password
    >>> browser.getControl(name='submit').click()
    >>> browser.open(portal_url)



