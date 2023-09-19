def solution(n):
    if n % 2 == 1:
        total_sum = sum(range(1, n + 1, 2)) 
    else:  
        total_sum = sum([i ** 2 for i in range(2, n + 1, 2)])
    
    return total_sum

print(solution(7))
print(solution(10))