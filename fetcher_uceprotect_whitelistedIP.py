import re
import shutil
import requests
import gzip
import os, subprocess

filename = '/tmp/ips.whitelisted.org'
feedID = 'uce_ips.whitelisted.org'
killchain = 'unknown'

# Fetch the file
if os.path.isfile(filename): os.remove(filename)
subprocess.check_call(["/usr/bin/rsync", "-azv", "rsync-mirrors.uceprotect.net::RBLDNSD-ALL/ips.whitelisted.org", "/tmp"], stdout=open(os.devnull, 'wb'))

# Read the contents
f = open(filename, 'r')
lines_raw = f.read()
lines = lines_raw.split('\n')
del lines_raw

print('ipv4,feedID,killchain,description')

for item in lines:
	if not re.search('^[0-9]', item): continue
	if re.search('^127', item): continue
	print("%s,%s,%s,%s" % (item, feedID, killchain, 'UCE Whitelisted IP'))

os.remove(filename)
