def solution(n, m):
    a, b = n, m

    while b:             # b가 0이 아닌 경우
        a, b = b, a % b  # a를 b로 나눈 나머지로 a를 갱신

    gcd = a  # 최대공약수는 최종적으로 a에 저장됨
    lcm = (n * m) // gcd  # 최소공배수는 (n * m)을 최대공약수로 나눈 값

    return [gcd, lcm]


# 아래의 방법은 잘못됨

def solution(n, m):
    answer = []
    if n < m:
        if m % n == 0:
            answer.extend([n, m])
        else:
            answer.extend([1, n*m])
            
    else:
        if n % m == 0:
            answer.extend([m, n])
        else:
            answer.extend([1, n*m])
            
    return answer

print(solution(3, 12))
print(solution(2, 5))


# 다른 방법 1
def solution(n, m):
    answer = []
    if n < m:
        if m % n == 0:
            answer.append(n)
            answer.append(m)
        else:
            answer.append(1)
            answer.append(n * m)
    else:
        if n % m == 0:
            answer.append(m)
            answer.append(n)
        else:
            answer.append(1)
            answer.append(n * m)
            
    return answer

print(solution(3, 12))
print(solution(2, 5))