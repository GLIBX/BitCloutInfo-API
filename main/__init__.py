from flask import Flask, Blueprint
from flask_restful import Api
from .routes import Base, Transactions, Blocks, ExchangeRate


api_bp = Blueprint('api', __name__)
api = Api(api_bp, prefix='/api/v1')

# Add Resources Here
api.add_resource(Base, '/')
api.add_resource(Blocks, '/block')
api.add_resource(Transactions, '/transaction-info')
api.add_resource(ExchangeRate, '/exchange-rate')

def create_app():
    app = Flask(__name__)
    app.register_blueprint(api_bp)
    return app
    