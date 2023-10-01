def solution(n):
    answer = 0
    for i in range(n+1):
        if i % 2 == 0:
            answer += i
    return answer

print(solution(10))
print(solution(4))


# 다른 방법 1
def solution(n):
    answer = range(2, n+1, 2)
    return sum(answer)

print(solution(10))
print(solution(4))


# 다른 방법 2
def solution(n):
    answer = []

    for i in range(n+1):
        if i % 2 == 0:
            answer.append(i)
    return sum(answer)

print(solution(10))
print(solution(4))