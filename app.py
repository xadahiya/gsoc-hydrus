# Using https://www.w3.org/community/hydra/wiki/Restbucks_with_Hydra as
# data source

# -*- coding: utf-8 -*-

from flask import Flask, jsonify, url_for, redirect, request
from flask_pymongo import PyMongo
from flask_restful import Api, Resource
import os

# MONGO_URL = os.environ.get('MONGO_URL')
# if not MONGO_URL:
# MONGO_URL = "mongodb://localhost:27017/hydra";

app = Flask(__name__)
# app.config['MONGO_URI'] = MONGO_URL

# mongo = PyMongo(app)


def set_response_headers(resp, ct="application/ld+json", status_code=200):
    """ Sets the response headers
        Default : { Content-type:"ld+json", status_code:200}"""
    resp.status_code = status_code
    resp.headers['Content-type'] = ct
    return resp


def gen_initial_context():
    return jsonify({

        "@type": "CafeOrCoffeeShop",
        "_id": "/",
        "name": "Kaffeehaus Hagen",
        "makesOffer": [
            {
                "@type": "Offer",
                "_id": "/offers/1234",
                "itemOffered": {
                    "@type": "pto:Latte_macchiato",
                    "_id": "/products/latte-1",
                    "productID": "latte-1",
                    "name": "Latte Macchiato",
                    "hydra:collection": [
                        {
                            "@type": "hydra:Collection",
                            "_id": "/orders",
                            "hydra:manages": {
                                "hydra:property": "orderedItem",
                                "hydra:subject": {"@type": "Order"}
                            },
                            "hydra:operation": {
                                "hydra:method": "POST",
                                "hydra:expects": {
                                    "hydra:supportedProperty": [
                                        {
                                            "@type": "PropertyValueSpecification",
                                            "hydra:property": "productID",
                                            "hydra:required": "true",
                                            "defaultValue": "latte-1",
                                            "readOnlyValue": "true"
                                        }
                                    ]
                                }
                            }
                        }
                    ]
                },
                "price": 2.8,
                "priceCurrency": "EUR"
            }
        ],
        "@context": {
            "@vocab": "/vocab#",
            "@base": "/",
            "hydra": "http://www.w3.org/ns/hydra/core#",
            "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
            "xsd": "http://www.w3.org/2001/XMLSchema#",
            "createdAt": {
                "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
            },
            "_id": "@id"
        }
    }
    )


def gen_vocab():
    return jsonify({
        {
            "@type": "hydra:ApiDocumentation",
            "hydra:entrypoint": "/",
            "hydra:supportedClass": [
                {
                    "_id": "vocab#Entrypoint",
                    "@type": "hydra:Class",
                    "hydra:description": "The main entry point of the API",
                    "hydra:supportedOperation": {
                        "@type": "hydra:Operation",
                        "hydra:description": "The APIs main entry point.",
                        "hydra:method": "GET",
                        "hydra:returns": {
                            "_id": "vocab#EntryPoint"
                        }
                    },
                    "hydra:supportedProperty": [],
                    "hydra:title": "EntryPoint"
                },
            ],
            "lvz:entrypointClass": "/vocab#EntryPoint",
            "@context": {
                "@vocab": "/vocab#",
                "@base": "/",
                "hydra": "http://www.w3.org/ns/hydra/core#",
                "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
                "xsd": "http://www.w3.org/2001/XMLSchema#",
                "createdAt": {
                    "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
                },
                "_id": "@id"
            }
        }
    })


class Index(Resource):
    """A link to main entry point of the Web API"""

    def get(self):
        return set_response_headers(gen_initial_context())

class Vocab(Resource):
    """ A generalized vocab for API"""

    def get(self):
        return set_response_headers(gen_vocab())

api = Api(app)
api.add_resource(Index, "/", endpoint="index")
api.add_resource(Vocab, "/vocab#", endpoint="vocab")
# api.add_resource(Student, "/api", endpoint="students")
# api.add_resource(Student, "/api/<string:registration>",
#  endpoint="registration")
# api.add_resource(Student, "/api/department/<string:department>",
#  endpoint="department")

if __name__ == "__main__":
    app.run(debug=True)
