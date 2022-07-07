import csv
# import pandas as pd
import random as r


# realdata = []

# f = open('/home/usacys/Desktop/Charron/python/fakephonenumber.csv', 'w')

def writeARealCallExchange():
    t = r.randint(1400,2100)
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


def writefakedata():
    dur = r.randint(15,60)
    t = r.randint(1400,2100)
    b = r.randint(1000,9999)
    c = r.randint(1000,9999)
    data = [f'{a}-{b}',dur,f'{a}-{c}',t]
    writer.writerow(data)


fran = '555-6969'
mule = '555-3452'
actcell = '555-6632'
header = ['phone_number', 'call_duration', 'recipient', 'time']
a = '555'


with open('fakephonenumber.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    for real in range(20):
        writeARealCallExchange()
        d = r.randint(15,25)
        for fake in range(d):
            writefakedata()
            
            

        










# writer.writerow('row')
f.close

# print(f'{a}-{b}')

