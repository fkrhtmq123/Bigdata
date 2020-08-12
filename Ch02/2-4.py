"""
    날짜 : 2020/07/22
    이름 : 김동욱
    내용 : 파이썬 Hadoop 실습하기
"""

#from pywebhdfs.webhdfs import PyWebHdfsClient as hadoop
import webhdfspy

#hadoop 접속
hdfs = webhdfspy.WebHDFSClient(host='192.168.100.101', port=50070, username='root')

#Local /home/bigdata/naver/naver-20-xx-xx 를 하둡 /naver/ 복사
hdfs.copyfromlocal(local_path='/home/bigdata/naver/naver-20-07-15', hdfs_path='/naver/', overwrite=None)

#Local /home/bigdata/naver/naver-20-xx-xx 를 삭제
hdfs.remove(path='/home/bigdata/naver/naver-20-07-15')

#프로그램 종료