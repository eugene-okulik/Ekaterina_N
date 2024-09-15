import requests
import allure
from endpoints.base_checks import Base


class CreateItem(Base):

    @allure.step("Create new item")
    def create_new_item(self, payload):
        self.response = requests.post(self.url, json=payload)
        return self.response
