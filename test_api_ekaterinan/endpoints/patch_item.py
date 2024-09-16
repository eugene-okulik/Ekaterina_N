import requests
import allure
from endpoints.base_checks import Base


class PatchItem(Base):
    payload = None

    @allure.step("Patch item")
    def patch_item(self, item_id, new_payload):
        self.response = requests.patch(f"{self.url}/{item_id}", json=new_payload)
        return self.response

    @allure.step("Check some item's data")
    def check_some_items_data(self, payload):
        assert self.response.json()["data"]["year"] == payload["data"]["year"], "Year is incorrect"
        assert self.response.json()["data"]["price"] == payload["data"]["price"], "Price is incorrect"
