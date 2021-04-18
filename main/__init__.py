from flask import Flask, Blueprint
from flask_restful import Api
from .routes import Base, Transactions, Blocks


api_bp = Blueprint('api', __name__)
api = Api(api_bp, prefix='/api/v1')

# Add Resources Here
api.add_resource(Base, '/')
api.add_resource(Blocks, '/blocks')
api.add_resource(Transactions, '/transactions')

def create_app():
    app = Flask(__name__)
    app.register_blueprint(api_bp)
    return app
    