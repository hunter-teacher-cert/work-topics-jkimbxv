secret = "computerscience"
key = "bcd"
#chr(ASCIICODE) --> character
#ord(CHARACTER) --> ASCII value

def encrypt(message,key):
    encrypted=""
    message = message.upper()
    key = key.upper()
    i = 0
    while (i<len(message)):
        iKey = i%len(key) #index of key string
        p = ord(message[i])-65 #ord to convert chr to ascii, 65 due to A's ascii code
        d = ord(key[iKey])-65
        c = chr(((p+d)%26)+65) #add 65 again to get to letters in ascii code
        encrypted+=c
        i+=1
    return encrypted
print(encrypt(secret,key))
