bloods = ['A','A','A','B','B','AB','AB','O','O','O']
bloods_dict = {
    'A': 0, 
    'O' : 0, 
    'B' : 0, 
    'AB' : 0
}

for i in bloods:
    bloods_dict[i] += 1

# for i in bloods:
#     if i == 'A':
#         bloods_dict['A'] += 1
#     elif i == 'O':
#         bloods_dict['O'] += 1        
#     elif i == 'B':
#         bloods_dict['B'] += 1
#     else:
#         bloods_dict['AB'] += 1

print(bloods_dict)


# 다른 예시
location_list = ['서울','부산','서울','서울','대전','제주','광주','부산']

location_dict = {}

for location in location_list:
    # 이미 기록을 한 경우
    if location in location_dict.keys():
        location_dict[location] += 1
    # 처음 등장한 경우
    else:
        location_dict[location] = 1
        
print(location_dict)



