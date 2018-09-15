import json
import requests

url = "http://ws.audioscrobbler.com/2.0/?method=geo.gettopartists&country=spain&api_key=4beab33cc6d65b05800d51f5e83bde1b&format=json"
def api_get_request(url):
    # In this exercise, you want to call the last.fm API to get a list of the
    # top artists in Spain. 
    # Once you've done this, return the name of the number 1 top artist in
    # Spain. 
    
    data = requests.get(url).text
    #transform JSON object into a Python dict.:
    data = json.loads(data)
    top_a = data["topartists"].values()
    without_header = top_a[1]
    result = without_header[0]["name"]   
    # return the top artist in Spain
    return result
api_get_request(url)
