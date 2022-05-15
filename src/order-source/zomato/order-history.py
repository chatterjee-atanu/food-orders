import requests
import yaml

#Read the configuration file
with open("order-source/zomato/config.yaml", 'r') as config_stream:
    config_data = yaml.safe_load(config_stream)

url = config_data['url']

querystring = {"page":"1"}

payload = ""

headers = {
    "cookie": config_data['browser']['cookie'],
    "User-Agent": config_data['browser']['user-agent']
}

response = requests.request("GET", url, data=payload, headers=headers, params=querystring)

print(response.text)
