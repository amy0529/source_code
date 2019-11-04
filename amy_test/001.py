import json
import sys
def saveTOJSON(filename,dicObject):
    flag=False
    if type(dicObject)!=dict:
        return flag
    try:
        j_file=open(filename,'w')
        json.dump(dicObject,j_file,ensure_ascii=False)
        flag=True
    except:
        print('写入%s出错'%(filename))
    finally:
        if flag:
            j_file.close()
    return flag

def GetFromJson(filename):
    flag=False
    dicObject={}
    try:
        j_file=open(filename,'r')
        dicObject=json.load(j_file)
        flag=True
    except:
        print('读取%s出错'%(filename))
    finally:
        if flag:
            j_file.close()
    return dicObject
d_student={'name':'丁丁','age':'12','birthday':'2016年12月25日'}
filename='d:\\student.json'
f_ok=saveTOJSON(filename,d_student)
if f_ok:
    print('学生信息保存成功')
else:sys.exit()
d_get_student=GetFromJson(filename)
if d_get_student:
    print(d_get_student)