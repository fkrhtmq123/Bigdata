"""
    날짜 : 2020/07/15
    이름 : 김동욱
    내용 : 파이썬 현재 날씨 크롤링
"""

import os
import requests as req
from bs4 import BeautifulSoup as bs
from datetime import datetime

sess = req.session()

html = sess.get('https://www.weather.go.kr/weather/observation/currentweather.jsp')

#print(html)

dom = bs(html.text, 'html.parser')

#지점, 시정, 현재기온, 이슬점온도, 체감온도, 일강수, 습도, 풍향, 해면기압
locals = dom.select('#content_weather > table > tbody > tr > td > a')
visibilities = dom.select('#content_weather > table > tbody > tr > td:nth-child(3)')
temps = dom.select('#content_weather > table > tbody > tr > td:nth-child(6)')
dews = dom.select('#content_weather > table > tbody > tr > td:nth-child(7)')
sensibles = dom.select('#content_weather > table > tbody > tr > td:nth-child(8)')
recipitations = dom.select('#content_weather > table > tbody > tr > td:nth-child(9)')
humidities = dom.select('#content_weather > table > tbody > tr > td:nth-child(10)')
direction_winds = dom.select('#content_weather > table > tbody > tr > td:nth-child(11)')
wind_speeds = dom.select('#content_weather > table > tbody > tr > td:nth-child(12)')
atiomspheric_pressure = dom.select('#content_weather > table > tbody > tr > td:nth-child(13)')

#저장 디렉터리 생성
dir = '/home/bigdata/weather/weather-{:%y-%m-%d}'.format(datetime.now())
if not os.path.exists(dir):
    os.mkdir(dir)

#파일로 저장 20-07-15-16.csv
fname = "{:%y-%m-%d-%H.csv}".format(datetime.now())
file = open(dir + '/' + fname, mode='w', encoding='utf8')

#csv 헤더
file.write('지점, 시정, 현재기온, 이슬점온도, 체감온도, 일강수, 습도, 풍향, 해면기압\n')

for i in range(0, len(locals)):
    file.write(locals[i].text + ',' +
          visibilities[i].text + ',' +
          temps[i].text + ',' +
          dews[i].text + ',' +
          sensibles[i].text + ',' +
          recipitations[i].text + ',' +
          humidities[i].text + ',' +
          direction_winds[i].text + ',' +
          #wind_speeds[i].text + ',' +
          atiomspheric_pressure[i].text+'\n')

#파일 닫기
file.close()