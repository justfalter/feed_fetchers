import re
import shutil
import requests
import gzip
import os, subprocess

filename = '/tmp/dnsbl-3.uceprotect.net'
feedID = 'uce_dnsbl-3'
killchain = 'Reconnaissance'

# Fetch the file
if os.path.isfile(filename): os.remove(filename)
subprocess.check_call(["/usr/bin/rsync", "-azv", "rsync-mirrors.uceprotect.net::RBLDNSD-ALL/dnsbl-3.uceprotect.net", "/tmp"], stdout=open(os.devnull, 'wb'))

# Read the contents
f = open(filename, 'r')
lines_raw = f.read()
lines = lines_raw.split('\n')
del lines_raw

print('ipv4prefix,feedID,killchain,description')

for item in lines:
	if not re.search('^[0-9]', item): continue
	if re.search('^127', item): continue
	xsplit = item.split()
	print("%s,%s,%s,%s" % (xsplit[0], feedID, killchain, 'UCE Level 3 Spam Source'))

os.remove(filename)
