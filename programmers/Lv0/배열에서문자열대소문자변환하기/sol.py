def solution(strArr):
    result = []
    for i in range(len(strArr)):
        if i % 2 == 0:
            result.append(strArr[i].lower())
        else:
            result.append(strArr[i].upper())
    
    return result

print(solution(["AAA","BBB","CCC","DDD"]))
print(solution(["aBc","AbC"]))

# result += strArr[i].lower()와 result += append(strArr[i].upper())에서 += 연산자를 사용하려는 것은 문자열을 리스트에 추가하려는 의도입니다. 
# 그러나 문자열을 추가할 때 += 연산자 대신 append() 메서드를 사용해야 합니다.

# append() 함수를 호출할 때 append 앞에 strArr[i]를 붙이는 것이 아니라 append 함수를 리스트에 직접 적용해야 합니다.

# 문자열을 추가할 때는 result 리스트에 문자열 그대로 추가하는 것이 아니라, 문자열을 리스트에 넣어야 합니다. 
# 그렇지 않으면 문자열이 문자 단위로 나뉘어 리스트에 추가됩니다.



# 두 줄의 차이는 문자열과 리스트를 어떻게 다루는지와 관련이 있습니다.

# result += strArr[i].lower(): 이 코드는 'result 변수에 문자열을 추가'하는 것으로, 
# strArr[i].lower()의 결과가 문자열로 반환되고 이를 result 문자열에 연결(concatenate)합니다. 
# 결과적으로 result는 문자열로 유지됩니다. 이 코드는 홀수 번째 인덱스의 문자열을 소문자로 변환하고 이어 붙이는 방식으로 작동합니다.

# result.append(strArr[i].upper()): 이 코드는 result 변수가 리스트로 취급되고, strArr[i].upper()의 '결과를 result 리스트에 추가'합니다. 
# append() 메서드는 원래 리스트에 새로운 요소를 추가하는 데 사용되므로 result는 리스트 형태로 유지됩니다. 
# 이 코드는 짝수 번째 인덱스의 문자열을 대문자로 변환하여 리스트에 추가하는 방식으로 작동합니다.

# 따라서 두 줄의 차이점은 result의 데이터 유형과 어떻게 추가되는지에 있습니다. 
# 첫 번째 줄은 result를 문자열로 유지하고, 두 번째 줄은 result를 리스트로 유지합니다. 
# 데이터 유형에 따라 코드의 의도와 결과가 다를 수 있으므로, 작업에 따라 적절한 데이터 유형을 사용해야 합니다.
