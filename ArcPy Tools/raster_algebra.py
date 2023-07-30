import arcpy
from arcpy.sa import *
arcpy.env.workspace = "C:\Geog 5620\PythonPro\Ex10\Ex10"
elevraster = arcpy.Raster("elevation")
slope = Slope(elevraster)
goodslope = slope < 20
goodelev = elevraster < 2500
goodfinal = goodslope & goodelev
goodfinal.save("final")
