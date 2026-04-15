import requests
from schemas.post_schema import Post

BASE_URL = "https://jsonplaceholder.typicode.com"

def test_schema_validation():
    response = requests.get(f"{BASE_URL}/posts")
    data = response.json()

    for item in data:
        Post(**item)
