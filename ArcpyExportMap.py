# -*- coding:utf-8 -*-
"""
File name: ArcpyExportMap2.py
date: 2020/3/17
author: lenovo
Describe:结合数据驱动界面设置配合出图
"""
import arcpy

mxd = arcpy.mapping.MapDocument(r'C:\Users\lenovo\Desktop\ExportMap.mxd')
for pageNum in range(1,mxd.dataDrivenPages.pageCount):
    mxd.dataDrivenPages.currentPageID = pageNum
    mapName = mxd.dataDrivenPages.pageRow.getValue(mxd.dataDrivenPages.pageNameField.name)
    print mapName
    arcpy.mapping.ExportToJPEG(mxd,r'G:\wl2020\ExportToMap\\'+mapName+'.jpg')
    print 'ok'