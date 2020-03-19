# -*- coding:utf-8 -*-
'''
File name: ArcpyExportMap3.py
date: 2020/3/19
author: lenovo
Describe:5个街道行政矢量shp，每个街道出一张图。
'''
import arcpy,os
from datetime import datetime
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def GetShpfiles(shpdir):
    shpfiles = []

    for file in os.listdir(shpdir):
        if os.path.isfile(os.path.join(shpdir, file)):
            if file.endswith('.shp'):
                shpfiles.append(os.path.join(shpdir,file))
        else:
            shpfiles.extend(GetShpfiles(file))
    return shpfiles

#加载地图文档
mxd = arcpy.mapping.MapDocument(r'G:\wl2020\HTXZQ\WFXZQ.mxd')
#获取图层
lyr=arcpy.mapping.ListLayers(mxd)[0]
fp = r'G:\wl2020\HTXZQ'
allshps = GetShpfiles(fp)
for shp in allshps:
    paths = os.path.split(shp)
    filename = paths[1].split('.')[0]
    #修改数据源
    lyr.replaceDataSource(paths[0], "SHAPEFILE_WORKSPACE", filename)
    #更新布局视图范围
    df = arcpy.mapping.ListDataFrames(mxd)[0]
    df.extent = lyr.getExtent()
    #修改标题
    title = arcpy.mapping.ListLayoutElements(mxd,"TEXT_ELEMENT","标题")[0]
    title.text = filename
    day_title = arcpy.mapping.ListLayoutElements(mxd,"TEXT_ELEMENT","日期")[0]
    day_title.text = "%s年%s月%s日制" % (datetime.today().year,datetime.today().month,datetime.today().day)

    export_path =r'G:\wl2020\HTXZQ\\'+filename+'.png'
    arcpy.mapping.ExportToPNG(mxd,export_path,resolution=200)

print 'ok'