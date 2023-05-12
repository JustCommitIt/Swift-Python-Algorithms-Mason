# 처음 생각한 솔루션
# 일단 먼저 숫자를 기준으로 해당 문자를 나눠야 하나?
# 해당 문자를 나눈 리스트를 만들고, ex) ["one", "4", "seveneight"]
# 해당 리스트를 for 문을 돌면서,
# if 숫자로 변환이 가능한 애들은 : 숫자로 변환하고,
# else 변환이 불가능한 애들은 문자인 애들은: startsWith 같은 메서드가 있을터이니...
# 어떤 문자로 start 가 가능한지 체크해서 해당 문자의 딕셔너리 value 를 넣어주자.

# 이후에 생각한 솔루션
# 문자열을 처음부터 쭉 순서대로 순회하면서...
# 숫자이면 그냥 넘어가고,
# 누적시킨 문자가 match_dict에 존재하면 바로 replace 해주고,
# replace 하고 나면 하나의 숫자로 바뀌니, 다음 문자로 쭉 넘어가면 상관없을듯!

# check_letter = ""
# solution_string = ""
#
# for letter in s:
#     if letter.isdigit():
#         check_letter = ""
#         solution_string += letter
#         continue
#     check_letter += letter
#     replace_number = match_dict.get(check_letter)
#     if replace_number:
#         solution_string += str(replace_number)
#         check_letter = ""
#
# answer = int(solution_string)

# 테스트 케이스 7,8,9가 계속 안풀려서 후에 고민한 것..!
# 아니 애초에... 숫자 안에서 특정 문자를 특정 문자로 변경하는 메서드가 있을 것이라 생각..! -> replace?
# 딕셔너리의 관점에서, 문자를 하나씩 돌면서 그 문자 내부에 해당되는 문자를 숫자로 변경해주면 될듯?

# 숫자 문자열과 영단어
def solution(s):
    # 숫자로 매칭되는 딕셔너리를 정의
    match_dict = {
        "zero": '0',
        "one": '1',
        "two": '2',
        "three": '3',
        "four": '4',
        "five": '5',
        "six": '6',
        "seven": '7',
        "eight": '8',
        "nine": '9'
    }

    answer = s
    for key, value in match_dict.items():
        answer = answer.replace(key, value)
    return int(answer)

print(solution("23four5six7"))
print(solution("2three45sixseven"))
print(solution("123"))
print(solution("oneseveneightseveneightseveneight"))
print(solution("oneseveneightseveneight0seven0eight0"))
print(solution("19999239913five"))