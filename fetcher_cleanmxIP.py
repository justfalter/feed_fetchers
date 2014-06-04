import requests
import re
from pymemcache.client import Client
from xml.dom.minidom import parseString
import sys

# User defined variables
feedaddr = 'http://support.clean-mx.de/clean-mx/xmlviruses.php?'
feedID = 'cleanmx'
mkey = 'fetcher_cleanmxDomain:feeddata'
killchain = 'Exploit'

# No user modifications needed below.
client = Client(('localhost', 11211))
result = client.get(mkey)

if isinstance(result, str):
	dom = parseString(result)
else:
	r = requests.get(feedaddr)
	client.set(mkey, r.content, expire=7200)
	dom = parseString(r.content)

xmlroot = dom.getElementsByTagName("output")[0]
xmlroot = xmlroot.getElementsByTagName("entries")[0]

print('ipv4,feedID,killchain,description,md5,vt_score,domain,email,url')

seen = []

for entry in xmlroot.getElementsByTagName("entry"):
	if entry.getElementsByTagName('md5')[0].firstChild != None:
		if entry.getElementsByTagName('md5')[0].firstChild.nodeValue in seen: 
			continue
		else:
			seen.append(entry.getElementsByTagName('md5')[0].firstChild.nodeValue)
	if entry.getElementsByTagName('ip')[0].firstChild == None: continue
	sys.stdout.write(entry.getElementsByTagName('ip')[0].firstChild.nodeValue)
	sys.stdout.write(',')
	sys.stdout.write(feedID)
	sys.stdout.write(',')
	sys.stdout.write(killchain)
	sys.stdout.write(',')
	sys.stdout.write('CleanMX malware relations')
	sys.stdout.write(',')
	if entry.getElementsByTagName('md5')[0].firstChild != None:
		sys.stdout.write(entry.getElementsByTagName('md5')[0].firstChild.nodeValue)
	sys.stdout.write(',')
	if entry.getElementsByTagName('vt_score')[0].firstChild != None:
		sys.stdout.write(entry.getElementsByTagName('vt_score')[0].firstChild.nodeValue)
	sys.stdout.write(',')
	if entry.getElementsByTagName('domain')[0].firstChild != None:
		sys.stdout.write(entry.getElementsByTagName('domain')[0].firstChild.nodeValue)
	sys.stdout.write(',')
	if entry.getElementsByTagName('email')[0].firstChild != None:
		sys.stdout.write(entry.getElementsByTagName('email')[0].firstChild.nodeValue)
	if entry.getElementsByTagName('url')[0].firstChild != None:
		sys.stdout.write(entry.getElementsByTagName('url')[0].firstChild.nodeValue)
	print


