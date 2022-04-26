def encrypt(message,key):
    #empty string that will be filled with the encrypted message
    encrypted=""
    #make all lowercase letters into uppercase (simplicity!)
    message = message.upper()
    key = key.upper()
    #while loop to iterate through my plaintext
    i = 0
    while (i<len(message)):
        #key needs a separate index, used to loop back to beginning of key
        #i = 3, len(key) = 3
        iKey = i%len(key)
        #if statements to handle spaces specifically. will concatonate a space and skip encoding it. 
        if (message[i]==" "):
            encrypted+=" "
        else :
            #plain text converting char into number, shifted by 65 to ensure A is 0
            p = ord(message[i])-65
            #key converting char into number, shifted by 65 to ensure A is 0
            d = ord(key[iKey])-65

            #p+d: doing shift
            #%26: loops back to the front of the alphabet
            #+65 undoing shift from line 15 & 17
            #chr: converting unicode into char
            c = chr(((p+d)%26)+65)

            #concatonate to our empty string that we are building on.
            encrypted+=c
        i+=1
    return encrypted

m = "ciphers are cool"
k = "vigenere"

print(m)
print(encrypt(m,k))
