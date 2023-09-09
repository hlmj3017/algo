def solution(num_list):
    answer = num_list[ : : -1]
    return answer

print(solution([1, 2, 3, 4, 5]))
print(solution([1, 1, 1, 1, 1, 2]))

# def solution(num_list):
#     return num_list[::-1]


# 다른 방법 1
def solution(num_list):
    num_list.reverse()
    return num_list


# 다른 방법 2
def solution(num_list):
    return list(reversed(num_list))


# 다른 방법 3
def solution(num_list):
    answer = []

    for i in range(len(num_list)):
        data = num_list[len(num_list)-i-1]
        answer.append(data)

    return answer

print(solution([1, 2, 3, 4, 5]))
print(solution([1, 1, 1, 1, 1, 2]))


# 다른 방법 4
def solution(num_list):
    answer = []

    for num in num_list:
        answer.insert(0,num) # num을 answer 리스트의 맨 앞에 추가
    return answer

print(solution([1, 2, 3, 4, 5]))
print(solution([1, 1, 1, 1, 1, 2]))
