from Wilson_Substitution import vowelsrgay, vowelsrnotgay
def scramblemeplz(plaintext):
    charcount = 0
    empty = ''
    empty2 = ''
    for i in range (len(plaintext)):
        if charcount % 2 == 0 :
            empty = empty + plaintext[i]
        else:
            empty2 = empty2 + plaintext[i]
        charcount = charcount + 1    
    cipher = empty + empty2     
    print(cipher)
    return(cipher)
#scramblemeplz("Did you know that i hate vowels? Vowels are highly offensive, racist, sexist, shovenist, and should all be executed ", '', '')
#print(vowelsrgay(scramblemeplz("Did you know that I hate vowels? Vowels are highly offensive, racist, sexist, shovenist, and should all be executed", '', ''),''))
binko = scramblemeplz(vowelsrgay("Did you know that I hate vowels? Vowels are highly offensive, racist, sexist, shovenist, and should all be executed "))
stanko = vowelsrnotgay(binko)

def descramblemeplz(ciphertext):
    half = len(ciphertext)/2
    fir = ciphertext[0:int(half)]
    las = ciphertext[int(half):len(ciphertext)]
    empto = ''
    count = 0
    plain = ''
    for i in range(len(fir)):
        #print (i)
        empto = fir[0 + count] + las[0 + count]
        plain = plain + empto
        count = count + 1
    print (plain)    
    return(plain)
#print (binko)
#print (stanko)
descramblemeplz(stanko)

