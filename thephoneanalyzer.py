import pandas as pd


phonelog = pd.read_csv('fakephonenumber.csv')

fran = (phonelog[phonelog['phone_number'] == '555-6969'])

unk = (phonelog[phonelog['phone_number'] == '555-6452'])
sunk = (phonelog[phonelog['phone_number'] == '555-6632'])

firstphonenumber = input('Enter the caller number: ')
secondphonenumber = input('Enter the phone number you wish to exclude (put 0 to exclude none): ')

isDesiredCaller = phonelog['phone_number'] == firstphonenumber
isDesiredRecip = phonelog['recipient'] != secondphonenumber
anded = isDesiredCaller & isDesiredRecip
# filters the file for the numbers
print(phonelog[anded])
