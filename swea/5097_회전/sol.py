import sys
from pathlib import Path

file_path = Path(__file__).parent
input_path = file_path / 'input.txt'
sys.stdin = open(input_path)

T = int(input())  

for tc in range(1, T+1):  
    N, M = map(int, input().split())  # 배열의 크기 N, 회전 횟수 M 입력

    q = list(map(int, input().split()))  # 배열 요소들을 리스트 q로 입력

    # 직접 M번 반복
    for i in range(M):  
        num = q.pop(0) # 리스트의 첫 번째 요소를 꺼내서 num에 저장
        q.append(num)  # num을 리스트의 마지막에 추가

    print(f'{tc} {q[0]}') 



    # # 두번째 방법
    # remain = M % N
    # print(q[remain])