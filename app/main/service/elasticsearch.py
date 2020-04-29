from app.main.adapter import ElasticsearchAdapter
from app.main.vo import ElasticsearchDocVO
from app.main.util.enumeration import SentimentType


def get_random_sentiment_doc(index):
    query = {
        'function_score': {
            'query': {
                'term': {
                    ElasticsearchDocVO.SENTIMENT: {
                        'value': SentimentType.UNK.value
                    }
                }
            },
            'functions': [
                {
                    'random_score': {
                        'field': '_seq_no'
                    }
                }
            ]
        }
    }

    res = ElasticsearchAdapter().get_doc(
        index=index,
        query=query,
        size=1
    )

    return res


def update_sentiment_doc(index, elastic_id, sentiment):
    doc = {
        ElasticsearchDocVO.SENTIMENT: sentiment
    }

    res = ElasticsearchAdapter().update_doc(
        index=index,
        elastic_id=elastic_id,
        doc=doc
    )

    return res

