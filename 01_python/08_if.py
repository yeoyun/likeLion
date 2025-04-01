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

# # if 문
# - if 문에 주어진 연산식의 결과가 True 일 경우에만 관리하는 코드를 수행한다.

a1 = 100

# a1 은 100이 저장되어 있으므로 True이기 때문에 관리하는 코드가 수행 된다
if a1 == 100 :
    print("a1은 100 입니다")# a1 은 100이 저장되어 있으므로 True이기 때문에 관리하는 코드가 수행 된다

# a1은 100이 저장되어 있으므로 False이기 때문에 관리하는 코드가 수행되지 않는다.
if a1 != 100 :
    print("a1은 100이 아닙니다")

# +
# 파이썬에서는 if문과 같이 어떠한 코드를 관리하는 요소들은 자신이 관리하는 코드의 범위를 들여쓰기로
# 구분한다.
# 파이썬 코드를 작성하실때는 들여쓰기를 반드시 주의해주세요~~~~
if a1 != 100 :
    print("for 1")
    print("이 부분이 수행될 까요? 1")

if a1 != 100 :
    print("for 2")
print("이 부분이 수행될 까요? 2")
# -


