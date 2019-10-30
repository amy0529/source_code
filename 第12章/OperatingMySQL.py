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
#============================对表进行插入、修改、删除、查找操作
cur=conn.cursor()
insertSQL='''insert into T_fish values('2018-3-28','黑鱼',10,28.3,'Tom')'''
insertSQL1='''insert into T_fish values('2018-3-29','鲤鱼',25,9.8,'John')'''
try:
    cur.execute(insertSQL)
    cur.execute(insertSQL1)
    conn.commit()
    print("两条记录插入成功！")
except:
    print("两条记录插入失败！")
    conn.close()
    sys.exit()
updateSQL="update T_fish set nums=12 where date1='2018-3-28'"
try:
    cur.execute(updateSQL)
    conn.commit()
    print("第一条记录修改成功！")
except:
    print("第一条记录修改失败！")
    conn.close()
    sys.exit()
deleteSQL="DELETE FROM t_fish WHERE date1='2018-3-29'"
try:
    cur.execute(deleteSQL)
    conn.commit()
    print("第二条记录删除成功！")
except:
    print("第二条记录删除失败！")
    conn.close()
    sys.exit()

selectSQL='Select * from T_fish'
cur.execute(selectSQL)
l_records=[]
for row in cur.fetchall():
    l_records.append(row)
print(l_records)

    
