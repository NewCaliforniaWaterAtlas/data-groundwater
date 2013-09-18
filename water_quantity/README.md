# Water Quantity Data

@TODO Change name of this folder? Move to own repository?

Team: New California Water Atlas @CAWaterAtlas, @chachasikes, @videmsky

--------------------------------------------------------------------------------
## Change Log

* September 17, 2013: Second import: June 22, 2013 - September 17, 2013 (98 new records)
* August 2, 2013: Import new data: June 21, 1983 - June 21 2013

--------------------------------------------------------------------------------
# Methods


## Timeseries
Getting Timeseries data for groundwater elevation


1. CASGEM: http://www.casgem.water.ca.gov
2. Login, create account
3. Go to Reports
4. Select time range
5. Filter by county: All counties
6. Get results > Export to CSV
7. Download.

### Timeseries Updates
Going forward, we can export several months at a time and add it to the folder of timeseries data.
* About one new record added to the system per day.

To update the data:


1. Select date range of the day after the last import to the current day.
2. Get results.
3. Download to CSV. Save to original_files/dwr_casgem/updates
4. Naming convention: All_Counties_M.D.YYYY-M.D.YYYY.csv  (for the date range)
5. Update git log.
6. @TODO Need a new import script to account for updates & missing county information.

### Loading Timeseries data into Mongo

1. Download files to the correct folder. 
  * "/timeseries" for data for counties saved with proper naming convention
  * "/updates" for data from all counties
2. To create mongo database from timeseries data, run 
```
./water_quantity/modified_files/dwr_casgem/scripts/python/./timeseries_csv.py
```
3. This will create a new CSV file of ALL of the timeseries data to ../database/casgem_timeseries.csv
4. You will need the csvjson converter: http://csvkit.readthedocs.org/en/latest/scripts/csvjson.html
5. In terminal, convert this file to geoJSON:
```
csvjson --lat latitude --lon longitude --k well --crs EPSG:4269 -i 4 ../../database/casgem_timeseries.csv > ../../database/casgem_timeseries.json
```
6. Drop the existing collection. Run mongod, run mongo. use watertable; db.database.drop();
7. Import geoJSON formatted data to Mongo
```
./water_quantity/modified_files/dwr_casgem/timeseries_js_to_mongo.py
```

8. Create a dump of the mongo database
```
mongodump --collection database --db watertable --dbpath ~/htdocs/nwca_dropbox/Dropbox/data/data-water-table/mongodb
```
9. Create indexes
```
db.database.ensureIndex({'geometry.coordinates': '2d'});
db.database.ensureIndex({'properties.isodate': 1})
db.database.ensureIndex({'properties.county': 1})
```
10. Copy mongodump to Dropbox
/Dropbox/data/data-water-table/mongodb/dump
Dropbox link: https://www.dropbox.com/sh/2drursxcmr01nkd/4tnSUMxIi0
11. Push to openshift server.
Need keys and credentials in order to do this, exmaple is for syntax purposes
12. Copy mongodump to server using secure copy:
scp -r watertable 521fe2dbe0xxxxxxxxxx@watertable-watertransfer.rhcloud.com:/var/lib/openshift/521fe2dbe0b8cdd7fb0001f2/app-root/data/dumps 
13. ssh into server: ssh 521fe2dbe0xxxxxxxxxx@watertable-watertransfer.rhcloud.com
14. 
```mongorestore -d watertable app-root/data/dumps/watertable 
```
or this @TODO test
```
mongorestore -h521fe390exxxxx-watertransfer.rhcloud.com:51xxx -uadmin -p xxxxxxxxxxxx -d watertable app-root/data/dumps/watertable
```
15. Tip: get openshift environment variables, get your ssh stuff by logging into openshift
```
ssh 521fe2dbe0xxxxxxxxxx@watertable-watertransfer.rhcloud.com
env |grep OPENSHIFT_MONGODB
```

@TODO test this
./water_quantity/modified_files/dwr_casgem/timeseries_js_to_mongo.py -- this script seems to deal with individual json files -- which might actually be the better way to do this because something in the process might hang… I forget though -- chach




### Notes
* Results are limited to 1000, so large ranges need to be broken up.
* We originally got data for counties, with counties with lots of data broken up by date range.
* To the best or our knowledge, this process cannot be automated because the .Net system used (Telerik?) uses sessions to store your query, and there is no way to get at the parameters to automatically do this.
* A form-based web-robot might be able to do this every few months. Otherwise a human can do it.


## Wells
Getting metadata about wells
* ArcGIS endpoint
* Run python script ./modified_files/dwr_casgem/scripts/python/wells_casgem_arcgis
* This downloads JSON data from ArcGIS endpoint.
* Check that results are not maxing out at 1000 - if they are, the script my need to be adjusted to get smaller units. Certain counties have a lot of well readings (Ex. Fresno), so the results are limited to voluntary collected data, by collecting agencies. To obtain a list of all collecting agencies, use the timeseries data to get a distinct list of counties. We did this with mongodb.
* Shorted facets that contain ampersand to just the first word. ArcGIS does a LIKE search for the district, so right now it doesn't matter. Changing '&' to a properly escaped character might also work, but need to see what ArcGIS accepts.
* Rebuild mongo collection of wells: ./modified_files/dwr_casgem/scripts/python/wells_json_to_mongo.py

```
> db.database.distinct('properties.collecting', {'properties.county':'Fresno'});
[
        "Department of Water Resources",
        "Bureau of Reclamation",
        "Westlands Water District",
        "RIVERDALE IRRIGATION DISTRICT",
        "Consolidated Irrigation District",
        "JAMES IRRIGATION DISTRICT",
        "Alta Irrigation District",
        "TRANQUILLITY RESOURCE CONSERVATION DISTRICT",
        "Orange Cove Irrigation District",
        "Fresno Irrigation District",
        "City of Fresno",
        "GARFIELD WATER DISTRICT",
        "RIVERDALE PUBLIC UTILITY DISTRICT",
        "LIBERTY WATER DISTRICT",
        "KINGS COUNTY WATER DISTRICT",
        "United States Geological Survey",
        "Panoche Water District",
        "Kings River Conservation District",
        "San Luis & Delta-Mendota Water Authority",
        "County of Fresno"
]
```
