import requests
from datetime import datetime

pixela_endpoint = "https://pixe.la/v1/users"

USERNAME = "quochung"
TOKEN = "lasjdflsdflkja;slkfjlqkwjer12341234"

user_params = {
    "token": "lasjdflsdflkja;slkfjlqkwjer12341234",
    "username": "quochung",
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_configs = {
    "id": "graph1",
    "name": "Research Work Graph",
    "unit": "Hour",
    "type": "int",
    "color": "sora"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(graph_endpoint, json=graph_configs, headers=headers)
# print(response.text)

post_to_graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{graph_configs['id']}"

today = datetime.now()

post_to_graph_configs = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("Good job boy. How many hours today? ")
}

# response = requests.post(post_to_graph_endpoint, json=post_to_graph_configs, headers=headers)
# print(response.text)

update_graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{graph_configs['id']}/{today.strftime('%Y%m%d')}"

update_graph_configs = {
    "quantity": "0"
}

# response = requests.put(update_graph_endpoint, json=update_graph_configs, headers=headers)
# print(response.text)

delete_graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{graph_configs['id']}/{today.strftime('%Y%m%d')}"

# response = requests.delete(delete_graph_endpoint, headers=headers)
# print(response.text)