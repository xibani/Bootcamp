import requests
from datetime import datetime

# Pixela
USERNAME = "ander"
TOKEN = "kljdsh3e9asdfi3894"
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id": GRAPH_ID,
    "name": "Python days",
    "unit": "day",
    "type": "float",
    "color": "kuro"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response)


# Pixel creation
pixel_cration_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now()
# print(today.strftime("%Y%m%d"))

pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many PythonDays have you done? "),
}

response = requests.post(url=pixel_cration_endpoint, json=pixel_data, headers=headers)
print(response)


# Cambiar valor de 3.0 a 2.698745
pixel_modification_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

pixel_modification_data = {
    "quantity": "1.098745"
}

# response = requests.put(url=pixel_modification_endpoint, json=pixel_modification_data, headers=headers)
# print(response.text)


# Delete method
pixel_delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

# response = requests.delete(url=pixel_delete_endpoint, headers=headers)
# print(response.text)

