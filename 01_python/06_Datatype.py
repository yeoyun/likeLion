# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.16.7
#   kernelspec:
#     display_name: Python [conda env:base] *
#     language: python
#     name: conda-base-py
# ---

# # 리터럴
# - 프로그램 코드 작성시 값을 작성하는 문법

# + jupyter={"source_hidden": true, "outputs_hidden": true}
print('정수 :', 100)
print('실수 :', 11.11)
print('문자열 :', '하하하')
print('참 :', True)
print('거짓 :', False)
print('지수 :', 2e5)
print('복소수 :', 10 + 8j)
print('세자리 마다 표시 :', 123_456_789)
print('없음 :', None)
# -

# type을 쓰면 값의 타입을 파악할 수 있다
print(type(100))
print(type(11.11))
print(type('하하하'))
print(type(True))
print(type(False))
print(type(2e10))
print(type(10 + 8j))
print(type(123_456_789))
print(type(None))

# # 변수
# - 개발자가 원하는 값을 저장할 수 있는 기억공간을 의미한다.
# - 파이썬은 이름만 정해주면 변수를 정의할 수 있다.

# 파이썬은 변수의 선언과 동시에 저장할 값을 지정해준다.
# = : 대입연산자. 오른쪽에 있는 값을 왼쪽의 변수에 저장하는 작업을 수행한다.
a1 = 10
a2 = 11.11
a3 = '안녕하세요'

# 변수의 이름만 사용하면 변수에 저장되어 있는 값을 가져와 사용할 수 있다.
print(a1)
print(a2)
print(a3)

# +
# 파이썬은 변수에 다른 타입의 값을 저장하는 것이 가능하다
a4 = 100
print(a4)

a4 = 11.11
print(a4)

a4 = '문자열'
print(a4)

# +
# 파이썬은 변수에 다른 타입의 값을 저장하는 것이 가능하다
a4 = 100
print(a4)
print(type(a4))

a4 = 11.11
print(a4)
print(type(a4))

a4 = '문자열'
print(a4)
print(type(a4))
# +
# 파이썬은 변수에 다른 타입의 값을 저장하는 것이 가능하다
a4 = 100
print(a4)
print(type(a4))

a4 = 11.11
print(a4)
print(type(a4))

a4 = '문자열'
print(a4)
print(type(a4))
# -


# 여러 변수에 같은 값을 저장하고자 한다면
a5 = a6 = a7 = 100
print(a5)
print(a6)
print(a7)

# 각 변수에 저장될 값을 각각 다를 경우 다음과 같이 하는 것도 가능하다.
# 여기에는 tuple 이라는 것과 관련된 비밀이 숨어 있다.
a8, a9, a10 = 100, 200, 300
print(a8)
print(a9)
print(a10)

# +
# 파이썬 3.6 부터 변수에 자료형을 명시할 수 있다.
# 변수를 정의할 때 자료형을 명시하면 값을 지정하지 않아도 된다.
# 단 변수를 사용하기 전에 반드시 값을 저장해야 한다.

# 변수에 자료형을 붙혀주는 이유
# 1. 변수를 선언할 때 최초의 값을 지정해주고 싶지 않을 때 -> 그냥 값을 0 같은 값을 넣어주면 된다
# 2. 변수의 타입을 명시적으로 표현하고 싶을때 -> 다른 타입의 값을 저장할 수 있기 때문에 별 의미가 없다
a11:int

a11 = 100
print(a11)

a11 = 11.11
print(a11)
# -


