def solution(numbers, hand):
    answer = ''
    num = { 1 : [0,0], 2 : [0,1], 3 : [0,2],
           4 : [1,0], 5 : [1,1], 6 : [1,2],
           7 : [2,0], 8 : [2,1], 9 : [2,2],
          '*' : [3,0], 0 : [3,1], '#' : [3,2] }
    
    left = '*'  # 왼손 초기 위치
    right = '#' # 오른손 초기 위치
    
    for i in numbers:
        now = num[i]
        
        if i in [1,4,7]:
            left = i
            answer += 'L'
        elif i in [3,6,9]:
            right = i
            answer += 'R'
        else:  
            # num[left][0]: 왼손의 현재 위치의 행
            # num[left][1]: 왼손의 현재 위치의 열
            # num[right][0]: 오른손의 현재 위치의 행
            # num[right][1]: 오른손의 현재 위치의 열
            # 맨해튼 거리 이용
            # 왼손의 현재 위치와 i의 위치 사이의 수평, 수직 이동 거리의 합
            left_dist = abs(num[left][0] - num[i][0]) + abs(num[left][1] - num[i][1])
            right_dist = abs(num[right][0] - num[i][0]) + abs(num[right][1] - num[i][1])
            
            if left_dist < right_dist:
                answer += 'L'
                left = i
            elif left_dist > right_dist:
                answer += 'R'
                right = i
            else:  # 거리가 같으면 사용자의 손잡이로 결정
                if hand == 'left':
                    answer += 'L'
                    left = i
                else: 
                    answer += 'R'
                    right = i

    return answer


# 다른 방법 1
# 좌표를 저장하는 것이 아니라 거리를 저장하는 방법
def solution(numbers, hand):
    l = 10
    r = 11
    answer = ""
    p = [[0, 4, 3, 4, 3, 2, 3, 2, 1, 2],  # 숫자 0에서 다른 숫자로 이동하는 거리
         [4, 0, 1, 2, 0, 2, 3, 0, 3, 4],
         [3, 1, 0, 1, 2, 1, 2, 3, 2, 3],
         [4, 2, 1, 0, 3, 2, 1, 4, 3, 2],
         [3, 0, 2, 3, 0, 1, 2, 0, 2, 3],
         [2, 2, 1, 2, 1, 0, 1, 2, 1, 2],
         [3, 3, 2, 1, 2, 1, 0, 3, 2, 1],
         [2, 0, 3, 4, 0, 2, 3, 0, 1, 2],
         [1, 3, 2, 3, 2, 1, 2, 1, 0, 1],
         [2, 4, 3, 2, 3, 2, 1, 2, 1, 0],
         [1, 0, 4, 5, 0, 3, 4, 0, 2, 3],
         [1, 5, 4, 0, 4, 3, 0, 3, 2, 0]]
    for i in numbers:
        if i in [1, 4, 7]:
            l = i
            answer += "L"
        elif i in [3, 6, 9]:
            r = i
            answer += "R"
        else:
            if p[l][i] < p[r][i]:
                l = i
                answer += "L"
            elif p[l][i] > p[r][i]:
                r = i
                answer += "R"
            elif hand == "left":
                l = i
                answer += "L"
            else:
                r = i
                answer += "R"
    return answer