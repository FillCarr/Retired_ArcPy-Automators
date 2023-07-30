import arcpy
arcpy.env.workspace = "C:\Geog 5620\PythonPro\Ex08"
fc = "airports.shp"
delimfield = arcpy.AddFieldDelimiters(fc, "STATE")
sql_exp = delimfield + " <> 'AK'"
with arcpy.da.UpdateCursor(fc, ["STATE"], sql_exp) as cursor: 
    for row in cursor:
        row[0] = "AK"
        cursor.updateRow(row) 
