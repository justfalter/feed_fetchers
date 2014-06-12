from FeedFetcher.BaseHandler import BaseHandler
import requests

class HttpHandler(BaseHandler):
    def __init__(self, feedaddr = None, *args, **kwargs):
        super(HttpHandler,self).__init__(*args, **kwargs)
        self._feedaddr = feedaddr

    def run(self):
        r = requests.get(self._feedaddr, stream=True)
        for line in r.iter_lines(1024):
            self.handle_line_from_feed(line)
