def solution(s):
    # 문자열이 숫자로만 구성되어 있는지: isdigit()
    if s.isdigit() and (len(s) == 4 or len(s) == 6):
        return True
    else:
        return False
    
print(solution("a234"))
print(solution("1234"))


# 다른 방법 1
def solution(s):
    if len(s) == 4 or len(s) == 6:
        try:
            int(s)
            return True
        except ValueError:
            return False
    else : 
        return False