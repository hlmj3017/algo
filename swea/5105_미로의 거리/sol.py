import sys
from pathlib import Path
from pprint import pprint

file_path = Path(__file__).parent
input_path = file_path / 'input.txt'
sys.stdin = open(input_path)

T = int(input())

for tc in range(1, T+1):
    N = int(input()) # 미로의 크기

    maze = [list(map(int, input())) for _ in range(N)]

    # 시작점 찾기, 도착점 찾기
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                start = (i, j)
            elif maze[i][j] == 3:
                end = (i, j)


    queue = [start]

    # 상하좌우 델타값
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    while len(queue):
        now = queue.pop(0)
        x, y = now[0], now[1]
    
        # 상하좌우 방향을 반복
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 미로 안에 있다면 진행
            if 0 <= nx < N and 0 <= ny < N:
                # 길 == 0
                if maze[nx][ny] == 0:
                    queue.append((nx, ny))
                # 도착 == 3
                elif maze[nx][ny] == 3:
                    
                    # 거리 계산 결과를 저장 
                    result = abs(maze[x][y]) - 1



    print(f"#{tc} {result}")


