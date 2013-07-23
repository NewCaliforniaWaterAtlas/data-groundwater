Downloading SRTM data for elevation.

SRTM 90m DEM version 4

@TODO add note about the resolution.

Data download date: July 23, 2013

1. http://srtm.csi.cgiar.org -- Click on Download data (left hand side.)
2. http://srtm.csi.cgiar.org/SELECTION/inputCoord.asp
3. Click on squares that encompass California (4 tiles.)
4. Download zip files of GeoTiffs. (See screenshots for settings we used, which were the defaults.)
5. Make sure you download the right tiles. The interface is a little weird.
6. Open in QGIS or ArcGIS to view. New Project. Add Raster Layer. Load the .tif file. Tiles will place themselves properly.


Files for California
srtm_12_04
srtm_12_05
srtm_12_06
srtm_13_04
srtm_13_05
srtm_13_06


To create contour file of CA.
In QGIS, with raster tiles loaded.
Raster > Analysis > Contours
- Create a folder ahead of time for each shapefile project (.shp) (based on file name & save the elevation increment setting)
- Select new file location for shapefile you will create of vectors of contours for a very large land mass (will be about 2GB vector file.)
- Resolution: 100 (meters)
- Check 'Attribute' ELEV



Tutorials:
* http://www.gistutor.com/quantum-gis/19-beginner-quantum-gis-tutorials/56-how-to-generate-contours-using-raster-data-in-quantum-gis-qgis.html
* http://www.gistutor.com/quantum-gis/19/55-how-to-generate-contours-using-point-data-in-quantum-gis-qgis.html
* http://www.mapbox.com/blog/contour-lines-density-mapping/



Data license: for non-commercial uses (@TODO check.)
Attribution: @TODO look up.

Shuttle Radar Topology Mission
NASA: http://www2.jpl.nasa.gov/srtm/
Wikipedia: http://en.wikipedia.org/wiki/Shuttle_Radar_Topography_Mission