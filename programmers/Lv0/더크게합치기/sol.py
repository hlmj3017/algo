def solution(a, b):
    if int(str(a) + str(b)) > int(str(b) + str(a)):
         return int(str(a) + str(b))
    else:
         return int(str(b) + str(a))

print(solution(9, 91))
print(solution(89, 8))


# 다른 방법 1
def solution(a, b):
    return int(max(f"{a}{b}", f"{b}{a}"))


# 다른 방법 2
def solution(a, b):
    return max(int(str(a)+str(b)), int(str(b)+str(a)))