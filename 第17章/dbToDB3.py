import pymongo
from pymongo.mongo_client import MongoClient
mongoClient=MongoClient('localhost',27017)
mongoDatabase=mongoClient.site
mongoCollection=mongoDatabase.T_context
gets=mongoCollection.find_one({"_id":2})

import re
pa=re.compile(r'<option.+>(.+?)</option>')
option=pa.findall(gets["context"])

mongoCollection=mongoDatabase.T_end_text
add={"_id":2,"context":option}
mongoCollection.insert(add)
import pprint                                              
for get in mongoCollection.find({"_id":2}):         
	pprint.pprint(get)                             
