import arcpy
aprx = arcpy.mp.ArcGISProject("Austin.aprx")
m = aprx.listMaps("Downtown")[0]
lyr = m.listLayers("parks")[0]
sym = lyr.symbology
red = {"RGB": [100, 175, 0, 100]}
if lyr.isFeatureLayer and hasattr(sym, "renderer"):
 sym.renderer.symbol.color = red
 lyr.symbology = sym
aprx.saveACopy("Austin_Symbology.aprx")
del aprx
