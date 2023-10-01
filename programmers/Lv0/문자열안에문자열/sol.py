def solution(str1, str2):
    if str2 in str1:
        return 1
    else:
        return 2

print(solution("ab6CDE443fgh22iJKlmn1o", "6CD"))
print(solution("ppprrrogrammers", "pppp"))
print(solution("AbcAbcA", "AAA"))