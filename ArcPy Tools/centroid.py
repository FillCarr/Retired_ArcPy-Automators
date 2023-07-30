import arcpy 
arcpy.env.workspace = "C:/Geog 5620/PythonPro/Ex05" 
in_fc = "parks.shp" 
out_fc = "parks_centroid.shp" 
if arcpy.ProductInfo() == "ArcInfo": 
 arcpy.FeatureToPoint_management(in_fc, out_fc) 
else: 
 print("An ArcInfo license is not available.")
 
