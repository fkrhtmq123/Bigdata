"""
    날짜 : 2020/08/13
    이름 : 김동욱
    내용 : 머신런닝 - 퍼셉트론 실습(인터넷 참고)
"""

import numpy as np

def AND(x1, x2):
    w1, w2, theta = 0.5, 0.5, 0.7 #가중치, theta 값 입력
    tmp = x1*w1 + x2*w2 #수식
    if tmp <= theta:
        return 0
    elif tmp > theta:
        return 1

#파이썬 코드: NAND 구현
def NAND(x1, x2):
    w1, w2, theta = -0.5, -0.5, -0.7 #가중치, theta 값 입력
    tmp = x1*w1 + x2*w2 #수식
    if tmp <= theta:
        return 0
    elif tmp > theta:
        return 1

def OR(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.2 #편향
    tmp = np.sum(w*x) +b
    if tmp <= 0:
        return 0
    else:
        return 1

#파이썬 코드: XOR 구현
def XOR(x1, x2):
    s1 = NAND(x1, x2)
    s2 = OR(x1, x2)
    y = AND(s1, s2)
    return y

print(XOR(1, 0))