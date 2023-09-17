def solution(myString, pat):
    myString_lower = myString.lower()
    pat_lower = pat.lower()
    
    if pat_lower in myString_lower:
        return 1
    else:
        return 0
    
print(solution("AbCdEfG","aBc"))
print(solution("aaAA","aaaaa"))


def solution(myString, pat):
    return int(pat.lower() in myString.lower())


def solution(myString, pat):
    if pat.lower() in myString.lower(): 
        return 1
    return 0