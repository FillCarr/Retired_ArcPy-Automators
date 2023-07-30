import arcpy
aprx = arcpy.mp.ArcGISProject("Austin.aprx")
m = aprx.listMaps("Downtown")[0]
m.addBasemap("Light Gray Canvas")
aprx.saveACopy("Austin_Canvas.aprx")
del aprx
