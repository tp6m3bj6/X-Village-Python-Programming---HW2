###台灣電力公司_過去電力供需資訊
###每日電力供需資訊及機組發電量對尖峰備轉容量率之影響(2017一月～2018六月)。
import json
import requests
import matplotlib.pyplot as plt
import pandas
from collections import Counter 
import numpy as np
from matplotlib.legend_handler import HandlerLine2D

url='https://quality.data.gov.tw/dq_download_json.php?nid=19995&md5_url=b19416acd7a4a1e9391f17095a0bbc7e'
r=requests.get(url)
r.encoding='urf-8'

###show json
data=json.loads(r.text)
data2=json.dumps(data, ensure_ascii=False, indent=4)
# print(data2)

###擷取資料
x=[]
y1=[]
y2=[]
y3=[]
y4=[]
y5=[]
y6=[]
y7=[]
y8=[]
y9=[]
y10=[]
y11=[]

for i in data:
    y1.append(float(i['工業用電(百萬度)']))
    y2.append(float(i['民生用電(百萬度)']))
    y3.append(float(i['尖峰負載(MW)']))
    y4.append(float(i['備轉容量(MW)']))
    y5.append(float(i['備轉容量率(%)']))
    y6.append(float(i['核一#1(萬瓩)']))
    y7.append(float(i['核一#2(萬瓩)']))
    y8.append(float(i['核二#1(萬瓩)']))
    y9.append(float(i['核二#2(萬瓩)']))
    y10.append(float(i['核三#1']))
    y11.append(float(i['核三#2']))


###繪製工業用電與民生用電圓餅圖
y1=sum(y1)
y2=sum(y2)
labels='For Industy use(GWh)','For General use(GWh)'
y=(y1,y2)
plt.pie(y , labels = labels,autopct='%1.1f%%')
plt.show()

###雙Ｙ軸圖表，比較尖峰負載以及備載容量
x=np.arange(0,len(y3),1)
fig = plt.figure()

ax1 = fig.add_subplot(111)
l1, =ax1.plot(x, y3, color='blue')
ax1.set_ylabel('Peaking power(MW)')
ax1.set_title("106/01/01-107/06/30")
ax1.set_xlabel('Day')

ax2 = ax1.twinx()  
l2, =ax2.plot(x, y4, 'r', color='red')
ax2.set_xlim([0, len(x)])
ax2.set_ylabel('Operating reserve(MW)')
ax2.set_ylim([500, 10000])

#上標籤
plt.legend(handles = [l1, l2,], labels = ['Peaking power(MW)', 'Operating reserve(MW)'], loc = 'best')
plt.show()

###統計各核能場總發電量
yt=sum(y6),sum(y7),sum(y8),sum(y9),sum(y10),sum(y11)
index = np.arange(1,7)
plt.bar(index,height =yt, width=0.35, alpha=0.4)
plt.xlabel('Nuclear Plant')
plt.ylabel('KW')
plt.xticks(index,('NP1#1','NP1#2','NP2#1','NP2#2','NP3#1','NP3#2'))
plt.show()

###統計核能場佔總發電量百分比
ytotal=sum(y)
ytotal_N=sum(yt)
labels='Traditional','Newclear'
y_present=(ytotal,ytotal_N)

##plot圓餅圖，比較工業用電和民生用電
plt.pie(y_present , labels = labels,autopct='%1.1f%%')
plt.show()
