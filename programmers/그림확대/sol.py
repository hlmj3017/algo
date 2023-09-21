def solution(picture, k):
    answer = []
    
    for row in picture: 
        resized = ''
        
        for i in row:
            resized += i * k # k배 만큼 가로로 늘린다

        for _ in range(k):
            answer.append(resized) # 가로로 늘려진 이미지 한 줄을 k배 만큼 세로로 늘린다
    
    return answer