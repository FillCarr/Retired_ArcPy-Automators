import arcpy
arcpy.env.workspace = "c:/Geog 5620/PythonPro/Ex03/Study.gdb"
arcpy.Clip_analysis("lakes","Basin","lakes_myClip")
