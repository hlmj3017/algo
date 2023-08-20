import sys
from pathlib import Path
from collections import deque

file_path = Path(__file__).parent
input_path = file_path / 'input.txt'
sys.stdin = open(input_path)

T = int(input())

for tc in range(1, T+1):
    # E : 간선의 개수
    # N : 서브트리의 루트 노드
    E, N = list(map(int, input().split()))

    nodes = list(map(int, input().split()))

    # 1. print(nodes)
    # E+2를 사용한 이유는 노드 번호가 1부터 E+1까지이기 때문 
    # 따라서 left_node와 right_node 배열의 크기는 노드 개수보다 하나 더 크게 설정
    left_node = [0] * (E+2)
    right_node = [0] * (E+2)

    for i in range(0, E*2, 2):
        parent = nodes[i]
        child = nodes[i+1]

        if left_node[parent] == 0:
            left_node[parent] = child
        else:
            right_node[parent] = child

    # 2. print(left_node)
    # print(right_node)

    stack = [N]
    count = 0

    while stack:
        now = stack.pop()
        count += 1

        if left_node[now]:
            stack.append(left_node[now])
        
        if right_node[now]:
            stack.append(right_node[now])

    print(count)

        



    # arr = list(map(int,input().split()))
    # # 노드 번호는 1번부터 E+1번까지
    # num = E+1
        
    # # 왼쪽 자식, 오른쪽 자식
    # left = [0] * (num + 1)
    # right = [0] * (num + 1)
    # for i in range(0, 2 * E, 2):
    #     # 왼쪽 자식이 없으면 왼쪽에 넣기
    #     if left[arr[i]] == 0:
    #         left[arr[i]] = arr[i + 1]
    #     else:
    #         right[arr[i]] = arr[i + 1]


    # queue = deque()
    # queue.append(N)
    # cnt = 0

    # while queue:
    #     v = queue.popleft()
    #     cnt += 1
    #     if left[v] != 0:
    #         queue.append(left[v])
    #     if right[v] != 0:
    #         queue.append(right[v])


    # print(f'#{tc} {cnt}')