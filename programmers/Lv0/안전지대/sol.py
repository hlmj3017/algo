# 좌표 문제: set
def solution(board):
    n = len(board)  # 행 또는 열의 길이
    danger = set()  # 위험지역의 좌표를 저장할 집합

    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                danger.add((i,j))  # 지뢰위치 추가
                
                # 좌표 이동에 사용(지뢰 주변 위험지역)
                for x in [-1,0,1]:
                    for y in [-1,0,1]:
                        x1, y1 = i + x, j + y
                        if 0 <= x1 < n and 0 <= y1 < n:
                            danger.add((x1,y1))
                        
    safe = n*n - len(danger)            
    return safe

print(solution([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0]]))
print(solution([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 1, 1, 0], [0, 0, 0, 0, 0]]))
print(solution([[1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1]]))