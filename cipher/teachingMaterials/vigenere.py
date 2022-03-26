def encrypt(message,key):
    encrypted=""
    message = message.upper()
    key = key.upper()
    i = 0
    while (i<len(message)): #iterating through the message
        iKey = i%len(key) #index of key string
        #getting each letter's ASCII and converting to 0-25
        p = ord(message[i])-65 #ord to convert chr to ascii, 65 due to A's ascii code
        d = ord(key[iKey])-65
        #vigenere encryption formula per char: C = (P+d)%26
        #adding by d in order to move that many steps ahead
        c = chr(((p+d)%26)+65) #add 65 again to get to letters in ascii code
        encrypted+=c
        i+=1
    return encrypted

def decrypt(secret,key):
    decrypted = ""
    secret = secret.upper()
    key = key.upper()
    i = 0
    while (i<len(secret)): #iterating through the decrypted message
        iKey = i%len(key) #index of key string
        #getting each letter's ASCII and converting to 0-25
        p = ord(secret[i])-65 #ord to convert chr to ascii, 65 due to A's ascii code
        d = ord(key[iKey])-65

        #vigenere decryption formula per char: P = (c-d)%26
        #subtracting d in order to move that many steps back
        c = chr(((p-d)%26)+65) #add 65 again to get to letters in ascii code
        decrypted+=c
        i+=1
    return decrypted


def enigma(message,key):
    i = 0
    while (i<6):
        message = encrypt(message,key)
        i+=1
    return message


m = "computerscience"
k = "bcd"

encrypted = encrypt(m,k)
decrypted = decrypt(encrypted,k)

print(encrypted)
print(decrypted)
