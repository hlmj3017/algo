import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    # K : 한번 충전으로 최대한 이동할 수 있는 정류장 수
    # N : 종점 정류장
    # M : 충전기가 설치된 정류장 수
    K, N, M = list(map(int, input().split()))

    # 충전기가 설치된 정류장 리스트
    station = list(map(int, input().split()))
    count = 0
    now = 0
      
    while now + K < N:
      
        for step in range(K, 0, -1):
        
            if (now + step) in station:
                now += step
                count += 1
                break

        else:
            count = 0
            break

    print(f'#{tc} {count}')


# k 범위만큼 이동거리를 조절하면서 충전기가 있으면 현재 위치를 변경하고 count를 1씩 늘려준다
# 충전기 설치가 잘못 되어있으면 while문을 더 이상 반복하지 않고 count값을 0으로 초기화하고 종료



    count = 0
    now = 0

    # 충전할 필요가 없이 바로 도착하는 경우
    if K >= N:
        count = 0

    # 충전을 하면서 지나가야 할 떄 
    else:
        # 버스가 아직 종점에 도착하지 않았다면 계속해서 반복
        while now < N:
            # 현재 위치(now)에서 최대로 갈 수 있는 범위를 찾는다.
            # 최대로 갈 수 있는 범위(now+k)부터 현재 위치까지 반복
            for i in range(now + k, now, -1):
                # 1. 최대범위가 종점을 넘는 경우
                if i >= N:
                    now = N
                    break

                # 2. 최대범위가 종점을 아직 넘지 않은 경우
                if i in station:
                    # 가장 뒤에 있는 충전소로 이동
                    now = i

                    # 충전을 하고 이동을 했으니 카운트 증가
                    count += 1

                    # 마지막 충전소를 찾았으니 더 이상 후진할 필요 없음
                    break

            # 현재 위치에서 최대 거리를 찾았는데, 충전소가 없다면 => 도착 불가능
            else:
                count = 0
                now = k  # while문을 끝내는 조건을 만들어주는 것

