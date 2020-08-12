"""
    날짜 : 2020/07/16
    이름 : 김동욱
    내용 : 파이썬 MongoDB find 실습하기
"""

from pymongo import MongoClient as mongo

#MongoDB 접속
conn = mongo('mongodb://kdw:1234@192.168.100.101:27017')

#db 접속
db = conn.get_database('kdw')

#collection 선택
collection = db.get_collection('member')

#select * from `member`
rs1 = collection.find()

for row in rs1:
    print('%s, %s' % (row['uid'], row['name']))

#select * from `member` where uid='A101'
rs2 = collection.find({'uid':'A101'})

for row in rs2:
    print('%s, %s, %s' % (row['uid'], row['name'], row['hp']))

#select * from `member` where uid='A101' and name='김유신'
rs3 = collection.find({'uid':'A101', 'name':'김유신'})

for row in rs3:
    print('%s, %s, %s, %s' % (row['uid'], row['name'], row['hp'], row['pos']))

#select * from `member` where dep > 103
rs4 = collection.find({'dep':{'$gt':103}})

for row in rs4:
    print('%s, %s, %s, %s, %s' % (row['uid'], row['name'], row['hp'], row['pos'], row['dep']))