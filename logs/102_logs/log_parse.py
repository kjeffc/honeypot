from datetime import datetime, timedelta
import re

input_file = "102_log-2017-12-03"

class Login: 
    def __init__(self, sshd, user, start):
        self.sshd = sshd   
        self.user = user
        self.start = start
        self.end = None
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
            
            # for general data
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
            line = re.findall(r'\S+', str_line)
            day = line[1]
            time = line[2]
            tmp_sshd = line[4]

            logouts += 1
            line = re.findall(r'\S+', str_line)
            
            if tmp_sshd in db_day2:
                db_day2[tmp_sshd].add_end(time)
            else:
                db_day1[tmp_sshd].add_end(time)
            

# done with parsing at this point, we have 2 db's 
FMT = '%H:%M:%S'
longest_name = ''
shortest_name = ''
longest = timedelta.min
shortest = timedelta.max
total_stay = timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0)
cut_off = 0

for login in db_day1:
    if db_day1[login].end:
        tdelta = datetime.strptime(db_day1[login].end, FMT) - datetime.strptime(db_day1[login].start, FMT)
        if tdelta.days < 0:
            change = timedelta(days=1)
            tdelta = tdelta + change

        time_spent.append(tdelta)
        
        if (tdelta > longest):
            longest_name = login
            longest = tdelta
        elif (tdelta < shortest):
            shortest_name = login
            shortest = tdelta
    else:
        cut_off += 1

for login in db_day2:
    if db_day2[login].end:
        tdelta = datetime.strptime(db_day2[login].end, FMT) - datetime.strptime(db_day2[login].start, FMT)
        if tdelta.days < 0:
            change = timedelta(days=1)
            tdelta = tdelta + change

        time_spent.append(tdelta)
        
        if (tdelta > longest):
            longest_name = login
            longest = tdelta
        elif (tdelta < shortest):
            shortest_name = login
            shortest = tdelta
    else:
        cut_off += 1
    
for times in time_spent:
    total_stay += times
    
print "File:", input_file
print "logins:", logins
print "logouts:", logouts
print "cutoffs:", cut_off
print "names:", names
print "longest stay:", longest
print "shortest stay:", shortest
print "longest_name:", longest_name
print "shortest_name:", shortest_name
print "total time spent:", total_stay

total_days = total_stay.days
total_days = int(total_days)
total_seconds = int(total_stay.seconds) + (24*60*60*total_days)
print total_seconds

print "avg time:", total_seconds/logouts
