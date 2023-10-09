# 발음할 수 있는 단어들을 공백(' ')으로 대체
# 대체 후 남는 문자들이 존재하면 해당 단어는 발음할 수 없는 단어
def solution(babbling):
    answer = 0
    can = ['aya', 'ye', 'woo', 'ma']
    
    for bab in babbling:  # babbling의 단어 하나씩 확인
        for c in can:
            # 연속으로 발음할 수는 없다고 명시했기 때문에 c * 2가 존재하지 않을 때만 공백으로 대체
            if c * 2 not in bab:  # 연속으로 나오지 않으면 공백(' ')으로 대체
                bab = bab.replace(c, ' ')
                
        if bab.isspace():  # 모든 발음 조합이 공백으로 대체되었으면 (발음 가능한 단어일 경우)
            answer += 1    # 발음 가능한 단어를 더해줌
            
    return answer

print(solution(["aya", "yee", "u", "maa"]))
print(solution(["ayaye", "uuu", "yeye", "yemawoo", "ayaayaa"]))