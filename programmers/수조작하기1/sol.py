def solution(n, control):
    for char in control:
        if char == 'w':
            n += 1
        elif char == 's':
            n -= 1
        elif char == 'd':
            n += 10
        elif char == 'a':
            n -= 10
    return n

print(solution(0,"wsdawsdassw"))


# 다른 방법 1
def solution(n, control):
    for i in range(len(control)):
        if control[i] == 'w':
            n += 1
        elif control[i] == 's':
            n -= 1
        elif control[i] == 'd':
            n += 10
        elif control[i] == 'a':
            n -= 10
    return n

print(solution(0,"wsdawsdassw"))


# 다른 방법 2
def solution(n, control):
    answer = n
    c = { 'w':1, 's':-1, 'd':10, 'a':-10}
    for i in control:
        answer += c[i]
    return answer

print(solution(0,"wsdawsdassw"))