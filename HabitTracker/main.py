import requests

user_params= {
    "token": "ABCDAFEGAHRHAGDFS", 
    "username": "maureendusing", 
    "agreeTermsofService": "yes", 
    "notMinor": "yes"
}
pixela_endpoint = "https://pixe.la/v1/users"
# response = requests.post(url=pixela_endpoint, json=user_params)
graph_endpoint = f"{pixela_endpoint}/{user_params['username']}/graphs"

graph_config = {
    "id": "reading",
    "name": "reading-graph",
    "unit": "pages",
    "type": "int",
    "color": "sora"
}

headers = {
    "X-USER-TOKEN": "ABCDAFEGAHRHAGDFS"
}

# response = requests.post(url= graph_endpoint, headers=headers, json=graph_config )

# # print(response.text)

# # requests.get(url="http://api.open-notify.org/iss-now.json", )

# print(response.text)

# graph = requests.get(url=f"{pixela_endpoint}/{user_params['username']}/graphs/{graph_config['id']}")
# print(graph.text)

body = {
    "date":"20240913",
    "quantity": "5",
}

graph_post=requests.post(url=f"{pixela_endpoint}/{user_params['username']}/graphs/{graph_config['id']}", headers=headers, json=body)
print(graph_post.text)