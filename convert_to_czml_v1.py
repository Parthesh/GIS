##### OGR text file to czml converter (use ogrinfo tool to get shape file info into text file). Without building elevation above ellipsoid.
##### Created by Parthesh B.

import os
f = open('file.txt','r')
g = open('write4.txt','a')
p = f.read()
str_len = len(p)
#str1 = "this is string example....wow!!!"
str1 = "Elevation_ (Real) = "
str2 = "Building_h (Real) = "
str3 = "POLYGON (("
count = p.count(str1,0,len(p))
#Extruded Height
ext_ht = 0   #define location of building height
positions = 0    #define location of building position
g.write('[{"id":"document","version":"1.0"},')


for ii in range(1,count):
    ext_ht = p.find(str2,ext_ht+1)  #index of next extruded height
    ht = ''
    
    for i in range(1,7):
        ht = ht + str(p[ext_ht+19+i])     #building height data
    g.write('\n{"id":'+'"'+str(ii)+'"'+',"description":"Building Height:'+ht+'m"'+',"polygon": {"extrudedHeight": {"number": '+ht+'},"outline":{"boolean":true},"outlineColor":{"rgba":[0,0,0,255]},"material":{"solidColor":{"color":{"rgba":[255,0,0,163]}}},"positions":{"cartographicDegrees":[')

    positions = p.find(str3,positions+1)
    counter = 10 #till end of polygon
    
    while (p[positions+counter]!=")"): #or p[positions+counter]!=","):
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
g.close()


with open('write.czml', 'rb+') as filehandle:
   filehandle.seek(-1, os.SEEK_END)
   filehandle.truncate()
g = open('write.czml','a')
g.write(']')   
g.close()
