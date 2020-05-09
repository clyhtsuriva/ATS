#!/usr/bin/python3
# -*- coding: utf-8 -*-

import mod_python                     
from fonctions import baseHTML, connexionBD, lien

def index(req):
    req.content_type="text/html"
    content=str()
    
    conn=connexionBD()
    cur=conn.cursor()

    sql="SELECT * FROM paquet ORDER BY heure DESC;"

    cur.execute(sql)
    conn.commit()
    data=cur.fetchall()

    conn.close()

    for i in data:
        content+=("""<tr>""" +
"""<td>""" + str(i[1]) + """</td>""" +
"""<td>""" + str(i[2]) + """</td>""" +
"""<td>""" + str(i[3]) + """</td>""" +
"""<td>""" + lien('destination.py?ip=' + str(i[4]), str(i[4])) + """</td>""" +
"""<td>""" + str(i[5]) + """</td>""" +
"""<td>""" + str(i[6]) + """</td>""" +
"""</tr>""")

    req.write("""
<table class="data_tab">
<tr><th>Heure</th><th>Protocole</th><th>IP Source</th><th>IP Destination</th><th>Port Source</th><th>Port Destination</th></tr>
"""
+ content + 
"""
</table>""")
