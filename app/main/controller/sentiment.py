from flask import Blueprint
from flask import request

from app.main.service import elasticsearch as es_service
from app.main.util.serializer import GetSerializer
from app.main.util.serializer import UpdateSerializer
from app.main.util.decorator import validate_input


sentiment = Blueprint('sentiment', __name__)


@sentiment.route('/random', methods=['GET'])
def get_random():
    doc = es_service.get_random_sentiment_doc(index='test')

    res = GetSerializer().serialize(doc)

    return res, 200


@sentiment.route('/', methods=['PATCH'])
@validate_input
def update():
    payload = request.get_json()

    elastic_id = payload['id']
    sentiment = payload['sentiment']

    doc = es_service.update_sentiment_doc(
        index='test',
        elastic_id=elastic_id,
        sentiment=sentiment
    )

    res = UpdateSerializer().serialize(doc)

    return res, 200

