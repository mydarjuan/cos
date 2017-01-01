from elasticsearch import Elasticsearch

esClient = Elasticsearch([{'host': 'localhost', 'port': 9200}])


def search(req):
    return esClient.search(index='djshop', body=req)


def add(doc_id, doc_type, req):
    return esClient.index(index='djshop', doc_type=doc_type, body=req, id=doc_id)
