#!/usr/bin/python3
# -*- coding: utf-8 -*-

import mod_python
import fonctions

def index(req):
    req.content_type="text/html"
    req.write(fonctions.baseHTML("Test","""
This is a test page.</p>
"""))
