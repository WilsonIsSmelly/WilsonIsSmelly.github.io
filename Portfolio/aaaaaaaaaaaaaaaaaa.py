string = 'I think that using your left toe for combat is not as efficient as using a Scorpion EVO 45'
empty = ''
for i in string:
    if i is 'A':
        empty = empty + '!'
    elif i is 'a':
        empty = empty + '@'
    elif i is 'E':
        empty = empty + '#'
    elif i is 'e':
        empty = empty + '$'
    elif i is 'I':
        empty = empty + '%'
    elif i is 'i':
        empty = empty + '^'
    elif i is 'O':
        empty = empty + '&'
    elif i is 'o':
        empty = empty + '*'
    elif i is 'U':
        empty = empty + '+'
    elif i is 'u':
        empty = empty + '?'
    else:
        empty = empty + i
        
