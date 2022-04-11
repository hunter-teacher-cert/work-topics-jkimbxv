#Teacher version

def encrypt(message,key):
    #empty string to store our encrypted message as we build it
    encrypted=""
    #make all uppercase to avoid lowercase issues
    message = message.upper()
    #key should be all uppercase
    key = key.upper()
    #while loop to index through your array
    i = 0
    while (i<len(message)):
        #use of % to loop through the key index and back around
        #i.e. if i = 4, len(key) = 3, then would return 1
        iKey = i%len(key)
        #convert current char to ASCII and reset to 0
        p = ord(message[i])-65
        d = ord(key[iKey])-65
        #p+d is the shifting where the ASCII is shifted by d
        #%26 to loop back to the front
        #+65 to turn index into ASCII
        #chr to convert ASCII to char
        c = chr(((p+d)%26)+65)
        #add on to empty string from before with our new encrypted letter
        encrypted+=c
        i+=1
    return encrypted
