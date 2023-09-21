def solution(M, N):
    if M == 1 and N == 2 or M == 2 and N == 1:
        return 1
    else:
        # M X N 인 경우 (M-1)번으로 나뉜 후 각각 M개의 (N-1)번 잘리게 됨
        return (M - 1) + M * (N - 1)
    
print(solution(2, 2))
print(solution(2, 5))
print(solution(1, 1))