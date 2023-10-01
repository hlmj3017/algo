def solution(my_string, target):
    if target in my_string:
        return 1
    else:
        return 0
    
print(solution("banana", "ana"))
print(solution("banana","wxyz"))