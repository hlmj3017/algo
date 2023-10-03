def solution(s):
    # 문자열을 분해하는 함수 정의
    def split_string(s):
        x = s[0]  # 첫 글자를 x로 지정
        count_x = 0  # x로 시작한 문자열의 길이를 세기 위한 변수
        count_not_x = 0  # x가 아닌 다른 글자의 길이를 세기 위한 변수
        i = 0  # 문자열을 읽는 인덱스

        while i < len(s):
            if s[i] == x:
                count_x += 1
            else:
                count_not_x += 1

            # x와 x가 아닌 글자의 길이가 같아지면 분해 멈춤
            if count_x == count_not_x:
                break

            i += 1

        if count_x == count_not_x:
            return s[:i+1], s[i+1:]  # 분해한 문자열과 남은 문자열 반환
        else:
            return s, ""  # 분해할 수 없으면 원래 문자열과 빈 문자열 반환

    result = []  # 분해한 문자열을 저장할 리스트
    while s:
        segment, s = split_string(s)  # 문자열 분해
        # segment는 현재 분해된 부분 문자열
        # s는 남은 문자열
        result.append(segment)  # 분해한 문자열을 결과 리스트에 추가

    return len(result)  # 분해한 문자열의 개수 반환

print(solution("banana"))
print(solution("abracadabra"))
print(solution("aaabbaccccabba"))