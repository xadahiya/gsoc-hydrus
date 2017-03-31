# Using http://www.markus-lanthaler.com/hydra/event-api/

# -*- coding: utf-8 -*-

from flask import Flask, jsonify, url_for, redirect, request
from flask_pymongo import PyMongo
from flask_restful import Api, Resource
from contexts import gen_entrypoint_context, gen_product_collection_context, gen_product_context
from jsonld_gen import gen_entrypoint, gen_vocab
import os

# MONGO_URL = os.environ.get('MONGO_URL')
# if not MONGO_URL:
    # MONGO_URL = "mongodb://localhost:27017/hydra";

app = Flask(__name__)
# app.config['MONGO_URI'] = MONGO_URL

# mongo = PyMongo(app)


def set_response_headers(resp, ct="application/ld+json", status_code=200):
    """ Sets the response headers
        Default : { Content-type:"JSON-LD", status_code:200}"""
    resp.status_code = status_code
    resp.headers['Content-type'] = ct
    return resp

##For now I am using dummy data, later on we can switch to dynamic data
def gen_products():
    return jsonify({
  "@context": "/coffeeshop-api/contexts/ProductCollection.jsonld",
  "@id": "/coffeeshop-api/products/",
  "@type": "ProductCollection",
  "members": [
    {
      "@id": "/coffeeshop-api/products/80",
      "@type": "http://schema.org/Product"
    },
    {
      "@id": "/coffeeshop-api/products/81",
      "@type": "http://schema.org/Product"
    },
    {
      "@id": "/coffeeshop-api/products/83",
      "@type": "http://schema.org/Product"
    },
    {
      "@id": "/coffeeshop-api/products/84",
      "@type": "http://schema.org/Product"
    },
    {
      "@id": "/coffeeshop-api/products/85",
      "@type": "http://schema.org/Products"
    },
    {
      "@id": "/coffeeshop-api/products/86",
      "@type": "http://schema.org/Product"
    },
    {
      "@id": "/coffeeshop-api/products/87",
      "@type": "http://schema.org/Product"
    }
  ]
}
)


class Index(Resource):
    """A link to main entry point of the Web API"""

    def get(self):
        return set_response_headers(gen_entrypoint())


class Vocab(Resource):
    """A general vocab for the API"""

    def get(self):
        return set_response_headers(gen_vocab())

class Product(Resource):
    """All operations related to products"""

    def get(self):
        return set_response_headers(gen_products)

    def post(self):
        pass

class EntryPointContext(Resource):
    """Handles entrpoint contexts"""

    def get(self):
        return set_response_headers(gen_entrypoint_context())

class ProductCollectionContext(Resource):
    """Handles Product collection Contexts"""

    def get(self):
        return set_response_headers(gen_product_collection_context())

class ProductContext(Resource):
    """ Handles Product contexts"""

    def get(self):
        return set_response_headers(gen_product_context())


api = Api(app)
api.add_resource(Index, "/coffeeshop-api/", endpoint="coffeeshop-api")
api.add_resource(Vocab, "/coffeeshop-api/vocab", endpoint="vocab")
api.add_resource(EntryPointContext, "/coffeeshop-api/contexts/EntryPoint.jsonld", endpoint="entry_point_context")
api.add_resource(ProductCollectionContext, "/coffeeshop-api/contexts/ProductCollection.jsonld", endpoint="product_collection_context")
api.add_resource(ProductContext, "/coffeeshop-api/contexts/Product.jsonld", endpoint="product_context")
# api.add_resource(Student, "/api", endpoint="students")
# api.add_resource(Student, "/api/<string:registration>",
#  endpoint="registration")
# api.add_resource(Student, "/api/department/<string:department>",
#  endpoint="department")

if __name__ == "__main__":
    app.run(debug=True)
