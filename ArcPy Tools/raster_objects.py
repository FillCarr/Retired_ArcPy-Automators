import arcpy
arcpy.env.workspace = "C:\Geog 5620\PythonPro\Ex10\Ex10"
outraster = arcpy.sa.Slope("elevation")
outraster.save("slope")
