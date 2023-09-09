def solution(num1, num2):
    answer = num1 // num2
    return answer

print(solution(10,5))
print(solution(7,2))


# 다른 방법 1
def solution(num1, num2):
    return divmod(num1, num2)[0]

print(solution(10,5))
print(solution(7,2))


# 다른 방법 2
def solution(num1, num2):
    answer = int(num1/num2)
    return answer

print(solution(10,5))
print(solution(7,2))