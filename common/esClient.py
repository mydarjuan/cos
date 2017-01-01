from elasticsearch import Elasticsearch
esClient = Elasticsearch([{'host': 'localhost', 'port': 9200}])


def search(req):
    return esClient.search(index='djshop', body=req);