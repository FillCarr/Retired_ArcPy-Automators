import arcpy
arcpy.env.workspace = "C:\Geog 5620\PythonPro\Ex09"
fc = "rivers.shp"
with arcpy.da.SearchCursor(fc, (["OID@", "SHAPE@"])) as cursor:
    for row in cursor:
        print("Feature {0}: ".format(row[0]))
        for point in row[1].getPart(0):
            print("{0:.3f}, {1:.3f}".format(point.X, point.Y))
