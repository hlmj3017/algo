def solution(arr1, arr2):
    
    # 두 행렬의 행과 열의 개수
    rows = len(arr1)
    cols = len(arr1[0])
    # 빈 행렬 생성
    answer = [[0] * cols for _ in range(rows)]

    for i in range(rows):
        for j in range(cols):
            answer[i][j] = arr1[i][j] + arr2[i][j]
    
    return answer

print(solution([[1,2],[2,3]],[[3,4],[5,6]]))
print(solution([[1],[2]],[[3],[4]]))