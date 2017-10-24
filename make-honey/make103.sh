
sudo vzctl create 103
sudo vzctl set 103 --netif_add eth0 --save
sudo vzctl start 103
sudo vzctl exec 103 ifconfig eth0 128.8.238.103 netmask 255.255.255.192
sudo vzctl exec 103 route add default gw 128.8.238.65
sudo brctl addif br0 veth103.0
sudo vzctl set 103 --nameserver 8.8.8.8 --save
