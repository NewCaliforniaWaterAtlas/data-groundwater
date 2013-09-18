--------------------------------------------------------------------------------
# Water Quantity Data
--------------------------------------------------------------------------------

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

1.CASGEM: http://www.casgem.water.ca.gov
2.Login, create account
3.Go to Reports
4.Select time range
5.Filter by county: All counties
6.Get results > Export to CSV
7.Download.

### Timeseries Updates
Going forward, we can export several months at a time and add it to the folder of timeseries data.
* About one new record added to the system per day.

To update the data:

1.Select date range of the day after the last import to the current day.
2.Get results.
3.Download to CSV. Save to original_files/dwr_casgem/updates
4.Naming convention: All_Counties_M.D.YYYY-M.D.YYYY.csv  (for the date range)
5.Update git log.
6.@TODO Need a new import script to account for updates & missing county information.



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
