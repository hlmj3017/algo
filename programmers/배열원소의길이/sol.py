def solution(strlist):
    answer = []
    for my_string in strlist:
        answer.append(len(my_string))
    return answer

print(solution(["We", "are", "the", "world!"]))
print(solution(["I", "Love", "Programmers."]))


# map()함수
# map(f, iterable)은 함수(f)와 반복가능한(iterable) 자료형을 입력받고,
# 입력받은 자료형의 각 요소를 함수(f)가 수행한 결과를 묶어서 반환하는 함수

# 다른 방법 1
def solution(strlist):
    answer = list(map(len, strlist))
    return answer

print(solution(["We", "are", "the", "world!"]))
print(solution(["I", "Love", "Programmers."]))