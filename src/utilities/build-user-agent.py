
def get_user_agents():
    
    import requests

    reqUrl = "https://jnrbsn.github.io/user-agents/user-agents.json"

    response = requests.request("GET", reqUrl)

    user_agents = response.json()

    return user_agents