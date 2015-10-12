from pygeocoder import Geocoder
import csv
myGeocoder = Geocoder(api_key='AIzaSyBAzuNOEkkrvRptzCPMNMhl5PUnyYYtzJ4')
with open("383_spine.csv") as spine:
    spine1 = open("383_spine.csv")
    reader = csv.DictReader(spine)
    line = csv.reader(spine1)
    All = []
    fieldnames = next(line)
    fieldnames.append("LAT")
    fieldnames.append("LNG")
    print(fieldnames)
    All.append(fieldnames)
    for row in reader:
        print((row['SCHNAME'], row['POSTCODE']))
        try:
            geo = myGeocoder.geocode(row['SCHNAME'] + ", " + row['POSTCODE'])
        except:
            try:
                geo = myGeocoder.geocode(row['POSTCODE'])
            except:
                print("Oh Noes!")
        curLine = next(line)
        curLine.append(geo[0].coordinates[0])
        curLine.append(geo[0].coordinates[1])
        All.append(curLine)
        row['LAT'] = geo[0].coordinates[0]
        row['LNG'] = geo[0].coordinates[1]
        print((row['LAT'], row['LNG']))
    print(All)
    newspine = open('383_newspine.csv', 'w')
    writer = csv.writer(newspine, lineterminator='\n')
    writer.writerows(All)

"""
googleLatLng = Geocoder.geocode("Yeadon Westfield Junior School")
print(googleLatLng[0].coordinates)
#print(googleLatLng.raw)
"""