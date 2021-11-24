import requests

API_URL = 'https://cube-64e0d7d8-1a3d-4fec-82da-fa7afea9138e.api.my.faculty.ai'
API_KEY = 'i0cgsdYL3hpeOGkoGmA2TxzJ8LbbU1HpbkZo8B3kFG2bRKjx3V'

headers = {'UserAPI-Key': API_KEY}

response = requests.get('{}/files'.format(API_URL), headers=headers)

response.json()