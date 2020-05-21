#!/usr/bin/python3
# -*- coding: utf-8 -*-

import mod_python
from fonctions import baseHTML, connexionBD, lien
import socket

def index(req):
    req.content_type="text/html"

#partie socket

#check si ip est bien la
    try:
        ip=req.form["ip"]
    except KeyError:
        mod_python.util.redirect(req, "index.py")

#check si ip a le bon format
    try:
        socket.inet_aton(ip)
    except socket.error:
        mod_python.util.redirect(req, "index.py")

    content=str()

#reverse dns
    try:
        rdns=socket.gethostbyaddr(ip)[0]
    except socket.herror:
        rdns="<em>Non connu</em>"

#partie socket

#sql part    
    conn=connexionBD()
    cur=conn.cursor()

    sql="SELECT * FROM paquet WHERE ip_destination=%s ORDER BY heure DESC"
    sql_count="SELECT COUNT(*) FROM paquet WHERE ip_destination=%s"

    cur.execute(sql, (ip, ))
    conn.commit()
    data=cur.fetchall()

    cur.execute(sql_count, (ip, ))
    conn.commit()
    count=cur.fetchone()

    conn.close()
#sql part

#takes every lines from the select
    for i in data :
        content+=("""<tr>""" +
"""<td>""" + str(i[1]) + """</td>""" +
"""<td>""" + str(i[2]) + """</td>""" +
"""<td>""" + lien('ip_source.py?ip=' + str(i[3]), str(i[3])) + """</td>""" +
"""<td>""" + lien('ip_destination.py?ip=' + str(i[4]), str(i[4])) + """</td>""" +
"""<td>""" + lien('port_source.py?port=' + str(i[5]), str(i[5])) + """</td>""" +
"""<td>""" + lien('port_destination.py?port=' + str(i[6]), str(i[6])) + """</td>""" +
"""</tr>""")


#write the html page
    req.write(baseHTML("ATS - " + ip,"""
<h1>IP destination : """ + ip + """</h1>
<p>Nombre de paquets en destination de """+ ip + """ : <b>"""+ str(count[0])+ """</b></p>
<p>Reverse DNS : <b>"""+rdns+"""</b><p>
<div id="tab">
<table class="data_tab">
<tr><th>Heure</th><th>Protocole</th><th>IP Source</th><th>IP Destination</th><th>Port Source</th><th>Port Destination</th></tr>
"""
+ content + 
"""
</table>
</div>
"""))
