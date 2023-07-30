import arcpy
arcpy.env.workspace = "C:\Geog 5620\PythonPro\Ex07\PythonScripting_Ex07_Data"
fclist = arcpy.ListFeatureClasses()
for fc in fclist:
    desc = arcpy.da.Describe(fc)
    print(f'{desc["baseName"]}: {desc["shapeType"]}')
   
