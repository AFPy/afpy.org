README
=======

Installation
-------------

  >> python bootstrap.py
  >> ./bin/buildout

You may have to install libxslt1-dev, libxml-dev, libldap2-dev, libsasl2-dev.

Architecture du site
--------------------

**A remplir correctement par quelqu'un qui connait l'archi du site**

L'architecture du site est relativement compliqué. Le site est construit a
partir de plusieurs applications différentes, tournant sous diverses
technologies (plone, pylons, des trucs en pur wsgi sans framework, un
agrégateur de rss non maintenu mais qui marche, un moinmoin tout pété, et
surements d'autres trucs)

Le tout est rassemblé derriere un proxy deliverance
(http://packages.python.org/Deliverance/), un varnish et un apache.

* http://hg.afpy.org/afpy.org/:
  La partie CMS du site.
  Utilise le framework plone (vieille version).
  Utilise buildout pour le déploiment.

  - sabrina qui a entre autres migré les forums :
  http://dev.afpy.org/python/forum_python/forum_general

  - kiorky qui a entre autres mis une gallery photo :
  http://dev.afpy.org/photos/sl2008

* https://bitbucket.org/gawel/afpymembers/
  L'applications "membres". S'occupe de l'inscription, du paiment des
  cotisations,

  Utilise le framework pylons.
  Le README inclus donne quelques directives d'installation.
