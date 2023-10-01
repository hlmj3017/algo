def solution(n):
    # 3진법으로 변환
    to3 = []
    while n > 0:
        remain = n % 3
        to3.append(remain)
        n //= 3
    # 3진법 역순으로 뒤집기
    to3.reverse()
    
    # 10진법으로 변환
    answer = 0
    for i in range(len(to3)):
        answer += to3[i] * (3 ** i)
    return answer

print(solution(45))
print(solution(125))