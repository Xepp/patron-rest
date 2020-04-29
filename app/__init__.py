import os
from dotenv import load_dotenv
from werkzeug.exceptions import HTTPException
from elasticsearch.exceptions import TransportError

from app.main import create_app
from app.main.controller.sentiment import sentiment


load_dotenv()

app = create_app(os.getenv('ENV') or 'dev')


@app.errorhandler(HTTPException)
def http_exception(error):
    return error.get_response()


@app.errorhandler(TransportError)
def transport_error(error):
    return error.error, error.status_code


app.register_blueprint(sentiment, url_prefix='/api/sentiment')

