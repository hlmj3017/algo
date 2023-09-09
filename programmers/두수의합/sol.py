def solution(num1, num2):
    answer = num1 + num2
    return answer

print(solution(2,3))
print(solution(100,2))


# 다른 방법 1
solution = lambda x,y: x + y

print(solution(2,3))
print(solution(100,2))