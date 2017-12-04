#throw this script into crontab and it runs
# path to this file: ~/honeypot/lifecycle
# cronjob

#write authlog (located in host, not honeypot) to a different file
_now=$(date +"%F")
touch /home/hp/logs/auth101_$_now.txt #date stays constant

cat /home/hp/101auth.txt >> /home/hp/logs/auth101_$_now.txt 
#chmod this?

#destroy container
sudo vzctl stop 101
sudo vzctl destroy 101

#clear auth log
truncate -s 0 /home/hp/101auth.txt

#remake container
chmod a+x /home/hp/honeypot/make-honey/make101.sh #necessary?
/home/hp/honeypot/make-honey/make101.sh

#don't need tilde, messes with path
