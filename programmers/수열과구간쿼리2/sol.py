# query[0] : 시작 인덱스
# query[1] : 끝 인덱스
# query[2] : 비교대상 k

def solution(arr, queries):
    answer = []
    for query in queries:
        query_list = []
        for i in range(query[0], query[1]+1):
            if arr[i] > query[2]:
                query_list.append(arr[i])
                
        if query_list:           # 비어있지 않으면
            answer.append(min(query_list))
        else:                    # 비어있으면
            answer.append(-1)
    return answer

print(solution([0, 1, 2, 4, 3],[[0, 4, 2],[0, 3, 2],[0, 2, 2]]))


# 다른 방법 1
def solution(arr, queries):
    answer = []
    for s, e, k in queries:
        tmp = []
        for x in arr[s:e+1]:
            if x > k:
                tmp.append(x)
        answer.append(-1 if not tmp else min(tmp))
    return answer

print(solution([0, 1, 2, 4, 3],[[0, 4, 2],[0, 3, 2],[0, 2, 2]]))