def solution(n):
    result = []
    for i in range(1, n+1, 2):
        result.append(i)
    return result

print(solution(10))
print(solution(15))


# 다른 방법 1
def solution(n):
    return [i for i in range(1, n+1, 2)]

print(solution(10))
print(solution(15))


def solution(n):
    return [x for x in range(n + 1) if x % 2]

print(solution(10))
print(solution(15))