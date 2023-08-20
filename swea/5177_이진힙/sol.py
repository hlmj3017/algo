import sys
from pathlib import Path

file_path = Path(__file__).parent
input_path = file_path / 'input.txt'
sys.stdin = open(input_path)

T = int(input())

for tc in range(1, T+1):
    N = int(input())

    numbers = list(map(int, input().split()))

    heap = [0] * (N+1)
    heap_size = 0

    for i in range(N):
        heap_size += 1
        # 맨 마지막 노드에 삽입하려는 데이터를 할당
        heap[heap_size] = numbers[i]

        child_idx = heap_size
        parent_idx = child_idx // 2

        # 힙에 조건이 맞도록 교환 반복
        while parent_idx and heap[parent_idx] > heap[child_idx]:
            heap[parent_idx], heap[child_idx] = heap[child_idx], heap[parent_idx]

            child_idx = parent_idx
            parent_idx = child_idx // 2

    #print(heap)
    node = N // 2
    total = 0

    # 조상에 조상에 조상을 찾다가 루트를 찾을때까지
    while node:
        total += heap[node]
        node //= 2

    print(total)





# 참고한 풀이

    tree = []

def min_heap(node):
    up_node = node // 2

    if up_node < 0: # 루트노드에 도달하면 리턴
        return
    else:
        # 부모노드가 더 크면 자리 바꿔줌
        if tree[up_node] > tree[node]:
            tree[node], tree[up_node] = tree[up_node], tree[node]
            min_heap(up_node)


    node_num = 1 
    for num in map(int, input().split()):
        tree.append(num)
        min_heap(node_num)
        node_num += 1
    
    sum_value = 0
    while N: # N(마지막)노드의 조상노드 값들 더함
        N //= 2
        sum_value += tree[N]
    
    print(f'#{tc} {sum_value}')


