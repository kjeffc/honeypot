
sudo vzctl create 102
sudo vzctl set 102 --netif_add eth0 --save
sudo vzctl start 102
sudo vzctl exec 102 ifconfig eth0 128.8.238.102 netmask 255.255.255.192
sudo vzctl exec 102 route add default gw 128.8.238.65
sudo brctl addif br0 veth102.0
sudo vzctl set 102 --nameserver 8.8.8.8 --save
