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
    
    cur.execute("SELECT COUNT(*) FROM paquet")
    conn.commit()
    total=str(cur.fetchone()[0])
    
    cur.execute("SELECT COUNT(DISTINCT ip_source) FROM paquet")
    conn.commit()    
    total_ip_src=str(cur.fetchone()[0])

    cur.execute("SELECT COUNT(DISTINCT ip_destination) FROM paquet")
    conn.commit()    
    total_ip_dst=str(cur.fetchone()[0])

    cur.execute("SELECT COUNT(DISTINCT port_source) FROM paquet")
    conn.commit()    
    total_port_src=str(cur.fetchone()[0])

    cur.execute("SELECT COUNT(DISTINCT port_destination) FROM paquet")
    conn.commit()
    total_port_dst=str(cur.fetchone()[0])

    conn.close()
#sql part

#write the html page

    req.write(baseHTML("ATS-Project","""
<h1>Analyse</h1>
<p>Nombre total de paquets : <b>"""+total+"""</b></p>
<p>Nombre total d'adresses IP source differentes : <b>"""+total_ip_src+"""</b></p>
<p>Nombre total d'adresses IP destination differentes : <b>"""+total_ip_dst+"""</b></p>
<p>Nombre total de ports source differents : <b>"""+total_port_src+"""</b></p>
<p>Nombre total de ports destination differents : <b>"""+total_port_dst+"""</b></p>
"""
))
