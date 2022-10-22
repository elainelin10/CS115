import bottle
import json
import cache
import backend

@bottle.route("/")
def index():
    htmlfile=bottle.static_file("index.html",root=".")
    return htmlfile

@bottle.route("/frontend.js")
def jscode():
    jsfile=bottle.static_file("frontend.js",root=".")
    return jsfile

@bottle.route("/towsByDay")
def scatterplot():
  data=cache.read_cache("cached_data.csv")
  towsByDay=backend.count_by_day(data)
  json_blob=json.dumps(towsByDay)
  return json_blob

@bottle.route("/towsByDistrict")
def piechart():
  data=cache.read_cache("cached_data.csv")
  towsByDistrict=backend.count_by_day(data)
  json_blob=json.dumps(towsByDistrict)
  return json_blob

@bottle.route("/towsByMonth")
def linegraph():
  data=cache.read_cache("cached_data.csv")
  towsByMonth=backend.count_by_month(data)
  json_blob=json.dumps(towsByMonth)
  return json_blob
  
import os.path
import cache
def load_data( ):
   csv_file = 'cached_data.csv'
   if not os.path.isfile(csv_file):
       query_str = "?$limit=10000"
       url = "https://data.buffalony.gov/resource/5c88-nfii.json" + query_str
       data = cache.get_data(url)
       data = cache.minimize_dictionaries(data, ['tow_date', 'tow_description', 'police_district'])
       cache.write_cache(data, csv_file)

load_data()
bottle.run(host="0.0.0.0", port=8080, debug=True)