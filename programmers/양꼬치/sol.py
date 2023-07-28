def solution(n, k):
    answer = (n * 12000) + (k * 2000) - (n//10*2000)
    return answer


# def solution(n, k):
#     return 12000 * n + 2000 * (k - n // 10)

print(solution(10,3))
print(solution(64,6))
