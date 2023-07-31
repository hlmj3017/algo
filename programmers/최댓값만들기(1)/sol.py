# def solution(numbers):
#     answer = 0
    
#     for i in range(len(numbers)):
#         for j in range(i+1, len(numbers)):
#             # print(i, j)
#             result = numbers[i] * numbers[j]
            
#             if answer < result:
#                 answer = result
    
#     return answer


def solution(numbers):
    answer = 0
    
    numbers.sort(reverse=True)
    answer = numbers[0] * numbers[1]
    
    return answer