#!/bin/bash

file="/home/hp/scripts/containerNames.txt"
while IFS= read -r line
do
	echo $line
	sudo vzctl create $line
	sudo vzctl set $line --netif_add eth0 --save
	sudo vzctl start $line
	sudo vzctl exec $line ifconfig eth0 128.8.238.$line netmask 255.255.255.192
	sudo vzctl exec $line route add default gw 128.8.238.65
	sudo brctl addif br0 veth$line.0
	sudo vzctl set $line --nameserver 8.8.8.8 --save
done
