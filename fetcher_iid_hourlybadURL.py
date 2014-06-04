import requests
import re
import csv

feedaddr = 'https://feed.internetidentity.com/xxxxxxxx/URL%20Threats/hourly_combined_detected_standard.csv'
feedID = 'iid_hourlybadURL'
user = 'myusername'
password = 'mysecretpassword'
killchain = 'Delivery'

r = requests.get(feedaddr, auth=(user, password))
splitlines = r.content.split('\n')
splitlines.pop(0)

print('url,feedID,killchain,description,sid,target,date_iso,baddom,domain,class_name')

csvreader = csv.reader(splitlines, delimiter=',', quotechar='"')
for row in csvreader:
	if len(row) == 0: continue # Skip any blank lines
	if row[0] == 'EOF': continue
	row[2] = re.sub(',', '', row[2])
	print("%s,%s,%s,%s,%s,%s,%s,%s,%s,%s" % (row[1], feedID, killchain, 'IID Hourly Bad URL', row[0], row[2], row[3], row[4], row[5], row[6]))