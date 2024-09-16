import requests
import allure
from endpoints.base_checks import Base


class UpdateItem(Base):

    @allure.step("Update item")
    def update_item(self, item_id, new_payload):
        self.response = requests.put(f"{self.url}/{item_id}", json=new_payload)
        return self.response
