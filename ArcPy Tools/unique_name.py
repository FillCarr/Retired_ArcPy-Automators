import arcpy
arcpy.env.workspace = "C:\Geog 5620\PythonPro\Ex08"
fc = "airports.shp"
unique_name = arcpy.CreateUniqueName("buffer.shp")
arcpy.Buffer_analysis(fc, unique_name, "5000 METERS")
