def solution(dot):
    if dot[0] > 0 and dot[1] > 0:
        return 1
    elif dot[0] < 0 and dot[1] > 0:
        return 2
    elif dot[0] < 0 and dot[1] < 0:
        return 3
    else:
        return 4

print(solution([2, 4]))
print(solution([-7, 9]))


# 다른 방법 2
def solution(dot):
    if dot[0] > 0:
        if dot[1] > 0:
            return 1
        return 4
    else:
        if dot[1] > 0:
            return 2
        return 3

print(solution([2, 4]))
print(solution([-7, 9]))