from datetime import datetime
from elasticsearch import Elasticsearch
from elasticsearch import helpers

es = Elasticsearch()


def bulk(elasticSearchObject, index, type,jsonData)
    data = [
      {
        "_index": str(index),
        "_type": str(type),
        "_id": j,
        "_source": jsonData[j]
      for j in range(0, len(jsonData))
    ]
    helpers.bulk(elasticSearchObject, data)




es = Elasticsearch()
es.indices.create(index='my-index', ignore=400)
# {'index': 'my-index', 'acknowledged': True, 'shards_acknowledged': True}
es.index(index="my-index", doc_type="test-type", id=42, body={"any": "data", "timestamp": datetime.now()})
# {'_id': '42', '_primary_term': 1, 'result': 'created', '_type': 'test-type', '_seq_no': 0, '_index': 'my-index', '_version': 1, '_shards': {'failed': 0, 'total': 2, 'successful': 1}}
es.get(index="my-index", doc_type="test-type", id=42)['_source']
# {'any': 'data', 'timestamp': '2018-06-25T18:43:29.626240'}
