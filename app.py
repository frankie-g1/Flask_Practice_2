from flask import Flask, request
from flask_restful import Resource, Api


app = Flask(__name__)
api = Api(app)

items = []

class ItemList(Resource):
    def get(self):
        return {'Items ': items}


class Item(Resource):
    def get(self, name):
        for item in items:
            if name == item['name']:
                return item
        return {'Item': None}, 404

    def post(self, name):
        request_data = request.get_json(silent=True)
        new_item = {
            'name': name,
            'price': request_data['price']
        }
        items.append(new_item)
        return new_item


api.add_resource(Item, '/item/<string:name>')  # Access students like so http:/127.0.0.1:5000/student/Rolf
api.add_resource(ItemList, '/items')

app.run(port=5000, debug = True)
