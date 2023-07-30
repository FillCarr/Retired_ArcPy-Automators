import arcpy
aprx = arcpy.mp.ArcGISProject("Austin.aprx")
aprx.saveACopy("Austin_Copy.aprx")
del aprx
