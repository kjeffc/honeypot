#!/bin/bash

file="/home/hp/scripts/commands.txt"

cat $file | while read LINE
do
	num=$(( $RANDOM % 6 + 5))
	echo "alias $LINE='sleep $num;$LINE'" >> /../../vz/private/103/root/.bashrc
done
