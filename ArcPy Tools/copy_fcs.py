import arcpy
import os
arcpy.env.workspace = "C:\Geog 5620\PythonPro\Ex07\PythonScripting_Ex07_Data\Ex07"
arcpy.env.overwriteOutput = True
fgdb = "Demo.gdb"
try:
 fclist = arcpy.ListFeatureClasses()
 for fc in fclist:
     desc = arcpy.da.Describe(fc)
 outfc = os.path.join(fgdb, desc["baseName"])
 arcpy.CopyFeatures_management(fc, outfc)
except arcpy.ExecuteError: 
 print(arcpy.GetMessages(2)) 
except: 
 print("There has been a nontool error.") 
