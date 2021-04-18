import os
from flask import make_response
from flask_restful import Resource
import cloudscraper
import json

scraper = cloudscraper.create_scraper()


class Base(Resource):
    def get(self):
        res = scraper.get('https://api.bitclout.com/api/v1').text
        response = json.loads(res)
        return make_response(response)


class Transactions(Resource):
    def get(self):
        obj = {
            'PublicKeyBase58Check': '',
            'IsMempool': True
        }
        res = scraper.post(
            'https://api.bitclout.com/api/v1/transaction-info', json=obj).text

        response = json.loads(res)
        return make_response(response)


class Blocks(Resource):
    def get(self):
        obj = {
            'PublicKeyBase58Check': '',
            'IsMempool': True
        }
        res = scraper.post('https://api.bitclout.com/api/v1/block', json=obj).text

        response = json.loads(res)
        return make_response(response)
