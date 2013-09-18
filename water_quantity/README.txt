# Methods to obtain Groundwater elevation data

## Getting Timeseries data for groundwater elevation
* CASGEM: http://www.casgem.water.ca.gov
* Login, create account
* Reports > Select time range, Filter by county, All counties > Get results > Export to CSV

* Results are limited to 1000, so large ranges need to be broken up.
* We originally got data for counties, with counties with lots of data broken up by date range.
* Going forward, we can export several months at a time and add it to the folder of timeseries data.
  * Date range
  * First import: June 21, 1983 - June 21 2013
  * Second import: June 22, 2013 - September 17, 2013 (98 new records)
  * About one new record per day.
  
* To the best or our knowledge, this process cannot be automated because the .Net system used (Telerik?) uses sessions to store your query, and there is no way to get at the parameters to automatically do this.
* A form-based web-robot might be able to do this every few months. Otherwise a human can do it.


## Getting metadata about wells
* ArcGIS endpoint
* Run python script ./modified_files/dwr_casgem/scripts/python/wells_casgem_arcgis
* This downloads JSON data from ArcGIS endpoint.
* Check that results are not maxing out at 1000 - if they are, the script my need to be adjusted to get smaller units. Certain counties have a lot of well readings (Ex. Fresno), so the results are limited to voluntary collected data, by collecting agencies. To obtain a list of all collecting agencies, use the timeseries data to get a distinct list of counties. We did this with mongodb.
* Shorted facets that contain ampersand to just the first word. ArcGIS does a LIKE search for the district, so right now it doesn't matter. Changing '&' to a properly escaped character might also work, but need to see what ArcGIS accepts.
* Rebuild mongo collection of wells: ./modified_files/dwr_casgem/scripts/python/wells_json_to_mongo.py

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
