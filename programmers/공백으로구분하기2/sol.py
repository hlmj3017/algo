def solution(my_string):
    return my_string.split() # 문자열을 공백을 기준으로 분할하여 배열로 만듦

print(solution(" i    love  you"))
print(solution("    programmers  "))


# 다른 방법 1
def solution(my_string):
    my_string = my_string.strip()
    words = my_string.split()
    return words

# 다른 방법 2
def solution(my_string):
    return [i for i in my_string.split(" ") if i != ""]  # " " : 빈 칸 하나, "" 문자열 값이 없음