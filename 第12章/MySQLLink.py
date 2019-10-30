import pymysql
import sys
#============================连接数据库
try:   
   conn=pymysql.connect(host='localhost', user='root', passwd='mysql123', db='test', port=3306,
                                 charset='utf8')
except:
    print("打开数据库连接出错，请检查！")
    conn.close()
    sys.exit()
#============================判断表是否存在，不存在时建立新表
cur=conn.cursor()
sql='''create table if not exists T_fish
    (date1 char(12) primary key not null,
     name char(10) not null,
     nums int not null,
     price decimal(10,2) not null,
     sExplain varchar(200));'''
try:
    cur.execute(sql)
    conn.commit()
    print("T_fish表可以使用！")
except:
    print("T_fish表是否建立过程出错！")
conn.close()
