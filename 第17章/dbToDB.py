import pymongo
from pymongo.mongo_client import MongoClient
mongoClient=MongoClient('localhost',27017)
mongoDatabase=mongoClient.site
mongoCollection=mongoDatabase.T_context
gets=mongoCollection.find_one({"_id":2})

import re
pa=re.compile(r'<option.+>(.+?)</option>')
option=pa.findall(gets["context"])
To_text=[]
for get_text in option:
    To_text.append(get_text)
mongoCollection=mongoDatabase.T_end_text
add={"_id":1,"context":To_text}
mongoCollection.insert(add)
import pprint                                              
for get in mongoCollection.find({"_id":1}):         
	pprint.pprint(get)                             
