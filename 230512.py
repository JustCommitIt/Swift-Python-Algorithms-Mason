while False:
    print(1)

numbers = [1, 2, 3, 4, 5]
i = 0
while i < len(numbers):
    if numbers[i] % 2 == 0:
        print(numbers[i])
    i += 1

while numbers:
    deleted_number = numbers.pop()
    print(deleted_number)
print(numbers)

number_set = {1, 2, 3, 4, 5}
while number_set:
    popped_number = number_set.pop()
    print(popped_number)
print(number_set)

number_dict = {1: 1, 2: 2, 3: 3, 4: 4}
while number_dict:
    key, value = number_dict.popitem()
    print(key, value)
print(number_dict)

print("-------------")
number_list = [1, 2, 3, 4, 5]
for _ in range(0, len(number_list)):
    popped_number = number_list.pop()
    print(popped_number)
print(number_list)

print("-------------")
number_list = [1, 2, 3, 4, 5]
for i in number_list:
    # popped_number = number_list.pop()
    popped_number = number_list.pop(0)
    print(f'i:{i}, popped:{popped_number}')
    print(popped_number)
print(number_list)

print("--------------")
numbers = [1, 2, 3, 4, 5]
for number in numbers:
    print(number)
    if number == 2:
        print(f"{number}를 만남. 반복 종료")
        break
        print("이 프린트문은 실행되지 않음")

i = 0
while True:
    print(numbers[i])
    if numbers[i] == 2:
        print(f"{number}를 만남. 반복 종료")
        break
        print("이 프린트문은 실행되지 않음")
    i += 1

for number in numbers:
    if number % 2 == 0:
        continue
    print(number)

print("--------------")
number = 0
while number <= 5:
    number += 1

    if number % 2 == 0:
        continue
    print(number)
