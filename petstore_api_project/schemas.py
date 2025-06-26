post_pet_schemas = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "type": "object",
    "properties": {
        "id": {
            "type": "integer"
        },
        "name": {
            "type": "string"
        },
        "photoUrls": {
            "type": "array",
            "items": {}
        },
        "tags": {
            "type": "array",
            "items": {}
        }
    },
    "required": [
        "id",
        "name",
        "photoUrls",
        "tags"
    ]
}

delete_pet_schemas = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "type": "object",
    "properties": {
        "code": {
            "type": "integer"
        },
        "type": {
            "type": "string"
        },
        "message": {
            "type": "string"
        }
    },
    "required": [
        "code",
        "type",
        "message"
    ]
}

get_pet_schemas = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "type": "object",
    "properties": {
        "id": {
            "type": "integer"
        },
        "name": {
            "type": "string"
        },
        "photoUrls": {
            "type": "array",
            "items": {}
        },
        "tags": {
            "type": "array",
            "items": {}
        }
    },
    "required": [
        "id",
        "name",
        "photoUrls",
        "tags"
    ]
}
