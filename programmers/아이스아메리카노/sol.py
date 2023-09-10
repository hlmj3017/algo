def solution(money):
    return list(divmod(money, 5500))

print(solution(5500))  
print(solution(15000)) 


# 다른 방법 1
def solution(money):
    answer = [money // 5500, money - ((money // 5500) * 5500)]
    return answer

print(solution(5500))  
print(solution(15000)) 


def solution(money):
    answer = [money // 5500, money % 5500]
    return answer
