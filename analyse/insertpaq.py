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


DerniereLigneHeureTCP = LireHeureTCP.read().splitlines()
LireHeureTCP.close()

DerniereLigneProtocoleTCP = LireProtocoleTCP.read().splitlines()
LireProtocoleTCP.close()

DerniereLigneIPSRCTCP = LireIPSRCTCP.read().splitlines()
LireIPSRCTCP.close()

DerniereLignePortSRCTCP = LirePortSRCTCP.read().splitlines()
LirePortSRCTCP.close()

DerniereLigneIPDSTTCP = LireIPDSTTCP.read().splitlines()
LireIPDSTTCP.close()

DerniereLignePortDSTTCP = LirePortDSTTCP.read().splitlines()
LirePortDSTTCP.close()

#Coucou

DerniereLigneHeureUDP = LireHeureUDP.read().splitlines()
LireHeureUDP.close()

DerniereLigneProtocoleUDP = LireProtocoleUDP.read().splitlines()
LireProtocoleUDP.close()

DerniereLigneIPSRCUDP = LireIPSRCUDP.read().splitlines()
LireIPSRCUDP.close()

DerniereLignePortSRCUDP = LirePortSRCUDP.read().splitlines()
LirePortSRCUDP.close()

DerniereLigneIPDSTUDP = LireIPDSTUDP.read().splitlines()
LireIPDSTUDP.close()

DerniereLignePortDSTUDP = LirePortDSTUDP.read().splitlines()
LirePortDSTUDP.close()


#print "Heure TCP:"
HeureTCP = str(DerniereLigneHeureTCP[-1])

#print "Protocole TCP:"
ProtocoleTCP = str(DerniereLigneProtocoleTCP[-1])

#print "IP Source TCP:"
IPsrcTCP = str(DerniereLigneIPSRCTCP[-1])

#print "Port Source TCP:"
PortsrcTCP = str(DerniereLignePortSRCTCP[-1])

#print "IP Destination TCP:"
IPdstTCP = str(DerniereLigneIPDSTTCP[-1])

#print "Port Destination TCP:"
PortdstTCP = str(DerniereLignePortDSTTCP[-1])


#Re coucou

#print "Heure UDP:"
HeureUDP = str(DerniereLigneHeureUDP[-1])

#print "Protocole UDP:"
ProtocoleUDP = str(DerniereLigneProtocoleUDP[-1])

#print "IP Source UDP:"
IPsrcUDP = str(DerniereLigneIPSRCUDP[-1])

#print "Port Source UDP:"
PortsrcUDP = str(DerniereLignePortSRCUDP[-1])

#print "IP Destination UDP:"
IPdstUDP = str(DerniereLigneIPDSTUDP[-1])

#print "Port Destination UDP:"
PortdstUDP = str(DerniereLignePortDSTUDP[-1])


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
        (HeureTCP, 'TCP', IPsrcTCP, IPdstTCP, PortsrcTCP, PortdstTCP))
cur.execute("INSERT INTO paquet (heure,protocole,ip_source,ip_destination,port_source,port_destination) VALUES (%s, %s, %s, %s, %s, %s)",
        (HeureUDP, 'UDP', IPsrcUDP, IPdstUDP, PortsrcUDP, PortdstUDP))

#cur.execute(sql)

conn.commit()
conn.close()
