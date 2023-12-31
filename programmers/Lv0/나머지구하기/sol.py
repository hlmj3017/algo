def solution(num1, num2):
    answer = num1 % num2
    return answer

print(solution(3,2))
print(solution(10,5))


# 다른 방법 1
def solution(num1, num2):
    return divmod(num1, num2)[1]

print(solution(3,2))
print(solution(10,5))


# 다른 방법 2
solution = lambda num1, num2 : num1 % num2

print(solution(3,2))
print(solution(10,5))