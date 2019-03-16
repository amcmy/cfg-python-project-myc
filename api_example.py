import requests as re

payload = {'q':'Sheffield, UK', 'units':'metric', 'appid':"84600bca7507293656495e8972aec659"}
endpoint = "http://api.openweathermap.org/data/2.5/weather"

def query_weather(payload, endpoint):
   # endpoint = "http://api.openweathermap.org/data/2.5/weather"
    response = re.get(endpoint, params=payload)

    return response

response = query_weather(payload, endpoint)
if response.status_code ==200:
    print(response.text) 
else:
    response = query_weather(payload, endpoint)

#TIDY THE LAYOUT BY JSON CONVERTION
def jsonify(response):
    json_response = response.json()
    return json_response


json_response = jsonify(response)
print("\n")
print(json_response)

print(json_response['coord']['lon'])

temp = json_response['coord']['lon']

#if temp <10:
#    start_boiler()
#else:
#    leave_it_off()