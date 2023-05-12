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

print("--------------")
# 회문 검사 (문자열 뒤집었을 때 동일한지)

word = "level"
reversed_word = ""

for i in word:
    reversed_word = i + reversed_word
if word == reversed_word:
    print("회문입니다만, O(n) 입니다.")
else:
    print("회문이 아닙니다만, O(n) 입니다.")

if word == word[::-1]:
    print("회문입니다만, O(n) 입니다.")
else:
    print("회문이 아닙니다만, O(n) 입니다.")

# 포인터 활용 최적화
is_palindrome = True
for i in range(0, len(word) // 2): # 절반 몫 만큼
    if word[i] == word[-i - 1]:
        continue
    else:
        is_palindrome = False
        break
if is_palindrome:
    print("회문입니다만, 최적화된 O(n) 입니다.")

# 투포인터 활용 -> 필요한 순간이 존재함.

left = 0 # 시작 인덱스
right = len(word)-1 # 마지막 인덱스

is_palindrome = True
while left < right:  # 왼쪽과 오른쪽이 유지될때까지 돌아라!
    if word[left] == word[right]:  # 같은 경우라면 아직은 회문 조건을 만족함
        left += 1  # 왼쪽 포인터를 한칸 오른쪽으로 증가시키고
        right -= 1  # 오른쪽 포인터를 한 칸 왼쪽으로 감소
        continue
    else:  # 다른 경우라면 그 즉시 안된다고 표시하고 break
        is_palindrome = False
        break

print(is_palindrome)


print("--------------")
def my_func(depth):
    if depth == 3:
        return
    print(f'{depth} 단계에서 안녕!')
    my_func(depth + 1)
    print(f'끝났다 {depth} 단계!')

my_func(0)

def fibo(n):
    if n < 2:
        return n
    else:
        return fibo(n-1) + fibo(n-2)
print(fibo(10))

memo = [0, 1]
def fibo(n):
    if n >= 2 and n >= len(memo):
        memo.append(fibo(n-1) + fibo(n-2))
    return memo[n]
print(fibo(2))

# L E G B
a = 3
b = 3
def my_f():
    a = 8
    global b  # global 으로 b에 참조해야 수정할 수 있음.
    b = 8
my_f()
print(a)   # a는 8로 변경되지 않는다. -> 내부에서 외부를 변경할 수 없다.
print(b)   # b는 변경된다.

#
a = [1, 2, 3]
def some_f():
    print(a[1])
    # 얘는 할당이 아니라, 참조이기 때문에 내부의 값을 변경할 수 있다!
    a[1] = 0
some_f()
print(a[1])
# 참조는 가능하되, 재할당은 불가능하다.

a = [1, 2, 3]
print(id(a), "최초 a의 id값")
def my_f(input_list):
    print(id(input_list), "들어간 input_list의 id값")
    input_list[0] = 99
my_f(a)
print(a)


# ✨✨set의 복사.✨✨
a = {1, 2, 3, 4}
print("a의 id", id(a))
b = a   # 이렇게 하면 set 이 주소로 전달됨
print("b의 id", id(b))
b = set(a)  # 이렇게 해야 복사되어 전달됨
print("b의 id", id(b))

