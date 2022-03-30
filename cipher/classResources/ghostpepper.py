#using the ceasar cipher from class, write a decryption mechanism without
#knowing the shift

#you will need to complete the ceasar cipher async work first
#bellpepper also suggested first.

#copy paste your code from the async and bellpepper.py here:

def decryptNoKey(secretMessage):
    #write a function that is able to decrypt a message without
    #the shift of the caesar cipher
    commonWords = []
    #how could we step through a message and look for possible clues?
    #In this resource: https://www.dcode.fr/caesar-cipher what does "brute force" mean?
    #returns decrypted string possibilities

message1 = "this is a secret"
encrypted = encrypt(message1,1)
decrypted = decryptNoKey(encrypted)
print(encrypted)
print(decrypted)
