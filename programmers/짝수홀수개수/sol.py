def solution(num_list):
    answer = [0,0]
    for num in num_list:
        if num % 2 == 0:
            answer[0] += 1
        else:
            answer[1] += 1
    return answer

print(solution([1, 2, 3, 4, 5]))
print(solution([1, 3, 5, 7]))


# 다른 방법 1
def solution(num_list):
    answer = [0,0]
    for n in num_list:
        answer[n%2]+=1
    return answer

print(solution([1, 2, 3, 4, 5]))
print(solution([1, 3, 5, 7]))