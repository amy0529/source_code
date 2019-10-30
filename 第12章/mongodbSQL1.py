import pymongo
from pymongo.mongo_client import MongoClient
import pymongo.errors
    
try:
    mongoClient=MongoClient('localhost',27017)#建立mongodb数据库连接通道
    mongoDatabase=mongoClient.goods          #若没有goods数据库则建立新空库，否则建立跟该数据库的连接
    print("数据库连接成功！")
    mongoCollection=mongoDatabase.T_fish    #若没有T_fish集合则建立空集合，否则建立跟该集合的连接
    mongoCollection.remove()                #移除该集合所有记录
     # 添加数据
    mongoCollection.insert_many([{"date1": "2018年3月28", "name": "黑鱼", "nums": "10","price":"28.3", "Explain": "Tom"},
                         {"date1": "2018年3月29", "name": "鲤鱼", "nums": "25","price":"9.8", "Explain": "John"},
                          {"date1": "2018年3月30", "name": "鲫鱼", "nums": "30","price":"23.9", "Explain": "Jack"}
                                , ])
 
    #获取集合中的值
    for row in mongoCollection.find():
        print(row)
 
except pymongo.errors.PyMongoError as e:
    print("mongo Error:", e)
