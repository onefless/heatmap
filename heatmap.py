#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 21 19:26:32 2019

@author: shaoqiandong
"""

import numpy as np
import pandas as pd
import seaborn as sns
import folium
import webbrowser
from folium.plugins import HeatMap
# posi=pd.read_csv("D:\\Files\\datasets\\CitiesLatLon_China.csv")
posi=pd.read_excel("2015Cities-CHINA.xlsx")
posi.dropna(axis = 0, how = 'any', subset = ['lat','lon'],inplace = True)
num = len(posi)
lat = np.array(posi["lat"][0:num])                        # 获取维度之维度值
lon = np.array(posi["lon"][0:num])                        # 获取经度值
age = np.array(posi["pop"][0:num],dtype=float)    # 获取人口数，转化为numpy浮点型
#gdp = np.array(posi["GDP"][0:num],dtype=float)    # 获GDP口数，转化为numpy浮点型
data1 = [[lat[i],lon[i],1] for i in range(num)]    #将数据制作成[lats,lons,weights]的形式
map_osm = folium.Map(location=[35,110],zoom_start=5)    #绘制Map，开始缩放程度是5倍
HeatMap(data1).add_to(map_osm)  # 将热力图添加到前面建立的map里


file_path = r"heatmap9.html"
map_osm.save(file_path)     # 保存为html文件

webbrowser.open(file_path)  # 默认浏览器打开
#%%

data_path = r'地图sample.csv'
data = pd.read_csv(data_path,encoding='gb18030')

data_cols = list(data.columns)
dic = {}
for col in data_cols:
    dic[col] = list(set(data[col]))
    
#selection = {
#        '分部':['郑州','重庆'],
#        'i.sex_typ': ['男']
#        }

def lst_judge(key,selection,data):
    lst = []
    for i in data[key]:
        if i in selection[key]:
            lst.append(True)
        else:
            lst.append(False)
    return lst

selected_data = data.copy()
for key in selection:
    lst = lst_judge(key,selection,selected_data)
    selected_data = selected_data.loc[lst,:]

num = len(selected_data)
lat = np.array(selected_data["g.parallel_submit"])                        # 获取维度之维度值
lon = np.array(selected_data["g.meridian_submit"])                        # 获取经度值
age = np.array(selected_data["i.age_val"]*10,dtype=float)    # 获取人口数，转化为numpy浮点型

data2 = [[lat[i],lon[i],age[i]] for i in range(num)]    #将数据制作成[lats,lons,weights]的形式
map_osm = folium.Map(location=[35,110],zoom_start=5)    #绘制Map，开始缩放程度是5倍
HeatMap(data2).add_to(map_osm) 
file_path = r"heatmap10.html"
map_osm.save(file_path) 
    #%%
class ditui_heatmap(object):
    
    def __init__(self):
        pass
    
    def lst_judge(self,key,selection,data):
        self.lst = []
        for i in data[key]:
            if i in selection[key]:
                self.lst.append(True)
            else:
                self.lst.append(False)
        return self.lst
    
    
    
    def output_map(self,data,selection,file_path = 'heatmap01.html'):
        file_path,data,selection = file_path,data.copy(),selection.copy()
        self.selected_data = data.copy()

        for key in selection:
            lst = self.lst_judge(key,selection,self.selected_data)
            self.selected_data = self.selected_data.loc[lst,:]
            
        self.num = len(self.selected_data)
        lat = np.array(selected_data["g.parallel_submit"])                       
        lon = np.array(selected_data["g.meridian_submit"])
        
        self.location = [[lat[i],lon[i]] for i in range(self.num)]
        
        try:
            folium
        except:
            import folium
        
        try:
            HeatMap
        except:
            from folium.plugins import HeatMap
            
        map_osm = folium.Map(location=[35,110],zoom_start=5) 
        HeatMap(self.location).add_to(map_osm)
        for i,point in zip(range(self.num),self.location):
            folium.Marker(point,tooltip=('Age:{}'.format(self.selected_data['i.age_val'][i])))
        map_osm.save(file_path) 
        print('一共有{}个用户'.format(len(self.location)))
        print('热点图已保存.')
        
#%%
selection = {
        '分部':['郑州','重庆','广州','深圳'],
        'i.sex_typ': ['男'],
        '自填学历':['大专','高中']
        
        }

heatmap = ditui_heatmap()
heatmap.output_map(data,selection)


        
        
        
test = heatmap.selected_data     
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    