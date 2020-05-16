#!/usr/bin/python3
# -*- coding: utf-8 -*-

import mod_python
from fonctions import baseHTML, connexionBD, lien

def index(req):
    req.content_type="text/html"
    content=str()

#sql part    
    conn=connexionBD()
    cur=conn.cursor()
###    
    cur.execute("SELECT COUNT(*) FROM paquet")
    conn.commit()
    total=str(cur.fetchone()[0])
#   
    cur.execute("SELECT COUNT(DISTINCT ip_source) FROM paquet")
    conn.commit()    
    total_ip_src=str(cur.fetchone()[0])
#
    cur.execute("SELECT COUNT(DISTINCT ip_destination) FROM paquet")
    conn.commit()    
    total_ip_dst=str(cur.fetchone()[0])
#
    cur.execute("SELECT COUNT(DISTINCT port_source) FROM paquet")
    conn.commit()    
    total_port_src=str(cur.fetchone()[0])
#
    cur.execute("SELECT COUNT(DISTINCT port_destination) FROM paquet")
    conn.commit()
    total_port_dst=str(cur.fetchone()[0])
#
    cur.execute("SELECT COUNT(*) FROM paquet WHERE (heure>=( SELECT LOCALTIME - interval '1 hour' ) AND heure<= (SELECT LOCALTIME));")
    conn.commit()
    total_uneheure=str(cur.fetchone()[0])
#
    cur.execute("SELECT ip_destination, COUNT(ip_destination) FROM paquet GROUP BY ip_destination")
    conn.commit()
    each_ip_dest=cur.fetchall()
###
    conn.close()
#sql part

#loop
    for i in each_ip_dest :
        content+=("""<tr>
<td>""" + str(i[0]) + """</td>
<td>""" + str(i[1]) + """</td>
                </tr>""")
#loop

#write the html page

    req.write(baseHTML("ATS-Project","""
<h1>Bilan</h1>
<ul>
<li>Nombre total de paquets : <b>"""+total+"""</b></li>
<li>Nombre total de paquets depuis 1h : <b>"""+total_uneheure+"""</b></li>
<li>Nombre total d'adresses IP source differentes : <b>"""+total_ip_src+"""</b></li>
<li>Nombre total d'adresses IP destination differentes : <b>"""+total_ip_dst+"""</b></li>
<li>Nombre total de ports source differents : <b>"""+total_port_src+"""</b></li>
<li>Nombre total de ports destination differents : <b>"""+total_port_dst+"""</b></li>
</ul>
<br/>
<table>
<tr><th>IP destination</th><th>Recurrence</th></tr>
"""+str(content)+"""
</table>
<canvas id="protocole" width="20vh" height="40vw"></canvas>
<script src="/Chart.js"></script>
<script src="/pie.js"></script>
"""
))
