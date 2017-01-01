from common import esClient


def get_user_by_id(user_id):
    req = {
        "query": {
            "match": {
                "user_id": user_id
            }
        }
    }
    return esClient.search(req)
