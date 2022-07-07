
from posixpath import join
# a cool tool i created for generating encryption keys
import random as r
plaintext = 'abcdefghijklmnopqrstuvwxyz 0123456789'
listtext = list(plaintext)
key = r.sample(listtext, k=37)
output = ''.join(key)
print(output)