from flask import jsonify
# Contexts


def gen_entrypoint_context():
    return jsonify(
        {
            "@context": {
                "hydra": "http://www.w3.org/ns/hydra/core#",
                "vocab": "https://polar-peak-76271.herokuapp.com/coffeeshop-api/vocab",
                "EntryPoint": "vocab#EntryPoint",
                "products": {
                    "@id": "vocab#EntryPoint/products",
                    "@type": "@id"
                }
            }
        }

    )


def gen_product_collection_context():
    return jsonify({
        "@context": {
            "hydra": "http://www.w3.org/ns/hydra/core#",
            "vocab": "https://polar-peak-76271.herokuapp.com/coffeeshop-api/vocab",
            "ProductCollection": "vocab#ProductCollection",
            "members": "http://www.w3.org/ns/hydra/core#member"
        }
    })


def gen_product_context():
    return jsonify({
        "@context": {
            "hydra": "http://www.w3.org/ns/hydra/core#",
            "vocab": "https://polar-peak-76271.herokuapp.com/coffeeshop-api/vocab",
            "Product": "http://schema.org/Product",
            "name": "http://schema.org/name",
            "description": "http://schema.org/description",

        }
    })
