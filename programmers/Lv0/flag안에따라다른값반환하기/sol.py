def solution(a, b, flag):
    if flag == True:
        return a + b
    else:
        return a - b

print(solution(-4, 7, True))
print(solution(-4, 7, False))