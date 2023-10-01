## 풀이
## 일단 2차원 배열을 만들어야 함 -> 해당 위치 인형을 가져오려면
## 1. board에서 basket에 담으면 0 -> 리스트의 마지막부터 담고 0으로 바꿔줌
## 2. basket에 같은 인형 2개가 들어오면 인형이 터짐 -> pop() 사용?, answer += 2 사용하면 될 듯

def solution(board, moves):
    answer = 0   # 터진 인형의 개수를 반환
    basket = []  # 바구니
    for i in moves:    # moves 리스트에 있는 움직임을 반복하여 실행
        column = i - 1 # 크레인이 움직일 열의 인덱스
        # 가장 위에 있는 인형을 뽑음
        for row in range(len(board)):
            doll = board[row][column]  # 해당 위치 인형을 가져옴
            if doll != 0: # 인형이 있으면
                board[row][column] = 0 # 뽑은 자리는 0
                # 바구니 맨 위와 같은 인형이면 터뜨림
                if len(basket) > 0 and basket[-1] == doll:
                    basket.pop() # 맨 위 인형 터뜨림
                    answer += 2
                else:
                    basket.append(doll) # 다른 인형이면 바구니에 넣음
                break          
    return answer

print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4]))


# 다른 방법 1
def solution(board, moves):
    basket = []
    answer = 0

    for i in moves:
        for j in range(len(board)):
            if board[j][i-1] != 0:
                basket.append(board[j][i-1])
                board[j][i-1] = 0

                if len(basket) > 1:
                    if basket[-1] == basket[-2]:
                        basket.pop()
                        basket.pop()
                        answer += 2     
                break

    return answer

print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4]))