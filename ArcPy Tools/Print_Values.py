import arcpy
arcpy.env.workspace = "C:\Geog 5620\PythonPro\Ex08"
fc = "airports.shp"
cursor = arcpy.da.SearchCursor(fc, ["NAME"])
for row in cursor:
 print("Airport name = {0}".format(row[0])) 
