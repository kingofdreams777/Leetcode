def canConstruct(target: str, wordBank: list[str]) -> bool:
    if target == "":
        return True

    for word in wordBank:
        if target.find(word) == 0:
            suffix = target[len(word):]
            if canConstruct(suffix, wordBank) == True:
                return True

    return False


print(canConstruct("abcdef",["ab","abc","cd","def","abcd"])) #True
print(canConstruct("skateboard", ["bo","rd","ate","t","ska","sk","boar"])) #False
print(canConstruct("enterapotentpot", ["a","p","ent","enter","ot","o","t"])) #True