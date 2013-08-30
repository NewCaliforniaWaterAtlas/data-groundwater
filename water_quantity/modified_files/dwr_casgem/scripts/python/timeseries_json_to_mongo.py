#!/usr/bin/python
import sys, os, simplejson, pymongo

# Create list of files.
file_list = []

# Connect to mongodb
conn = pymongo.Connection("localhost",27017)

# Set path to list of files.
path = "../../database/geojson"

# Read each file in the directory.
for file in [doc for doc in os.listdir(path)

# Build list of file names in the directory.
if doc.endswith(".json")]:
    file_list.append(file)
    
# Read file list.
for i in file_list:

    print "Processing file: " + path + i

    # Connect to mongo database
    db = conn.watertable
    # Connect to collection
    c = db.database
    # Open geoJSON file
    o = open(path + "/" + i)
    # Read into memory
    s = simplejson.load(o)
    o.close()  

    # Read the features part of the geoJSON document and insert into mongoDB.
    for x in s['features']:
        c.insert(x)

print "Done."
sys.exit()
