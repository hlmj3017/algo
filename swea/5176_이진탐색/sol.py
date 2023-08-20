import sys
from pathlib import Path

file_path = Path(__file__).parent
input_path = file_path / 'input.txt'
sys.stdin = open(input_path)

T = int(input())

def inorder(idx):
    global count

    if idx <= N:

        # 왼쪽 자식
        inorder(idx * 2)

        # 현재 노드
        tree[idx] = count
        count += 1

        # 오른쪽 자식
        inorder(idx * 2 + 1)


for tc in range(1, T+1):
    N = int(input())

    tree = [0] * (N+1)   #값이랑 인덱스랑 구별할 줄 알야야 함

    count = 1

    inorder(1)

    print(tree[1], tree[N//2])





# def complete_binary_tree(root, n):
#     if root <= n:
#         # 왼쪽 자식의 노드 번호
#         left_node = root * 2 
#         # 오른쪽 자식의 노드 번호
#         right_node = root * 2 + 1
        
#         # 왼쪽 자식으로 이동하여 완전 이진 트리 구성
#         complete_binary_tree(left_node, n)
        
#         # 현재 노드(root)의 값을 출력 
#         if root == 1:
#             print(root)
        
#         # N/2번 노드의 값을 출력 (N이 홀수인 경우 소수점 버림)
#         if n % 2 == 0:
#             if root == n // 2:
#                 print(root)
#         else:
#             if root == n // 2 + 1:
#                 print(root)
        
#         # 오른쪽 자식으로 이동하여 완전 이진 트리 구성
#         complete_binary_tree(right_node, n)
