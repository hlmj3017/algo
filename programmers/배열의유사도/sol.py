def solution(s1, s2):
    return len(set(s1).intersection(s2))

print(solution(["a", "b", "c"], ["com", "b", "d", "p", "c"]))
print(solution(["n", "omg"], ["m", "dot"]))


# 다른 방법 1
def solution(s1, s2):
    return len(set(s1)&set(s2))

# 다른 방법 2
def solution(s1, s2):
    answer = 0

    for i in s1:
        for j in s2:
            if i == j:
                answer += 1

    return answer

print(solution(["a", "b", "c"], ["com", "b", "d", "p", "c"]))
print(solution(["n", "omg"], ["m", "dot"]))