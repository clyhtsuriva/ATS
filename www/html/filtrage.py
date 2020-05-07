#!/usr/bin/python3
# -*- coding: utf-8 -*-

import mod_python
from fonctions import baseHTML, connexionBD, lien

def index(req):
    req.content_type="text/html"
    content=str()

#write the html page
    req.write(baseHTML("ATS-Project","""
<center><h1>Filtrage</h1></center>
<b>Filtre</b>
<input type="text" id="condition" onkeyup="cherche()">
<div id="tab">
</div>
<script src="filtre.js"></script>
"""))
