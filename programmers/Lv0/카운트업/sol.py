def solution(start_num, end_num):
    answer = []
    for i in range (start_num, end_num+1):
        answer.append(i)
    return answer

print(solution(3, 10))


# 다른 방법 1
def solution(start, end):
    answer = []

    answer=list(range(start,end+1))

    return answer

print(solution(3, 10))