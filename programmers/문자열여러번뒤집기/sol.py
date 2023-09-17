def solution(my_string, queries):
    for query in queries:
        start, end = query[0], query[1]
        my_string = my_string[:start] + my_string[start:end+1][::-1] + my_string[end+1:]
    return my_string

print(solution("rermgorpsam",[[2, 3], [0, 7], [5, 9], [6, 10]]))


# 다른 방법 1
def solution(my_string, queries):
    answer=list(my_string)
    for s,e in queries:
        answer[s:e+1]=answer[s:e+1][::-1]
    return ''.join(answer)

print(solution("rermgorpsam",[[2, 3], [0, 7], [5, 9], [6, 10]]))