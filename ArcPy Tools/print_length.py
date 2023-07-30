import arcpy
arcpy.env.workspace = "C:\Geog 5620\PythonPro\Ex09"
fc = "rivers.shp"
with arcpy.da.SearchCursor(fc, ["SHAPE@LENGTH"]) as cursor:
 length = 0
 for row in cursor:
    length = length + row[0]
    desc = arcpy.da.Describe(fc)
 units = desc["spatialReference"].linearUnitName
 print(f"{length:.2f} {units}")
