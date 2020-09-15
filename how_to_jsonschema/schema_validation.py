# https://json-schema.org/learn/getting-started-step-by-step.html Following this example

from jsonschema import validate

schema = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "$id": "http://example.com/product.schema.json",
    "title": "Product",
    "description": "A product from Acme's catalog",
    "type": "object",
    "properties": {
        "productId": {
            "description": "The unique identifier for a product",
            "type": "integer"
        },
        "productName": {
            "description": "Name of the product",
            "type": "string"
        },
        "price": {
            "description": "The price of the product",
            "type": "number",
            "exclusiveMinimum": 0
        },
        "tags": {
            "description": "Tags for the product",
            "type": "array",
            "items": {
                "type": "string"
            },
            "minItems": 1,
            "uniqueItems": True
        }
    },
    "required": ["productId", "productName", "price"]
}

data1 = {"productId": 123,
         "productName": "ACME Rocket skates",
         "price": 199.99}
data2 = {"productId": 124,
         "productName": "ACME Rocket skates",
         "price": None}

validate(instance=data1, schema=schema)  # Passing
validate(instance=data2, schema=schema)  # Failing

print("That was fun.")