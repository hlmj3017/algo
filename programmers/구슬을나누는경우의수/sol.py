# 조합
# 서로 다른 n개 중에 r개를 선택하는 경우의 수
# comb(n,k)
# nCk와 같은 조합 값을 반환합니다.
# 조합은 n개의 수 중 k개를 꺼내는 수와 동일하며 n개의 수는 모두 같은 수라고 가정합니다.
# n과 k는 모두 int값만 가능합니다.
import math
def solution(balls, share):
    return math.comb(balls, share)

print(solution(3, 2))
print(solution(5, 3))


# 다른 방법 1
# nCk = n! / (n-k)! * k!
from math import factorial
def solution(balls, share):
    return factorial(balls) / (factorial(balls - share) * factorial(share))

print(solution(3, 2))
print(solution(5, 3))