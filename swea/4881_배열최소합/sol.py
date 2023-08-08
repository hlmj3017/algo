import sys
from pathlib import Path

file_path = Path(__file__).parent
input_path = file_path / 'input.txt'
sys.stdin = open(input_path)

T = int(input())

def min_v(n, total):
    global min_sum  # min_sum을 함수 내에서 변경하기 위해 global로 선언

    # 모두 고른 경우
    if n == N:
        if total < min_sum:
            min_sum = total  # 현재 합이 최소 합보다 작으면 실행
        return  # 더 이상 진행하지 않고 리턴

    # 최소 합보다 크면 리턴
    if total > min_sum:
        return

    for i in range(N):
        if i not in visited:  # 이미 방문한 열은 건너뛰기
            visited.append(i)
            min_v(n+1, total+matrix[n][i])
            visited.pop()


for tc in range(1, T+1):
    N = int(input())
    # N x N 배열
    matrix = [list(map(int, input().split())) for _ in range(N)] 
    min_sum = 10000
    visited = []
    min_v(0,0)

    print(f'{tc} {min_sum}')









