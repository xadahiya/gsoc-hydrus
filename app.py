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

## Contects
def gen_entrypoint_context():
    return jsonify(
    {
  "@context": {
    "hydra": "http://www.w3.org/ns/hydra/core#",
    "vocab": "https://polar-peak-76271.herokuapp.com/coffeeshop-api/vocab#",
    "EntryPoint": "vocab:EntryPoint",
    "products": {
      "@id": "vocab:EntryPoint/products",
      "@type": "@id"
    }
  }
}

    )

def gen_product_collection_context():
    return jsonify({
    {
  "@context": {
    "hydra": "http://www.w3.org/ns/hydra/core#",
    "vocab": "https://polar-peak-76271.herokuapp.com/coffeeshop-api/vocab#",
    "EventCollection": "vocab:ProductCollection",
    "members": "http://www.w3.org/ns/hydra/core#member"
  }
}
    })

def gen_product_context():
    return jsonify({
  "@context": {
    "hydra": "http://www.w3.org/ns/hydra/core#",
    "vocab": "https://polar-peak-76271.herokuapp.com/coffeeshop-api/vocab#",
    "Event": "http://schema.org/Product",
    "name": "http://schema.org/name",
    "description": "http://schema.org/description",

  }
})


def gen_entrypoint():
    return jsonify({
  "@context": "https://polar-peak-76271.herokuapp.com/coffeeshop-api/contexts/EntryPoint.jsonld",
  "@id": "https://polar-peak-76271.herokuapp.com/coffeeshop-api/",
  "@type": "EntryPoint",
  # "products": "https://polar-peak-76271.herokuapp.com/coffeeshop-api/products/"
    })


def gen_vocab():
    return jsonify(
    {
  "@context": {
    "vocab": "https://polar-peak-76271.herokuapp.com/coffeeshop-api/vocab#",
    "hydra": "http://www.w3.org/ns/hydra/core#",
    "ApiDocumentation": "hydra:ApiDocumentation",
    "property": {
      "@id": "hydra:property",
      "@type": "@id"
    },
    "readonly": "hydra:readonly",
    "writeonly": "hydra:writeonly",
    "supportedClass": "hydra:supportedClass",
    "supportedProperty": "hydra:supportedProperty",
    "supportedOperation": "hydra:supportedOperation",
    "method": "hydra:method",
    "expects": {
      "@id": "hydra:expects",
      "@type": "@id"
    },
    "returns": {
      "@id": "hydra:returns",
      "@type": "@id"
    },
    "statusCodes": "hydra:statusCodes",
    "code": "hydra:statusCode",
    "rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
    "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
    "label": "rdfs:label",
    "description": "rdfs:comment",
    "domain": {
      "@id": "rdfs:domain",
      "@type": "@id"
    },
    "range": {
      "@id": "rdfs:range",
      "@type": "@id"
    },
    "subClassOf": {
      "@id": "rdfs:subClassOf",
      "@type": "@id"
    }
  },
  "@id": "https://polar-peak-76271.herokuapp.com/coffeeshop-api/vocab",
  "@type": "ApiDocumentation",
  "supportedClass": [
    {
      "@id": "http://www.w3.org/ns/hydra/core#Collection",
      "@type": "hydra:Class",
      "hydra:title": "Collection",
      "hydra:description": None,
      "supportedOperation": [
      ],
      "supportedProperty": [
        {
          "property": "http://www.w3.org/ns/hydra/core#member",
          "hydra:title": "members",
          "hydra:description": "The members of this collection.",
          "required": None,
          "readonly": False,
          "writeonly": False
        }
      ]
    },
    {
      "@id": "http://www.w3.org/ns/hydra/core#Resource",
      "@type": "hydra:Class",
      "hydra:title": "Resource",
      "hydra:description": None,
      "supportedOperation": [
      ],
      "supportedProperty": [
      ]
    },
    {
      "@id": "http://schema.org/Product",
      "@type": "hydra:Class",
      "hydra:title": "Product",
      "hydra:description": None,
      "supportedOperation": [
        {
          "@id": "_:product_replace",
          "@type": "http://schema.org/UpdateAction",
          "method": "PUT",
          "label": "Replaces an existing Product entity",
          "description": None,
          "expects": "http://schema.org/Product",
          "returns": "http://schema.org/Product",
          "statusCodes": [
            {
              "code": 404,
              "description": "If the Product entity wasn't found."
            }
          ]
        },
        {
          "@id": "_:product_delete",
          "@type": "http://schema.org/DeleteAction",
          "method": "DELETE",
          "label": "Deletes a Product entity",
          "description": None,
          "expects": None,
          "returns": "http://www.w3.org/2002/07/owl#Nothing",
          "statusCodes": [
          ]
        },
        {
          "@id": "_:product_retrieve",
          "@type": "hydra:Operation",
          "method": "GET",
          "label": "Retrieves a Product entity",
          "description": None,
          "expects": None,
          "returns": "http://schema.org/Product",
          "statusCodes": [
          ]
        }
      ],
      "supportedProperty": [
        {
          "property": "http://schema.org/name",
          "hydra:title": "name",
          "hydra:description": "The product's name",
          "required": True,
          "readonly": False,
          "writeonly": False
        },
        {
          "property": "http://schema.org/description",
          "hydra:title": "description",
          "hydra:description": "Description of the product",
          "required": True,
          "readonly": False,
          "writeonly": False
        },
      ]
    },
    {
      "@id": "vocab:EntryPoint",
      "@type": "hydra:Class",
      "subClassOf": None,
      "label": "EntryPoint",
      "description": "The main entry point or homepage of the API.",
      "supportedOperation": [
        {
          "@id": "_:entry_point",
          "@type": "hydra:Operation",
          "method": "GET",
          "label": "The APIs main entry point.",
          "description": None,
          "expects": None,
          "returns": "vocab:EntryPoint",
          "statusCodes": [
          ]
        }
      ],
      "supportedProperty": [
        {
          "property": {
            "@id": "vocab:EntryPoint/products",
            "@type": "hydra:Link",
            "label": "products",
            "description": "The products collection",
            "domain": "vocab:EntryPoint",
            "range": "vocab:ProductCollection",
            "supportedOperation": [
              {
                "@id": "_:product_collection_retrieve",
                "@type": "hydra:Operation",
                "method": "GET",
                "label": "Retrieves all Product entities",
                "description": None,
                "expects": None,
                "returns": "vocab:ProductCollection",
                "statusCodes": [
                ]
              }
            ]
          },
          "hydra:title": "products",
          "hydra:description": "The products collection",
          "required": None,
          "readonly": True,
          "writeonly": False
        }
      ]
    },
    {
      "@id": "vocab:ProductCollection",
      "@type": "hydra:Class",
      "subClassOf": "http://www.w3.org/ns/hydra/core#Collection",
      "label": "ProductCollection",
      "description": "A collection of products",
      "supportedOperation": [
        {
          "@id": "_:product_create",
          "@type": "http://schema.org/AddAction",
          "method": "POST",
          "label": "Creates a new Product entity",
          "description": None,
          "expects": "https://schema.org/Product",
          "returns": "https://schema.org/Product",
          "statusCodes": [
            {
              "code": 201,
              "description": "If the Product entity was created successfully."
            }
          ]
        },
        {
          "@id": "_:product_collection_retrieve",
          "@type": "hydra:Operation",
          "method": "GET",
          "label": "Retrieves all Product entities",
          "description": None,
          "expects": None,
          "returns": "vocab:ProductCollection",
          "statusCodes": [
          ]
        }
      ],
      "supportedProperty": [
        {
          "property": "http://www.w3.org/ns/hydra/core#member",
          "hydra:title": "members",
          "hydra:description": "The products",
          "required": None,
          "readonly": False,
          "writeonly": False
        }
      ]
    }
  ]
}

    )

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
