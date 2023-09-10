def solution(num_list):
    if len(num_list) >= 11:
        return sum(num_list)
    elif len(num_list) <= 10:
        result = 1
        for num in num_list:
            result *= num
        return result

print(solution([3, 4, 5, 2, 5, 4, 6, 7, 3, 7, 2, 2, 1]))
print(solution([2, 3, 4, 5]))


# 다른 방법 1
from math import prod
def solution(num_list):
    return sum(num_list) if len(num_list)>=11 else prod(num_list)

print(solution([3, 4, 5, 2, 5, 4, 6, 7, 3, 7, 2, 2, 1]))
print(solution([2, 3, 4, 5]))


# 다른 방법 2
def mul(l):
    r = 1
    for i in l:
        r *= i
    return r
def solution(num_list):
    return sum(num_list) if len(num_list) >= 11 else mul(num_list)

print(solution([3, 4, 5, 2, 5, 4, 6, 7, 3, 7, 2, 2, 1]))
print(solution([2, 3, 4, 5]))