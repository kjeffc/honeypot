DATE=`date +%Y-%m-%d`

touch /home/ubuntu/workspace/honeypot/ssh-parse-$DATE

echo "Statistics for $DATE" >> /root/ssh-stats-$DATE

echo "---" >> /root/ssh-stats-$DATE


logins=$(cat /home/hp/101_logs/101_auth_1.log | grep "snoopy" | wc -l)
users=$(cat /home/hp/101_logs/101_auth_1.log | grep -o "invalid user [a-zA-Z0-9]*" | uniq | wc -l)
ips=$(cat /home/hp/101_logs/101_auth_1.log | grep -Eo "from [0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}" | uniq | wc -l)

echo "Number of SSH login attempts: $logins" >> /root/ssh-stats-$DATE
echo "Number of different usernames: $users" >> /root/ssh-stats-$DATE
echo "Number of offending IP: $ips" >> /root/ssh-stats-$DATE

echo "---" >> /root/ssh-stats-$DATE
echo "Username list:" >> /root/ssh-stats-$DATE
echo "" >> /root/ssh-stats-$DATE

name=$(cat /home/hp/101_logs/101_auth_1.log | grep -o "invalid user [a-zA-Z0-9]*" | uniq | cut -d " " -f 3)
arr=($name)
for i in "${arr[@]}"
do
        tmp=$(cat /home/hp/101_logs/101_auth_1.log | grep -o "invalid user $i" | wc -l)
        echo "$tmp $i" >> /root/ssh-stats-$DATE
done

echo "---" >> /root/ssh-stats-$DATE
echo "Offending IPs list:" >> /root/ssh-stats-$DATE
echo "" >> /root/ssh-stats-$DATE

iplist=$(cat /home/hp/101_logs/101_auth_1.log | grep -Eo "from [0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}" | uniq | cut -d " " -f 2)

iparr=($iplist)

for i in "${iparr[@]}"
do
        tmp=$(cat /home/hp/101_logs/101_auth_1.log | grep -Eo "from $i" | wc -l)
        echo "$tmp $i" >> /root/ssh-stats-$DATE
done

cp /home/hp/101_logs/101_auth_1.log /home/hp/101_logs/old_logs/ssh-log-$DATE
echo -n > /home/hp/101_logs/101_auth_1.log