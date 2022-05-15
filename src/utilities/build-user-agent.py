import requests

reqUrl = "https://jnrbsn.github.io/user-agents/user-agents.json"

response = requests.request("GET", reqUrl)

print(response.text)