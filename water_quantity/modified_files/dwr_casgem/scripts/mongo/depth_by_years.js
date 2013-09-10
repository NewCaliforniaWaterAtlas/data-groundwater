/**

 Usage: 
 mongo watertable depth_by_years.js
 - Will create 30 collections for each year, with geocoordinates.
 - Groundwater well metadata will need to be looked up by id.

 @TODO not sure this is super awesome
 @TODO check that the reference point doesn't move from one year to the next, if so.. adjust?

**/

var years = 30;
var current_year = 1983;

for (var year = 0;year <= years;year++) { 
  //aggregateDepths(current_year);
  ensureIndexes(current_year);
  current_year = current_year + 1;
}

function aggregateDepths(year) {
  var year = year.toString();
  var result = db.database.aggregate(
    { $match: { "properties.year": year}},
    { $group : { 
        _id : "$id", 
        average : { $avg : "$properties.gs_to_ws" },

        well : {"$addToSet": {
            geometry: "$geometry"
/*             type: "$geometry.type", */
/*             coordinates: "$geometry.coordinates" */
            }
        }

      }
    }
  );
    
  var collectionName = "depth_" + year;

  db[collectionName].drop();  
  db[collectionName].insert(result.result);

}

function ensureIndexes(year) {
  var collectionName = "depth_" + year;
  db[collectionName].ensureIndex({ "well.geometry.coordinates": "2d" });
}
       
       
       
       
/*

db.depth_2013.aggregate(
[{ $geoNear: {
      near:  [-121.8404,38.7647],
      maxDistance: 0.008,
      includeLocs: "dist.location",
      uniqueDocs: true,
      num: 5
    }
  }]
);


	{$match: { 
	     "properties.year": 2013}},
  {$group : { 
      _id : "$id", 
      average : { $avg : "$properties.gs_to_ws" },
      well : {
        "$addToSet": {
          geometry: "$geometry"
        }
      }
    }
  }



       
*/