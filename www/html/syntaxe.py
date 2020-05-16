#!/usr/bin/python3
# -*- coding: utf-8 -*-

import mod_python
from fonctions import baseHTML, connexionBD, lien

def index(req):
    req.content_type="text/html"
    content=str()

#write the html page
    req.write(baseHTML("ATS-Project","""
<h1>Syntaxe</h1>
<p>La """+lien('syntaxe.py','syntaxe')+""" pour utiliser les filtres disponibles sur la page """+lien('filtrage.py','filtrage')+""" est la suivante :</p>
<p>&lt;colonne&gt;='&lt;valeur&gt;'</p><br/>
<table>
<tr><th>colonne</th><th>valeur</th><th>exemple</th></tr>
<tr><td>heure</td><td>hh:mm:ss</td><td>heure='10:41:30'</td></tr>
<tr><td>protocole</td><td>texte</td><td>protocole='TCP'</td></tr>
<tr><td>ip_source</td><td>W.X.Y.Z</td><td>ip_source='10.0.2.15'</td></tr>
<tr><td>ip_destination</td><td>W.X.Y.Z</td><td>ip_destination='1.1.1.1'</td></tr>
<tr><td>port_source</td><td>X</td><td>port_source='35042'</td></tr>
<tr><td>port_destination</td><td>X</td><td>port_destination='80'</td></tr>
</table>
"""))
