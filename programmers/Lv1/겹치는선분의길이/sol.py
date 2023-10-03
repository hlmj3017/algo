def solution(lines):
    # 각 선분을 좌표 집합으로 변환
    s1 = set(i for i in range(lines[0][0], lines[0][1]))
    s2 = set(i for i in range(lines[1][0], lines[1][1]))
    s3 = set(i for i in range(lines[2][0], lines[2][1]))

     # 각 선분의 좌표 집합에 대해 교집합을 구하고 길이를 반환
    return len((s1 & s2) | (s2 & s3) | (s1 & s3))

print(solution([[0, 1], [2, 5], [3, 9]]))
print(solution([[-1, 1], [1, 3], [3, 9]]))
print(solution([[0, 5], [3, 9], [1, 10]]))