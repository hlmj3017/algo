def solution(arr):
    answer = []

    for num in arr:
        # answer 배열이 비어있거나 answer 배열의 마지막 요소와 현재 숫자 num이 다를 경우
        if not answer or answer[-1] != num: 
            answer.append(num)
    
    return answer

print(solution([1,1,3,3,0,1,1]))
print(solution([4,4,4,3,3]))