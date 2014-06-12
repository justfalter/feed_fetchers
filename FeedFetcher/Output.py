import sys
import csv
from FeedFetcher.FeedRecordType import FeedRecordType

class Output:
  def __init__(self, io = sys.stdout ): 
    self.io = io

  def start(self):
    pass

  def set_fields(self, fields):
    self.fields = ['feedID', 'killchain'] + fields

  def emit(self, feedID, record_type, row_dict):
    row_dict['feedID'] = feedID
    row_dict['killchain'] = FeedRecordType.to_string(record_type)
