def solution(array, n):
    return array.count(n)

print(solution([1, 1, 2, 3, 4, 5], 1))
print(solution([0, 2, 3, 4], 1))


# 다른 방법 1
def solution(array, n):
    count = 0
    for i in array:
        if i == n :
            count +=1
    return count

print(solution([1, 1, 2, 3, 4, 5], 1))
print(solution([0, 2, 3, 4], 1))