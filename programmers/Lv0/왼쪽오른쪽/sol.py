def solution(str_list):
    
    for i in range(len(str_list)):
        if str_list[i] == "l":
            return str_list[:i]
        elif str_list[i] == "r":
            return str_list[i+1:]
    
    return []

print(solution(["u", "u", "l", "r"]))
print(solution(["l"]))


# 다른 방법 
# 이렇게 하면 안되는 이유 => "l"와 "r"이 여러번 나오는 것을 고려하지 않음 
def solution(str_list):
    result = []
    for string in str_list:
        if 'l' in string:
            answer = string.split('l', 1)  # "l"을 기준으로 1번 분할
            result.append(answer[0])
        elif 'r' in string:
            answer = string.split('r', 1)  # "r"을 기준으로 1번 분할
            result.append(answer[1])
    if result:
        return result
    else:
        return []
    
# print(solution(["u", "u", "l", "r"]))
# print(solution(["l"]))