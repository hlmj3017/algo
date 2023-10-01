def solution(id_pw, db):

    for i in db:
        if i[0] == id_pw[0]:       # 아이디 일치
            if i[1] == id_pw[1]:   # 비밀번호 일치
                return 'login'
            else:
                return 'wrong pw'
            
    return 'fail'

print(solution(["meosseugi", "1234"], [["rardss", "123"], ["yyoom", "1234"], ["meosseugi", "1234"]]))
print(solution(["programmer01", "15789"], [["programmer02", "111111"], ["programmer00", "134"], ["programmer01", "1145"]]))
print(solution(["rabbit04", "98761"], [["jaja11", "98761"], ["krong0313", "29440"], ["rabbit00", "111333"]]))