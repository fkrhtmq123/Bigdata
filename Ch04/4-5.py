"""
    날짜 : 2020/08/11
    이름 : 김동욱
    내용 : 머신런닝 - 다중 선형회귀 분석 연습문제
"""

from sklearn.linear_model import LinearRegression

#학습데이터
train_data = [[170, 30, 1], [155, 60, 2], [150, 50, 2], [175, 40, 1], [165, 20, 1]]
train_label = [65, 50, 45, 70, 55]

#학습하기
model = LinearRegression()
model.fit(train_data, train_label)

#모델검증
test_data = [[180, 27, 1], [168, 20, 2]]
result = model.predict(test_data)
print('result : ', result)