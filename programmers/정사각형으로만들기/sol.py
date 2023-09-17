def solution(arr):
    # 현재 배열의 행 수와 열 수 구하기
    rows = len(arr)
    cols = len(arr[0])  

    # 행 수가 더 많은 경우
    if rows > cols:
        # 각 행의 끝에 0을 추가하여 열 수를 행 수와 동일하게 만듦
        for row in arr:
            while len(row) < rows:
                row.append(0)
    # 열 수가 더 많은 경우
    elif cols > rows:
        # 각 열의 끝에 0을 추가하여 행 수를 열 수와 동일하게 만듦
        while len(arr) < cols:
            arr.append([0] * cols)
    
    return arr

print(solution([[572, 22, 37], [287, 726, 384], [85, 137, 292], [487, 13, 876]]))
print(solution([[57, 192, 534, 2], [9, 345, 192, 999]]))
print(solution([[1, 2], [3, 4]]))


# 다른 방법 1
# 아직 이해 중
def solution(arr):
    max_size = max(len(arr), len(arr[0]))
    answer = [[0] * max_size for _ in range(max_size)]
    
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            answer[i][j] = arr[i][j]
        
    return answer

print(solution([[572, 22, 37], [287, 726, 384], [85, 137, 292], [487, 13, 876]]))
print(solution([[57, 192, 534, 2], [9, 345, 192, 999]]))
print(solution([[1, 2], [3, 4]]))


# 다른 방법 2
def solution(arr):
    n=len(arr)
    m=len(arr[0])
    if n>m:
        for i in range(n):
            for j in range(n-m):
                arr[i].append(0)
    else:
        for i in range(m-n):
            arr.append([0]*m)

    return arr


# row를 arr[i]로 바꿔서 수행한 경우
def solution(arr):
    # 현재 배열의 행 수와 열 수 구하기
    rows = len(arr)
    cols = len(arr[0])  

    # 행 수가 더 많은 경우
    if rows > cols:
        # 각 행의 끝에 0을 추가하여 열 수를 행 수와 동일하게 만듦
        for i in range(rows):  # i를 정의하여 행의 인덱스를 추적
            while len(arr[i]) < rows:
                arr[i].append(0)
    # 열 수가 더 많은 경우
    elif cols > rows:
        # 각 열의 끝에 0을 추가하여 행 수를 열 수와 동일하게 만듦
        while len(arr) < cols:
            arr.append([0] * cols)
    
    return arr