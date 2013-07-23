# New California Water Atlas: Data - Groundwater
--------------------------------------------------------------------------------

THIS IS A WORK IN PROGRESS. 7/2/2013

##About this repository
Timeseries data downloads for well readings in California for the last 30 years. {{@TODO right?}}

This is a sample data set for development, will be replaced with full readings until we reach our maximum file space allotment on github, at which point we will move data to dropbox or equivalent.


How we are improving the data:
- Documenting the fields
- Exploring visualization opportunities


## Method of download:
1. Visit ____
2. Select each county and manually download records for each county with appropriate time thresholds to get all records since there is a limit of 1500 items per query. (There is no obvious way to scrape this data and we will find out how we can get a stream of continuous data.)

## Data citation
DWR {{??}}

--------------------------------------------------------------------------------
New California Water Atlas
Making Water Understandable in California
http://ca.statewater.org

Groundwater Workgroup on New California Water Atlas website
http://ca.statewater.org/groundwater  (currently: http://live-ca-statewater.gotpantheon.com/groundwater)

This repository location
https://github.com/NewCaliforniaWaterAtlas/data-aquifer-boundaries.git

--------------------------------------------------------------------------------

##### Team
Laci Videmsky @videmsky (Research)
Chach Sikes @chachasikes (Open Sourcing the process, Documentation)

##### Groups
If you are interested in helping to make groundwater data better in California, please contact the New California Water Atlas at info@statewater.org. 
* Blog and file sharing: http://ca.statewater.org/groundwater

#### Sponsors
New California Water Atlas: Making Water Understandable in California
http://ca.statewater.org  @CAStateWater

Work done as part of California Groundwater project, incubated by the Resource Renewal Institute http://rri.org with financial support from Patagonia. http://patagonia.com.


--------------------------------------------------------------------------------

#### What is this Groundwater data useful for?


#### Sample applications

--------------------------------------------------------------------------------
## Fields

Field Documentation can be found here: ??


Field Template:
### machine_readable_name | Human Readable Field Name
* Description: What the field is for
* Definition: Technical definition
* Format: string, machine-readable (alphanumeric, no spaces, etc), Integer, etc.
* Examples: Samples, along with the syntax format of the fields {{description}}_{{number}}  (ignore the braces {{}} )
* Notes: Notes about this field, used for complex fields
* Proposed changes: Ideas about ways to better represent the data in future versions.
* Values: some of the fields have specific kinds of values that have important meaning (ex. water right status) - we will note where there is a list of the values and their definitions.


### casgem_id | CASGEM ID
* Description: This is a location address that also gives latitude and longitude. Parse to get latitude and longitude.
* Definition: 
* Format: 
* Examples: 375259N1219869W001


### lat
* Description: Parsed latitude
* Definition: 
* Format: 
* Examples: 37.5259

### long
* Description: Parsed longitude
* Definition: 
* Format: 
* Examples: -121.9869 

### local_well_number | Local Well Number
* Description: 
* Definition: 
* Format: 
* Examples: 5S/1W-05H004

### Date
* Description: Date of the reading.
* Definition: 
* Format: 
* Examples: 1/4/2011

### Military Time (PST)
* Description: 
* Definition: 
* Format: 
* Examples: 00:00

### No Measurement
* Description: 
* Definition: 
* Format: 
* Examples: 
* Values

7 - Special/Other                 1197
9 - Temporarily inaccessible      1084
1 - Pumping                       945
4 - Can't get tape in casing      635
0 - Measurement Discontinued      395
2 - Pump house locked             333
6 - Well has been destroyed       303
3 - Tape hung up                  194
D - Dry well                      192
5 - Unable to locate well         159
8 - Casing leaking or wet         17
F - Flowing artesian well         10
(blank)                           31518


### Questionable Measurement
* Description: 
* Definition: 
* Format: 
* Examples: 
* Values

9 - Acoustical sounder                            1047
8 - Oil or foreign substance in casing            731
2 - Nearby pump operating                         484
6 - Other                                         309
4 - Pumped recently                               206
1 - Pumping                                       147
3 - Casing leaking or wet                         39
7 - Recharge or surface water effects near well   21
0 - Caved or deepened                             9
5 - Air or pressure gauge measurement             2
G - Nearby flowing                                2
F - Flowing                                       1
(blank)                                           33686


### Reading @RP
* Description: 
* Definition: Reading at Reference Point
* Format: Numerical value. Approximate range: -100.00 — 1,000.00
* Examples: 

### Reading @WS
* Description: 
* Definition: Reading at Water Surface
* Format: Numerical value. Approximate range: -400.00 — 1,000.00
* Examples: 

### RP to WS
* Description: 
* Definition: Reference point to water surface
* Format: Numerical value. Approximate range: -300.00 — 900.00
* Examples: 

### RP Elevation
* Description: 
* Definition: Reference point elevation
* Format: Numerical value. Approximate range: -200.00 — 1,000.00
* Examples: 

### GS Elevation
* Description: 
* Definition: Ground surface elevation
* Format: Numerical value. Approximate range: -200.00 — 1,000.00
* Examples: 

### WSE
* Description: 
* Definition: 
* Format: Numerical value. Approximate range: -300.00 — 1,000.00
* Examples: 

### GS to WS
* Description: 
* Definition: Ground surface to water surface
* Format: Format: Numerical value. Approximate range: -300.00 — 900.00
* Examples: 

### Measurement Method
* Description: 
* Definition: 
* Format: 
* Examples: 
* Values: 

UNK - Unknown                                               22943
ES - Electric sounder measurement                           8166
TR - Electronic pressure transducer                         4462
ST - Steel tape measurement                                 2127
AS - Acoustic or sonic sounder                              1050
OTH - Other                                                 334
PG - Airline measurement, pressure gage, or manometer       13
(blank)                                                     4701

### Measurement Accuracy
* Description: 
* Definition: 
* Format: 
* Examples: 
* Values

Unknown                                                     21699
0.1 Ft                                                      8750
0.01 Ft                                                     7615
1 Ft                                                        1031
(blank)                                                     4701

### Collecting/ Co-op Agency
* Description: 
* Definition: 
* Format: 
* Examples: 

Department of Water Resources                               15396
United States Geological Survey                             7362
Six Basins Watermaster                                      3954
CHOWCHILLA WATER DISTRICT                                   2853
Bureau of Reclamation                                       2707
Madera Irrigation District                                  2579
Los Angeles Department of Water and Power                   2124
Westlands Water District                                    1536
... and more

### Voluntary or CASGEM Measurement
* Description: 
* Definition: 
* Format: 
* Examples: 

Voluntary           32594
CASGEM              11965


### Comments
* Description: 
* Definition: 
* Format: 
* Examples: 

No access                       134
Kings River Basin               128
Tulare Lake Basin               115
GATE LOCKED                     76
NOT AVAILABLE                   72
CASING PLUGGED                  71
ROAD CLOSED/TOO MUDDY           45

### ÔªøCASGEM ID
* Description: 
* Definition: 
* Format: 
* Examples: 

