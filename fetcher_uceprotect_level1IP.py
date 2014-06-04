import re
import shutil
import requests
import gzip
import os, subprocess

filename = '/tmp/dnsbl-1.uceprotect.net'
feedID = 'uce_dnsbl-1'
killchain = 'Reconnaissance'

# Fetch the file
if os.path.isfile(filename): os.remove(filename)
subprocess.check_call(["/usr/bin/rsync", "-azv", "rsync-mirrors.uceprotect.net::RBLDNSD-ALL/dnsbl-1.uceprotect.net", "/tmp"], stdout=open(os.devnull, 'wb'))

# Read the contents
f = open(filename, 'r')
lines_raw = f.read()
lines = lines_raw.split('\n')
del lines_raw

print('ipv4,feedID,killchain,description')

for item in lines:
	if not re.search('^[0-9]', item): continue
	if re.search('^127', item): continue
	print("%s,%s,%s,%s" % (item, feedID, killchain, 'UCE Level 1 Spam Source'))

os.remove(filename)
