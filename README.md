# New California Water Atlas: Data - Ground Water Aquifer Boundaries & Elevation
--------------------------------------------------------------------------------

##About this repository

Improved aquifer boundary data for California.
Improved groundwater elevation data for California.
- Using USGS data obtained from the National Atlas.
- Using CA Department of Water Resources data.

How we are improving the data:
- Add tilemill styles
- Explore design conventions for illustrating aquifers in the best way.
- Documenting and publicizing how to get the primary sources of data & our transformations
- Explaining what the data is
- Pruning disconnected data from CA (but showing people in other states how to do similar things)
- Documenting the naming conventions of the aquifer to make it easier to link aquifers to other datasets.
- Blogging about different aquifer boundary files. Ex. ESRI?
- Differences are probably: resolution, id's naming, accuracy and methods
- Look into GRACE Ground Water Storage data from NASA and compare to other groundwater sources. http://drought.unl.edu/MonitoringTools/NASAGRACEDataAssimilation.aspx

--------------------------------------------------------------------------------
New California Water Atlas
Making Water Understandable in California
http://ca.statewater.org

Groundwater Workgroup on New California Water Atlas website
http://ca.statewater.org/groundwater  (currently: http://live-ca-statewater.gotpantheon.com/groundwater)

This repository location
https://github.com/NewCaliforniaWaterAtlas/data-aquifer-boundaries.git

*Creators*
Laci Videmsky @videmsky (Research)
Chach Sikes @chachasikes (Open Sourcing the process, Documentation)

Work done as part of Summer of Groundwater project, incubated by the Resource Renewal Insititute http://rri.org with financial support from Patagonia. http://patagonia.com.

If you are interested in helping to make aquifer data better in California, please contact the New California Water Atlas at info@statewater.org.
--------------------------------------------------------------------------------
## How to obtain the original files

### USGS Aquifer Boundaries from 2003

Steps:
- Download from National Atlas homepage http://nationalatlas.gov

## How to find the file 
- Go to Map Layers http://nationalatlas.gov/maplayers.html
- Click on Water
- Select Aquifers
- Click on “View Map Layer Description”
- “This is aquifers that supply groundwater to the lower 48 states.”
- USGS
- Federally funded clearing house
- Click on Data Download
- Map Layers is Aquifers
- Release October 2003
- Download the Shapefile: aquifrp025.tar.gz ~ 10MB

Features
* Contains rock type for basis
* Contains aquitard shapes. (Aquitard = non-water bearing material, not really a word)

@TODO Document ID's

## References
GROUND WATER ATLAS of the UNITED STATES
California, Nevada

* Documents different rock types used in USGS Aquifer boundaries shape file
http://pubs.usgs.gov/ha/ha730/ch_b/index.html



### Department of Water Resources

* Higher resolution than USGS
* Includes subbasins
* Does not include a shapefile for everything else

"Out of 431 delineated groundwater basins, 24 basins are subdivided to create an additional 108 subbasins. These 515 distinct groundwater systems underlie about 40 percent of the surface area of the State.

Many of the subbasin boundaries were developed or modified with public input, but little physical data. Because they should not be considered precise boundaries, a detailed local study should determine whether any specific area lies within a groundwater basin boundary."

To obtain a shapefile of Groundwater Basin data for California: DWR-B118_BasinBoundaries_v41.zip
- Visit: http://www.water.ca.gov/groundwater/bulletin118/gwbasin_maps_descriptions.cfm
- Download shape file (ZIP: 3.78 MB)  http://www.water.ca.gov/groundwater/bulletin118/maps/B118_BasinBoundaries_v4_1.zip



