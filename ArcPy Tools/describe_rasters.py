import arcpy
arcpy.env.workspace = "C:\Geog 5620\PythonPro\Ex10\Ex10"
raster = "tm.img"
desc = arcpy.da.Describe(raster)
for rband in desc["children"]:
         bandname = rband["baseName"]
         x = rband["meanCellHeight"]
         y = rband["meanCellWidth"]
         spatialref = desc["spatialReference"]
         units = spatialref.angularUnitName
         print("The resolution of {0} is {1:.7f} by {2:.7f}{3}."
               .format(bandname, x, y, units))
