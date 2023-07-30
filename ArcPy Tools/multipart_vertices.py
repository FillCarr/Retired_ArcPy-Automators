import arcpy
arcpy.env.workspace = "C:\Geog 5620\PythonPro\Ex09"
fc = "hawaii.shp"
cursor = arcpy.da.SearchCursor(fc, ["OID@", "SHAPE@"])
for row in cursor:
    print("Feature {0}: ".format(row[0]))
    partnum = 0
    for part in row[1]:
        print("Part {0}: ".format(partnum))
        for point in part:
            print("{0:.2f}, {1:.2f}".format(point.X, point.Y))
            partnum += 1
