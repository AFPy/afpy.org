#!/usr/bin/env python
# coding:utf-8
"""
(notes tshirtman + sabrina)

Pré-requis : libxml2 et libxslt installé

1/ Mise en place de l'environement de travail :

--> Dupliquer l'instance Plone 2.0 et la déployer dans un environnement de test 
    avec python2.4
--> Reprendre le buildout du nouveau site afpy en Plone 4 et le déployer

2/ Export des forums :

À partir du Plone 2.0 :

ATTENTION BUG à fixer (unauthorized) :
Pour que le script d'export fonctionne il est nécessaire que le module 
'Products.CMFBoard.forum_export' soit préalablement autorisé. Or le code 
le permettant se trouve dans un try/except dans lequel le code plante en prod 
(import forum_import -> from xml.sax import saxlib => ImportError: cannot import name saxlib)
Du coup "allow_module('Products.CMFBoard.forum_export')" indispensable au 
fonctionnement du script d'export n'est jamais exécuté.

--> Pour corriger rapidement ce problème, sortir du try le : 
"allow_module('Products.CMFBoard.forum_export')"
ligne 82 Products/CMFBoard/__init__.py du Plone 2.0

--> Redémarrer l'instance.

--> Lancer l'export des 2 forums via : {your_portal_url}/forum_import_export_form

--> récupérer les exports des 2 forums : afpy_python_forum_python.data et afpy_zope_forum_zope.data


3/ Préparation des imports :

Installation de ploneboard_anyxmlimport dans products de plone 4 :

--> Télécharger http://plone.org/products/ploneboard_anyxmlimport/releases/1.0/ploneboard_anyxmlimport-tar.gz
--> Décompresser le dans le dossier products du buildout (afpy.org/products)
--> dans afpy.org/products/ploneboard_anyxmlimport/interfaces.py, 
    corriger l'import de Interface (changer les 2 premières lignes) :
    
            from zope.interface import Interface
            
            class IController(Interface):

--> Création d'un lien symbolique entre products/ploneboard_anyxmlimport et 
    parts/instance/Products/ploneboard_anyxmlimport
    /!\ ne pas oublier de renouveler cette dernière étape si un buildout est 
    relancé plus tard

--> Copier les fichiers d'export de CMFBoard (afpy_python_forum_python.data et 
    afpy_zope_forum_zope.data) dans le dossier inputxml de 
    ploneboard_anyxmlimport

--> le XML extrait contient quelques caractères qui font planter 
    libxml2.parseFile, il est nécessaire de lancer le script fixforumdata.py 
    pour les corriger :
            $ python fixforumdata.py products/ploneboard_anyxmlimport/inputxml/afpy_zope_forum_zope.data
            $ python fixforumdata.py products/ploneboard_anyxmlimport/inputxml/afpy_python_forum_python.data

4/ Imports

--> sauvegarder la Data.fs, on ne sait jamais ;)

Dans le Plone 4 :

--> Créer un dossier python (Python) à la racine du site afpy Plone4

--> En ZMI dans le dossier python ({your_portal_url}/python/manage) ajouter un 
    Objet PloneboardAnyXMLImportController (avec comme id : 'controller' 
    par exemple)

--> Lancer l'import via : {your_portal_url}/python/controller/manage
        avec :
            name of the xml file to be used: (in directory /inputxml)
            afpy_zope_forum_zope.data

--> attendre ~ 20mn pour l'import

--> supprimer l'objet d'import

--> redemarrer l'instance sinon le deuxième forum va se coller dans le même 
    dossier que le premier !

--> Faite de même pour le deuxième forum, créer un dossier zope (Zope) à la 
    racine du site afpy Plone4...


5/ Conversion des forums

Quelques boulettes subsistent dans le contenu des comments du forum. Le script 
convert_forums.py permet de les corriger.

--> Si vous souhaitez faire des modifs sur le script, il est préférable de 
    faire une sauvegarde de la Data.fs, pour la restaurer au cas où il faudrait
    faire des réajustements.

--> Lancer le script de conversion des forums au format html en lançant 
    la commande
        $ bin/instance run convert_forums.py
    vous pouvez spécifier l'id de l'instance du site Plone dans lequel se
    trouve les forums à traiter.
        $ bin/instance run convert_forums.py monsite

En cas de correction sur la conversion de forum, soit restaurer la Data.fs,
soit supprimer les deux forums, faire un réindex du catalog, et refaire les
imports (voir 4).
"""

import re
import transaction
import parser
import sys


instance_id = 'afpy'
if len(sys.argv) > 1:
    instance_id = sys.argv[3]
if instance_id not in app.keys():
    if instance_id != 'afpy.org':
        print "Le site '%s' n'existe pas. Renseignez le bon id de votre site \
contenant les forums à corriger !" % instance_id
        sys.exit(1)
    print """Vous n'avez pas de site afpy, passez en paramètre l'id de votre \
site Plone contenant les forums à corriger :
$ bin/instance run convert_forums.py monsite
"""
    sys.exit(2)

pl = app[instance_id]
comments = pl.portal_catalog(portal_type='PloneboardComment')
total = len(comments)
print "TOTAL %s" % total
for e, comment in enumerate(comments):
    print "Reste %s items" % str(int(total) - e)
    text = comment.getObject().getText()
    text = text.replace('\n', '<br />')
    text = re.sub(r'\[strong\](.*?)\[/strong\]',
                  r'<strong>\1</strong>',
                  text)
    text = re.sub(r'\[code\](.*?)\[/code\]',
                  r'<pre><code>\1</code></pre>',
                  text)
    text = re.sub(r'\[b\](.*?)\[/b\]',
                  r'<b>\1</b>',
                  text)
    text = re.sub(r'\[u\](.*?)\[/u\]',
                  r'<u>\1</u>',
                  text)
    text = re.sub(r'\[i\](.*?)\[/i\]',
                  r'<i>\1</i>',
                  text)

    # URL
    text = re.sub(r'\[(?i)url href="<a href="(.*?)">(.*?)</a>"\]<a href="(.*?)">(.*?)</a>\[/url\]',
                  r'<a href="\1">\4</a>',
                  text)
    # lien avec lien foireux dedans
    text = re.sub(r'\[(?i)url=<a href="(.*?)">(.*?)</a>\](.*?)\[/url\]',
                  r'<a href="\1">\3</a>',
                  text)
    text = re.sub(r'\[(?i)url href="<a href="(.*?)">(.*?)</a>"\](.*?)\[/url\]',
                  r'<a href="\1">\3</a>',
                  text)
    text = re.sub(r'\[(?i)url\]<a href="(.*?)">(.*?)</a>\[/url\]',
                  r'<a href="\1">\2</a>',
                  text)
    # liens avec lien foireux à l'interieur et urltitle
    text = re.sub(r'\[url= ?<a href="?(.*?)"?>.*?</a> urltitle="?(.*?)"?\]\[/url\]',
                  r'<a href="\1">\2</a>',
                  text)
    # lien correct avec urltitle
    text = re.sub(r'\[url="?(.*?)"? urltitle="?(.*?)"?\]\[/url\]',
                  r'<a href="\1">\2</a>',
                  text)

    # IMAGE
    # image avec lien foireux
    text = re.sub(r'\[(?i)img\]<a href="(.*?)">(.*?)</a>\[/img\]',
                  r'<a href="\1"><img src="\1" alt="\2"/></a>',
                  text)
    # images formatées correctement
    text = re.sub(r'\[(?i)img\](.*?)\[/img\]',
                  r'<img src="\1" alt="\1"></img>',
                  text)
#    # images avec url=
#    text = re.sub(r'\[img url="?(.*?)"?\](.*?)\[/img\]',
#                  r'<img src="\1" alt="\2"></img>', text)

    # AUTRE
    # citation avec identifiant
    text = re.sub(r'\[quote:(.*?) (.*?)\](.*?)\[/quote\]',
                  r'\1" a écrit:<blockquote>\3</blockquote>',
                  text)
    # citations avec identifiant
    text = re.sub(r'\[quote:(.*?)\](.*?)\[/quote\]',
                  r'\1" a écrit:<blockquote>\2</blockquote>',
                  text)
#    # balise code avec précision du langage après ":"
#    text = re.sub(
#            r'\[code:(.*?)\](.*?)\[/code\]',
#            r"""<p>code: "\1"</p>
#            <pre><code>\2</code></pre>""",
#            text)

    comment.getObject().setText(text)
    comment.getObject().reindexObject()

transaction.commit()
