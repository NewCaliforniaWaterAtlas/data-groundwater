#!/usr/bin/python
import sys, os, simplejson, pymongo, datetime, time

# Create list of files.
file_list = []

# Connect to mongodb
conn = pymongo.Connection("localhost",27017)

# Set path to list of files.
path = "../../wells"

# Read each file in the directory.
for file in [doc for doc in os.listdir(path)

# Build list of file names in the directory.
if doc.endswith(".json")]:
    file_list.append(file)

def stringToFloat(val):
    if(val != "NULL"):
        if(val != ""):
            if(val != "Unknown"):
                val = val.replace(",","")
                return float(val)
    else:
        return val
    
# Read file list.
for i in file_list:

    print "Processing file: " + path + "/" + i

    # Connect to mongo database
    db = conn.watertable
    # Connect to collection
    c = db.wells
    # Open geoJSON file
    o = open(path + "/" + i)
    # Read into memory
    s = simplejson.load(o)
    o.close()  


    # Read the features part of the geoJSON document and insert into mongoDB.
    if s != None:
        if s['features'] != None:
            for x in s['features']:
                x['properties'] = x['attributes']
        
                x['geometry']['coordinates']= [ x['properties']['LONGITUDE'],x['properties']['LATITUDE'] ]
        
                date = x['properties']['SUBMIT_DATE']
                ts = datetime.datetime.strptime(date, '%m/%d/%Y')
                #isodate = datetime.datetime.fromtimestamp(ts, None)
                x['properties']['isodate'] = ts
            
                x['properties']['source'] = "DWR CASGEM"
                x['properties']['updated'] = datetime.datetime.today()
        
                # Convert string values to floats or integers.
                if(x['properties']['TOTAL_WELL_DEPTH'] != "NULL"):
                    x['properties']['TOTAL_WELL_DEPTH'] = stringToFloat(x['properties']['TOTAL_WELL_DEPTH'])
                if(x['properties']['CASGEM_WELL_ID'] != "NULL"):
                    x['properties']['CASGEM_WELL_ID'] = stringToFloat(x['properties']['CASGEM_WELL_ID'])
                if(x['properties']['ME_ID'] != "NULL"):
                    x['properties']['ME_ID'] = stringToFloat(x['properties']['ME_ID'])
        
                del x['attributes']
                del x['geometry']['x']
                del x['geometry']['y']
        
                c.insert(x)

print "Done."
sys.exit()


# Dump mongo database
# mongodump --collection database --db watertable --dbpath ~/htdocs/nwca_dropbox/Dropbox/data/data-water-table/mongodb

# db.database.ensureIndex({'geometry.coordinates': '2d'});
# db.database.ensureIndex({'properties.isodate': 1})
# db.database.ensureIndex({'properties.county': 1})