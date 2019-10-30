import requests                                         
r=requests.get('https://www.amazon.cn/')                       
dis={"_id":2,"context":r.text}            
import pymongo                                            
from pymongo.mongo_client import MongoClient 
mongoClient=MongoClient('localhost',27017)       
mongoDatabase=mongoClient.site                     
mongoCollection=mongoDatabase.T_end_text
#mongoCollection.insert(dis)                         
import pprint                                              
for get in mongoCollection.find({"_id":1}):         
	pprint.pprint(get)                             
