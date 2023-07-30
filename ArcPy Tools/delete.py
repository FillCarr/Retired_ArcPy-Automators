import arcpy
arcpy.env.workspace = "C:\Geog 5620\PythonPro\Ex08"
fc = "airports.shp"
with arcpy.da.UpdateCursor(fc, ["TOT_ENP"]) as cursor:
    for row in cursor:
        if row[0] < 100000:
            cursor.deleteRow() 
