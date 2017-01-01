from common import esClient
import random


def get_user_by_id(user_id):
    req = {
        "query": {
            "match": {
                "user_id": user_id
            }
        }
    }
    return esClient.search(req)


def add_user(user):
    return esClient.add(random.randint(1, 10000000), 'user', user)
