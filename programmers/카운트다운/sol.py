def solution(start_num, end_num):
    answer = []
    for i in range(start_num, end_num-1, -1):
        answer.append(i)
    return answer

print(solution(10, 3))


# 다른 방법 1
def solution(start, end):
    return list(range(start,end-1,-1))

print(solution(10, 3))