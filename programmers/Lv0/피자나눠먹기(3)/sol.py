def solution(slice, n):
    if n % slice == 0:
        return n // slice
    else:
        return (n // slice) + 1

print(solution(7, 10))
print(solution(4, 12))


# 다른 방법 1
def solution(slice, n):
    return ((n - 1) // slice) + 1

print(solution(7, 10))
print(solution(4, 12))