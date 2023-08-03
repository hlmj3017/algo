import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())  # N : 칠할 영역의 개수

    # arr = [[0 for _ in range(10)] for _ in range(10)]
    arr = [[0] * 10 for _ in range(10)]  # 10x10 격자
    count = 0  # 겹치는 칸의 수

    for _ in range(1,N+1):
        r1, c1, r2, c2, color = map(int, input().split())

        for row in range(r1, r2+1):
            for col in range(c1, c2+1):
                if color == 1: # 빨간색이면
                    if arr[row][col] == 0:   # 색이 안 칠해진 경우
                        arr[row][col] = 1    # 빨간색
                    elif arr[row][col] == 2: # 파란색이 칠해진 경우
                        arr[row][col] = 3    # 보라색
                        count += 1

                else:  # 파란색이면
                    if arr[row][col] == 0:   # 색이 안 칠해진 경우
                        arr[row][col] = 2    # 파란색
                    elif arr[row][col] == 1: # 빨간색이 칠해진 경우
                        arr[row][col] = 3    # 보라색
                        count += 1

    print(f'#{tc} {count}')