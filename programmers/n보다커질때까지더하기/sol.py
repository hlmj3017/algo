def solution(numbers, n):
    answer = 0
    for i in range(0, len(numbers)):
        answer += numbers[i]
        if answer > n:
            return answer
        
print(solution([34, 5, 71, 29, 100, 34], 123))
print(solution([58, 44, 27, 10, 100], 139))

# append는 리스트에 새로운 요소를 추가할 때 사용하는 메서드이며, 
# 여기서는 단순히 숫자들을 더해서 합계를 구하는 작업이 필요하므로 append 불가능

# 다른 방법 1
def solution(numbers, n):
    answer = 0

    for i in numbers:
        answer += i

        if answer > n:
            return answer

print(solution([34, 5, 71, 29, 100, 34], 123))
print(solution([58, 44, 27, 10, 100], 139))
