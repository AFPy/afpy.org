"""Common configuration constants
"""

from Products.Archetypes.public import DisplayList


PROJECTNAME = 'afpy.contenttypes'

ADD_PERMISSIONS = {
    # -*- extra stuff goes here -*-
    'ZopeHowto': 'afpy.contenttypes: Add Zope Howto',
    'PythonHowto': 'afpy.contenttypes: Add Python Howto',
    'FicheZope': 'afpy.contenttypes: Add Fiche Zope',
    'FichePython': 'afpy.contenttypes: Add Fiche Python',
    'AFPYProduct': 'afpy.contenttypes: Add AFPY Product',
    'AFPYPressRelease': 'afpy.contenttypes: Add AFPY Press Release',
    'AFPYNews': 'afpy.contenttypes: Add AFPY News',
    'AFPYLink': 'afpy.contenttypes: Add AFPY Link',
    'AFPYJob': 'afpy.contenttypes: Add AFPY Job',
    'AFPYEvent': 'afpy.contenttypes: Add AFPY Event',
}


VALUATION_GROUPS = DisplayList((
    ('1','*'),
    ('2','**'),
    ('3','***'),
    ('4','****'),
    ('5','*****'),
))

SECTION_GROUPS = DisplayList((
  ('AFPY', 'AFPY'),
  ('Python', 'Python'),
  ('Zope', 'Zope'),
  ('PythonDailyUrl', 'PythonDailyUrl'),
  ))
           

ZOPE_HOWTO_CATEGORIES = (
  ('CPS', 'CPS'),
  ('Ikaroo', 'Ikaroo'),
  ('Zwook', 'ZWOOK'),
  ('CMF', 'CMF'),
  ('Plone', 'Plone'),
  ('Silva', 'Silva'),
  ('Zope', 'Zope'),
  ('Zope3', 'Zope3'),
  ('Autre', 'Autre')
)

ENVIRONMENT_GROUPS = DisplayList(ZOPE_HOWTO_CATEGORIES)

PYTHON_HOWTO_CATEGORIES = (
  ('bd','Base de donnee'),
  ('date', 'Date'),
  ('fichier', 'Fichier'),
  ('graphique', 'Graphique'),
  ('maths', 'Maths'),
  ('messagerie', 'Messagerie'),
  ('reseau','Reseau'),
  ('securite', 'Securite'),
  ('autre', 'Autre')
  )

