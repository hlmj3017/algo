def solution(n, k):
    answer = []
    for i in range(1,n+1):
        if i * k <= n:
            answer.append(k*i)
    return answer

print(solution(10, 3))
print(solution(15, 5))