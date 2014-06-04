import requests
import re
import csv

# User defined variables
feedaddr = 'https://feed.internetidentity.com/xxxxxxxx/Hostname%20Threats/active_bad_hostnames_standard.csv'
feedID = 'iid_activebaddomain'
user = 'myusername'
password = 'mysecretpassword'
killchain = 'Delivery'

r = requests.get(feedaddr, auth=(user, password))
splitlines = r.content.split('\n')
splitlines.pop(0)

print('domain,feedID,killchain,description,date_iso,class,property')

csvreader = csv.reader(splitlines, delimiter=',', quotechar='"')
for row in csvreader:
	if len(row) == 0: continue # Skip any blank lines
	if row[0] == 'EOF': continue
	row[2] = re.sub(',', '', row[2])
	print("%s,%s,%s,%s,%s,%s,%s" % (row[0], feedID, killchain, 'IID Active Bad IPs', row[1], row[2], row[3]))