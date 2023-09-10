def solution(my_string):
    result = 0
    for i in my_string:
        if i.isdigit():   # 문자열의 각 문자가 숫자인지 확인
            result += int(i)
    return result

print(solution("aAb1B2cC34oOp"))  
print(solution("1a2b3c4d123"))


# 다른 방법 1 (예외처리)
def solution(my_string):
    answer = 0
    for i in my_string:
        try:
            answer += int(i)
        except:
            pass

    return answer

print(solution("aAb1B2cC34oOp"))
print(solution("1a2b3c4d123"))