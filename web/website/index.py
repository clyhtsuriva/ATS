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
        content+=("""<tr>""" + 
"""<td>""" + str(i[1]) + """</td>""" +
"""<td>""" + str(i[2]) + """</td>""" +
"""<td>""" + str(i[3]) + """</td>""" +
"""<td>""" + str(i[4]) + """</td>""" +
"""</tr>""")
    
    req.write(baseHTML("ATS-Project","""
<center><h1>ATS-Project</h1></center>
<table>
<tr><th>Heure</th><th>Protocole</th><th>Source</th><th>Destination</th></tr>
"""
+ content + 
"""
</table>
"""))

