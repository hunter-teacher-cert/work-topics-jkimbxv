import random


def makeKey():
    alphaKey = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','Y','Z',' ','!','.','?',','];
    random.shuffle(alphaKey)
    return alphaKey

def substitutionCipher(message,key):
    message = message.upper() #converts everything into upper case cuz i'm lazy
    encoded = ""
    i = 0;
    while (i<len(message)):
        #getting index of current letter in regular alphabet
        #to then get corresponding letter in shuffled vers
        currIndex = alphabet.index(message[i])
        encoded+=key[currIndex]
        i+=1
    return encoded

#your alphabet
alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','Y','Z',' ','!','.','?',','];

message = "Hi my name is Jiyoon."
key = makeKey()

print(substitutionCipher(message,key))
