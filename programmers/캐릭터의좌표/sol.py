def solution(keyinput, board):
    # 초기 위치
    x, y = 0, 0
    # 보드의 가로 길이와 세로 길이 구하기
    width = len(board[0])
    height = len(board)
    
    # 방향 키 입력 처리
    for key in keyinput:
        if key == "up":
            if y + 1 < height // 2:  # 위로 이동 가능한 경우
                y += 1
        elif key == "down":
            if y - 1 > -height // 2:  # 아래로 이동 가능한 경우
                y -= 1
        elif key == "left":
            if x - 1 > -width // 2:  # 왼쪽으로 이동 가능한 경우
                x -= 1
        elif key == "right":
            if x + 1 < width // 2:  # 오른쪽으로 이동 가능한 경우
                x += 1
    
    return [x, y]