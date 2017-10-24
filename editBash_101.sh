#!/bin/bash

file="/home/hp/scripts/commands.txt"

cat $file | while read LINE
do
	echo $LINE
	num=$(( $RANDOM % 3 + 1))
	echo $num
	echo "alias $LINE='sleep $num;$LINE'" >> /../../vz/private/101/root/.bashrc
done
