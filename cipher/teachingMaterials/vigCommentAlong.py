def encrypt(message,key):
    encrypted=""
    message = message.upper()
    key = key.upper()
    i = 0
    while (i<len(message)):
        iKey = i%len(key)
        p = ord(message[i])-65 
        d = ord(key[iKey])-65
        c = chr(((p+d)%26)+65)
        encrypted+=c
        i+=1
    return encrypted
