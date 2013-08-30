#!/usr/bin/python
import sys, os, simplejson, pymongo

# Create list of files.
file_list = []

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

    db = conn.watertable
    c = db.database
    o = open(path + "/" + i)
#    contents = o.read()
    s = simplejson.load(o)
    o.close()
    #clean = contents.replace('\n', '')

  

    print "Loading" + " into MongoDB"
    for x in s['features']:
        c.insert(x)

print "Done."

sys.exit()
