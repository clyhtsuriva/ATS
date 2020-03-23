#!/usr/bin/python3
# -*- coding: utf-8 -*-

import mod_python
from fonctions import baseHTML, connexionBD

def index(req):
    req.content_type="text/html"
    
    content=str()

#sql part    
    conn=connexionBD()
    cur=conn.cursor()
    sql="select * from trame;"
    cur.execute(sql)
    conn.commit()
    data=cur.fetchall()
    conn.close()
#sql part

    for i in data :
        content+=("""<ul><li>""" + str(i[1]) + str(i[2]) + str(i[3]) + str(i[4]) + """</li></ul>""")
    
    req.write(baseHTML("ATS-Project","""
<center><h1>ATS-Project</h1></center>"""
+ content))

