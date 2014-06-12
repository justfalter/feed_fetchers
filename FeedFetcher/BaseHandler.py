from FeedFetcher.CSVOutput import CSVOutput

class BaseHandler(object):
    def __init__(self, feedID, fields, output, mkey):
        self._feedID = feedID
        self._fields = fields
        self._output = output
        self._output.set_fields(self._fields)
        self._output.start()
        self._mkey = mkey

    def mkey(self):
        return self._mkey

    def feedID(self):
        return self._feedID

    def fields(self):
        return self._fields

    def emit(self, record_type, data_dict):
        self._output.emit(self._feedID, record_type, data_dict)

    def run(self):
        pass



