
sudo vzctl create 101
sudo vzctl set 101 --netif_add eth0 --save
sudo vzctl start 101
sudo vzctl exec 101 ifconfig eth0 128.8.238.101 netmask 255.255.255.192
sudo vzctl exec 101 route add default gw 128.8.238.65
sudo brctl addif br0 veth101.0
sudo vzctl set 101 --nameserver 8.8.8.8 --save
