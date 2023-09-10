def solution(n):
    answer = 0

    while n > 0:
        a, b = divmod(n,10)

        n = a
        answer += b
    return answer

print(solution(1234))  
print(solution(930211))  


# 다른 방법 1
# 문자열로 변환하면 각 자릿수를 개별적으로 접근할 수 있음
# 자릿수를 분리하거나 각 자릿수를 다른 목적으로 사용할 때 유용
def solution(n):
    answer=0
    for i in str(n):
        answer += int(i)

    return answer

print(solution(1234)) 
print(solution(930211))    