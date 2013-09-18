#!/usr/bin/python
import sys, os, json, urllib2, urllib, requests

# For each collecting agency, download voluntary wells and save as JSON file.

small_counties = [
"Alameda",
"Alpine",
"Amador",
"Butte",
"Calaveras",
"Colusa",
"Contra Costa",
"Del Norte",
"El Dorado",
"Glenn",
"Humboldt"
"Imperial",
"Inyo",
"Lake",
"Lassen",
"Madera",
"Marin",
"Mariposa",
"Mendocino",
"Modoc",
"Monterey",
"Napa",
"Nevada",
"Orange",
"Placer",
"Plumas",
"Sacramento",
"San Benito",
"San Francisco",
"San Luis Obispo",
"San Mateo",
"Santa Barbara",
"Santa Clara",
"Santa Cruz",
"Shasta",
"Sierra",
"Siskiyou",
"Solano",
"Sonoma",
"Sutter",
"Tehama",
"Trinity",
"Tuolemne",
"Ventura", 
"Yolo",
"Yuba"
]



# Create list of files.
counties = [["Fresno",[
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
]],

["Kern",
[
        "Department of Water Resources",
        "United States Geological Survey",
        "Wheeler Ridge-Maricopa Water Storage District",
        "Bureau of Reclamation",
        "Arvin-Edison Water Storage District",
        "Kern County Water Agency",
        "Buena Vista Water Storage District",
        "CALIFORNIA WATER SERVICE COMPANY",
        "Cawelo Water District",
        "North Kern Water Storage District",
        "Shafter-Wasco Irrigation District",
        "SAN JOAQUIN, SOUTHERN, MUNICIPAL UTILITY DISTRICT",
        "Delano Earlimart ID",
        "Semitropic Water Storage District",
        "KINGS COUNTY WATER DISTRICT",
        "VENTURA COUNTY FLOOD CONTROL DISTRICT",
        "TENNECO-WEST",
        "TULE RIVER ASSOCIATION",
        "TERRA BELLA IRRIGATION DISTRICT",
        "JAMES IRRIGATION DISTRICT",
        "Kern River Fan Group",
        "Kern Water Bank Authority",
        "Kern County Water Agency Improvement District No. 4",
        "Indian Wells Valley Cooperative Groundwater Management Group",
        "Kern-Tulare Wate District",
        "Deer Creek & Tule River Authority"
]],

["Kings",

[
        "Department of Water Resources",
        "Westlands Water District",
        "Bureau of Reclamation",
        "Kaweah Delta Water Conservation District",
        "Tulare Irrigation District",
        "KINGS COUNTY WATER DISTRICT",
        "LAKESIDE IRRIGATION WATER DISTRICT",
        "Alta Irrigation District",
        "Kings River Conservation District",
        "Consolidated Irrigation District",
        "Fresno Irrigation District"
]],


["Los Angeles",

[
        "United States Geological Survey",
        "Puente Basin Watermaster",
        "Water Replenishment District of Southern California",
        "Main San Gabriel Basin Watermaster",
        "Chino Basin Watermaster",
        "Six Basins Watermaster",
        "Raymond Basin Management Board"
]],

["Merced",

[
        "Department of Water Resources",
        "Bureau of Reclamation",
        "SAN LUIS CANAL COMPANY",
        "Merced Irrigation District",
        "EL NIDO IRRIGATION DISTRICT",
        "CHOWCHILLA WATER DISTRICT",
        "TURLOCK IRRIGATION DISTRICT",
        "San Luis & Delta-Mendota Water Authority",
        "Merced Area Groundwater Pool Interests (MAGPI)",
        "Madera-Chowchilla Basin Regional Groundwater Monitoring Group",
        "City of Merced"
]],

["Riverside",
[
        "Coachella Valley Water District",
        "United States Geological Survey",
        "Rancho California Water District",
        "Elsinore Valley Municipal Water District",
        "Eastern Municipal Water District",
        "Western Municipal Water District",
        "San Gorgonio Pass Water Agency",
        "Chino Basin Watermaster",
        "Mission Springs Water District"
]],

["San Diego",

[
        "United States Geological Survey",
        "City of San Diego - Public Utilities Department",
        "Borrego Water District",
        "Vista Irrigation District"
]],


["San Joaquin",
[
        "Bureau of Reclamation",
        "San Joaquin County Flood Control and Water Conservation District",
        "Department of Water Resources",
        "Oakdale Irrigation District",
        "East Bay Municipal Utility District"
]],

["Stanislaus",
[
        "Department of Water Resources",
        "San Luis & Delta-Mendota Water Authority",
        "Bureau of Reclamation",
        "TURLOCK IRRIGATION DISTRICT",
        "City of Modesto",
        "Stanislaus & Tuolumne Rivers Groundwate Basin Association",
        "Modesto Irrigation District",
        "Oakdale Irrigation District"
]],

["Tulare",
[
        "Department of Water Resources",
        "Delano Earlimart ID",
        "Bureau of Reclamation",
        "TENNECO-WEST",
        "Pixley Irrigation District ",
        "SAN JOAQUIN, SOUTHERN, MUNICIPAL UTILITY DISTRICT",
        "SAUCELITO IRRIGATION DISTRICT",
        "TERRA BELLA IRRIGATION DISTRICT",
        "JAMES IRRIGATION DISTRICT",
        "TULE RIVER, LOWER, IRRIGATION DISTRICT",
        "TULE RIVER ASSOCIATION",
        "Porterville Irrigation District",
        "Tulare Irrigation District",
        "Kaweah Delta Water Conservation District",
        "LINDMORE IRRIGATION DISTRICT",
        "EXETER IRRIGATION DISTRICT",
        "Lindsey-Strathmore Irrigation District",
        "KINGS COUNTY WATER DISTRICT",
        "City of Fresno",
        "LAKESIDE IRRIGATION WATER DISTRICT",
        "EL NIDO IRRIGATION DISTRICT",
        "LEWIS CREEK WATER DISTRICT",
        "Fresno Irrigation District",
        "IVANHOE IRRIGATION DISTRICT",
        "Alta Irrigation District",
        "Buena Vista Water Storage District",
        "Stone Corral Irrigation District",
        "Consolidated Irrigation District",
        "Orange Cove Irrigation District",
        "Kern-Tulare Wate District",
        "Deer Creek & Tule River Authority",
        "Kings River Conservation District",
        "Cawelo Water District"
]]
]

'''
for i in small_counties:
    countyName = i
    
    fileName = "../../wells/" + countyName + ".json" 
    path = "http://casgemgis.water.ca.gov/ArcGIS/rest/services/CASGEM_DWR_BASE_LAYERS/MapServer/0/query?text=&geometry=&geometryType=esriGeometryEnvelope&inSR=&spatialRel=esriSpatialRelIntersects&where=UPPER%28COUNTY%29+%3D+%27" + countyName.upper() + "%27&returnGeometry=true&outSR=102100&outFields=*&f=pjson"   
    print path
    r = requests.get(path)
    content = r.content
    
    with open(fileName, "wb") as f:
        f.write(content)

'''
for i in counties:
  countyName = i[0]
  # @TODO add filename and source
  fileName_casgem = "../../wells/" + countyName + "_CASGEM.json" 
  path_casgem = "http://casgemgis.water.ca.gov/ArcGIS/rest/services/CASGEM_DWR_BASE_LAYERS/MapServer/0/query?text=&geometry=&geometryType=esriGeometryEnvelope&inSR=&spatialRel=esriSpatialRelIntersects&where=UPPER%28COUNTY%29+%3D+%27" + countyName.upper() + "%27+AND+UPPER%28IS_VOLUNTARY%29+%3D+%27N%27&returnGeometry=true&outSR=102100&outFields=*&f=pjson"  

  print path_casgem
  r_casgem = requests.get(path_casgem)
  content_casgem = r_casgem.content

  with open(fileName_casgem, "wb") as f:
            f.write(content_casgem)
'''
  for j in i[1]:
        agencyName = j
        fileName = "../../wells/" + countyName + "_Voluntary_" + agencyName + ".json" 
        path = "http://casgemgis.water.ca.gov/ArcGIS/rest/services/CASGEM_DWR_BASE_LAYERS/MapServer/0/query?text=&geometry=&geometryType=esriGeometryEnvelope&inSR=&spatialRel=esriSpatialRelIntersects&where=UPPER%28COUNTY%29+%3D+%27" + countyName.upper() + "%27+AND+UPPER%28ME_NAME%29+LIKE+%27%25" + agencyName.upper() + "%25%27+AND+UPPER%28IS_VOLUNTARY%29+%3D+%27Y%27&returnGeometry=true&outSR=102100&outFields=*&f=pjson"    

    
        path_casgem = "http://casgemgis.water.ca.gov/ArcGIS/rest/services/CASGEM_DWR_BASE_LAYERS/MapServer/0/query?text=&geometry=&geometryType=esriGeometryEnvelope&inSR=&spatialRel=esriSpatialRelIntersects&where=UPPER%28COUNTY%29+%3D+%27" + countyName.upper() + "%27+AND+UPPER%28IS_VOLUNTARY%29+%3D+%27N%27&returnGeometry=true&outSR=102100&outFields=*&f=pjson"  
    
        print path
        r = requests.get(path)
        content = r.content

        with open(fileName, "wb") as f:
            f.write(content)




        print countyName + " " + agencyName
        #print path
'''
  
print "Done."

sys.exit()
