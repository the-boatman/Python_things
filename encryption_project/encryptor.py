"""goal: to generate an encryption key that lets you 'encrypt' messages"""

# encryption keys
plainkey = b'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ 0123456789/?.>,<!@#$%^&*()-_=+[{]}|`~'
charron = b"uO0N9PJMdyY]c&{L`W /Bh*~?.[-+}jSlptX_)C76G@qrx^4<#m|>DewH=,8i%ngTFf(3oKRVaQZv2!zA5s$EUbkI1"
gordon = b"B!t$w7@~D0L#+{mU?h-d9&feIQnJ2NMusGq}yp=Ci[gV%RTz4.Wx^,oX]A_(aZ5FlE*jr<v1Pc|`3OSY)H K>/b6k8"
gigachad = b"2zy^{hTIb+G_Vn`/56}j]%SxgX[D71f#vw!L?(R4qJ-WQ*pPKCFe>OMl$c8&)mUu.dE |kY@it0s,Ao~<9NBHZr3=a"




# endmessage = 'nothing'

# end of encryption keys

choice = input('Would you like to encrypt or decrypt?\n')
if choice.lower() == 'encrypt':
    message = input('\nEnter your message\n')
    encryptionkey = input('\nEnter your encryption code\n')
    if encryptionkey.lower() == 'charron':
        encryptionkey = charron
    elif encryptionkey.lower() == 'gordon':
        encryptionkey = gordon
    elif encryptionkey.lower() == 'gigachad':
        encryptionkey = gigachad
    else:
        print('invalid encryption key')
    encrypt_table = bytes.maketrans(plainkey, encryptionkey)
    endmessage = message.translate(encrypt_table)
elif choice.lower() == 'decrypt':
    message = input('\nEnter your message\n')
    encryptionkey = input('\nEnter your encryption code\n')
    if encryptionkey.lower() == 'charron':
        encryptionkey = charron
    elif encryptionkey.lower() == 'gordon':
        encryptionkey = gordon
    elif encryptionkey.lower() == 'gigachad':
        encryptionkey = gigachad
    else:
        print('invalid encryption key')
    decrypt_table = bytes.maketrans(encryptionkey, plainkey)
    endmessage = message.translate(decrypt_table)

print(endmessage)


