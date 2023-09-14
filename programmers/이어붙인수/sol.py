# 문자열은 .append() 메서드를 지원하지 않습니다. 
# 문자열을 수정하려면 새로운 문자열에 기존 문자열을 연결해야 합니다.

def solution(num_list):
    even = ''
    odd = ''
    for i in num_list:
        if i % 2 == 0:
            even += str(i)
        else:
            odd += str(i)
            
    return int(odd) + int(even)

print(solution([3, 4, 5, 2, 1]))
print(solution([5, 7, 8, 3]))