#패턴매칭, 조건표현식을 통해 변수 매칭 과정에 대해 이해한다.
#리스트/딕셔너리 순회에 대해 이해한다.
#예외 처리 (try...except)에 대해 이해한다.
#for문과 enumerate, 조건문을 이용하여 연속된 중복 숫자를 제거한다.

# 1.정수 0부터 9까지로 이루어진 list를 전달 받아,
# 연속적으로 나타나는 숫자는 하나만 남기고 제거한 list를 출력하라.
# 이때, 제거된 후 남은 수들이 담긴 list의 요소들은 기존의 순서를 유지

numbers = [1, 1, 3, 3, 0, 1, 1]

new_numbers = []

for idx, item in enumerate(numbers):
    if idx == 0:
        new_numbers.append(numbers[idx])
    elif new_numbers[-1] != item:
        new_numbers.append(item)

print(new_numbers)