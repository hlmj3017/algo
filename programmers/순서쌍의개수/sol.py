def solution(n):
    answer = 0
    
    for num in range(1,n+1):
        if n % num == 0:
            answer += 1
    return answer


def solution(n):
    answer = 0
    
    for num in range(1, int(n ** 0.5) + 1):
        if n % num == 0:
            answer += 2
            
            if num * num == n:
                answer -= 1
    return answer