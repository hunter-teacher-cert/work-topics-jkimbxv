###Vigenere Notes

Let's say A is 0 and Z is 25
The A row has a shift of A = 0
The B row has a shift of B = 1 Etc

C is ciphered text
P is plain letter text
d is position shift (due to key letter)

C = (P+d)%26
per letter...

decryption is using...
P = (c-k)%26
where k is key word letter


source: https://pages.mtu.edu/~shene/NSF-4/Tutorial/VIG/Vig-Algebraic.html  
