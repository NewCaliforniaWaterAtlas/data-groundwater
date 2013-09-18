

var map = L.mapbox.map('map', 'examples.map-vyofok3q').setView([44, -100], 2);

var layer = L.geoJson(null, { style: { color: '#333', weight: 1 }});

map.addLayer(layer);

d3.json('topojson/dwr_basin_boundaries.json', function(error, data) {
  var basins = topojson.feature(data, data.objects.database);          
  layer.addData(basins);
})
