import psutil

import time


starttime=time.time()
while True:
  print "tick"
  time.sleep(5.0 - ((time.time() - starttime) % 5.0))



# USER PART
userString = psutil.users()
currentUser = userString[0][0]

print "\n***********************************"
print "Current user is : " + currentUser
print "**********************************\n"

# CPU PART
print "\n************** CPU ***************"

print "Number of cores : " + str(psutil.cpu_count()) + "\n"

freq = psutil.cpu_freq()
currentFreq = freq[0]
maxFreq = freq[1]
minFreq = freq[2]

print "Current frequecy : " + str(currentFreq) + " Mhz"
print "Max frequency : " + str(maxFreq) + " Mhz"
print "Min frequency : " + str(minFreq) + " Mhz"
print "**********************************\n"


# DISK USAGE PART
hdd = psutil.disk_usage('/')

total = str(hdd[0] / 1000000) + " Mo"
used = str(hdd[1] / 1000000) + " Mo"
free = str(hdd[2] / 1000000) + " Mo"
percent = str(hdd[3]) + "%"

print "\n***************** DISK USAGE ***************************"
print "Total memory : " + total + ", Used : " + used + ", Free : " + free;
print "Percentage of used memory : " + percent
print "********************************************************\n"


# MEMORY PART
mem = psutil.swap_memory()

memTot = str(mem[0] / 1000000000) + " Go"
memUsage = str(mem[1] / 1000000) + " Mo"
memPercent = str(mem[3]) + " %"

print "\n*************** RAM **********************"
print "Total RAM : " + memTot + ", Used : " + memUsage
print "RAM percentage used : " + memPercent
print "******************************************\n"