import sys
from pathlib import Path

file_path = Path(__file__).parent
input_path = file_path / 'input.txt'
sys.stdin = open(input_path)


# def bfs(v):
#     q = []
#     q.append(v)
#     # 방문표시
#     visited[v] = 1
#     while q:
#         # 방향이 따로 없으니 이어져 있는 노드 모두 탐색
#         # 첫번째 원소부터 탐색
#         v = q.pop(0)
#         for i in range(E):
#             # 앞 먼저 탐색
#             # 현재 노드와 그에 이어져 있는 간선을 방문하지 않은 경우
#             if node[i][0] == v and visited[node[i][1]] == 0:
#                 # 다음 탐색을 위해 v 와 이어져 있는 간선 q에 append
#                 q.append(node[i][1])
#                 # 다음 노드 방문 표시
#                 visited[node[i][1]] = 1
#                 distance[node[i][1]] = distance[v] + 1
#             if node[i][1] == v and visited[node[i][0]] == 0:
#                 # 다음 탐색을 위해 v 와 이어져 있는 간선 q에 append
#                 q.append(node[i][0])
#                 visited[node[i][0]] = 1
#                 distance[node[i][0]] = distance[v] + 1


T = int(input())

for tc in range(T):
    # V : 노드 수 / E : 간선 수

    nodes = [ [0] * (V+1) for _ in range(V+1) ]
    V, E = map(int, input().split())

    for line in range(E):
        start, end = list(map(int, input().split()))

        nodes[start][end] = 1
        nodes[end][start] = 1    

    # S: 출발노드 / G: 도착노드
    S, G = list(map(int, input().split()))
    # pprint(nodes)

    # 방문 체크용 리스트
    check_list = [False] * (V+1)

    # bfs를 구현하기 이한 queue
    queue = []

    # bfs 시작을 하기 위해 시작 노드를 queue에 저장

    now = S
    check_list[now] = True
    queue.append(now)



    # 큐가 비어있지 않으면 계속 반복
    while len(queue):
        now = queue.pop(0)
        check_list[now] = True

        # now와 연결된 다른 노드를 순회
        for link in range(V+1):
            if nodes[now][link] == 1:

                # 아직 방문하지 않은 노드가 있다면
                if not check_list[link]:
                    # 큐에 추가
                    queue.append(link)


    # node = [list(map(int, input().split())) for _ in range(E)]
    # S, G = map(int, input().split())
    # visited = [0] * (V+1)
    # distance = [0] * (V+1)
    # bfs(S)
    # print(f'#{tc+1} {distance[G]}')



