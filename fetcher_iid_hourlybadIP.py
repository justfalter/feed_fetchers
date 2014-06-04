import requests
import re
import csv

# User defined variables
feedaddr = 'https://feed.internetidentity.com/xxxxxxxx/IP%20Threats/hourly_badip_standard.csv'
feedID = 'iid_hourlybadIP'
user = 'myusername'
password = 'mysecretpassword'
killchain = 'Command & Control'

r = requests.get(feedaddr, auth=(user, password))
splitlines = r.content.split('\n')
splitlines.pop(0)

print('ipv4,feedID,killchain,description,class,property')

csvreader = csv.reader(splitlines, delimiter=',', quotechar='"')
for row in csvreader:
	if len(row) == 0: continue # Skip any blank lines
	if row[0] == 'EOF': continue
	row[2] = re.sub(',', '', row[2])
	print("%s,%s,%s,%s,%s,%s" % (row[0], feedID, killchain, 'IID Hourly Bad IPs', row[2], row[3]))