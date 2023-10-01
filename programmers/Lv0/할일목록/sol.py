def solution(todo_list, finished):
    answer = []
    for i in range(len(todo_list)):
        if not finished[i]:
            answer.append(todo_list[i])
    return answer

print(solution(["problemsolving", "practiceguitar", "swim", "studygraph"],[True, False, True, False]))


# 다른 방법 1
def solution(todo_list, finished):
    answer = []
    for i in range(len(finished)):
        if finished[i]==False:
            answer.append(todo_list[i])
    return answer
