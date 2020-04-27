from flask import jsonify
from werkzeug.exceptions import NotFound

from app.main.vo import ElasticsearchDocVO


class GetSerializer:

    @staticmethod
    def serialize(doc):
        try:
            item = doc['hits']['hits'][0]
        except IndexError:
            raise NotFound()

        res = {
            'id': item['_id'],
            'content': item['_source'][ElasticsearchDocVO.CONTENT]
        }

        return jsonify(res)


class UpdateSerializer:

    @staticmethod
    def serialize(doc):
        res = {
            'id': doc['_id'],
            'result': doc['result']
        }

        return jsonify(res)

