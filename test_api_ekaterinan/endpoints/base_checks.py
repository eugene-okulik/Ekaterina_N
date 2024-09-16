import allure


class Base:
    url = "https://api.restful-api.dev/objects"
    response = None
    json = None

    @allure.step("Check response status is 200")
    def response_status_200(self):
        assert self.response.status_code == 200, "Status code is incorrect"

    @allure.step("Check item's data")
    def check_items_data(self, payload):
        assert self.response.json()["name"] == payload["name"], "Name is incorrect"
        assert self.response.json()["data"]["year"] == payload["data"]["year"], "Year is incorrect"
        assert self.response.json()["data"]["price"] == payload["data"]["price"], "Price is incorrect"
        assert self.response.json()["data"]["CPU model"] == payload["data"]["CPU model"], "CPU model is incorrect"
        assert self.response.json()["data"]["Hard disk size"] == payload["data"]["Hard disk size"], \
            "Hard disk size is incorrect"
        assert self.response.json()["id"] is not None, "ID is incorrect"

    @allure.step("Get item ID")
    def item_id(self):
        item_id = self.response.json()["id"]
        return item_id
