
def disemvowel(str: str) -> str:
    vowels = ("a","e","i","o","u","A","E","I","O","U")
    res = ""
    res = ""
    for c in str:
        if c in vowels:
            next
        else:
            res = res + c
    return res

def disemvowel2(str: str) -> str:
    vowels = ("a","e","i","o","u","A","E","I","O","U")
    res = ""

    splt = str.split(' ')

    for word in splt:
        for c in range(len(word)):
            if c == 0:
                res = res + word[c]
                continue
            if word[c] in vowels:
                continue
            else:
                res = res + word[c]

        res = res + " "

    return res

ex1 = "if a sentence is unreadable"
print(disemvowel2(ex1))
ex2 = input()
print(disemvowel2(ex2))