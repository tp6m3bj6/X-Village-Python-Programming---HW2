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
list1=[]
list2=[]
list3=[]
list4=[]
list5=[]
for i in data:
    list1.append(float(i['工業用電(百萬度)']))
    list2.append(float(i['民生用電(百萬度)']))
    list3.append(float(i['尖峰負載(MW)']))
    list4.append(float(i['備轉容量(MW)']))
    list5.append(float(i['備轉容量率(%)']))

###繪製工業用電與民生用電圓餅圖
y1=sum(list1)
y2=sum(list2)
labels='For Industy use(GWh)','For General use(GWh)'
y=(y1,y2)

##plot圓餅圖，比較工業用電和民生用電
plt.pie(y , labels = labels,autopct='%1.1f%%')
plt.show()

###雙Ｙ軸圖表，比較尖峰負載以及備載容量
x=np.arange(0,len(list3),1)
fig = plt.figure()

ax1 = fig.add_subplot(111)
l1, =ax1.plot(x, list3, label='Peaking power(MW)', color='blue')
ax1.set_ylabel('Peaking power(MW)')
ax1.set_title("106/01/01-107/06/30")
ax1.set_xlabel('Day')

ax2 = ax1.twinx()  
l2, =ax2.plot(x, list4, 'r',label='Operating reserve(MW)', color='red')
ax2.set_xlim([0, len(x)])
ax2.set_ylabel('Operating reserve(MW)')
ax2.set_ylim([500, 10000])

#上標籤
plt.legend(handles = [l1, l2,], labels = ['Peaking power(MW)', 'Operating reserve(MW)'], loc = 'best')
plt.show()

###


