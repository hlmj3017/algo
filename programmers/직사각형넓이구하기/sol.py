def solution(dots):
    width = max(dots)[0] - min(dots)[0]
    height = max(dots)[1] - min(dots)[1]
    
    return width * height

print(solution([[1, 1], [2, 1], [2, 2], [1, 2]]))
print(solution([[-1, -1], [1, 1], [1, -1], [-1, 1]]))