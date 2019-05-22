#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 22 21:13:06 2019

@author: shaoqiandong
"""

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
            
        num = len(self.selected_data)
        lat = np.array(selected_data["g.parallel_submit"])                       
        lon = np.array(selected_data["g.meridian_submit"])
        
        self.location = [[lat[i],lon[i]] for i in range(num)]
        
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
        map_osm.save(file_path) 
        print('一共有{}个用户'.format(len(self.location)))
        print('热点图已保存.')
#%%
import numpy as np
import pandas as pd

data_path = r'地图sample.csv'
data = pd.read_csv(data_path,encoding='gb18030')

selection = {
        '分部':['郑州','重庆','广州','深圳'],
        'i.sex_typ': ['男'],
        '自填学历':['大专','高中']
        
        }

heatmap = ditui_heatmap()
heatmap.output_map(data,selection)

selected_people = heatmap.selected_data  
        
        
        
        