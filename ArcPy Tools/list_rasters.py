import arcpy
arcpy.env.workspace = "C:\Geog 5620\PythonPro\Ex10\Ex10"
rasterlist = arcpy.ListRasters()
for raster in rasterlist:
    print(raster)
