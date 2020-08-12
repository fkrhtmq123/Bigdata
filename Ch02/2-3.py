"""
    날짜 : 2020/07/22
    이름 : 김동욱
    내용 : 파이썬 Hadoop 실습하기
"""

#from pywebhdfs.webhdfs import PyWebHdfsClient as hadoop
import webhdfspy

#hadoop 접속
hdfs = webhdfspy.WebHDFSClient(host='192.168.100.101', port=50070, username='root')

#HDFS 디렉토리 생성
hdfs.mkdir('/sample')

#HDFS 파일 생성
text = 'Hello Hadoop! 반갑습니다.'
hdfs.create('/sample/test.txt', text.encode('UTF-8'), overwrite=True)

print('프로그램 종료...')