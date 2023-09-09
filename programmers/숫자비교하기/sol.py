def solution(num1, num2):
    if num1 == num2:
        return 1
    else:
        return -1

print(solution(2,3))
print(solution(11,11))
print(solution(7,99))


# 다른 방법 1
def solution(num1,num2):
    return 1 if num1 == num2 else -1

print(solution(2,3))
print(solution(11,11))
print(solution(7,99))


# 다른 방법 2
def solution(num1, num2):
    answer = -1
    if num1 == num2:
        answer = 1
    return answer

print(solution(2,3))
print(solution(11,11))
print(solution(7,99))
