#!/usr/bin/python3
# -*- coding: utf-8 -*-

import mod_python
from fonctions import baseHTML, connexionBD, lien

def index(req):
    req.content_type="text/html"
    ipdst=str()
    portdst=str()
    ipsrc=str()
    portsrc=str()

#sql part    
    conn=connexionBD()
    cur=conn.cursor()
###    
    sql=["SELECT COUNT(*) FROM paquet","SELECT COUNT(DISTINCT ip_source) FROM paquet","SELECT COUNT(DISTINCT ip_destination) FROM paquet","SELECT COUNT(DISTINCT port_source) FROM paquet","SELECT COUNT(DISTINCT port_destination) FROM paquet","SELECT COUNT(*) FROM paquet WHERE (heure>=( SELECT LOCALTIME - interval '1 hour' ) AND heure<= (SELECT LOCALTIME));"]
    var=["total","total_ip_src","total_ip_dst","total_port_src","total_port_dst","total_uneheure"]
    for x,y in zip(sql,var):
        cur.execute(x)
        conn.commit()
        globals()[y]=str(cur.fetchone()[0])
#        
    sql=["SELECT ip_destination, COUNT(ip_destination) FROM paquet GROUP BY ip_destination ORDER BY count DESC","SELECT port_destination, COUNT(port_destination) FROM paquet GROUP BY port_destination ORDER BY count DESC","SELECT ip_source, COUNT(ip_source) FROM paquet GROUP BY ip_source ORDER BY count DESC","SELECT port_source, COUNT(port_source) FROM paquet GROUP BY port_source ORDER BY count DESC"]
    var=["each_ip_dst","each_port_dst","each_ip_src","each_port_src"]
    for x,y in zip(sql,var):
        cur.execute(x)
        conn.commit()
        globals()[y]=cur.fetchall()
###
    conn.close()

#sql part

    champs=["ip","port"]
    suff=["dst","src"]
    global each_ip_dst
    global each_ip_src
    global each_port_dst
    global each_port_src
    global ipdst
    global ipsrc
    global portdst
    global portsrc

    for j in champs:
        for k in suff:
            nom="each_"+j+"_"+k
            for i in globals()[nom]:
                if j=="ip" and k=="dst":
                    globals()[j+k]+=("""<tr>
<td>""" +lien('ip_destination.py?ip='+str(i[0]), str(i[0]) )+ """</td>
<td>""" + str(i[1]) + """</td>
                        </tr>""")
                
                elif j=="port" and k=="dst":
                    globals()[j+k]+=("""<tr>
<td>""" +lien('port_destination.py?port='+str(i[0]), str(i[0]) )+ """</td>
<td>""" + str(i[1]) + """</td>
                        </tr>""")

                elif j=="ip" and k=="src":
                    globals()[j+k]+=("""<tr>
<td>""" + lien('ip_source.py?ip='+str(i[0]), str(i[0]) ) + """</td>
<td>""" + str(i[1]) + """</td>
                        </tr>""")

                else:
                    globals()[j+k]+=("""<tr>
<td>""" + lien('port_source.py?port='+str(i[0]), str(i[0]) ) + """</td>
<td>""" + str(i[1]) + """</td>
                        </tr>""")

#write the html page

    req.write(baseHTML("ATS - Bilan","""
<h1>Bilan</h1>
<div id="tip" style="display:block;">
Afin de voir le reverse DNS d'une adresse IP, cliquez sur cette dernière dans le tableau <button id="ok" onclick="toggle_div(this,'tip');">OK</button></div>
<ul>
<li>Nombre total de paquets : <b>"""+total+"""</b></li>
<li>Nombre total de paquets depuis 1h : <b>"""+total_uneheure+"""</b></li>
<li>Nombre total d'adresses IP source differentes : <b>"""+total_ip_src+"""</b></li>
<li>Nombre total d'adresses IP destination differentes : <b>"""+total_ip_dst+"""</b></li>
<li>Nombre total de ports source differents : <b>"""+total_port_src+"""</b></li>
<li>Nombre total de ports destination differents : <b>"""+total_port_dst+"""</b></li>
</ul>
<div id="bilan_tab">
<table class="inlineTable">
<tr><th>IP destination</th><th>Récurrence</th></tr>
"""+str(ipdst)+"""
</table>
<table class="inlineTable">
<tr><th>Port destination</th><th>Récurrence</th></tr>
"""+str(portdst)+"""
</table>
<table class="inlineTable">
<tr><th>IP source</th><th>Récurrence</th></tr>
"""+str(ipsrc)+"""
</table>
<table class="inlineTable">
<tr><th>Port source</th><th>Récurrence</th></tr>
"""+str(portsrc)+"""
</table>
</div>
<script src="tip.js"></script>
"""
))
