

var map = L.mapbox.map('map', 'examples.map-vyofok3q').setView([44, -100], 2),
layer = L.geoJson(null, { style: { color: '#333', weight: 1 }});
map.addLayer(layer);

d3.json('topojson/dwr_basin_boundaries.json', function(error, data) {
  var basins = topojson.feature(data, data.objects.database);

var svg = d3.select(map.getPanes().overlayPane).append("svg"),
    g = svg.append("g").attr("class", "leaflet-zoom-hide");
              
  layer.addData(basins);
})

  
  
/*
  d3.json("topojson/dwr_basin_boundaries.json", function(error, shapes) {
          var basins = topojson.feature(shapes, shapes.objects.database);
        
          var projection = d3.geo.mercator()
              .scale(6000)
              .center([-122,38])
  
              .precision(.1);
          
          var path = d3.geo.path()
              .projection(projection);
  
          svg.selectAll(".subunit")
              .data(basins.features)
            .enter().append("path")
              .attr("class", function(d) { return "basin " + d.id + " " + d.properties.GWBASIN; })
              .attr("d", path);
  
  });
*/



