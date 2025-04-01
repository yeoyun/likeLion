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

# # 주석
# - 프로그램 코드 실행 시 건너뛰는 부분을 의미한다.
# - 앞에 (#)을 붙여주면 그 라인은 주석처리됨.
# - 보통 설명을 작성하거나, 실행하고 싶지 않은 코드가 있을 경우 사용.

# +
# 이 부분은 주석입니다.
# 실행할 때 건너뛰는 부분입니다.
a1 = 10 + 20
print(a1)

# 여러 줄을 선택 후 ctrl+/ 시 한번에 주석처리 가능
# -

#파이썬에서는 기본적으로 한줄 주석만 지원
'''
문자열 처리가 되어있으므로 (메모리에 존재)
만약에 이 부분이 제일 마지막에 있다면
실행결과에 출력되며, prompt에서도 입력시 출력됨
'''
a1=10+20
print(a1)

# # 출력
# - print() : ( ) 안에 출력하고자 하는 것을 넣어주면 출력을 하고 밑으로 내려준다 (tab) .

print(100)
print(11.11)

# 쉼표로 구분하여 여러 개를 작성해주면 띄어쓰기를 하여 출력해준다.
print(100,200,300)

# # 문자열
# - 파이썬은 작은 따옴표('), 큰 따옴표(") 모두 문자열로 취급한다.
# - 작은 따옴표 세개('''), 큰 따옴표 세개(""")로 묶어주는 문자열도 제공된다.

print('문자열')
print("문자열")
print('''동해물과 백두산이
마르고 닳도록''')
print("""동해물과 백두산이
마르고 닳도록""")


