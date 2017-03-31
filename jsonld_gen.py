from flask import jsonify
## Json-ld data generators
def gen_entrypoint():
    return jsonify({
  "@context": "https://polar-peak-76271.herokuapp.com/coffeeshop-api/contexts/EntryPoint.jsonld",
  "@id": "https://polar-peak-76271.herokuapp.com/coffeeshop-api/",
  "@type": "EntryPoint",
  "products": "https://polar-peak-76271.herokuapp.com/coffeeshop-api/products/"
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
