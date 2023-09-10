def solution(my_string):
    for i in 'aeiou':
        my_string = my_string.replace(i, "")
    return my_string

print(solution("bus"))  
print(solution("nice to meet you")) 


# 다른 방법 1
def solution(my_string):
    result = []
    a = 'aeiou'
    for char in my_string:
        if char not in a:
            result.append(char)
            
    answer = ''.join(result)
            
    return answer

print(solution("bus"))  
print(solution("nice to meet you"))