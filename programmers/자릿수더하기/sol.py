def solution(n):
    answer = 0

    while n > 0:
        a, b = divmod(n,10)

        n = a
        answer += b
    return answer

 print(solution(1234))  


# def solution(n):
#     answer=0

#     for i in str(n):
#         answer += int(i)

#     return answer

#  print(solution(1234))   