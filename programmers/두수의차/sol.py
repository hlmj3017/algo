def solution(num1, num2):
    answer = num1 - num2
    return answer

print(solution(2,3))
print(solution(100,2))


# 다른 방법 1
solution = lambda num1, num2 : num1 - num2

print(solution(2,3))
print(solution(100,2))


# 다른 방법 2 (타입 힌트)
def solution(num1:int, num2:int)->int:
    answer = num1 - num2
    return answer

print(solution(2,3))
print(solution(100,2))