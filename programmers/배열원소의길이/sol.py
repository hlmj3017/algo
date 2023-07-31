def solution(strlist):
    answer = []
    for my_string in strlist:
        answer.append(len(my_string))
    return answer

print(solution(["We", "are", "the", "world!"]))
print(solution(["I", "Love", "Programmers."]))