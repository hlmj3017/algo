def solution(array, height):
    count = 0
    for i in array:
        if i > height:
            count += 1
    return count

print(solution([149, 180, 192, 170], 167))
print(solution([180, 120, 140], 190))


# 다른 방법 1
# sort() : 리스트를 정렬하는 함수로, reverse = True로 하게 되면 내림차순으로 정렬이 가능하다.
#          리스트의 함수로 리스트만을 받고 리스트 자체를 변경해버린다. 
# sorted() : sort()와 똑같은 기능을 하지만, 단, 리스트 자체를 변경하지 않고 정렬된 리스트를 새로 반환한다. 
#            리스트 외에도 다양한 이터러블 객체도 받을 수 있다.
# index() : [찾을 리스트].index(위치를 찾고자 하는 값) / 특정 리스트에서 특정 값이 몇 번째에 위치해 있는지 index 값을 반환해준다.

def solution(array, height):
    array.append(height)
    array.sort(reverse=True)
    return array.index(height)

print(solution([149, 180, 192, 170], 167))
print(solution([180, 120, 140], 190))