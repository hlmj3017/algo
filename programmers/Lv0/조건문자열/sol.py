def solution(ineq, eq, n, m):
    if ineq == '<':
        if eq == '=':
            if n <= m:
                return 1
            else:
                return 0
        else:
            if n < m:
                return 1
            else:
                return 0
    else:
        if eq == '=':
            if n >= m:
                return 1
            else:
                return 0
        else:
            if n > m:
                return 1
            else:
                return 0

print(solution("<","=",20,50))
print(solution(">","!",41,78))


# 다른 방법 1
def solution(ineq, eq, n, m):
    answer = 0

    if (ineq, eq) == ('<', '='):
        answer = int(n <= m)
    elif (ineq, eq) == ('>', '='):
        answer = int(n >= m)
    elif (ineq, eq) == ('<', '!'):
        answer = int(n < m)
    elif (ineq, eq) == ('>', '!'):
        answer = int(n > m)
    else:
        pass

    return answer

print(solution("<","=",20,50))
print(solution(">","!",41,78))