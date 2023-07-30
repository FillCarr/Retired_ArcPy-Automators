import arcpy
arcpy.env.workspace = "C:\Geog 5620\PythonPro\Ex09"
fc = "dams.shp"
with arcpy.da.SearchCursor(fc, ["SHAPE@XY"]) as cursor:
 for row in cursor:
     x, y = row[0]
 print("{0:.3f}, {1:.3f}".format(x, y))
