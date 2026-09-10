# -*- coding: utf-8 -*-
"""
Course Title: Geocomputation and Spatial Science
Lab 2 - Exercise 3: Automating Spatial Workflows with Standalone Python

Author: Mekonnen Gidey
Date: June, 2026
Purpose: This script automatically reads all feature classes in a source 
         geodatabase and copies them into a new target feature dataset. 
         Datasets not natively matching the target projected coordinate 
         system (WKID 2248) are automatically projected on-the-fly.
"""

import arcpy
import os

# --- PATH AND VARIABLE CONFIGURATIONS ---
# Updated path pointing to your active workspace directory
mypath = r"D:\Geostatstics\Lab2\PythonWorkflow"
gdb = "Transportation.gdb"
new_gdb = "Metro_Transport.gdb"
fds = "Metro_Network"
target_wkid = 2248  # NAD 1983 StatePlane Maryland FIPS 1900 (US Feet)

# Set the active geoprocessing workspace
arcpy.env.workspace = os.path.join(mypath, gdb)

# Enable environment control to overwrite historical outputs during testing
arcpy.env.overwriteOutput = True

try:
    print("Starting automated spatial workflow pipeline...")

    # 1. Automated File Geodatabase Schema Creation
    print(f"Creating new file geodatabase: {new_gdb}...")
    new_gdb_path = arcpy.CreateFileGDB_management(mypath, new_gdb)
    print(f"Success: The geodatabase {new_gdb} has been created.")

    # 2. Automated Target Feature Dataset Creation with Specified Spatial Reference
    print(f"Creating feature dataset '{fds}' with projected WKID {target_wkid}...")
    arcpy.CreateFeatureDataset_management(new_gdb_path, fds, target_wkid)
    print(f"Success: The feature dataset {fds} has been created.")

    # 3. List and Evaluate Source Feature Classes
    print("Reading and indexing source feature classes...")
    fcs = arcpy.ListFeatureClasses()

    # 4. Conditional Data Processing Loop
    for fc in fcs:
        # Retrieve properties and spatial reference details for the feature class
        desc = arcpy.da.Describe(fc)
        sr = desc["spatialReference"]
        
        # Build the absolute target file destination path
        new_fc = os.path.join(mypath, new_gdb, fds, fc)
        
        # Check if the feature class matches the target coordinate system natively
        if sr.factoryCode == target_wkid:
            # Condition True: Copy feature class directly
            arcpy.CopyFeatures_management(fc, new_fc)
            print(f" -> [COPY] Feature class '{fc}' natively matches WKID {target_wkid}. Copied successfully.")
        else:
            # Condition False: Project feature class to target coordinate system
            arcpy.Project_management(fc, new_fc, target_wkid)
            print(f" -> [PROJECT] Feature class '{fc}' is in '{sr.name}'. Projected to WKID {target_wkid} successfully.")

    print("\nWorkflow completed successfully! All layers are standardly unified in the target dataset.")

except Exception as e:
    print(f"\nAn error occurred during execution: {e}")