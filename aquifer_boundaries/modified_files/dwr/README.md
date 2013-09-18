# DWR boundaries

## Change Log
* 9-18-2013 -- Created documentation and topojson from DWR aquifer boundaries.

## Accuracy
The boundaries themselves may not be exact.

## Methods
Data obtained from:
Data documented here:
Date data obtained

## Updating data:
1. Download new data
2. Unzip file
3. Resave .shp file as geoJSON
4. Export topojson
5. Update documentation

## Team
@CAWaterAtlas, @chachasikes, @videmsky

## Fields

OBJECTID_1,OBJECTID,DWR_,SUBBSN_,BAS_SBBSN,GWBASIN,SUBNAME,ACRES,BUDGET_TYP,Regional_O,Shape_Leng,Shape_Le_1,Shape_Area
1,1,9-19,,9-19,TIA JUANA,,   7448.09100000000,A,4,  30362.24447650000,      0.30571005104,      0.00287445514

OBJECTID_1  - Duplicate Primary key, increment (integer) [Why is this here?]
OBJECTID    - Primary key, increment (integer) 
DWR_        - DWR Groundwater basin ID number (Example: 9-19)
SUBBSN_     - Extra ID for subbasin - 8-2.09
BAS_SBBSN   - DWR Groundwater basin ID number (Example: 9-19) [Duplicate?]
GWBASIN     - Name of the groundwater basin (Example: SAN DIEGUITO CREEK)
SUBNAME     - Name of groundwater subbasin (Example: YUCAIPA)
ACRES       - Acres covered (Example:  180356.73999999999)
BUDGET_TYP  - How well the groundwater basin is understood (Values, A, B, C)
Regional_O  - ?  Values, 3, 4
Shape_Leng  - Circumference?
Shape_Le_1  - ?
Shape_Area  - ?

## TopoJSON
Conversion of DWR Groundwater basins to TopoJSON
https://github.com/mbostock/topojson
http://bost.ocks.org/mike/map/

1. Install TopoJSON (https://github.com/mbostock/topojson/wiki/Installation)
```
sudo npm install -g topojson
```
2. Test TopoJSON installed
```
which topojson
/opt/local/bin/topojson
```
3. Resave .shp file to geojson from DWR (using QGIS or ArcGIS)
* Can edit your file to reduce extra data as necessary.

4. Convert .shp file to topoJSON . https://github.com/mbostock/topojson/wiki/Command-Line-Reference
* Add -p to preserve properties.
* properties: OBJECTID_1,OBJECTID,DWR_,SUBBSN_,BAS_SBBSN,GWBASIN,SUBNAME,ACRES,BUDGET_TYP,Regional_O,Shape_Leng,Shape_Le_1,Shape_Area
* Make the DWR_ the id


OBJECTID,SUBBSN_,BAS_SBBSN,GWBASIN,SUBNAME,ACRES,BUDGET_TYP,Shape_Area

```
$ sudo topojson -o html/topojson/dwr_basin_boundaries.json BasinBoundaries/database.geojson -p OBJECTID,SUBBSN_,BAS_SBBSN,GWBASIN,SUBNAME,ACRES,BUDGET_TYP,Shape_Area --id-property BAS_SBBSN
Password:
bounds: -124.35855919099993 32.53402814800006 -114.22581840399994 42.00378792300006 (spherical)
quantization: 113m (0.00101°) 105m (0.000947°)
topology: 2641 arcs, 285588 points
prune: retained 2641 / 2641 arcs (100%)
```

5. From command line in html folder, run simply python webserver (or other webserver such as MAMP)
```
python -m SimpleHTTPServer 8008 &
```
```
sudo pip install SimpleHTTPServer
```

6. See html: Visit: http://localhost:8008/
* To kill the server, top, find pid of Python and kill [pid]
