##### OGR text file to czml converter (use ogrinfo tool to get shape file info into text file). With building elevation above ellipsoid.
##### Created by Parthesh B.

import os
f = open('hyd_fin_data.txt','r')
g = open('write.czml','a')
p = f.read()
str_len = len(p)
str1 = "ZS_mean (Real) = "
str2 = "Building_h (Real) = "
str3 = "POLYGON (("
count = p.count(str1,0,len(p))
#Extruded Height
ext_ht = 0   #define location of building height
elev = 0     #define location of building elevation
positions = 0    #define location of building position
g.write('[{"id":"document","version":"2.0"},')


for ii in range(1,count):
    ext_ht = p.find(str2,ext_ht+1)  #index of next extruded height
    ht = ''
    elev = p.find(str1,elev+1)
    h = ''
    
    for i in range(1,7):
        ht = ht + str(p[ext_ht+19+i])     #building height data
        
    for j in range(1,7):
        h = h + str(p[elev+16+j])         #building elevation data
        
    ht = float(ht)
    h = float(h)
    total_height = ht+h
    g.write('\n{"id":'+'"'+str(ii)+'"'+',"description":"Building Height:'+str(total_height)+'m"'+',"polygon": {"extrudedHeight": {"number": '+str(total_height)+'},"height": {"number": '+str(h)+'},"outline":{"boolean":true},"outlineColor":{"rgba":[0,0,0,255]},"material":{"solidColor":{"color":{"rgba":[255,0,0,163]}}},"positions":{"cartographicDegrees":[')

    positions = p.find(str3,positions+1)
    counter = 10 #till end of polygon
    
    while (p[positions+counter]!=")"): #or p[positions+counter]!=","):
        #while (p[positions+counter]!=" "):
        if (p[counter+positions]!=","):
            if (p[counter+positions]!=" "):
                g.write(p[counter+positions])
                counter += 1
            else:
                g.write(",")
                counter += 1   
        else:
            g.write(",")    
            counter += 1
    g.write("]}}},")
#g.write(']')
g.close()


with open('write.czml', 'rb+') as filehandle:
   filehandle.seek(-1, os.SEEK_END)
   filehandle.truncate()
   
g = open('write.czml','a')
g.write(']')   
g.close()
