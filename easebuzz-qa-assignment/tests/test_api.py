import requests
import time

BASE_URL = "https://jsonplaceholder.typicode.com"

def test_response_time():
    start = time.time()
    response = requests.get(f"{BASE_URL}/posts")
    end = time.time()

    assert response.status_code == 200
    assert (end - start) < 2
