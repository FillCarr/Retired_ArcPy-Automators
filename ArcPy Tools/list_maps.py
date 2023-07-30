import arcpy
aprx = arcpy.mp.ArcGISProject("Austin.aprx")
m = aprx.listMaps("Region")[0]
m.name = "County"
aprx.saveACopy("Austin_County.aprx")
del aprx
