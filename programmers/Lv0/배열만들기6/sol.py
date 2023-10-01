def solution(arr):
    stk = []  # stk를 빈 리스트로 초기화
    i = 0

    while i < len(arr):
        if not stk:
            stk.append(arr[i])
            i += 1
        elif stk[-1] == arr[i]:
            stk.pop()
            i += 1
        else:
            stk.append(arr[i])
            i += 1

    if not stk:
        return [-1]
    else:
        return stk

print(solution([0, 1, 1, 1, 0]))
print(solution([0, 1, 0, 1, 0]))
print(solution([0, 1, 1, 0]))


# 다른 방법 1
def solution(arr):
    stk = []  # stk를 빈 리스트로 초기화
    i = 0

    while i < len(arr):
        if not stk:
            stk += [arr[i]]  # += 연산자를 사용하여 리스트에 요소 추가
            i += 1
        elif stk[-1] == arr[i]:
            stk.pop()
            i += 1
        else:
            stk += [arr[i]]  # += 연산자를 사용하여 리스트에 요소 추가
            i += 1

    if not stk:
        return [-1]
    else:
        return stk
    
print(solution([0, 1, 1, 1, 0]))
print(solution([0, 1, 0, 1, 0]))
print(solution([0, 1, 1, 0]))