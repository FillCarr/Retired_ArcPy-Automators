import arcpy
arcpy.env.workspace = "C:\Geog 5620\PythonPro"
fc = "cities.shp"
newfc = "cities_copy.shp"
if arcpy.Exists(fc):
    arcpy.CopyFeatures_management(fc, newfc)
