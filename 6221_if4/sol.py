import sys
sys.stdin = open('input.txt', encoding='utf-8')

man1 = input()
man2 = input()
case = ['가위', '바위','보']

if case.index(man1) < case.index(man2):
    if case.index(man1) == 0 and case.index(man2) == 2:
        print('Result : Man1 Win!')
    else:
        print('Result : Man2 Win!')

if case.index(man1) > case.index(man2):
    if case.index(man1) == 2 and case.index(man2) == 0:
        print('Result : Man2 Win!')
    else:
        print('Result : Man1 Win!')

if case.index(man1) == case.index(man2):
    print('Result : Draw')

# 쌤 풀이 1

# man1 = input()
# man2 = input()

# if man1 == '가위' and man2 == '가위':
#     print('Result : Man1 Win!')
# elif man1 == '가위' and man2 == '바위':
#     print('Result : Man2 Win!')
# elif man1 == '가위' and man2 == '보':
#     print('Result : Man1 Win!')
# elif man1 == '바위' and man2 == '가위':
#     print('Result : Man1 Win!')

# 쌤 풀이 2

# 가위, 바위, 보
#   0     1   2

# 가위, (바위) win2 -1
# 가위, 보
# 바위, 보
# 보, 가위
# 보, 바위

man1 = input()
man2 = input()
rcp = ['가위', '바위','보']

man1_idx = rcp.index(man1)
man2_idx = rcp.index(man2)

result = man1_idx - man2_idx

if result == 0:
    print('Result : Draw')
elif result > 0:
    print(f'Result : Man{result} Win!')
else:
    if result == -1:
        print('Result : Man2 Win!')
    else:
        print('Result : Man1 Win!')
