# 두 정수 X와 Y에서 공통으로 나타나는 정수를 찾고 각각 몇개인지 찾아서 더 적은 것 추가
# 큰 숫자부터 정렬(sort이용)하여 가장 큰 정수를 반환
def solution(X, Y):
    answer = []
    
    # 두 정수 X와 Y를 문자열로 변환
    X_str = str(X)
    Y_str = str(Y)
    
    # 두 문자열에서 공통으로 나타나는 숫자를 찾음
    common_digits = set(X_str) & set(Y_str)
    
    # 공통으로 나타나는 숫자를 각가 몇개인지 세는 것
    for digit in common_digits:
        count_X = X_str.count(digit)
        count_Y = Y_str.count(digit)
        
        # 두 정수에서 해당 숫자가 더 적게 나타난만큼 추가
        for _ in range(min(count_X, count_Y)):
            answer.append(digit)
    
    # 정렬하여 가장 큰 숫자부터 나열
    answer.sort(reverse=True)
    
    # 결과 문자열 생성
    if len(answer) == 0:
        return "-1"
    if answer[0] == "0":
        return "0"

    answer = "".join(answer)
    return answer

print(solution("100","2345"))
print(solution("100","203045"))
print(solution("100","123450"))
print(solution("12321","42531"))
print(solution("5525","1255"))


# 다른 방법
def solution(X, Y):
    answer = []
    for i in (set(X)&set(Y)) :
        for j in range(min(X.count(i), Y.count(i))) :
            answer.append(i)
    answer.sort(reverse=True)
    if len(answer) == 0:
        return "-1"
    if answer[0] == "0":
        return "0"
    answer = "".join(answer)
    return answer