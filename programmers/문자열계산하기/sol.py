def solution(my_string):
    s = my_string.split()
    answer = int(s[0])
    for i in range(1,len(s),2):
        if s[i]=='+':
            answer+=int(s[i+1])
        else:
            answer-=int(s[i+1])
    return answer




# 다른 방법 1
def solution(my_string):
    return eval(my_string)

print(solution("3 + 4"))


# eval("1+2") = 3
# eval("abs(-8)") = 8


def solution(my_string):
    answer = 0



