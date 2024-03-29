from FishDB_class import FishDB

content1={1:[0,'<fish day="2018-1-1">'],
         2:[4,'<goods>'],
         3:[8,'<name>鲫鱼</name>'],
         4:[8,'<amount>17</amount>'],
         5:[8,'<price>10.5</price>'],
         6:[4,'</goods>'],
         7:[4,'<goods>'],
         8:[8,'<name>鲤鱼</name>'],
         9:[8,'<amount>8</amount>'],
         10:[8,'<price>6.2</price>'],
         11:[4,'</goods>'],
         12:[4,'<goods>'],
         13:[8,'<name>鲢鱼</name>'],
         14:[8,'<amount>7</amount>'],
         15:[8,'<price>4.7</price>'],
         16:[4,'</goods>'], 
         17:[0,'</fish>']}

content2={1:[0,'<fish day="2018-1-2">'],
         2:[4,'<goods>'],
         3:[8,'<name>草鱼</name> '],
         4:[8,'<amount>2</amount>'],
         5:[8,'<price>7.2</price>'],
         6:[4,'</goods>'],
         7:[4,'<goods>'],
         8:[8,'<name>鲫鱼</name> '],
         9:[8,'<amount>3</amount>'],
         10:[8,'<price>12</price>'],
         11:[4,'</goods>'],
         12:[4,'<goods>'],
         13:[8,'<name>黑鱼</name> '],
         14:[8,'<amount>6</amount>'],
         15:[8,'<price>15</price>'],
         16:[4,'</goods>'],
         17:[0,'</fish>']}

content3={1:[0,'<fish day="2018-1-3">'], 
         2:[4,'<goods>'],
         3:[8,'<name>乌鱼</name> '],
         4:[8,'<amount>1</amount>'],
         5:[8,'<price>78.10</price>'],
         6:[4,'</goods>'],
         7:[4,'<goods>'],
         8:[8,'<name>鲫鱼</name> '],
         9:[8,'<amount>1</amount>'],
         10:[8,'<price>10.78</price>'],
         11:[4,'</goods>'],
         12:[4,'<goods>'],
         13:[8,'<name>草鱼</name> '],
         14:[8,'<amount>5</amount>'],
         15:[8,'<price>7.92/price>'],
         16:[4,'</goods>'],
         17:[0,'</fish>']}
new_xml=FishDB()
DBRecord=[] #索引记录
DBRecord.append([0,'<DBrecord">'])
def writeDBrecord(DBR,no,filename,path,date,dbName):
    DBR.append([4,'<record>'])
    DBR.append([8,'<no>'+str(no)+'</no>'])
    DBR.append([8,'<filename>'+filename+'</filename>'])
    DBR.append([8,'<path>'+path+'</path>'])
    DBR.append([8,'<date>'+date+'</date>'])
    DBR.append([8,'<dbName>'+dbName+'</dbName>'])
    
#====================写入2018年1月1日的钓鱼记录
filename="Fish_record1.xml"
new_xml.filename="\\"+filename
new_xml.path="d:\cat_fish"
new_xml.check_path()
flag=False
try:
    new_xml.openfile()
    for get_item in content1.items():
        new_xml.writeXML(get_item[1][0],get_item[1][1])
        flag=True
except:
    print('往文件内容出错,退出程序!')
    sys.exit()
finally:
    if flag:
        new_xml.closeXML()
        print('往%s写内容完成!'%(filename))
        writeDBrecord(DBRecord,1,'Fish_record1.xml','d:\cat_fish','2018-1-1','Cat_Fish')

#====================写入2018年1月2日的钓鱼记录
filename="Fish_record2.xml"
new_xml.filename="\\"+filename
new_xml.path="d:\cat_fish"
new_xml.check_path()
flag=False
try:
    new_xml.openfile()
    for get_item in content2.items():
        new_xml.writeXML(get_item[1][0],get_item[1][1] )
        flag=True
except:
    print('往文件内容出错,退出程序!')
    sys.exit()
finally:
    if flag:
        new_xml.closeXML()
        print('往%s写内容完成!'%(filename))
        writeDBrecord(DBRecord,2,'Fish_record2.xml','d:\cat_fish','2018-1-2','Cat_Fish')
#====================写入2018年1月3日的钓鱼记录
filename="Fish_record3.xml"
new_xml.filename="\\"+filename
new_xml.path="d:\cat_fish"
new_xml.check_path()
flag=False
try:
    new_xml.openfile()
    for get_item in content3.items():
        new_xml.writeXML(get_item[1][0],get_item[1][1] )
        flag=True
except:
    print('往文件内容出错,退出程序!')
    sys.exit()
finally:
    if flag:
        new_xml.closeXML()
        print('往%s写内容完成!'%(filename))
        writeDBrecord(DBRecord,3,'Fish_record3.xml','d:\cat_fish','2018-1-3','Cat_Fish')
DBRecord.append([0,'</DBrecord">'])
#====================写入索引记录
filename="index_database.xml"
new_xml.filename="\\"+filename
new_xml.path="d:\cat_fish"
new_xml.check_path()
flag=False
try:
    new_xml.openfile()
    for get_item in DBRecord:
        new_xml.writeXML(get_item[0],get_item[1])
        flag=True
except:
    print('往文件内容出错,退出程序!')
    sys.exit()
finally:
    if flag:
        new_xml.closeXML()
        print('往%s写内容完成!'%(filename))
