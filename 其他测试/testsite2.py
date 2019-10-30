#coding : UTF-8
import requests
import csv
import random
import time
import socket
import http.client
#import urllib.request
from bs4 import BeautifulSoup

def get_content(url):  # 该方法传入url，返回url的html的源码  
    headers = {  
        'User-Agent': 'MMozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20100101 Firefox/31.0'  
    }  
  
    r= requests.get(url,headers=headers)  
    r.encoding='UTF-8'  
    page = r.text  
    return page  


def get_data(html_text):
    final = []
    bs =BeautifulSoup(html_text, "html.parser") # 创建BeautifulSoup对象
    body = bs.body # 获取body部分
    data =body.find('div', {'id': '7d'})  # 找到id为7d的div
    ul = data.find('ul')  # 获取ul部分
    li =ul.find_all('li')  # 获取所有的li
 
    for day in li: # 对每个li标签中的内容进行遍历
        temp = []
        date =day.find('h1').string  # 找到日期
        temp.append(date)  # 添加到temp中
        inf =day.find_all('p')  # 找到li中的所有p标签
        temp.append(inf[0].string,)  # 第一个p标签中的内容（天气状况）加到temp中
        if inf[1].find('span') is None:
           temperature_highest = None# 天气预报可能没有当天的最高气温（到了傍晚，就是这样），需要加个判断语句,来输出最低气温
        else:
           temperature_highest = inf[1].find('span').string  # 找到最高温
           temperature_highest = temperature_highest.replace('℃', '')  # 到了晚上网站会变，最高温度后面也有个℃
        temperature_lowest = inf[1].find('i').string  # 找到最低温
        temperature_lowest = temperature_lowest.replace('℃', '')  # 最低温度后面有个℃，去掉这个符号
        temp.append(temperature_highest)  # 将最高温添加到temp中
        temp.append(temperature_lowest)   #将最低温添加到temp中
        final.append(temp)   #将temp加到final中
 
    return final
if __name__ == '__main__':
    url ='http://www.weather.com.cn/weather/101190401.shtml'
    html =get_content(url)
    result =get_data(html)
    print(result)
    #rite_data(result, 'weather.csv')
