// Usage: 
// mongo watertable depth_by_years.js

// @TODO check that the reference point doesn't move from one year to the next, if so.. adjust?

var years = 30;
var current_year = 1983;

for (var year = 0;year <= years;year++) { 
  aggregateDepths(current_year);
  current_year = current_year + 1;
}

function aggregateDepths(year) {
  var year = year.toString();
  var result = db.database.aggregate(
    { $match: { "properties.year": year}},
    { $group : { 
        _id : "$id", 
        average : { $avg : "$properties.gs_to_ws" },
        geometry : {
         "$push": {
            coordinates: "$geometry.coordinates",
            type: "$geometry.type"
        }
        }
      }
    }
  );
    
  var collectionName = "depth_" + year;

  db[collectionName].drop();  
  db[collectionName].insert(result.result);  
}
         
              
              