#!/usr/bin/python3
# -*- coding: utf-8 -*-

import mod_python
from fonctions import baseHTML, connexionBD, lien

def index(req):
    req.content_type="text/html"
    content=str()

#write the html page
    req.write(baseHTML("Filtrage","""
<h1>Filtrage</h1>
<div id="tip" style="display:block;">
Pour voir le nombre de paquets en destination d'une adresse IP, cliquez sur cette dernière dans le tableau <button id="ok" onclick="toggle_div(this,'tip');">OK</button></div>
<b>Filtre</b>
<input type="text" id="condition" onkeyup="cherche()">
<div id="tab">
</div>
<script src="filtre.js"></script>
<script src="tip.js"></script>                   
"""))
