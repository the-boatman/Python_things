import csv
import random as r

# this creates the 'real' data so we have something to analyze
def writeARealCallExchange():
    t = r.randint(1000,2359)
    dur = r.randint(15,60)
    ftm = r.sample([fran,mule], k=2)
    caller, callee = ftm
    data = [caller,dur,callee,t]
    writer.writerow(data)
    dur = r.randint(15,60)
    mta = r.sample([mule,actcell], k=2)
    caller,callee = mta
    data = [caller,dur,callee,t]
    writer.writerow(data)

# this creates the fake 'chaff' data
def writefakedata():
    dur = r.randint(15,60)
    t = r.randint(1400,2100)
    b = r.randint(6000,6999)
    c = r.randint(6000,6999)
    data = [f'{a}-{b}',dur,f'{a}-{c}',t]
    writer.writerow(data)

# define the 'real' phone numbers we care about "a" enforces the 555 area code
fran = '555-6969'
mule = '555-6452'
actcell = '555-6632'
# the collum titles
header = ['phone_number', 'call_duration', 'recipient', 'time']
a = '555'

# first line creates the .csv | 'w' makes it writeable | rest of the code uses the functions to generate the call log
with open('fakephonenumber.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    for real in range(20):
        writeARealCallExchange()
        d = r.randint(15,25)
        for fake in range(d):
            writefakedata()
            
# this closes the file and saves
f.close



