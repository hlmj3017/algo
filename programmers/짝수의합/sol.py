def solution(n):
    answer = 0
    for i in range(n+1):
        if i % 2 == 0:
            answer += i
    return answer

# def solution(n):
#     answer = range(2, n+1, 2)
#     return sum(answer)

print(solution(10))
print(solution(4))