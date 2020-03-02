#!/bin/bash

while :
do

	sudo tcpdump -i eth1 -nn -c1 -A src 192.168.52.19 -w capture.pcap
	sudo tcpdump -r capture.pcap > grostas
	cat grostas | cut -d" " -f1 >> /tmp/heure.txt
	cat grostas | cut -d" " -f2 >> /tmp/protocole.txt
	cat grostas | cut -d" " -f3 >> /tmp/source.txt
	cat grostas | cut -d" " -f5 >> /tmp/destination.txt
	tail -n1 /tmp/heure.txt
	tail -n1 /tmp/protocole.txt
	tail -n1 /tmp/source.txt
	tail -n1 /tmp/destination.txt
done



