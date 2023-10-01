def solution(arr):
    stk = []
    i = 0
    while i < len(arr):
        if not stk:
            stk.append(arr[i])
            i += 1
        elif stk[-1] < arr[i]:
            stk.append(arr[i])
            i += 1
        else:
            stk.pop()
    return stk

print(solution([1, 4, 2, 5, 3]))


# 다른 방법 1
# += 연산자를 사용할 때에는 다른 리스트나 이터러블이 오거나, 
# 추가하려는 요소가 하나일 때에는 []와 같이 리스트로 래핑해서 사용
def solution(arr):
    stk = []
    i = 0

    while i < len(arr):
        if not stk:
            stk += [arr[i]]
            i += 1
        elif stk[-1] < arr[i]:
            stk += [arr[i]]
            i += 1
        else:
            stk.pop()

    return stk

print(solution([1, 4, 2, 5, 3]))