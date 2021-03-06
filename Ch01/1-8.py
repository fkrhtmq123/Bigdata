"""
    날짜 : 2020/07/14
    이름 : 김동욱
    내용 : 파이썬 가상 웹브라우저 실습하기(네이버)
"""

import requests as req
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from datetime import datetime
from openpyxl import Workbook

#크롬 가상브라우저 실행
browser = webdriver.Chrome('./chromedriver.exe')

#네이버 데이터 랩 메인 이동
browser.get('https://datalab.naver.com/keyword/realtimeList.naver?where=main')

#네이버 실검 1~10위 파싱
item_boxs = browser.find_elements_by_css_selector('#content > div > .selection_area > .selection_content > .field_list > div > div > ul:nth-child(1) > li > .item_box')

#파일로 저장
"""
fname = "{:%y-%m-%d-%H-%M.txt}".format(datetime.now())
file = open(fname, mode='w', encoding='utf8')

file.write('순위, 제목, 날짜\n')
now = "{:%y-%m-%d-%H:%M:%S}".format(datetime.now())

for item in item_boxs:
    file.write('%s,' % item.find_element_by_css_selector('.item_num').text)
    file.write('%s' % item.find_element_by_css_selector('.item_title_wrap > .item_title').text)
    file.write('%s\n' % now)

#파일 닫기
file.close()
"""

#새로운 엑셀 파일 생성
workbook = Workbook()

#현재 acrive sheet 열기
sheet = workbook.active

for item in item_boxs:
    num = item.find_element_by_css_selector('.item_num').text
    tit = item.find_element_by_css_selector('.item_title_wrap > .item_title').text
    now = "{:%y%m%d%H%M%S}".format(datetime.now())

    sheet.append(['%s' % num, '%s' % tit, '%s' % now])

#엑셀파일 저장
workbook.save('./naver.xlsx')
workbook.close()