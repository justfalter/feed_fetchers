import sys
import csv
from FeedFetcher.Output import Output

class CSVOutput(Output):
  def start(self):
    self.csv_writer = csv.DictWriter(self.io, self.fields)
    self.csv_writer.writeheader()

  def emit(self, feedID, record_type, row_dict):
    Output.emit(self, feedID, record_type, row_dict)
    self.csv_writer.writerow(row_dict)
