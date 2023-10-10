# 6개 번호가 모두 일치하는 경우: 7 - 6 = 1등
# 5개 번호가 일치하는 경우: 7 - 5 = 2등

def solution(lottos, win_nums):
    # 고른 로또 번호 중에서 win_nums와 일치하는 번호의 개수를 센다
    win_count = len(set(lottos) & set(win_nums))
    
    # 고른 로또 번호 중에서 0(모르는 번호)인 번호의 개수를 센다
    zero_count = lottos.count(0)
    
    # win_count로 최저 랭킹을 계산한다.
    if win_count > 0:
        min_rank = 7 - win_count
    else:
        min_rank = 6  # 아무 번호도 맞추지 못한 상황이므로 순위를 6으로 설정
    
    # zero_count + win_count로 최고 랭킹을 계산한다.
    if zero_count + win_count > 0:
        max_rank = 7 - (zero_count + win_count)
    else:
        max_rank = 6  # 아무 번호도 맞추지 못한 상황이므로 순위를 6으로 설정
    
    return [max_rank, min_rank]

print(solution([44, 1, 0, 0, 31, 25],[31, 10, 45, 1, 6, 19]))
print(solution([0, 0, 0, 0, 0, 0],[38, 19, 20, 40, 15, 25]))
print(solution([45, 4, 35, 20, 3, 9],[20, 9, 3, 45, 4, 35]))


# 다른 사람 풀이 1
def solution(lottos, win_nums):
    rank = {
        0: 6,
        1: 6,
        2: 5,
        3: 4,
        4: 3,
        5: 2,
        6: 1
    }
    return [rank[len(set(lottos) & set(win_nums)) + lottos.count(0)], rank[len(set(lottos) & set(win_nums))]]

# 다른 사람 풀이 2
def solution(lottos, win_nums):

    rank=[6,6,5,4,3,2,1]

    cnt_0 = lottos.count(0)
    ans = 0
    for x in win_nums:
        if x in lottos:
            ans += 1
    return rank[cnt_0 + ans],rank[ans]


# 다른 사람 풀이 3

# count가 2보다 작으면(즉, 0 또는 1인 경우), 함수는 6을 반환합니다. 
# 이 경우, 일치하는 번호가 2개 미만이므로 최저 등수인 6등(낙첨)으로 판단합니다.
# 그 외의 경우에는, 7 - count를 반환합니다. 
# 이 경우, count가 2 이상인 경우에는 일치하는 번호의 개수에 따라 7에서 빼서 등수를 계산합니다. 
# 예를 들어, count가 2인 경우에는 7 - 2 = 5가 되므로 5등으로 계산됩니다.

def calc_rank(count):
    return 6 if count < 2 else 7 - count  

def solution(lottos, win_nums):
    answer = []
    
    zero_count = 0
    win_count = 0
    
    for lotto in lottos:
        if lotto in win_nums:
            win_count +=1
        
        elif lotto == 0:
            zero_count += 1  
    
    min_rank = calc_rank(win_count)
    max_rank = calc_rank(win_count + zero_count)
    
    answer = [max_rank, min_rank]
        
    return answer