
string = "Hello World   I love you  !"
empty = ""
"""
for i in (string):
    #print(ord(i))
    empty = i + empty
    print(empty)

def Encrypt (hehe, empty):
    for i in (hehe):
        hehe = ord(i)
        if ord(i) == 32:
            hehe = hehe
        else:
            hehe = hehe + 5
            hehe = chr(hehe)
            empty = empty + hehe
    return empty
print (Encrypt(string, empty))
enc = Encrypt(string, empty)

def Decrypt (haha, empty):
    for i in (haha):
        haha = ord(i)
        haha = haha - 5
        haha = chr(haha)
        empty = empty + haha
        
            
    return empty
print (Decrypt (enc, empty))
"""



"""
for i in range (len(plaintext)):
    print(plaintext[i])
"""

def scramblemeplz(plaintext, empty, empty2):
    charcount = 0
    for i in range (len(plaintext)):
        if charcount % 2 == 0 :
            empty = empty + plaintext[i]
        else:
            empty2 = empty2 + plaintext[i]
        charcount = charcount + 1    
    cipher = empty + empty2     
    print(cipher)
    return cipher
killme = scramblemeplz("1234567890", '', '')

def descramblemeplz(ciphertext):
    half = len(ciphertext)/2
    fir = ciphertext[0:int(half)]
    las = ciphertext[int(half):len(ciphertext)]
    empto = ''
    wtf = ''
    wtf = fir[0] + las[0] + fir[1] + las[1]
    #print (wtf)
    count = 0
    plain = ''
    for i in range(len(fir)):
        #print (i)
        empto = fir[0 + count] + las[0 + count]
        plain = plain + empto
        count = count + 1
    print(plain)        
    


print(descramblemeplz(killme))






                     
    
