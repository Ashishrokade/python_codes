import urllib.request
import json

def get_json_opt(url_to_parse):

  req = urllib.request.Request(url_to_parse)
  ##parsing response
  r = urllib.request.urlopen(req).read()
  data = json.loads(r.decode('utf-8'))
  return data

def get_all_titles(substr):
  url_base = "https://jsonmock.hackerrank.com/api/movies/search/?Title="+ substr
  parsed_data =  get_json_opt(url_base)

  #print ("parsed_data:",parsed_data)
  #print ("total",parsed_data['total'])

  return parsed_data['total']
    
