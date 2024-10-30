from locust import task, HttpUser
import random


class MemeUser(HttpUser):
    token = None

    def on_start(self):
        response = self.client.post(
            '/authorize',
            json={'name': 'vlad'}
        )
        self.token = response.json()['token']

    @task(1)
    def get_all_memes_performance(self):
        self.client.get(
            '/meme',
            headers={'Authorization': self.token}
        )

    @task(1)
    def get_one_meme_performance(self):
        self.client.get(
            f'/meme/{random.choice([21, 29, 44, 50])}',
            headers={'Authorization': self.token}
        )

    @task(4)
    def post_meme_performance(self):
        self.client.post(
            '/meme',
            json={
                "id": 23,
                "text": "wolf",
                "url": "https://static.independent.co.uk/s3fs-public/thumbnails/image/2010/07/01/16/405231.jpg",
                "tags": ["red - blu", "black - gold"],
                "info": {"44": ["55", "33", "65"]}
            },
            headers = {'Authorization': self.token}
        )

    @task(1)
    def put_meme_performance(self):
        self.client.put(f'/meme/{random.choice([21, 29, 44, 50])}',
            json={
                "id": 10,
                "text": "big shrek",
                "url": "https://static.independent.co.uk/s3fs-public/thumbnails/image/2010/07/01/16/405231.jpg",
                "tags": ["updated", "meme"],
                "info": {"author": "Miqael"}
            },
            headers={'Authorization': self.token}
        )

    @task(1)
    def delete_product_performance(self):
        self.client.delete(f'/meme/{random.choice([21, 29, 44, 50])}',
            headers={'Authorization': self.token}
        )

    #  http://167.172.172.115:523
    #  55