HEALTH_DATA_SCHEMA = {
    "type": "object",
    "required": [
        "id",
        "height",
        "weight",
        "allergies",
        "diagnoses",
        "medication",
        "surgery",
        "interviewId",
    ],
    "properties": {
        "id": {
            "type": "string",
            "minLength": 1,
        },
        "height": {
            "type": "integer",
        },
        "weight": {
            "type": "integer",
        },
        "allergies": {
            "type": "string",
        },
        "diagnoses": {
            "type": "string",
        },
        "medication": {
            "type": "string",
        },
        "surgery": {
            "type": "string",
        },
        "interviewId": {
            "type": ["string", "null"],
        },
    },
}