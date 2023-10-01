def solution(num_list):
    for i in range(len(num_list)):
        if num_list[i] < 0:
            return i
        
    return -1

print(solution([12, 4, 15, 46, 38, -2, 15]))
print(solution([13, 22, 53, 24, 15, 6]))

# for 루프가 모든 요소에 대해 순회한 후 음수를 찾지 못한 경우 -1을 반환하도록 해야 함