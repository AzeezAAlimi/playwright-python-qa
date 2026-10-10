AUTH_SCHEMA = {
    "type": "object",
    "required": [
        "token",
    ],
    "properties": {
        "token": {
            "type": "string",
            "minlength": 1
        }
    }
}