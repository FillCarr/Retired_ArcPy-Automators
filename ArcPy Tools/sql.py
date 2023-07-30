import arcpy
arcpy.env.workspace = "C:\Geog 5620\PythonPro\Ex08"
fc = "airports.shp"
delim_field = arcpy.AddFieldDelimiters(fc, "COUNTY")
sql_exp = delim_field + " = 'Anchorage Borough'"
cursor = arcpy.da.SearchCursor(fc, ["NAME"], sql_exp)
for row in cursor:
 print(row[0])
