def solution(arr):
    answer = []
    for i in arr:
        answer += [i] * i   # i를 i번 추가하여 answer에 누적
    return answer

print(solution([5, 1, 4]))
print(solution([6, 6]))
print(solution([1]))


# 다른 방법 1
def solution(arr):
    ans = []
    for n in arr:
        ans.extend([n]*n)
    return ans

# 다른 방법 2
def solution(arr):
    answer = []
    for x in arr:
        for i in range(x):
            answer.append(x)
    return answer