import os
from flask import make_response, request
from flask_restful import Resource
import cloudscraper
import json

scraper = cloudscraper.create_scraper()


class Base(Resource):
    def get(self):
        res = scraper.get('https://api.bitclout.com/api/v1').text
        response = json.loads(res)
        return make_response(response)

class ExchangeRate(Resource):
    def get(self):
        res = scraper.get('https://api.bitclout.com/api/v1/creators')

        if res.status_code == 404:
            return res.text
        else:
            response = json.loads(res.text)
            return make_response(response)

    def post(self):
        payload = request.get_json()

        res = scraper.post('https://api.bitclout.com/api/v1/get-profiles', json=payload)

        if res.status_code == 404:
            return res.text
        else:
            response = json.loads(res.text)
            return make_response(response)
class Transactions(Resource):
    def post(self):
        payload = request.get_json()

        # obj = {
        #     'PublicKeyBase58Check': '',
        #     'IsMempool': True
        # }
        res = scraper.post('https://api.bitclout.com/api/v1/transaction-info', json=payload).text

        response = json.loads(res)
        return make_response(response)


class Blocks(Resource):
    def post(self):
        payload = request.get_json()

        # obj = {
        #     'PublicKeyBase58Check': '',
        #     'IsMempool': True
        # }
        res = scraper.post('https://api.bitclout.com/api/v1/block', json=payload).text

        response = json.loads(res)
        return make_response(response)