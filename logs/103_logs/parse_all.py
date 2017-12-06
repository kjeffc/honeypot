from datetime import datetime, timedelta
import re
import sys

class Login: 
    def __init__(self, sshd, user, start, ip):
        self.sshd = sshd   
        self.user = user
        self.start = start
        self.ip = ip
        self.end = None
    def add_end(self, end):
        self.end = end

# general information
in_file = "103_log-2017-12-0"
curr_log = 1

ip_list = {}

# databases

while curr_log < 5:
    input_file = in_file + str(curr_log)
    with open(input_file) as f:
        for str_line in f:
            if "Accepted password for " in str_line and "ovzhost CRON" not in str_line:
                line = re.findall(r'\S+', str_line)
                ip = line[10]
                if ip in ip_list:
                    ip_list[ip].append(curr_log)
                else:
                    ip_list[ip] = [curr_log]
    curr_log += 1


for ips in ip_list:
    ip_list[ips] = list(set(ip_list[ips]))

once = []
twice = []
thrice = []
quad = []

for ips in ip_list:
    if len(ip_list[ips]) == 1:
        once.append(ips)
    elif len(ip_list[ips]) == 2:
        twice.append(ips)
    elif len(ip_list[ips]) == 3:
        thrice.append(ips)
    elif len(ip_list[ips]) == 4:
        quad.append(ips)
    else:
        print "I fucked up"
    
print "Appeared one time:", len(once)
print "Appeared two times:", len(twice)
print "Appeared three times:", len(thrice)
print "Appeared four times:", len(quad)
