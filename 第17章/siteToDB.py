import requests                                         
r=requests.get('https://www.amazon.cn/')                       
dis={"_id":2,"context":r.text}            
import pymongo                                            
from pymongo.mongo_client import MongoClient 
mongoClient=MongoClient('localhost',27017)       
mongoDatabase=mongoClient.site                     
mongoCollection=mongoDatabase.T_context
#mongoCollection.insert(dis)                         
import pprint                                              
for get in mongoCollection.find({"_id":2}):         
	pprint.pprint(get)                             
