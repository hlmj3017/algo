def solution(my_string, letter):
    return my_string.replace(letter, '')
    
print(solution("abcdef", "f"))  
print(solution("BCBdbe", "B"))


# 다른 방법 1
def solution(my_string, letter):
    answer = ''
    
    for string in my_string:
        if string != letter:
            answer += string
    return answer

print(solution("abcdef", "f"))  
print(solution("BCBdbe", "B")) 