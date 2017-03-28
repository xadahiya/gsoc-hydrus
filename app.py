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
        Default : { Content-type:"JSON-LD", status_code:200}"""
    resp.status_code = status_code
    resp.headers['Content-type'] = ct
    return resp


def gen_initial_context():
    return jsonify({
        "_id": "/",
        "@type": "Entrypoint",
        "store": {
            "_id": "store"
        },

        "products": {
            "@type": "hydra:IriTemplate",
            "hydra:mapping": {
                "@type": "hydra:IriTemplateMapping",
                "hydra:property": {
                    "@type": "rdfs:Property",
                    "rdfs:range": {
                        "_id": "xsd:number"
                    }
                },
                "hydra:required": "true",
                "hydra:variable": "product_id"
            },
            "hydra:template": "/product{?product_id}",
            "hydra:variableRepresentation": "BasicRepresentation"
        },
        "product": {
            "_id": "product"
        },
        "hydra:title": "Main API Entry Point",
        "@context": {
            "@vocab": "https://polar-peak-76271.herokuapp.com/vocab#",
            "@base": "https://polar-peak-76271.herokuapp.com/",
            "pto": "http://www.productontology.org/doc/",
            "hydra": "http://www.w3.org/ns/hydra/core#",
            "_id": "@id"
        }
    }


    )


def gen_vocab():
    return jsonify(
        {
            "@type": "hydra:ApiDocumentation",
            "hydra:entrypoint": "/",
            "hydra:supportedClass": [
                {
                    "_id": "vocab:Entrypoint",
                    "@type": "hydra:Class",
                    "hydra:description": "The main entry point of the API",
                    "hydra:supportedOperation": {
                        "@type": "hydra:Operation",
                        "hydra:description": "The APIs main entry point.",
                        "hydra:method": "GET",
                        "hydra:returns": {
                            "_id": "vocab:EntryPoint"
                        }
                    },
                    "hydra:supportedProperty": [
                        {
                            "_id": "vocab:get-store-link",
                            "@type": "hydra:SupportedProperty",
                            "hydra:property": {
                                "_id": "vocab:store",
                                "@type": "hydra:Link",
                                "rdfs:comment": "Redirects the user to the store",
                                "hydra:supportedOperation": {
                                    "@type": "hydra:Operation",
                                    "hydra:method": "GET",
                                }
                            }
                        },
                        {
                            "_id": "vocab:search-product",
                            "@type": "hydra:SupportedProperty",
                            "hydra:property": {
                                "_id": "vocab:offer",
                                "@type": "hydra:TemplatedLink",
                                "rdfs:comment": "Search product by product_id",
                                "hydra:supportedOperation": {
                                    "@type": "hydra:Operation",
                                    "hydra:method": "GET",
                                    "hydra:returns": {
                                        "_id": "vocab:product"
                                    }
                                }
                            }
                        }
                    ],
                    "hydra:title": "EntryPoint"
                },

                {
                    "_id": "vocab:products",
                    "@type": "hydra:Class",
                    "hydra:description": "A product represents a servable item like coffee or something from the store",
                    "hydra:supportedOperation": [
                        {
                            "_id": "vocab:product_retrieve",
                            "@type": "hydra:Operation",
                            "hydra:description": "Retrieves a product",
                            "hydra:method": "GET",
                            "hydra:returns": {
                                "_id": "vocab:product"
                            }
                        }
                    ],
                    "hydra:supportedProperty": [
                        {
                            "@type": "hydra:SupportedProperty",
                            "hydra:property": {
                                "_id": "vocab:name",
                                "@type": "http://www.w3.org/1999/02/22-rdf-syntax-ns#Property",
                                "rdfs:comment": "The products's name",
                                "hydra:supportedOperation": [
                                ]
                            }
                        },
                        {
                            "@type": "hydra:SupportedProperty",
                            "hydra:property": {
                                "_id": "vocab:price",
                                "@type": "http://www.w3.org/1999/02/22-rdf-syntax-ns#Property",
                                "rdfs:comment": "The product's price",
                                "hydra:supportedOperation": [
                                ]
                            },
                            "hydra:required": "true"
                        },

                    ],
                    "hydra:title": "Product"
                },
            ],
            "@context": {
                "@vocab": "https://polar-peak-76271.herokuapp.com/vocab#",
                "@base": "https://polar-peak-76271.herokuapp.com/",
                "pto": "http://www.productontology.org/doc/",
                "hydra": "http://www.w3.org/ns/hydra/core#",
                "_id": "@id"
            }
        }


    )


class Index(Resource):
    """A link to main entry point of the Web API"""

    def get(self):
        return set_response_headers(gen_initial_context())


class Vocab(Resource):
    """A general vocab for the API"""

    def get(self):
        return set_response_headers(gen_vocab())


api = Api(app)
api.add_resource(Index, "/", endpoint="index")
api.add_resource(Vocab, "/vocab", endpoint="vocab")
# api.add_resource(Student, "/api", endpoint="students")
# api.add_resource(Student, "/api/<string:registration>",
#  endpoint="registration")
# api.add_resource(Student, "/api/department/<string:department>",
#  endpoint="department")

if __name__ == "__main__":
    app.run(debug=True)
