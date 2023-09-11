def solution(numbers):
    nums = {
        'zero': '0',
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'
    }
    for i, j in nums.items():
        numbers = numbers.replace(i, j)
    return int(numbers)

print(solution("onetwothreefourfivesixseveneightnine"))
print(solution("onefourzerosixseven"))


    # for i in nums.keys():
    #     if j in nums.values():
    #         numbers = numbers.replace(i, j)
    # return numbers

# 다른 방법 1
#     for i in nums.keys():
#         numbers = numbers.replace(i, nums[i])  # 딕셔너리 메소드
#     return int(numbers)

# print(solution("onetwothreefourfivesixseveneightnine"))
# print(solution("onefourzerosixseven"))