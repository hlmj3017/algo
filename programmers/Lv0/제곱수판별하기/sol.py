def solution(n):
    if (n ** (1/2)) % 1 == 0:
        return 1
    else:
        return 2

print(solution(144))
print(solution(976))