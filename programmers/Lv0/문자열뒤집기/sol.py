def solution(my_string):
    return my_string[::-1]

print(solution("jaron"))
print(solution("bread"))


# 다른 방법 1
def solution(my_string):
    return ''.join(list(reversed(my_string)))

print(solution("jaron"))
print(solution("bread"))


# string은 변경 불가능한(immutable) 객체이므로 문자열의 내용을 직접 변경할 수 없음
# def solution(my_string):
#     my_string.reverse()
#     return my_string