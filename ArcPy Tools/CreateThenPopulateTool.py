import arcpy

# Set workspace and environment settings
arcpy.env.workspace = r"C:\Geog 5620\FinalProj\FinalProj\FinalProj.gdb"
arcpy.env.overwriteOutput = True

# Create a new point feature class
fc_name = "FinalPoints"
fc_path = arcpy.management.CreateFeatureclass(arcpy.env.workspace, fc_name, "POINT", spatial_reference=4326)

# Add fields to the feature class
field_names = ["Name", "Value"]
for field_name in field_names:
    arcpy.management.AddField(fc_path, field_name, "TEXT")

# Define a list of features to insert
features = [("Point 1", "10"), ("Point 2", "20"), ("Point 3", "30")]

# Insert features into the feature class using a cursor
with arcpy.da.InsertCursor(fc_path, ["SHAPE@", "Name", "Value"]) as cursor:
    for feature in features:
        try:
            # Convert the value field to an integer before inserting it
            value = int(feature[1])
            # Create a point geometry object
            point = arcpy.Point(value, value)
            # Create a feature object and set its geometry and attributes
            new_feature = [point, feature[0], feature[1]]
            # Insert the new feature into the feature class
            cursor.insertRow(new_feature)
            print(f"Added feature {feature[0]} with value {value}.")
        except Exception as e:
            print(f"Error adding feature {feature[0]}: {e}")
            # Roll back the transaction if an error occurs
            cursor.rollback()

print("Features added successfully.")
