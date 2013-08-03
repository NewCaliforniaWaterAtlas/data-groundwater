#!/usr/bin/python
import sys, os, datetime

# Create list of files.
file_list = []
 

# Set path to list of files.
path = "../../timeseries_test/"
# @TODO Alternately, take argument from command row
# print "command row argument is", sys.argv[1]

# Open file we will write to, replace it with new data.
fout=open("../../database/casgem_timeseries.csv","r+")
fout.seek(0)

# Read each file in the directory.
for file in [doc for doc in os.listdir(path)

# Build list of file names in the directory.
if doc.endswith(".csv")]:
    file_list.append(file)

# Test if string represents an integer.
def RepresentsInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False

# Return time file was created.
def modificationDate(filename):
    t = os.path.getmtime(filename)
    return datetime.datetime.fromtimestamp(t)

# Process a row, adding extra handling to remove errors in mapping.
def cleanupRow(row):

    # Split row into array based on comma.
    row_list = row.split(",")

    # Create empty values for month, day, year
    date_csv = ",,,"

    # Split the / separated date and convert into comma-separated string.
    if(row_list[8] != '' and row_list[8] != "Date"):
        date = row_list[8].strip()
        date_list = date.split("/")
        date_csv = ",".join(date_list)

    # Error checking for null and empty values. Convert to empty string or NULL value.
    if(row_list[10] == ''):
        row_list[10] = "" #No Measurement

    if(row_list[11] == ''):
        row_list[11] = "" #Questionable Measurement

    if(row_list[12] == ''):
        row_list[12] = 'NULL' #Reading @RP

    if(row_list[13] == ''):
        row_list[13] = 'NULL' #Reading @WS

    if(row_list[14] == ''):
        row_list[14] = 'NULL' #RP to WS

    if(row_list[15] == ''):
        row_list[15] = 'NULL' #RP Elevation

    if(row_list[16] == ''):
        row_list[16] = 'NULL' #GS Elevation

    if(row_list[17] == ''):
        row_list[17] = 'NULL' #WSE

    if(row_list[18] == ''):
        row_list[18] = 'NULL' #GS to WS
    
    # Put array back together
    row = ",".join(row_list)

    # Append date.
    row = row + "," + date_csv
    
    return row

# Count total records.
totalcount = 0

# Read file list.
for i in file_list:

    print "Processing file: " + path + i

    # Open file
    f = open(path + i, 'r')

    filecount = 0
    rowcount = 0

    filetime = modificationDate(path + i)

    # Read each row, perform cleanup functions.
    for row in f:
        if row != '':
            # Remove whitespace
            row = row.strip()

            # Create placeholder names for columnn header rows.
            if rowcount == 0:
                filename = "filename"
                latitude = "latitude"
                longitude = "longitude"
                county = "county"      
                well = "well"
                filetime = "filetime"

            else:

                filename = str(i)

                county = i.split("_", 1)[0]
    
                # Parse latitude and longitude
                # 397135N1219039W001
                location = row.split(",")[0]
                latitude = location[0:6]
                if(RepresentsInt(latitude)):
                    latitude = float(latitude) * 0.0001
                longitude = location[7:14]
                if(RepresentsInt(longitude)):
                    longitude = float(longitude)  * -0.0001
                
                #W001
                well = ""            
                if location[14:15] == 'W':
                    well = location[14:18]
                else:
                    well = ""

            # Build row.
            row = filename + "," + county + "," + str(latitude) + "," + str(longitude) + "," + well + "," + str(filetime) + "," + row

            # Resplit row, clean up columns, add date facets.
            row_dated = cleanupRow(row) + "\n"

            # Write row to output file.
            if filecount != 0:
                if rowcount != 0:
                    fout.write(row_dated)

            # Add cleaned up column headers.
            else:
                row = "filename,county,latitude,longitude,well,filetime,casgem_id,local_well_number,date,military_time_pst,no_measurement,questionable_measurement,reading_ap,reading_ws,rp_to_ws,rp_elecation,gs_elevation,wse,gs_to_ws,measurement_method,measurement_accuracy,collecting,comments,month,day,year"

                fout.write(row + '\n')

            rowcount = rowcount + 1
            totalcount = totalcount + 1
        filecount = filecount + 1

fout.truncate()
fout.close()
print "Done. Processed " + str(totalcount) + " records."
sys.exit()
