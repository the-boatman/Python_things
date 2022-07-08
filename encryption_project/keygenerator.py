# a cool tool i created for generating encryption keys
import random as r
plaintext = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ 0123456789/?.>,<!@#$%^&*()-_=+[{]}|`~'
listtext = list(plaintext)
key = r.sample(listtext, k=len(plaintext))
output = ''.join(key)
print(output)
