#!/usr/bin/python3
# -*- coding: utf-8 -*-

import mod_python                     
from fonctions import baseHTML, connexionBD, lien

def index(req):
    req.content_type="text/html"
    content=str()

    condition=req.form["condition"]
    
    conn=connexionBD()
    cur=conn.cursor()
    sql="select * from paquet where {} ORDER BY heure DESC;".format(condition)
    cur.execute(sql)
    conn.commit()
    data=cur.fetchall()
    conn.close()

    for i in data :
        content+=("""<tr>""" +
"""<td>""" + str(i[1]) + """</td>""" +
"""<td>""" + str(i[2]) + """</td>""" +
"""<td>""" + lien('ip_source.py?ip=' + str(i[3]), str(i[3])) + """</td>""" +
"""<td>""" + lien('ip_destination.py?ip=' + str(i[4]), str(i[4])) + """</td>""" +
"""<td>""" + lien('port_source.py?port=' + str(i[5]), str(i[5])) + """</td>""" +
"""<td>""" + lien('port_destination.py?port=' + str(i[6]), str(i[6])) + """</td>""" +
"""</tr>""")

    req.write("""
<table class="data_tab">
<tr><th>Heure</th><th>Protocole</th><th>IP Source</th><th>IP Destination</th><th>Port Source</th><th>Port Destination</th></tr>
"""
+ content + 
"""
</table>""")
