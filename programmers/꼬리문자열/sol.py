def solution(str_list, ex):
    # 결과 꼬리 문자열 초기화
    result = ""
    # str_list에서 ex를 포함하지 않는 문자열들을 결과에 추가
    for string in str_list:
        if ex not in string:
            result += string

    return result

print(solution(["abc", "def", "ghi"],"ef"))
print(solution(["abc", "bbc", "cbc"],"c"))