import arcpy
import fileinput
import os
ws = "C:\Geog 5620\PythonPro\Ex09"
arcpy.env.workspace = ws
arcpy.env.overwriteOutput = True
newfc = "newpolyline.shp"
arcpy.CreateFeatureclass_management(ws, newfc,"Polyline", 
spatial_reference = "dams.prj")
