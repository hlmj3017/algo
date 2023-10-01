def solution(num_list, n):
    result = []
    for i in range(0, len(num_list), n):
        result.append(num_list[i])
    return result

print(solution([4, 2, 6, 1, 7, 6], 2))
print(solution([4, 2, 6, 1, 7, 6], 4))


# 다른 방법 1
def solution(num_list, n):
    result = list(num_list[::n])
    return result

print(solution([4, 2, 6, 1, 7, 6], 2))
print(solution([4, 2, 6, 1, 7, 6], 4))