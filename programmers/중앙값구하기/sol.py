def solution(array):
    array = sorted(array)
    return array[len(array)//2]

print(solution([1, 2, 7, 10, 11]))
print(solution([9, -1, 0]))


# 같은 풀이
def solution(array):
    array.sort()
    return array[len(array)//2]

print(solution([1, 2, 7, 10, 11]))
print(solution([9, -1, 0]))