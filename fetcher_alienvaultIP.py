import requests
import re

feedaddr = 'https://reputation.alienvault.com/reputation.generic'
feedID = 'alienvault'
mkey = 'fetcher_alienvault:feeddata'
killchain = 'Reconnaissance'

r = requests.get(feedaddr)
splitlines = r.content.split('\n')

print('ipv4,feedID,killchain,description,type,info')

for x in splitlines:
	x = x.strip()
	if re.search('^#', x): continue
	if len(x) == 0: continue
	xlist = x.split(' # ')
	xlist_pt2 = xlist[1].split(',')
	if re.search('C\&C', xlist_pt2[0]):
		print("%s,%s,%s,%s,%s" % (xlist[0], feedID, 'Command & Control', 'Alienvault nasty IPs',xlist_pt2[0]))
	elif re.search('Malware', xlist_pt2[0]):
		print("%s,%s,%s,%s,%s" % (xlist[0], feedID, 'Exploit', 'Alienvault nasty IPs',xlist_pt2[0]))
	elif re.search('Malicious', xlist_pt2[0]):
		print("%s,%s,%s,%s,%s" % (xlist[0], feedID, 'Delivery', 'Alienvault nasty IPs',xlist_pt2[0]))
	elif re.search('Spamming', xlist_pt2[0]):
		print("%s,%s,%s,%s,%s" % (xlist[0], feedID, 'Delivery', 'Alienvault nasty IPs',xlist_pt2[0]))
	else:
		print("%s,%s,%s,%s,%s" % (xlist[0], feedID, killchain, 'Alienvault nasty IPs',xlist_pt2[0]))
	
