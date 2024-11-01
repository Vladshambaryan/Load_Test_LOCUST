from locust import task, HttpUser
import random

class FakeStore(HttpUser):

    @task(1)
    def get_all_products_performance(self):
        self.client.get(
            '/products',
            headers = {'Accept': 'application/json'}
        )

    @task(1)
    def get_one_product_performance(self):
        self.client.get(
            f'/products/{random.choice([21, 29, 44, 50])}',
            headers = {'Accept': 'application/json'}
        )

    @task(1)
    def post_product_performance(self):
        self.client.post(
            '/products',
            json={
                "title": "test product",
                "price": 13.5,
                "description": "lorem ipsum set",
                "image": "https: //i.pravatar.cc",
                "category": "electronic"
            },
            headers={'Accept': 'application/json'}
        )


    @task(1)
    def put_product_performance(self):
        self.client.put(
            f'/products/{random.choice([21, 29, 44, 50])}',
            json={
                "title": "new product",
                "price": 103.5,
                "description": "lorem set",
                "image": "https: google.com",
                "category": "electronic 777"
            },
            headers={'Accept': 'application/json'}
        )

    @task(1)
    def patch_product_performance(self):
        self.client.patch(
            f'/products/{random.choice([21, 29, 44, 50])}',
            json={
                "title": "new product",
                "price": 10000.5,
                "description": "lorem set",
                "image": "https: google.com",
                "category": "electronic 55555"
            },
            headers={'Accept': 'application/json'}
        )

    @task(1)
    def delete_product_performance(self):
        self.client.delete(
            f'/products/{random.choice([21, 29, 44, 50])}',
            headers={'Accept': 'application/json'}
        )


#  url = 'https://fakestoreapi.com'

