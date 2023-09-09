def solution(numbers):
    answer = []
    for i in numbers:
        answer.append(i * 2)
    return answer

print(solution([1, 2, 3, 4, 5]))
print(solution([1, 2, 100, -99, 1, 2, 3]))


# 다른 방법 1
def solution(numbers):
    def num(x):
        return x * 2
    answer = list(map(num, numbers))
    return answer

print(solution([1, 2, 3, 4, 5]))
print(solution([1, 2, 100, -99, 1, 2, 3]))


# 다른 방법 2
def solution(numbers):
    return [num*2 for num in numbers]

print(solution([1, 2, 3, 4, 5]))
print(solution([1, 2, 100, -99, 1, 2, 3]))