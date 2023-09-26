# skip에 해당하는 단어는 넘어가고, 단어가 있는 곳에서 index만큼 떨어진 알파벳으로 변환

def solution(s, skip, index):
    answer = ''
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    
    for char in skip:
        alpha = alpha.replace(char, '')
    
    for i in s:
        # 단어가 있는 곳에서 index만큼 떨어진 알파벳으로 변환
        # len(alpha)는 새로운 위치가 알파벳 범위를 벗어나지 않도록 하기 위해 사용
        idx = (alpha.index(i) + index ) % len(alpha)
        answer += alpha[idx]
    
    return answer

print(solution("aukks","wbqd",5))