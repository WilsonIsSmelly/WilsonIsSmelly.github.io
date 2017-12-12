def vowelsrgay(string):
    empty = ''
    for i in string:
        if i is "A": 
            empty = empty + "!"
        elif i is 'a':
            empty = empty + "@"
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
            empty = empty + '>'
        else:
            empty = empty + i
    return (empty)
#vowelsrgay("Did you know that i hate vowels? Vowels are highly offensive, racist, sexist, shovenist, and should all be executed","")

def vowelsrnotgay(string):
    empty = ''
    for i in string:
        if i is "!": 
            empty = empty + "A"
        elif i is '@':
            empty = empty + "a"
        elif i is '#':
            empty = empty + 'E'
        elif i is '$':
            empty = empty + 'e'
        elif i is '%':
            empty = empty + 'I'
        elif i is '^':
            empty = empty + 'i'
        elif i is '&':
            empty = empty + 'O'
        elif i is '*':
            empty = empty + 'o'
        elif i is '+':
            empty = empty + 'U'
        elif i is '>':
            empty = empty + 'u'
        else:
            empty = empty + i
    return (empty)
#vowelsrnotgay('D^d y*> kn*w th@t ^ h@t$ v*w$ls? V*w$ls @r$ h^ghly *ff$ns^v$, r@c^st, s$x^st, sh*v$n^st, @nd sh*>ld @ll b$ $x$c>t$d','')
