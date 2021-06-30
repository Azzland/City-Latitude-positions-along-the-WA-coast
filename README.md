# City-Latitude-positions-along-the-WA-coast
Map designed in QGIS of city latitude positions compared to positions along the WA coast.

# Software
QPython 3L
QGIS 3.14
Google Sheets
Google.com

# Process
On my mobile phone I have an app to write Python code called QPython 3L.
I searched the latitude and longitude coordinates of several places in the Southern Hemisphere on Google. I created a CSV file to store this information using Google Sheets.
I downloaded a geojson file showing the outlines of all Australian state borders.
I created a python code that reads in the CSV file and geojson file and uses the latitude coordinates from all the place locations in the CSV file to find the corresponding or approximate longitude value on the WA state border from the geojson file.
I assumed a longitude value (maximum value) to create a series of lines, each representing the latitude location of a place from the CSV.
I created a linestring geojson file to store these lines, along with the place from the CSV file they correspond to.
I used QGIS to import both the state geojson file and this cities line geojson file.
I made only the WA state visible and had the state's layer overlap the latitude layer.
I edited the place latitude line layer to omit a few places clearly too south or too north of WA and a few others due to overlap.
The finished presented map was manually completed using the QGIS GUI and exported as an image file 
 
