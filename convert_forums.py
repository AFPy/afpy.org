#!/usr/bin/env python
# coding:utf-8
"""
(notes tshirtman)

1/ mise en place de l'environement de travail
déploiement afpy.org sur un plone 2.0 avec python 2.3
déploiement nouveau afpy avec un plone 4

2/ export des forums
export des forums du plone 2 via interface CMFPlone (afpy_python_forum_python.data et afpy_zope_forum_zope.data par exemple)

3/ préparation des imports
installation de ploneboard_anyxmlimport dans products de plone 4
ajout du module Interface de Plone 3 dans le dossier du module de ploneboard_anyxmlimport
commenter la ligne de log dans ploneboard_anyxmlimport/

Création d'un lien symbolique entre products/ploneboard_anyxmlimport et parts/instance/Products/ploneboard_anyxmlimport
/!\ ne pas oublier de renouveler cette dernière étape si un buildout est
relancé plus tard

copie des fichiers d'export de CMFBoard dans le dossier imputxml de ploneboard_anyxmlimport

sauvegarde du Data.fs

4/ imports

création d'un dossier python (Python) et un dossier zope (Zope) dans afpy/ sur le plone4

création d'un Objet PloneboardAnyXMLImportController dans le dossier python

ouvrir cet objet et remplacer le nom par afpy_python_forum_python)

attendre ~ 20mn pour l'import

supprimer l'objet d'import

aller dans le dossier plone

créer un object PloneboardAnyXMLImportController

redémarrer le plone! (sinon les deux forums seront dans le dossier du premier import).

importer le forum zope de la même façon que le forum python.

arreter le plone

sauvegarder Data.fs

5/ conversion des forums
lancer le script de conversion des forums au format html en lançant la commande

    bin/instance run convert_forums.py

En cas de correction sur la conversion de forum, soit restaurer le data.fs,
soit supprimer les deux forums, faire un réindex du catalog, et refaire les
imports (voir 4).


"""
import re
import transaction
import parser

pl = app['afpy']
comments = pl.portal_catalog(portal_type='PloneboardComment')

for comment in comments:
    text = comment.getObject().getText()
    # replace <> in a <pre> with &lt; and &gt;
    #if "[code]" in text:
        ## TODO
    text = text.replace('\n','<br />')
    text = text.replace('[b]','<b>').replace('[/b]','</b>')
    text = text.replace('[i]','<i>').replace('[/i]','</i>')
    text = text.replace('[code]','<pre><code>').replace('[/code]','</code></pre>')
    text = text.replace('[u]','<u>').replace('[/u]','</u>')
    text = text.replace('[u]','<u>').replace('[/u]','</u>')
    text = text.replace('[strong]','<strong>').replace('[/strong]','</strong>')

    # balise code avec précision du langage après ":"
    text = re.sub(
            r'\[code:(.*?)\](.*?)\[/code\]',
            r"""<p>code: "\1"</p>
            <pre><code>\2</code></pre>""",
            text)

    # citation avec identifiant
    text = re.sub(
            r'\[quote:(.*?) (.*?)\](.*?)\[/quote\]',
            r"""<p> Précedemment "\1" a écrit:"</p>
            <blockquote>\3</blockquote>""",
            text)

    # citations avec identifiant
    text = re.sub(
            r'\[quote:(.*?)\](.*?)\[/quote\]',
            r"""<p> Précedemment "\1" a écrit:"</p>
            <blockquote>\2</blockquote>""",
            text)

    # image avec lien foireux
    text = re.sub(
            r'\[img\]<a href="(.*?)">.*?</a>\[/img\]',
            r'<img src="\1" alt="no alternative text"></img>',
            text)

    # images formatées correctement (je ne sais même pas s'il y en a)
    text = re.sub(
            r'\[img\](.*?)\[/img\]',
            r'<img src="\1" alt="no alternative text"></img>',
            text)

    # images avec url=
    text = re.sub(
            r'\[img url="?(.*?)"?\](.*?)\[/img\]',
            r'<img src="\1" alt="\2"></img>',
            text)

    # liens avec lien foireux à l'interieur et urltitle
    text = re.sub(
            r'\[url= ?<a href="?(.*?)"?>.*?</a> urltitle="?(.*?)"?\]\[/url\]',
            r'<a href="\1">\2</href>',
            text)

    # lien avec lien foireux dedans
    text = re.sub(
            r'\[url href="<a href="?(.*?)"?>\](.*?)\[/url\]',
            r'<a href="\1">\2</href>',
            text)

    # lien correct avec urltitle
    text = re.sub(
            r'\[url="?(.*?)"? urltitle="?(.*?)"?\]\[/url\]',
            r'<a href="\1">\2</href>',
            text)

    # lien correct sans urltitle
    text = re.sub(
            r'\[url href=(.*?)\](.*?)\[/url\]',
            r'<a href="\1">\2</href>',
            text)

    comment.getObject().setText(text)

transaction.commit()

