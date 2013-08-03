#!/usr/bin/python
import sys, os, datetime
 
file_list = []
 
#print "command line argument is", sys.argv[1]
path = "../../timeseries_test/"

fout=open("../../database/casgem_timeseries.csv","r+")
fout.seek(0)

for file in [doc for doc in os.listdir(path)

if doc.endswith(".csv")]:
    file_list.append(file)

def RepresentsInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False

def modification_date(filename):
    t = os.path.getmtime(filename)
    return datetime.datetime.fromtimestamp(t)


def cleanupLine(line):
    line_list = line.split(",")
    
    if(line_list[10] == ''):
        line_list[10] = "" #No Measurement

    if(line_list[11] == ''):
        line_list[11] = "" #Questionable Measurement

    if(line_list[12] == ''):
        print "rp null"
        line_list[12] = 'NULL' #Reading @RP

    if(line_list[13] == ''):
        line_list[13] = 'NULL' #Reading @WS

    if(line_list[14] == ''):
        line_list[14] = 'NULL' #RP to WS

    if(line_list[15] == ''):
        line_list[15] = 'NULL' #RP Elevation

    if(line_list[16] == ''):
        line_list[16] = 'NULL' #GS Elevation

    if(line_list[17] == ''):
        line_list[17] = 'NULL' #WSE

    if(line_list[18] == ''):
        line_list[18] = 'NULL' #GS to WS
    
    line = ",".join(line_list)
    
    return line

totalcount = 0
for i in file_list:
    print "Processing file: " + path + i
    f = open(path + i, 'r')
    filecount = 0
    linecount = 0
    filetime = modification_date(path + i)
    for line in f:
        if line != '':
            line = line.strip()
            #print filecount
            if linecount == 0:
                filename = "filename"
                latitude = "latitude"
                longitude = "longitude"
                county = "county"      
                well = "well"
            else:
                filename = str(i)

                county = i.split("_", 1)[0]
    
                # 397135N1219039W001
                location = line.split(",")[0]
                latitude = location[0:6]
                if(RepresentsInt(latitude)):
                    latitude = float(latitude) * 0.0001
                longitude = location[7:14]
                if(RepresentsInt(longitude)):
                    longitude = float(longitude)  * -0.0001
    
                well = ""            
                if location[14:15] == 'W':
                    well = location[14:18]
                else:
                    well = ""

            line = filename + "," + county + "," + str(latitude) + "," + str(longitude) + "," + well + "," + str(filetime) + "," + line + "\n"

            line = cleanupLine(line)

            if filecount != 0:
                if linecount != 0:
                    fout.write(line)
            else:
                fout.write(line)

            linecount = linecount + 1
            totalcount = totalcount + 1

        filecount = filecount + 1

fout.truncate()
fout.close()
print "Done. Processed " + str(totalcount) + " records."
sys.exit()
