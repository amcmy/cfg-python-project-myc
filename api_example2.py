import requests as re

endpoint = "http://api.openweathermap.org/data/2.5/weather"

def query_weather(city):
    pd = {'q':city, 'units':'metric', 'appid':"84600bca7507293656495e8972aec659"}
    endpoint = "http://api.openweathermap.org/data/2.5/weather"
    response = re.get(endpoint, params=pd)
    return jsonify(response)['main']['temp']

def jsonify(response):
    json_response = response.json()
    return json_response

print("The temperature is {} is {}".format('London', query_weather('London'),'Sheffield', query_weather('Sheffield')))