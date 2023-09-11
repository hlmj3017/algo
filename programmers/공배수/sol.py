def solution(number, n, m):
    if number % n == 0 and number % m == 0:
        return 1
    else:
        return 0
    
print(solution(60, 2, 3))
print(solution(55, 10, 5))


# 다른 방법 1
def solution(number, n, m):
    if number % n == 0:
        if number % m == 0:
            return 1
        else:
            return 0
    else:
        return 0
    
print(solution(60, 2, 3))
print(solution(55, 10, 5))