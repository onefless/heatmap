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
    
    def categorical_numerical_cols(self,data,cols = None):
        lon_lat = set(['g.parallel_submit','g.meridian_submit'])
        if cols == None:
            self.numeric_cols = list(set(data._get_numeric_data().columns)-lon_lat)
            self.categorical_cols = list(set(data.columns)-set(self.numeric_cols)-lon_lat)
        else:
            self.numeric_cols = []
            self.categorical_cols = []
            for i in cols:
                if i in data[cols].select_dtypes(exclude=["number","bool_"]).columns: #categorical
                    self.categorical_cols.append(i)
                else:
                    self.numeric_cols.append(i)
    
    def get_selection(self,data,cols = None):
        '''
        Input selected cols as a list. 
        '''
        data = data.copy()
        self.categorical_numerical_cols(data,cols)
        dic = {}
        for col in self.categorical_cols:
            dic[col] = list(set(data[col]))
            print(col,':',dic[col])
        for col in self.numeric_cols:
            print(col,': 最大值 {}, 最小值 {}, 缺失值占比 {}'.format(max(data[col]),min(data[col]),data[col].isnull().mean()))   
            
    
    def output_map(self,data,selection,file_path = 'heatmap01.html',marker_info = [],spec_icon = None):
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

        if spec_icon == None:
            for i,point in zip(self.selected_data.index,self.location):
                text = ''
                for col in marker_info:
                    text = text + col + ': ' + str(self.selected_data[col][i]) + '; \n '
                folium.Marker(point,tooltip=(text)).add_to(map_osm)
            map_osm.save(file_path)
            map_osm.save(file_path) 
            print('一共有{}个用户'.format(len(self.location)))
            print('热点图已保存.')
        else:
            color_lst = ['red', 'blue', 'green', 'purple', 'orange', 'darkred','lightred', 'beige', 'darkblue', 
                         'darkgreen', 'cadetblue', 'darkpurple', 'white', 'pink', 'lightblue', 'lightgreen', 'gray', 
                         'black', 'lightgray']
            
            icon_set = set(self.selected_data[spec_icon])
            color_lst_here = color_lst[:num]
            spec_info_value = {}#
            
            for val,i in zip(icon_set,range(num)):
                spec_info_value[val] = i
                
            for i,point in zip(self.selected_data.index,self.location):
                text = ''
                for col in marker_info:
                    text = text + col + ': ' + str(self.selected_data[col][i]) + '; \n '
                
                icon = folium.Icon(color=color_lst[spec_info_value[self.selected_data[spec_icon][i]]])
                folium.Marker(point,tooltip=(text),icon=icon).add_to(map_osm)
            map_osm.save(file_path)
            map_osm.save(file_path) 
            print('一共有{}个用户'.format(len(self.location)))
            print('热点图已保存.')
        #%%
import numpy as np
import pandas as pd

data_path = r'地图sample.csv'
data = pd.read_csv(data_path,encoding='gb18030')

heatmap = ditui_heatmap()

cols = ['分部','自填学历','i.age_val','授信额','i.sex_typ']
heatmap.get_selection(data)

selection = {
        'i.sex_typ': ['男'],
        '自填学历':['本科','大专']
        }

marker_info = ['自填学历']

spec_icon = '自填学历'
heatmap.output_map(data,selection,marker_info = marker_info,spec_icon = spec_icon)

selected_people = heatmap.selected_data  
        

        
        
        