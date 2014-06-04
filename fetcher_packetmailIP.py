import requests
import re
import csv

# User defined variables
feedaddr = 'https://www.packetmail.net/iprep.txt'
feedID = 'packetmail'
killchain = 'Reconnaissance'

r = requests.get(feedaddr)
splitlines = r.content.split('\n')

print('ipv4,feedID,killchain,description,last_seen,context,cumulative_history')

csvreader = csv.reader(splitlines, delimiter=';')
for row in csvreader:
	if len(row) == 0: continue # Skip any blank lines
	if re.search('^#', row[0]): continue
	row[2] = re.sub(',', '', row[2])
	print("%s,%s,%s,%s,%s,%s,%s" % (row[0], feedID, killchain, 'Packetmail Honeypot hits', row[1], row[2], row[3]))