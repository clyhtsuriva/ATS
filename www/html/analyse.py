#!/usr/bin/python3
# -*- coding: utf-8 -*-

import mod_python
from fonctions import baseHTML, connexionBD, lien

def index(req):
    req.content_type="text/html"
    content=str()

#sql part    
#    conn=connexionBD()
#    cur=conn.cursor()
#    sql="select * from paquet;"
#    cur.execute(sql)
#    conn.commit()
#    data=cur.fetchall()
#    conn.close()
#sql part


#write the html page

    req.write(baseHTML("ATS-Project","""
<h1>Analyse</h1>
"""
+ content
))
