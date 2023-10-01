def solution(num_list):
    
    if num_list[-1] > num_list[-2]:
        num_list.append(num_list[-1] - num_list[-2])
    else:
        num_list.append(num_list[-1] * 2)
    return num_list

print(solution([2, 1, 6]))
print(solution([5, 2, 1, 7, 5]))


# 좀 더 편학게
def solution(num_list):
    n1, n2 = num_list[-1], num_list[-2]
    if n1 > n2:
        num_list.append(n1 - n2)
    else:
        num_list.append(n1 * 2)
    return num_list

print(solution([2, 1, 6]))
print(solution([5, 2, 1, 7, 5]))
