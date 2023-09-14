def solution(sides):
#     # 주어진 두 변이 최대 길이의 변이 아닌 경우
#     a < sum(sides)
    
#     # 주어진 두 변 중에 긴 변이 최대 길이의 변인 경우
#     max(sides) < min(sides) + a
    
#     max(sides) - min(sides) < a < sum(sides)
    return sum(sides) - (max(sides) - min(sides)) - 1

print(solution([1, 2]))
print(solution([3, 6]))
print(solution([11, 7]))