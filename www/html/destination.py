#!/usr/bin/python3
# -*- coding: utf-8 -*-

import mod_python
from fonctions import baseHTML, connexionBD, lien
import socket

def index(req):
    req.content_type="text/html"
   
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

#sql part    
    conn=connexionBD()
    cur=conn.cursor()
    sql="select * from paquet where ip_destination='{}';".format(ip)
    cur.execute(sql)
    conn.commit()
    data=cur.fetchall()
    conn.close()
#sql part

#takes every lines from the select
    for i in data :
        content+=("""<tr>""" +
"""<td>""" + str(i[1]) + """</td>""" +
"""<td>""" + str(i[2]) + """</td>""" +
"""<td>""" + str(i[3]) + """</td>""" +
"""<td>""" + lien('destination.py?ip=' + str(i[4]), str(i[4])) + """</td>""" +
"""<td>""" + str(i[5]) + """</td>""" +
"""<td>""" + str(i[6]) + """</td>""" +
"""</tr>""")
    
#write the html page
    req.write(baseHTML("Destination","""
<center><h1>IP Destination : """ + ip + """</h1></center>
<center><table>
<tr><th>Heure</th><th>Protocole</th><th>IP Source</th><th>IP Destination</th><th>Port Source</th><th>Port Destination</th></tr>
"""
+ content + 
"""
</table></center>
"""))
