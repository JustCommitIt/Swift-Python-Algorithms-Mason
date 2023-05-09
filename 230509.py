a = [1, 2, 3]
if len(a) < 3 and a[4] != 4:
    print("if 통과")
else:
    print("else 통과")

if True:
    print("True")
else:
    print("else")

if 5 > 2:
    print("5가 2보다 큼!")

number = 3
if not number % 2: # 아래의 구문과 동일함!
# if number % 2 == 0:
    print("짝수임")
else:
    print("홀수임")

name = "Mason"
age = 1
if not name and not age:
    print("이름과 나이가 모두 없습니다")
elif not name:
    print("이름이 비어있습니다")
elif not age:
    print("나이가 0살입니다.")
else:
    print("이름이 나이가 모두 유효합니다.")


age = 15
if age >= 30:
    print("30세 이상입니다.")
else:
    if age >= 20:
        print("20대입니다.")
    else:
        print("미성년자입니다.")




age = 31
if age >= 30:
    print("30대입니다.")
else:
    if age >= 20:
        print("20대입니다.")
    else:
        print("미성년자입니다.")

if age >= 30:
    print("30대입니다.")
elif age >= 20:
    print("20대입니다.")
else:
    print("미성년자입니다.")


print(len([1, 2, 3, 4, 5]), "배열 사이즈")
print([0] * 10)

matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
print(matrix[0][0])
print(matrix[-1][-1])

matrix = [[0, 0, 0]] * 3
matrix[0][0] = 99
print(matrix)
# [[99, 0, 0], [99, 0, 0], [99, 0, 0]]
# 🤯참조로 복사되어 버린다!!

# 인접 행렬
print([1, 2, 3][-1])

a = [2, 3, 1]
appended = a.append(4)
poped = a.pop()
print(appended) # None. 결과값이 없다
print(poped)
print(a)
a.sort()
sorted_a = sorted(a)
# a.insert(0, )
print(a)
print(sorted_a)


# 정렬에 대해서...
a = [[4, 4, 16], [6, 1, 6], [4, 3, 12], [1, 12, 12], [5, 4, 20], [2, 3, 6], [3, 4, 12]]
b = ['hi', 'bbb', 'a-yo', 'byebye']

# 2차원 정렬, 문자열에서의 정렬은 첫번째 요소부터 비교하고 다음 요소 비교하는 식!
# 마치 올림픽에서 금메달이 우선기준인 것 처럼...
a.sort()
b.sort()

# 나만의 기준으로 정렬을 하고 싶을 때
a.sort()

print(a)
print(b)

nums = [3, 2, 3, 1, 2]
nums.sort(key=lambda x: -x)
print(nums)

matrix = [[4, 4, 16], [6, 1, 6], [4, 3, 12], [1, 12, 12], [5, 4, 20], [2, 3, 6], [3, 4, 12]]
matrix.sort(key=lambda numbers: sum(numbers))
print("총합 기준 정렬", matrix)

matrix.sort(key=lambda x: (x[1], x[2]))
print("2번째 요소 기준 정렬 -> 3번째 요소 기준 정렬 하겠다", matrix)

matrix.sort(key=lambda numbers: -numbers[-1])
print("마지막 요소가 큰 순서대로 정렬", matrix)

nums = [1, 2, 3, 4, 5]

nums.reverse()
print(nums)

nums.insert(1, 0)
nums.insert(1, 0)
print(nums)

print("0의 갯수", nums.count(0), "개")

print("0의 첫번째 인덱스", nums.index(0))

# copy 모듈을 쓰지 않고도 2차원 배열을 deepcopy 하는 법!
a = [[1, 2], [3, 4]]
b = []
for i in a:
    b.append(i[:])

a[0][0] = 100
print(a)
print(b)

# copy 모듈을 사용하는 법
import copy
c = copy.deepcopy(a)
a[0][0] = 1
print(a)
print(c)

# 안나온다...!
a = [[1, 2, 3], 4, [5, 6]]
b = []
for i in a:
    if isinstance(i, list):
        b.append(i[:])
    else:
        b.append(i)
print(b)
