def solution(my_string, overwrite_string, s):
    # str.replace() 함수가 문자열에서 해당 문자열을 처음 발견한 위치부터 대체하며, 
    # s 인덱스 이후의 부분을 대체하는 것이 아니라 my_string 전체에서 해당 부분을 대체하고 있습니다.
    
    # return my_string.replace(my_string[s:], overwrite_string, len(overwrite_string))

    return my_string[:s] + overwrite_string + my_string[s + len(overwrite_string):]

print(solution("He11oWor1d","lloWorl",2))
print(solution("Program29b8UYP","merS123",7))