import arcpy
from arcpy.sa import *
arcpy.env.workspace = "C:\Geog 5620\PythonPro\Ex10"
myremap = RemapRange([[1000,2000,1], [2000,3000,2],
[3000,4000,3]])
myremap = RemapValue([[41,1], [42,2], [43,3]])
outreclass = Reclassify("landcover.tif", "VALUE", myremap,"NODATA")
outreclass.save("lc_recl")
