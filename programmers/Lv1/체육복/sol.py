def solution(n, lost, reserve):
    # 학생들의 상태를 나타내는 리스트 생성
    students = [1] * n  # 처음에 모든 학생들은 체육복이 있는 상태

    # 체육복을 도난당한 학생 
    for lost_student in lost:
        # 도난당한 학생의 체육복 개수를 1 감소
        students[lost_student - 1] -= 1  

    # 여벌의 체육복을 가진 학생
    for reserve_student in reserve:
        # 여벌의 체육복을 가진 학생의 체육복 개수를 1 증가
        students[reserve_student - 1] += 1  

    # 체육복 빌려주기
    for i in range(n):
        # 체육복이 없는 학생이라면
        if students[i] == 0: 
            # 왼쪽 학생이 여벌의 체육복이 있는 경우
            if i > 0 and students[i - 1] == 2:  
                students[i - 1] = 1 # 빌려줘서 1 
                students[i] = 1     # 받아서 1 
                
            # 오른쪽 학생이 여벌의 체육복이 있는 경우
            elif i < n - 1 and students[i + 1] == 2:  
                students[i + 1] = 1  # 빌려줘서 1 
                students[i] = 1      # 받아서 1 

    # 체육 수업을 들을 수 있는 학생 수 세기
    answer = 0
    for s in students:
        if s > 0:
            answer += 1

    return answer

print(solution(5,[2, 4],[1, 3, 5]))
print(solution(5,[2, 4],[3]))
print(solution(3,[3],[1]))