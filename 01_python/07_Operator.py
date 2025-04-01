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

# # 연산자
# - 값 들을 가지고 계산을 하기 위한 특수 문자들
# - 키보드에 있는 특수문자 대부분이 연산자이다.

# ### 산술 연산자
# - "+" : 더하기
# - "-" : 빼기
# - "*" : 곱하기
# - "/" : 나누기. 결과가 실수
# - "//" : 나누기. 결과가 정수
# - "%" : 나머지
# - "**" : 거듭제곱

v1 = 10
v2 = 21

# +
# 더하기
a1 = v1 + v2
print('v1 + v2 =', a1)

# 빼기
a2 = v1 - v2
print('v1 - v2 =', a2)

# 곱하기
a3 = v1 * v2
print('v1 * v2 =', a3)

# 나누기 : 결과는 실수
a4 = v1 / v2
print('v1 / v2 =', a4)

# 나누기 : 결과는 정수
a5 = v1 // v2
print('v1 // v2 =', a5)

# 나머지
a6 = v1 % 3
print('v1 % 3 =', a6)

# 거듭 제곱
a7 = v1 ** 3
print('v1 ** 3 =', a7)
# -

# ### 비교 연산자
# - 좌측의 값이 우측값과 비교하여 어떻다 라는 비교 연산을 수행한다.
# - 결과는 True나 False로 나온다
# - "==" : 좌측의 값이 우측의 값과 같다
# - "!=" : 좌측의 값이 우측의 값과 다르다
# - ">" : 좌측의 값이 우측의 값보다 큰가
# - "<" : 좌측의 값이 우측의 값보다 작은가
# - ">=" : 좌측의 값이 우측의 값보다 크거나 같은가
# - "<=" : 좌측의 값이 우측의 값보다 작거나 같은가 

v1 = 10
print(v1 == 10)
print(v1 == 20)
print(v1 != 10)
print(v1 != 20)
print(v1 > 5)
print(v1 > 20)
print(v1 < 5)
print(v1 < 20)
print(v1 >= 5)
print(v1 >= 10)
print(v1 >= 20)
print(v1 <= 5)
print(v1 <= 10)
print(v1 <= 20)

# ### 증감 연산자
# - ++, -- : 변수에 저장되어 있는 값을 1 증가 시키거나 1 감소시키는 연산자이다. 파이썬은 지원하지 않는다.
# - +=, -=, *=, /=, //=, %=, **= 연산자를 사용할 수 있다

# +
v1 = 10
v2 = 10

v1 = v1 + 10
v2 += 10
print(v1)
print(v2)

# +
v1 = 10
v2 = 10

v1 = v1 * 3
v2 *= 3

print(v1)
print(v2)
# -

# ### 논리 연산자
# - 연산자 좌측과 우측에는 참, 거짓을 결과하는 연산식이 존재해야 한다.
# - and : 좌측과 우측이 하나라도 False면 최종 결과는 False가 된다.
# - or : 좌측과 우측이 하나라도 True면 최종 결과는 True가 된다.
# - not : 우측의 결과가 True면 False로, False면 True로 바꿔준다.

# +
v1 = 10
v2 = 20

print(v1 > 5 and v2 > 10)
print(v1 > 20 and v2 > 10)

print(v1 < 5 or v2 < 10)
print(v1 > 5 or v2 < 10)

print(not v1 < 5)
print(not v1 > 5)
# -


