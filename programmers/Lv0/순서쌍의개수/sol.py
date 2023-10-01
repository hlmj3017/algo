def solution(n):
    answer = 0
    
    for num in range(1,n+1):
        if n % num == 0:
            answer += 1
    return answer

print(solution(20))  
print(solution(100)) 


# 다른 방법 1
def solution(n):
    answer = 0
    
    for num in range(1, int(n ** 0.5) + 1):
        if n % num == 0:
            answer += 2       # 상응하는 또 다른 약수가 존재
            
            if num * num == n:
                answer -= 1   # 중복으로 계산된 약수 제거
    return answer

print(solution(20))  
print(solution(100))