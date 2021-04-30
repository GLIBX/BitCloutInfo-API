from flask import Flask, Blueprint
from flask_restful import Api
from .routes import *
from flask_cors import CORS


api_bp = Blueprint('api', __name__)
api = Api(api_bp, prefix='/api/v1')

# Add Resources Here
api.add_resource(Base, '/')
api.add_resource(Blocks, '/get-block')
api.add_resource(ExchangeRate, '/get-exchange-rate') #GET 
api.add_resource(AppState, '/get-app-state')
api.add_resource(Follows, '/get-follows')
api.add_resource(Messages, '/get-messages')
api.add_resource(Notifications, '/get-notifications')
api.add_resource(Posts, '/get-posts')
api.add_resource(Profiles, '/get-profiles')
api.add_resource(Users, '/get-users')
api.add_resource(Transactions, '/get-transactions')


def create_app():
    app = Flask(__name__)
    cors = CORS(app)
    app.register_blueprint(api_bp)
    return app
    