import arcpy
arcpy.env.workspace = "C:\Geog 5620\PythonPro\Ex08"
fc = "airports.shp"
with arcpy.da.InsertCursor(fc, "NAME") as cursor:
 cursor.insertRow(["New Airport"]) 
