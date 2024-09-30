from locust import task, HttpUser


class User(HttpUser):
    post_id = None

    def on_start(self):
        body = {
            "name": "Apple MacBook Pro 16",
            "data": {
                "year": 2019,
                "price": 1849.99,
                "CPU model": "Intel Core i9",
                "Hard disk size": "1 TB"
            }
        }
        response = self.client.post("/objects", json=body)
        self.post_id = response.json()["id"]

    @task(1)
    def get_all_items_perf(self):
        self.client.get("/objects")

    @task(3)
    def get_one_item_perf(self):
        self.client.get(f"/objects/{self.post_id}")
