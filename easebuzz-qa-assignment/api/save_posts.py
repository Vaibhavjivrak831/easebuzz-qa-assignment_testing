import json
from api.client import get_posts

def save_first_five_posts():
    response = get_posts()

    assert response.status_code == 200
    data = response.json()

    for post in data:
        assert all(key in post for key in ["userId", "id", "title", "body"])

    with open("first_5_posts.json", "w") as f:
        json.dump(data[:5], f, indent=4)

if __name__ == "__main__":
    save_first_five_posts()
