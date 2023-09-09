def solution(my_string, n):
    answer = []
    for i in my_string:
        answer.append(i * n)
    return ''.join(answer)

print(solution("hello", 3))


# 다른 방법 1
def solution(my_string, n):
    return ''.join(i*n for i in my_string)