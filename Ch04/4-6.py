"""
    날짜 : 2020/08/11
    이름 : 김동욱
    내용 : 머신런닝 - 로지스틱 회귀분석 실습
"""

from sklearn.linear_model import LogisticRegression

#훈련데이터
train_date = [[40, 30], [30, 80], [20, 70], [70, 40], [60, 20]]
train_label = [+1, -1, -1, +1, +1]

#학습하기
model = LogisticRegression()
model.fit(train_date, train_label)

#모델검증
result = model.predict(train_date)
print('result : ', result)

#새로운 데이터 검증
test_data = [[46.12, 62.53], [27.20, 45.12], [37.15, 51.22]]
test_result = model.predict(test_data)
print('test_result : ', test_result)