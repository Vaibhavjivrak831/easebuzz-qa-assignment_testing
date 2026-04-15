import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

def get_posts():
    response = requests.get(f"{BASE_URL}/posts")
    return response
