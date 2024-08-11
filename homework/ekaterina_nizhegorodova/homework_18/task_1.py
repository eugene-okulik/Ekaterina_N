import requests


def new_item():
    body = {
        "name": "Apple MacBook Pro 16",
        "data": {
            "year": 2019,
            "price": 1849.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB"
        }
    }
    response = requests.post("https://api.restful-api.dev/objects", json=body)
    return response.json()["id"]


def clear_item(post_id):
    response = requests.delete(f"https://api.restful-api.dev/objects/{post_id}")
    return response.json()


def post_item():
    body = {
        "name": "Apple MacBook Pro 16",
        "data": {
            "year": 2019,
            "price": 1849.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB"
        }
    }
    response = requests.post("https://api.restful-api.dev/objects", json=body)
    assert response.status_code == 200, "Status code is incorrect"
    assert response.json()["name"] == "Apple MacBook Pro 16", "Name is incorrect"
    assert response.json()["data"]["year"] == 2019, "Year is incorrect"
    assert response.json()["data"]["price"] == 1849.99, "Price is incorrect"
    assert response.json()["data"]["CPU model"] == "Intel Core i9", "CPU model is incorrect"
    assert response.json()["data"]["Hard disk size"] == "1 TB", "Hard disk size is incorrect"
    assert response.json()["id"] is not None, "ID is incorrect"
    item_id = response.json()["id"]
    clear_item(item_id)


def get_single_item():
    item_id = new_item()
    response = requests.get(f"https://api.restful-api.dev/objects/{item_id}")
    assert response.status_code == 200, "Status code is incorrect"
    assert response.json()["name"] == "Apple MacBook Pro 16", "Name is incorrect"
    assert response.json()["data"]["year"] == 2019, "Year is incorrect"
    assert response.json()["data"]["price"] == 1849.99, "Price is incorrect"
    assert response.json()["data"]["CPU model"] == "Intel Core i9", "CPU model is incorrect"
    assert response.json()["data"]["Hard disk size"] == "1 TB", "Hard disk size is incorrect"
    assert response.json()["id"] == item_id, "ID is incorrect"
    clear_item(item_id)


def get_items_by_ids():
    item_id1 = new_item()
    item_id2 = new_item()
    item_id3 = new_item()
    response = requests.get(
        "https://api.restful-api.dev/objects",
        params={"id": [item_id1, item_id2, item_id3]}
    )
    assert response.status_code == 200, "Status code is incorrect"
    assert response.json()[0]["id"] == item_id1, "Item 1 ID is incorrect"
    assert response.json()[1]["id"] == item_id2, "Item 2 ID is incorrect"
    assert response.json()[2]["id"] == item_id3, "Item 3 ID is incorrect"
    clear_item(item_id1)
    clear_item(item_id2)
    clear_item(item_id3)


def get_all_items():
    response = requests.get("https://api.restful-api.dev/objects")
    assert response.status_code == 200, "Status code is incorrect"
    assert type(response.json()) == list, "Response does not contain the items' list"


def update_item():
    new_data = {
        "name": "Lenovo Yoga 82YR0009US 13.3",
        "data": {
            "year": 2020,
            "price": 867.70,
            "CPU model": "AMD Ryzen 5 7530U",
            "Hard disk size": "256 GB"
        }
    }
    item_id = new_item()
    response = requests.put(f"https://api.restful-api.dev/objects/{item_id}", json=new_data)
    assert response.status_code == 200, "Status code is incorrect"
    assert response.json()["name"] == "Lenovo Yoga 82YR0009US 13.3", "Name is incorrect"
    assert response.json()["data"]["year"] == 2020, "Year is incorrect"
    assert response.json()["data"]["price"] == 867.70, "Price is incorrect"
    assert response.json()["data"]["CPU model"] == "AMD Ryzen 5 7530U"
    assert response.json()["data"]["Hard disk size"] == "256 GB", "Hard disk size is incorrect"
    assert response.json()["id"] == item_id, "ID is incorrect"
    clear_item(item_id)


def patch_item():
    data = {
        "data": {
            "year": 2020,
            "price": 867.70,
        }
    }
    item_id = new_item()
    response = requests.patch(f"https://api.restful-api.dev/objects/{item_id}", json=data)
    assert response.status_code == 200, "Status code is incorrect"
    assert response.json()["data"]["year"] == 2020, "Year is incorrect"
    assert response.json()["data"]["price"] == 867.70, "Price is incorrect"
    clear_item(item_id)


def delete_item():
    item_id = new_item()
    response = requests.delete(f"https://api.restful-api.dev/objects/{item_id}")
    assert response.status_code == 200, "Status code is incorrect"
    assert response.json()["message"] == "Object with id = 6, has been deleted.", "Incorrect message"
