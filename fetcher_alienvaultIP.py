import re
from FeedFetcher import FeedRecordType, HttpHandler

class Handler(HttpHandler):
    mkey = 'fetcher_alienvault:feeddata'

    MAPPING = {
        re.compile('C\&C'): FeedRecordType.COMMAND_AND_CONTROL,
        re.compile('Malware'): FeedRecordType.EXPLOIT,
        re.compile('Malicious'): FeedRecordType.DELIVERY,
        re.compile('Spamming'): FeedRecordType.SPAMMING
        }

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('feedID', 'alienvault')
        kwargs.setdefault('fields', ['ipv4','description','info'])
        kwargs.setdefault('feedaddr', 'https://reputation.alienvault.com/reputation.generic')
        kwargs.setdefault('mkey', 'fetcher_alienvault:feeddata')
        super(Handler, self).__init__(*args, **kwargs)

    def handle_line_from_feed(self, line):
        line = line.strip()
        if len(line) == 0: return
        if re.search('^#', line): return
        xlist = line.split(' # ')
        xlist_pt2 = xlist[1].split(',')
        ipv4 = xlist[0]
        info = xlist_pt2[0]

        record_type = FeedRecordType.RECONNAISSANCE
        for pattern, val in self.MAPPING.items():
            if pattern.match(info):
                record_type = val
                break

        self.emit(record_type, {
            'ipv4': ipv4, 
            'description': 'Alienvault nasty IPs',
            'info': info
            })


if __name__ == "__main__":
    from FeedFetcher import CSVOutput
    handler = Handler(output = CSVOutput())
    handler.run()
