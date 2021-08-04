message=input('Enter the message:')  #hello
alphabet='abcdefghijklmnopqrstuvwxyz'
key=5
encrypt=''
decrypt=''
for i in message:
    position=alphabet.find(i)
    newposition=(position+5)%26   #26%26=o
    encrypt+=alphabet[newposition]
print('Password=')
print(encrypt)

for i in encrypt:
    pos=alphabet.find(i)
    newpos=(pos-5)%26   #26%26=o
    decrypt+=alphabet[newpos]
print('Message=')
print(decrypt)
