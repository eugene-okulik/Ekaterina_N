import pytest
from endpoints.create_item import CreateItem
from endpoints.update_item import UpdateItem
from endpoints.patch_item import PatchItem
from endpoints.get_item import GetItem
from endpoints.delete_item import DeleteItem


@pytest.fixture()
def create_item():
    return CreateItem()


@pytest.fixture()
def new_item(create_item, delete_item_info):
    payload = {
        "name": "Apple MacBook Pro 16",
        "data": {
            "year": 2019,
            "price": 1849.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB"
        }
    }
    create_item.create_new_item(payload)
    item_id = create_item.item_id
    yield item_id
    delete_item_info.delete_item(item_id)


@pytest.fixture()
def change_item():
    return UpdateItem()


@pytest.fixture()
def change_some_data():
    return PatchItem()


@pytest.fixture()
def show_item_info():
    return GetItem()


@pytest.fixture()
def delete_item_info():
    return DeleteItem()
