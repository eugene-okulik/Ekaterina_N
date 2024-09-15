import requests
import allure
from endpoints.base_checks import Base


class DeleteItem(Base):

    @allure.step("Delete item")
    def delete_item(self, item_id):
        self.response = requests.delete(f"{self.url}/{item_id}")

    @allure.step("Check message after delete")
    def check_delete_message(self, item_id):
        assert self.response.json()["message"] == f"Object with id = {item_id} has been deleted.", \
            "Incorrect message"
