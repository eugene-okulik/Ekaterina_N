import pytest
import requests


@pytest.fixture(scope="session")
def start_complete():
    print("Start testing")
    yield
    print("Testing completed")


@pytest.fixture()
def before_after():
    print("before test")
    yield
    print("after test")


@pytest.fixture()
def new_item_data():
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
    post_id = response.json()["id"]
    print(f"Item has been created with id = {post_id}")
    yield response.json()
    requests.delete(f"https://api.restful-api.dev/objects/{post_id}")
    print(f"Item with id = {post_id} has been deleted")


@pytest.mark.critical
@pytest.mark.parametrize("body", [
    {
            "name": "Apple MacBook Pro 16",
            "data": {
                "year": 2019,
                "price": 1849.99,
                "CPU model": "Intel Core i9",
                "Hard disk size": "1 TB"
            }
        },
    {
            "name": "Lenovo Yoga 82YR0009US 13.3",
            "data": {
                "year": 2020,
                "price": 867.70,
                "CPU model": "AMD Ryzen 5 7530U",
                "Hard disk size": "256 GB"
            }
        },
    {
            "name": "ASUS Vivobook 16X",
            "data": {
                "year": 2023,
                "price": 2350.00,
                "CPU model": "AMD Ryzen 7 7730U",
                "Hard disk size": "512 GB"
            }
        }

])
def test_post_item(start_complete, before_after, body):
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
    assert response.json()["name"] == body["name"], "Name is incorrect"
    assert response.json()["data"]["year"] == body["data"]["year"], "Year is incorrect"
    assert response.json()["data"]["price"] == body["data"]["price"], "Price is incorrect"
    assert response.json()["data"]["CPU model"] == body["data"]["CPU model"], "CPU model is incorrect"
    assert response.json()["data"]["Hard disk size"] == body["data"]["Hard disk size"], "Hard disk size is incorrect"
    assert response.json()["id"] is not None, "ID is incorrect"
    post_id = response.json()["id"]
    requests.delete(f"https://api.restful-api.dev/objects/{post_id}")


@pytest.mark.medium
def test_get_single_item(before_after, new_item_data):
    response = requests.get(f"https://api.restful-api.dev/objects/{new_item_data["id"]}")
    assert response.status_code == 200, "Status code is incorrect"
    assert response.json()["name"] == new_item_data["name"], "Name is incorrect"
    assert response.json()["data"]["year"] == new_item_data["data"]["year"], "Year is incorrect"
    assert response.json()["data"]["price"] == new_item_data["data"]["price"], "Price is incorrect"
    assert response.json()["data"]["CPU model"] == new_item_data["data"]["CPU model"], "CPU model is incorrect"
    assert response.json()["data"]["Hard disk size"] == new_item_data["data"]["Hard disk size"], \
        "Hard disk size is incorrect"
    assert response.json()["id"] == new_item_data["id"], "ID is incorrect"


def test_get_items_by_ids(before_after, new_item_data):
    item_id1 = new_item_data["id"]
    item_id2 = new_item_data["id"]
    item_id3 = new_item_data["id"]
    response = requests.get(
        "https://api.restful-api.dev/objects",
        params={"id": [item_id1, item_id2, item_id3]}
    )
    assert response.status_code == 200, "Status code is incorrect"
    assert response.json()[0]["id"] == item_id1, "Item 1 ID is incorrect"
    assert response.json()[1]["id"] == item_id2, "Item 2 ID is incorrect"
    assert response.json()[2]["id"] == item_id3, "Item 3 ID is incorrect"


def test_get_all_items(before_after):
    response = requests.get("https://api.restful-api.dev/objects")
    assert response.status_code == 200, "Status code is incorrect"
    assert type(response.json()) == list, "Response does not contain the items' list"


def test_update_item(before_after, new_item_data):
    new_data = {
        "name": "Lenovo Yoga 82YR0009US 13.3",
        "data": {
            "year": 2020,
            "price": 867.70,
            "CPU model": "AMD Ryzen 5 7530U",
            "Hard disk size": "256 GB"
        }
    }
    response = requests.put(f"https://api.restful-api.dev/objects/{new_item_data["id"]}", json=new_data)
    assert response.status_code == 200, "Status code is incorrect"
    assert response.json()["name"] == new_data["name"], "Name is incorrect"
    assert response.json()["data"]["year"] == new_data["data"]["year"], "Year is incorrect"
    assert response.json()["data"]["price"] == new_data["data"]["price"], "Price is incorrect"
    assert response.json()["data"]["CPU model"] == new_data["data"]["CPU model"], "CPU model is incorrect"
    assert response.json()["data"]["Hard disk size"] == new_data["data"]["Hard disk size"], \
        "Hard disk size is incorrect"
    assert response.json()["id"] == new_item_data["id"], "ID is incorrect"


def test_patch_item(before_after, new_item_data):
    data = {
        "data": {
            "year": 2020,
            "price": 867.70,
        }
    }
    response = requests.patch(f"https://api.restful-api.dev/objects/{new_item_data["id"]}", json=data)
    assert response.status_code == 200, "Status code is incorrect"
    assert response.json()["data"]["year"] == data["data"]["year"], "Year is incorrect"
    assert response.json()["data"]["price"] == data["data"]["price"], "Price is incorrect"


def test_delete_item(before_after, new_item_data):
    response = requests.delete(f"https://api.restful-api.dev/objects/{new_item_data["id"]}")
    assert response.status_code == 200, "Status code is incorrect"
    assert response.json()["message"] == f"Object with id = {new_item_data["id"]} has been deleted.", \
        "Incorrect message"
