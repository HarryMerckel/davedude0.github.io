import csv
spine = open("383_newspine.csv")
data = open("383_census-1.csv")
spineReader = csv.DictReader(spine)
dataReader = csv.DictReader(data)
spineList = []
dataList = []
for row in spineReader:
    spineList.append(row)
for row in dataReader:
    dataList.append(row)
#print(spineList)
#print(dataList)


def merge_lists(l1, l2, key):
    merged = {}
    for item in l1 + l2:
        if item[key] in merged:
            merged[item[key]].update(item)
        else:
            merged[item[key]] = item
    return [val for (_, val) in list(merged.items())]

newlist = merge_lists(spineList, dataList, 'URN')

keys = []
for key in list(newlist[0].keys()):
    keys.append(key)
print(keys)
newcsv = open("new.csv", 'w')
writer = csv.DictWriter(newcsv, fieldnames=keys, lineterminator='\n')
writer.writeheader()
for i in range(len(newlist)):
    writer.writerow(newlist[i])