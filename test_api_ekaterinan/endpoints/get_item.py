import requests
import allure
from endpoints.base_checks import Base


class GetItem(Base):

    @allure.title("View item info")
    def get_item(self, item_id):
        self.response = requests.get(f"{self.url}/{item_id}")
        return self.response

    @allure.title("View all items' info")
    def get_all_items(self):
        self.response = requests.get(f"{self.url}")
        return self.response

    @allure.title("Check list of items is returned")
    def check_items_list(self):
        assert type(self.response.json()) == list, "Response does not contain the items' list"

    @allure.title("View several items' info")
    def get_items_by_ids(self, params):
        self.response = requests.get(f"{self.url}", params=params)
        return self.response
