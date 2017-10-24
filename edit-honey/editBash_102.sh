#!/bin/bash

file="edit-honey/commands.txt"

cat $file | while read LINE
do
	num=$(( $RANDOM % 4 + 2))
	echo "alias $LINE='sleep $num;$LINE'" >> /vz/private/102/root/.bashrc
done
echo "alias alias='sleep 3;'" >> /vz/private/102/root/.bashrc
