import os
from flask import make_response, request
from flask_restful import Resource
import cloudscraper
import json

scraper = cloudscraper.create_scraper()


class Base(Resource):
    def get(self):
        res = scraper.get('https://api.bitcloutbarbies.com/api/v1').text
        response = json.loads(res)
        return make_response(response)


class AppState(Resource):
    def post(self):
        payload = request.get_json()
        res = scraper.post(
            'https://api.bitcloutbarbies.com/get-app-state', json=payload)

        response = json.loads(res.text)
        return make_response(response)


class ExchangeRate(Resource):
    def get(self):
        res = scraper.get('https://api.bitcloutbarbies.com/get-exchange-rate')

        response = json.loads(res.text)
        return make_response(response)


class Follows(Resource):
    def post(self):
        payload = request.get_json()
        res = scraper.post('https://api.bitcloutbarbies.com/get-follows-stateless', json=payload)

        response = json.loads(res.text)
        return make_response(response)   

class Messages(Resource):
    def post(self):
        payload = request.get_json()
        res = scraper.post('https://api.bitcloutbarbies.com/get-messages-stateless', json=payload)

        response = json.loads(res.text)
        return make_response(response) 


class Notifications(Resource):
    def post(self):
        payload = request.get_json()
        res = scraper.post('https://api.bitcloutbarbies.com/get-notifications', json=payload)

        response = json.loads(res.text)
        return make_response(response)  

class Posts(Resource):
    def post(self):
        payload = request.get_json()
        res = scraper.post('https://api.bitcloutbarbies.com/get-posts-stateless', json=payload)

        response = json.loads(res.text)
        return make_response(response)


class Profiles(Resource):
    def post(self):
        payload = request.get_json()
        res = scraper.post('https://api.bitcloutbarbies.com/get-profiles', json=payload)

        response = json.loads(res.text)
        return make_response(response)


class Users(Resource):
    def post(self):
        payload = request.get_json()
        res = scraper.post('https://api.bitcloutbarbies.com/get-users-stateless', json=payload)

        response = json.loads(res.text)
        return make_response(response)


class Transactions(Resource):
    def post(self):
        payload = request.get_json()

        # obj = {
        #     'PublicKeyBase58Check': '',
        #     'IsMempool': True
        # }
        res = scraper.post('https://api.bitcloutbarbies.com/api/v1/transaction-info', json=payload)

        response = json.loads(res.text)
        return make_response(response)


class Blocks(Resource):
    def post(self):
        payload = request.get_json()

        # obj = {
        #     'PublicKeyBase58Check': '',
        #     'IsMempool': True
        # }
        res = scraper.post('https://api.bitcloutbarbies.com/api/v1/block', json=payload)

        if res.status_code != 200:
            response = {
                'message': "An error occured"
            }
            return make_response(response, res.status_code)
        else:
            response = json.loads(res.text)
            return make_response(response)



class VerifiedUsers(Resource):
    def post(self):
        payload = request.get_json()
        res = scraper.post('https://api.bitcloutbarbies.com/admin/get-verified-users', json=payload)

        if res.status_code != 200:
            response = {
                'message': "An error occured"
            }
            return make_response(response, res.status_code)
        else:
            response = json.loads(res.text)
            return make_response(response)



class BitcloutPrice(Resource):
    def get(self):
        res = scraper.get("https://api.cloutcompare.com/bitclout/price")
        
        if res.status_code != 200:
            response = {
                'message': "An error occured"
            }
            return make_response(response, res.status_code)
        else:
            data = json.loads(res.text)
            price = data['data']['bitclout_price']['bitclout_bitcoin_exchange_rate'] * data['data']['bitclout_price']['bitcoin_usd_exchange_rate']

            response = {
                'bitclout_price': float(price)
            }
            return make_response(response)