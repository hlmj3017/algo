def solution(my_string, n):
    return my_string[:n]

print(solution("ProgrammerS123", 11))
print(solution("He110W0r1d", 5))


# 다른 방법 1
def solution(my_string, n):
    answer = ''
    for i in range(n) :
        answer += my_string[i]
    return answer

print(solution("ProgrammerS123", 11))
print(solution("He110W0r1d", 5))


# 다른 방법 2
def solution(my_string, n):
    answer = []
    for i in range(n):
        answer.append(my_string[i])
    return ''.join(answer)

print(solution("ProgrammerS123", 11))
print(solution("He110W0r1d", 5))