#-*-coding:utf8;-*-
#qpy:console
import json
import csv
#from geojson import Line, Feature, FeatureCollection, dump


gjson = '/storage/emulated/0/SW_Maps/Maps/geojson/aus_state.geojson'
gjson_output = '/storage/emulated/0/SW_Maps/Maps/geojson/cities.geojson'
csv_input = '/storage/emulated/0/SW_Maps/Maps/shapefiles/SCities.csv'
	
Max_lon =	129.00095623
AllXY = []
maxpoints = -1
mainpoly = -1
with open (gjson) as f:
  data = json.load(f)
  features = data['features']
  for feat in features:
      if feat['properties']['STATE_NAME'] == 'Western Australia':
          geom = feat['geometry']['coordinates']
          #print(geom)
          numsections = len(geom)
          
          for i in range(numsections):             
              gm = geom[i][0]
              numpoints = len(gm)
              if numpoints > maxpoints:
                  maxpoints = numpoints
                  mainpoly = i
    
print(mainpoly)
print(maxpoints)

minX = 180
minY = 90
maxY = -90
          
gty = geom[mainpoly][0]
for i in range(maxpoints):
   if gty[i][0] <= minX:
       minX = gty[i][0]
   if gty[i][1] <= minY:
       minY = gty[i][1]
   elif gty[i][1] >= maxY:
       maxY = gty[i][1]
   AllXY.append(gty[i])
print(minX)
print(minY)
print(maxY)

with open(csv_input) as csv_file:
        print('Reading csv')
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        data = []
        for row in csv_reader:
            data.append(row)
            line_count += 1
geojson = {'type':'FeatureCollection', 'features':[]}
             
numplaces = len(data)

for i in range(numplaces):
    line = []
    y = float(data[i][1])
    
    mindist1 = 180
    mindist2 = 180
    x1 = 180
    x2 = 180
    ref = -1
    for j in range(numpoints):
        y_gj = AllXY[j][1]
        
        dist = y - y_gj
        
        if dist < 0:
            dist = 0 - dist
        if dist < mindist1:
            mindist1 = dist
            x1 = AllXY[j][0]
            y1 = y_gj
    
    if y < y1:
        for j in range(numpoints):
            y_gj = AllXY[j][1]
            if y_gj < y:
                dist = y - y_gj
                if dist < mindist2:
                    mindist2 = dist
                    x2 = AllXY[j][0]
                    y2 = y_gj
        grad = (y1 - y2)/(x1 - x2)
        x = x1 + (y1 - y)*grad                
    elif y > y1:
        for j in range(numpoints):
            y_gj = AllXY[j][1]
            if y_gj > y:
                dist = y_gj - y
                if dist < mindist2:
                    mindist2 = dist
                    x2 = AllXY[j][0]
                    y2 = y_gj
        x = x1 + (y - y1)*grad                 
    else:
        x = x1
        
        
    lx1 = x
    ly = y 
    lx2 = minX - 10
    line.append([lx1,ly])
    line.append([lx2,ly])
    feature = {'type':'Feature',
           'properties':{},
           'geometry':{'type':'Linestring',
                       'coordinates':[]}}
    feature['geometry']['coordinates'] = line
    feature['properties']['name'] = data[i][0]
    geojson['features'].append(feature) 
#print(Lines) 


      
with open(gjson_output, 'w') as f:
   json.dump(geojson, f, indent=2)        



          
             
          
      
