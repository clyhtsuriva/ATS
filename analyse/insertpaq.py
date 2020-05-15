#!/usr/bin/python
# coding: utf-8


import psycopg2

# read a text file as a list of lines
# find the last line, change to a file you have
LireHeureTCP = open ( '/tmp/heuretcp.txt',"r" )
LireProtocoleTCP = open ( '/tmp/protocoletcp.txt',"r" )
LireIPSRCTCP = open ( '/tmp/ipsrctcp.txt',"r" )
LirePortSRCTCP = open ( '/tmp/portsrctcp.txt',"r" )
LireIPDSTTCP = open ( '/tmp/ipdsttcp.txt',"r" )
LirePortDSTTCP = open ( '/tmp/portdsttcp.txt',"r" )

LireHeureUDP = open ( '/tmp/heureudp.txt',"r" )
LireProtocoleUDP = open ( '/tmp/protocoleudp.txt',"r" )
LireIPSRCUDP = open ( '/tmp/ipsrcudp.txt',"r" )
LirePortSRCUDP = open ( '/tmp/portsrcudp.txt',"r" )
LireIPDSTUDP = open ( '/tmp/ipdstudp.txt',"r" )
LirePortDSTUDP = open ( '/tmp/portdstudp.txt',"r" )

DerniereLigneHeureTCP = LireHeureTCP.readlines()
LireHeureTCP.close()

DerniereLigneProtocoleTCP = LireProtocoleTCP.readlines()
LireProtocoleTCP.close()

DerniereLigneIPSRCTCP = LireIPSRCTCP.readlines()
LireIPSRCTCP.close()

DerniereLignePortSRCTCP = LirePortSRCTCP.readlines()
LirePortSRCTCP.close()

DerniereLigneIPDSTTCP = LireIPDSTTCP.readlines()
LireIPDSTTCP.close()

DerniereLignePortDSTTCP = LirePortDSTTCP.readlines()
LirePortDSTTCP.close()

#Coucou

DerniereLigneHeureUDP = LireHeureUDP.readlines()
LireHeureUDP.close()

DerniereLigneProtocoleUDP = LireProtocoleUDP.readlines()
LireProtocoleUDP.close()

DerniereLigneIPSRCUDP = LireIPSRCUDP.readlines()
LireIPSRCUDP.close()

DerniereLignePortSRCUDP = LirePortSRCUDP.readlines()
LirePortSRCUDP.close()

DerniereLigneIPDSTUDP = LireIPDSTUDP.readlines()
LireIPDSTUDP.close()

DerniereLignePortDSTUDP = LirePortDSTUDP.readlines()
LirePortDSTUDP.close()


#print "Heure TCP:"
a = str(DerniereLigneHeureTCP[-1])

#print "Protocole TCP:"
b = str(DerniereLigneProtocoleTCP[-1])

#print "IP Source TCP:"
c = str(DerniereLigneIPSRCTCP[-1])

#print "Port Source TCP:"
d = str(DerniereLignePortSRCTCP[-1])

#print "IP Destination TCP:"
e = str(DerniereLigneIPDSTTCP[-1])

#print "Port Destination TCP:"
f = str(DerniereLignePortDSTTCP[-1])


#Re coucou

#print "Heure UDP:"
z = str(DerniereLigneHeureUDP[-1])

#print "Protocole UDP:"
y = str(DerniereLigneProtocoleUDP[-1])

#print "IP Source UDP:"
x = str(DerniereLigneIPSRCUDP[-1])

#print "Port Source UDP:"
w = str(DerniereLignePortSRCUDP[-1])

#print "IP Destination UDP:"
v = str(DerniereLigneIPDSTUDP[-1])

#print "Port Destination UDP:"
u = str(DerniereLignePortDSTUDP[-1])


print a,b,c


def connexionBD():
	connexion=psycopg2.connect ("host='localhost' dbname='atsdb' user='atsuser' password='123456'")
	return connexion

conn=connexionBD()
cur=conn.cursor()
	
#sql="""
#insert into paquet(heure,protocole,ip_source,ip_destination,port_source,port_destination) values ('{}','{}','{}','{}','{}','{}');
#insert into paquet(heure,protocole,ip_source,ip_destination,port_source,port_destination) values ('{}','{}','{}','{}','{}','{}');
#""".format(a,b,c,e,d,f,z,y,x,v,w,u)

cur.execute("INSERT INTO paquet (heure,protocole,ip_source,ip_destination,port_source,port_destination) VALUES (%s, %s, %s, %s, %s, %s)",
        (a, b, c, e, d, f))
cur.execute("INSERT INTO paquet (heure,protocole,ip_source,ip_destination,port_source,port_destination) VALUES (%s, %s, %s, %s, %s, %s)",
        (z, y, x, v, w, u))

#cur.execute(sql)

conn.commit()
conn.close()
