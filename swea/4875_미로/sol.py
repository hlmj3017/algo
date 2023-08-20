import sys
from pathlib import Path
from pprint import pprint

file_path = Path(__file__).parent
input_path = file_path / 'input.txt'
sys.stdin = open(input_path)

T = int(input())

for tc in range(1, T+1):
    N = int(input()) # N: 미로의 크기
    maze = [list(map(int, input())) for _ in range(N)] 
    pprint(maze)

    # 0은 통로, 1은 벽, 2는 출발, 3은 도착

    # def move(x, y, N):
    #     return 0 <= x < N and 0 <= y < N
    
    # def find_path(maze, x, y, N):
    #     if not move(x, y, N) or maze[x][y] == 1:
    #         return False
        
    #     if maze[x][y] == 3:
    #         return True
    
    #     maze[x][y] = 1  # 현재 위치 방문 표시
        
    #     directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # 상하좌우 이동 방향
        
    #     for dx, dy in directions:
    #         # 상하좌우로 이동하며 목적지까지 도달 가능한지 확인
    #         if find_path(maze, x + dx, y + dy, N):
    #             return True
        
    #     return False


    # 시작점 찾기
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                start = (i, j)

    # dfs를 동작하기 위한 스택
    stack = []
    stack.append(start)

    # 상하좌우 델타값
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    result = 0

    while len(stack):

        now = stack.pop()
        x, y = now[0], now[1]

        maze[x][y] = 1

        pprint(maze)
        print()


        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 미로 범위 안에 있다면 진행
            if 0 <= nx < N and 0 <= ny < N:
                #print(nx, ny)
                # 길이라면
                if maze[nx][ny] == 0:
                    stack.append((nx, ny))
                # 도착지점이라면
                elif maze[nx][ny] == 3:
                    result = 1
                    break
    #pprint(result)


    # # 도착한 경우
    # if find_path(maze, start_x, start_y, N):
    #     result = 1
    # else:
    #     result = 0


    print(f"#{tc} {result}")