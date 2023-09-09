def solution(sides):
    sides.sort()
    if sides[0] + sides[1] > sides[2]:
        return 1
    else:
        return 2

print(solution([1, 2, 3]))
print(solution([3, 6, 2]))
print(solution([199, 72, 222]))

# 위와 같은 풀이
def solution(sides):
    sides.sort()
    return 1 if sides[0]+sides[1]>sides[2] else 2