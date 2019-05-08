import json
import xml.etree.ElementTree as etree

class JSONParser:
    def __init__(self, filepath):
        self.data = {}
        with open(filepath) as f:
            self.data = json.load(f)

class XMLParser:
  def __init__(self, filepath):
      self.data = etree.parse(filepath)


def parser_factory(filepath):
    if filepath.endswith('json'):
        Parser = JSONParser
    elif filepath.endswith('xml'):
        Parser = XMLParser
    else:
        raise ValueError(f'Cannot parser data in file {filepath}')
    return Parser(filepath)