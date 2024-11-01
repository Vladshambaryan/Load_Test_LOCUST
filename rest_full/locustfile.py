from locust import task, HttpUser
import random


class Products(HttpUser):

    @task(1)
    def get_all_products_performance(self):
        self.client.get(
            "/objects",
            headers={"Content-Type": "application/json"}
        )

    @task(3)
    def get_one_product_performance(self):
        self.client.get(
            f"/objects/{random.choice([1, 2, 3, 4])}",
            headers={"Content-Type": "application/json"}
        )

    @task(1)
    def create_product_performance(self):
        self.client.post(
            "/objects",
            json={
                "name": "Apple MacBook Pro 16",
                "data": {
                    "year": 2019,
                    "price": 1849.99,
                    "CPU model": "Intel Core i9",
                    "Hard disk size": "1 TB"
                }
            },
            headers={"Content-Type": "application/json"}
        )

    @task(1)
    def update_one_product_performance(self):
        self.client.put(
            f"/objects/{random.choice([1, 2, 3, 4])}",
            json={
                "name": "Apple MacBook Pro 16",
                "data": {
                    "year": 2019,
                    "price": 2049.99,
                    "CPU model": "Intel Core i9",
                    "Hard disk size": "1 TB",
                    "color": "silver"
                }
            },
            headers={"Content-Type": "application/json"}
        )

    @task(1)
    def update_one_product_name_performance(self):
        self.client.patch(
            f"/objects/{random.choice([1, 2, 3, 4])}",
            json={"name": "Apple MacBook Pro 16 (Updated Name)"},
            headers={"Content-Type": "application/json"}
        )

    @task(1)
    def delete_product_performance(self):
        self.client.delete(
            f"/objects/{random.choice([1, 2, 3, 4])}",
            headers={"Content-Type": "application/json"}
        )

#  https://api.restful-api.dev