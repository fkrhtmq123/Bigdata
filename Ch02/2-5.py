"""
    날짜 : 2020/07/22
    이름 : 김동욱
    내용 : 파이썬 logging 실습하기
"""

import logging

# 기본 로그 레벨 설정
logging.basicConfig(filename='./2-5.log', level=logging.DEBUG)

# 각 로그 레벨 기본 출력
logging.debug('log debug...')
logging.info('log info...')
logging.warning('log warn...')
logging.error('log error...')
logging.fatal('log fatal...')

print('로그 파일 생성 완료...')