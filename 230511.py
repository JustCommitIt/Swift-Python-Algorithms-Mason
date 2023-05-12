# 딕셔너리
# if 1 in {1, 2, 3, 4, 5}:
#     print("Set에서 찾음")
# if 3 in [1, 2, 3, 4, 5]:
#     print("리스트에서 찾음")
#
# print(type({1, 2})) # set
# print(type([1, 2])) # list
# print(type({1: 1, 2: 2})) # dict
#
# user_info = {'name': 'alex'}
# print(user_info.get('name'))

gems = [3, 3, 1, 2, 3, 2, 2, 3, 1]
grades = {}
for i in gems:
    if grades.get(i, 0):
        grades[i] += 1
    else:
        grades[i] = 1

print(grades)

# 풀어쓴 버전!
nums = [1, 2, 3, 4, 5, 1, 2, 3]
count_dict = {}
for num in nums:
    if count_dict.get(num, "없음") == "없음":
        grades[num] = 1
    else:
        grades[num] += 1

# 축약 버전!
for num in nums:
    # 딕셔너리에서 num을 가져오는데,
    # 없으면 0을 가져와서 1을 더해서 할당하고
    # 있으면 거기서 1을 더해서 할당!
    count_dict[num] = count_dict.get(num, 0) + 1

my_dict = {'name': 'mason', 'address': 'seocho-gu'}
print(my_dict.pop('name'), "/ dict:", dict)
print(my_dict.pop('address'), "/ dict:", dict)

"""
my_dict = {'name': 'jane', 'age': 7, 'license': True}
for key in my_dict:
    if my_dict[key] == 7:
        # ✨딕셔너리를 순회하면서 딕셔너리를 변경할 수 없음!! -> 돌려써야 한다!!
        # RuntimeError: dictionary changed size during iteration
        my_dict.pop(key)
print(my_dict)
"""

my_dict = {'name': 'jane', 'age': 7, 'license': True}
# 그냥 뽑으면 키값이 뽑힌다!
for key in my_dict:
    print(key)
# 밸류값을 뽑고 싶을 땐?
for value in my_dict.values():
    print(value)
# 키, 밸류 값을 동시에 뽑고 싶다면!
for key, value in my_dict.items():
    print(key, value)

# 문자열 변경
word = "hello world!"
new_word = word.replace("o", "O")
new_word = new_word.replace("l", "L", 1) # 1개만 변경 처리함!
print(new_word)

input_string = "1 2"
inputs = input_string.split()
# inputs = list(map(lambda x: (int(x)), inputs))  # 이것과 동일한 로직임!
print(inputs)

# nums = list(map(int, input().split()))
# print(nums)

# nums = list(map(lambda x: (int(x) * 2), input().split(",")))
print(nums)

cities = {"seoul", "new york", "seoul"}
cities.add("new york")
cities.add("tokyo")
print(cities)

for i in range(0, 2):
    print(i, "range(0, 2)")
for j in range(5, 3, -1):
    print(j, "range(5, 3, -1)")
for k in range(0, 4, 2):
    print(k, "range(0, 4, 2)")

print(list(range(1, 10)))

print(dict(zip(range(3), [0]*3)))

name = "Mason"
greeting1 = f'{name}님 환영합니다!'
greeting2 = '{}님 안녕하세요!'.format(name)
print(greeting1)
print(greeting2)

word_list = list('mason')
print(word_list)
print(''.join(word_list))
print('/'.join(word_list))

# 거한 번만 등장한 문자
# def solution(s):
#     result_list = []
#     answer = ''
#     count_dict = {}
#
#     for letter in s:
#         count_dict[letter] = count_dict.get(letter, 0) + 1
#
#     for letter, count in count_dict.items():
#         if count == 1:
#             result_list.append(letter)
#     result_list.sort()
#     answer = ''.join(result_list)
#
#     return answer
# print(solution("abcabcadc"))

# 중복된 문자 제거
def solution(my_string):
    answer = ''
    letter_set = set()

    for letter in my_string:
        if not letter in letter_set:
            answer += letter
            letter_set.update(letter)

    return answer
print(solution("people"))