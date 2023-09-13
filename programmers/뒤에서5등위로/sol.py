def solution(num_list):
    num_list.sort()
    return num_list[5:]

print(solution([12, 4, 15, 46, 38, 1, 14, 56, 32, 10]))


# 다른 방법 1
def solution(num_list):
    return sorted(num_list)[5:]

print(solution([12, 4, 15, 46, 38, 1, 14, 56, 32, 10]))