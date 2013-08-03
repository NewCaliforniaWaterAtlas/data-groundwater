
Map {
//  background-color: #d3d3c7;
}

#aquifers_top {
  polygon-fill:#e8e4dc; 
}

// Aquetard
#aquifers,
#aquifers [ROCK_NAME = "Other rocks"]{
  //polygon-fill:#424242;
  // http://pngtextures.com/#opacity=0.58&texture=Lines%202&inverted=false
  // Save in ~/Documents/Mapbox/project/aquifers/images/filename.png
  // http://www.mapbox.com/tilemill/docs/guides/comp-op/
  //polygon-pattern-file: url(images/stripes.png);
  polygon-fill:#faf6f6;
  polygon-pattern-file: url(images/textured_paper.png);

  comp-op: screen;
  opacity: 1;
}

#aquifers [ROCK_NAME = "Unconsolidated sand and gravel aquifers"] {
  polygon-fill:#faf6f6;
  polygon-pattern-file: url(images/textured_paper.png);
  comp-op: multiply;
  opacity: 1;
}

#aquifers [ROCK_NAME = "Igneous and metamorphic-rock aquifers"] {
  polygon-fill:#d4d4d4;
  polygon-pattern-file: url(images/paper_2.png);
  comp-op: multiply;
  opacity: 1;
}

#aquifers [ROCK_NAME = "Carbonate-rock aquifers"] {
  polygon-fill:#e6e6e6;
  polygon-pattern-file: url(images/paper_2.png);
  comp-op: multiply;
  opacity: 1;
}


#dwr {
  line-color:#173930;
  line-width:0.5;
  line-opacity: 0.9;
  line-dasharray: 10, 3, 2, 3;
}

#dwr_labels[zoom > 8] {
  ::labels {
	text-name:[GWBASIN];
 	text-fill: #fff;
	text-size:8;
    text-min-padding: 0;
    text-min-path-length: 0;
    text-placement: interior;
	text-placement-type: simple; 
    text-face-name: 'Muli Regular';
    text-fill: #fff;
    text-wrap-width: 30;
    text-allow-overlap:false;
    text-halo-fill: fadeout(#346356, 40%);
    text-halo-radius: 2;
    text-dy: 5;
    text-max-char-angle-delta: 20;
  }
}

#dwr_labels[zoom > 8] {
  ::labels {
	text-size:12;
  }
}

// know how much water is going in and coming out // quality of the data
// A - well understood
// B - estimated
// C - poorly understood.


#dwr [BUDGET_TYP = "A"] {
  polygon-opacity:8;
  polygon-fill:#173930;
 // comp-op: hard-light;
}

// budget estimated
#dwr [BUDGET_TYP = "B"] {
  polygon-opacity:0.6;
  polygon-fill:#173930;
 // comp-op: hard-light; 
}

#dwr [BUDGET_TYP = "C"] {
  polygon-opacity:0.5;
  polygon-fill:#173930;
//  comp-op: hard-light;
}

#wells-glenn-2012,
#wells {
  ::labels{
  	text-name:"[wse]";
    text-size:10;
  	text-face-name: 'Muli Regular';
  	text-placement-type: simple;
  	text-dy: 3;
  	text-dx: 3;
  }
  marker-line-color:#110c0c;
  marker-line-width: 0.25px;
  marker-allow-overlap:false;
  marker-width:8px;
  marker-fill:transparent;
}
#wells-glenn-2012 [wse > -20],
#wells [wse > -10]{
  marker-width:6;
  marker-fill:#a4470a;
}
#wells-glenn-2012 [wse > 25],
#wells [wse > 0]{
  marker-width:6;
  marker-fill:#c46424;
}
#wells-glenn-2012 [wse > 100],
#wells [wse > 10]{
  marker-width:6;
  marker-fill:#ca7635;
}
#wells-glenn-2012 [wse > 200],
#wells [wse > 20]{
  marker-width:6;
  marker-fill:#f69d62;
}


/*
#wells [gs_to_ws > -500]{
  marker-width:6;
  marker-fill:#a4470a;
}

#wells [gs_to_ws > -200]{
  marker-width:6;
  marker-fill:#c46424;
}

#wells [gs_to_ws > 0]{
  marker-width:6;
  marker-fill:#ca7635;
}

#wells [gs_to_ws > 200]{
  marker-width:6;
  marker-fill:#f69d62;
}

#wells [gs_to_ws > 500]{
  marker-width:6;
  marker-fill:#ffffff;
}
*/


/*
{{{OBJECTID}}}
{{{ROCK_NAME}}}
{{{ROCK_TYPE}}}
{{{AQ_NAME}}}
{{{AQ_CODE}}}
{{{Shape_Leng}}}
{{{Shape_Area}}}
*/

/*{{{casgem_id}}}
{{{lat}}} {{{long}}} {{{local_well_number}}} {{{date}}} 
{{{military_time_pst}}} {{{no_measurement}}} 
{{{questionable_measurement}}} {{{reading_rp}}} {{{reading_ws}}} 
{{{rp_to_ws}}} {{{rp_elevation}}} {{{gs_elevation}}} {{{wse}}} 
{{{gs_to_ws}}} {{{measurement_method}}}
*/



#elevation {

  line-width:0.7;
  line-opacity:0.7;
//  [zoom < 11] { line-opacity: 0}
//  [zoom < 13] { line-width: .5}
  line-join:round;
  //line-gamma:1;
 //  line-comp-op: multiply;
//  line-smooth:1;
  line-color: #fff;

  [ELEV <= 4800] {  line-color: #a7a7a7; }
  [ELEV <= 2000] {  line-color: #9c9c9c; }
  [ELEV <= 500]  {  line-color: #838383; }
  [ELEV <= 200]  {  line-color: #5b5b5b; }
  [ELEV <= 100]  {  line-color: #494949; }
  [ELEV <= 50] 	 {  line-color: #383838; }
  [ELEV <= -70]  {  line-color: #313131; }
  //[ELEV <= -100] 	 {  line-color: #2d2d2d; }

}
