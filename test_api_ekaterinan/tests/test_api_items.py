import pytest


TEST_DATA = [
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
]


@pytest.mark.parametrize("payload", TEST_DATA)
def test_post_items(create_item, delete_item_info, payload):
    create_item.create_new_item(payload)
    create_item.response_status_200()
    create_item.check_items_data(payload)
    delete_item_info.delete_item(create_item.item_id())


def test_update_item(new_item, change_item):
    new_payload = {
        "name": "Lenovo Yoga 82YR0009US 13.3",
        "data": {
            "year": 2020,
            "price": 867.70,
            "CPU model": "AMD Ryzen 5 7530U",
            "Hard disk size": "256 GB"
        }
    }
    change_item.update_item(new_item(), new_payload)
    change_item.response_status_200()
    change_item.check_items_data(new_payload)


def test_patch_item(new_item, change_some_data):
    new_payload = {
        "data": {
            "year": 2020,
            "price": 867.70,
        }
    }
    change_some_data.patch_item(new_item(), new_payload)
    change_some_data.response_status_200()
    change_some_data.check_some_items_data(new_payload)


def test_get_single_item(new_item, show_item_info):
    payload = {
        "name": "Apple MacBook Pro 16",
        "data": {
            "year": 2019,
            "price": 1849.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB"
        }
    }
    show_item_info.get_item(new_item())
    show_item_info.response_status_200()
    show_item_info.check_items_data(payload)


def test_get_all_items(show_item_info):
    show_item_info.get_all_items()
    show_item_info.response_status_200()
    show_item_info.check_items_list()


def test_get_items_by_ids(new_item, show_item_info):
    item_id1 = new_item()
    item_id2 = new_item()
    params = {"id": [item_id1, item_id2]}
    show_item_info.get_items_by_ids(params)
    show_item_info.response_status_200()
    show_item_info.check_items_list()


def test_delete_item(new_item, delete_item_info):
    delete_item_info.delete_item(new_item())
    delete_item_info.response_status_200()
    delete_item_info.check_delete_message(new_item())
