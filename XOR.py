text='Hello my friend'
key='A'
encrypted=''.join([chr(ord(iter)^ord(key)) for iter in text])
print(encrypted)
decrypted=''.join([chr(ord(iter)^ord(key))for iter in encrypted]) 
print(decrypted)