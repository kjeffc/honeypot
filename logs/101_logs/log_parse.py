import re

input_file = "101_log-2017-12-01"

class Login: 
    def __init__(self, sshd, user, start):
        self.sshd = sshd   
        self.user = user
        self.start = start
    def add_end(self, end):
        self.end = end

# general information
logins = 0
logouts = 0
names = {}
ip_list = {}
time_spent = []

# databases
db_day1 = {}
db_day2 = {}

with open(input_file) as f:
    for str_line in f:
        if "Accepted password for " in str_line and "ovzhost CRON" not in str_line:
            line = re.findall(r'\S+', str_line)
            day = line[1]
            time = line[2]
            tmp_sshd = line[4]
            usr = line[8]
            ip = line[10]
            
            # just general data
            logins += 1
            if usr in names:
                names[usr] += 1
            else:
                names[usr] = 1
            if ip in ip_list:
                ip_list[ip] += 1
            else:
                ip_list[ip] = 1
            
            new_login = Login(tmp_sshd, usr, time)
            
            if tmp_sshd in db_day1:
                db_day2[tmp_sshd] = new_login
            else:
                db_day1[tmp_sshd] = new_login
        elif "session closed for user" in str_line and "ovzhost CRON" not in str_line:
            day = line[1]
            time = line[2]
            tmp_sshd = line[4]

            logouts += 1
            line = re.findall(r'\S+', str_line)
            
            if tmp_sshd in db_day2:
                db_day2[tmp_sshd].add_end(time)
            else:
                db_day1[tmp_sshd].add_end(time)
            

print "logins:", logins
print "logouts:", logouts
print "names:", names