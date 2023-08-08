import sys
from pathlib import Path

file_path = Path(__file__).parent
input_path = file_path / 'input.txt'
sys.stdin = open(input_path)

T = int(input())

def search(idx, visited, SUM):
    global MIN_SUM
    if idx >= N:
        if  SUM < MIN_SUM:
            MIN_SUM = SUM
        #print(result, sum(result))
        return

    if  SUM > MIN_SUM:
        return
    # 모든 경우의 수를 탐색하는 경우
    for i in range(N):
        if visited[i] == False:
            #print(idx, i)
            #result.append(numbers[idx][i])
            SUM += numbers[idx][i]
            visited[i] = True
            search(idx+1, visited, SUM)   # 안끝난 상황에서 내부로 들어가는 것
            #result.pop()
            SUM -= numbers[idx][i]
            visited[i] = False


for tc in range(1, T+1):
    N = int(input())

    numbers = []
    for _ in range(N):
        number = list(map(int, input().split()))
        numbers.append(number)

    #print(numbers)

    result = []
    visited = [False] * N

    SUM = 0
    MIN_SUM = 100000000

    search(0, visited, SUM)

    print(f'{tc} {MIN_SUM}')