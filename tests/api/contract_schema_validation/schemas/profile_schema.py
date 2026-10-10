PROFILE_SCHEMA = {
    "type": "object",
    "required": [
        "userProfile",
        "oneselfPatientProfile"
    ],
    "properties": {
        "userProfile": {
            "type": "object",
            "required": [
                "userId",
                "username",
                "givenName",
                "surname",
                "mobileNumber",
                "email",
                "preferredLanguage"
            ],
            "properties": {
                "userId": {
                    "type": "string",
                    "minLength": 1
                },
                "username": {"type": "string"},
                "givenName": {"type": "string"},
                "surname": {"type": "string"},
                "mobileNumber": {"type": "string"},
                "email": {
                    "type": "string",
                    "format": "email"
                },
                "preferredLanguage": {"type": "string"}
            }
        },

        "oneselfPatientProfile": {
            "type": "object",
            "required": [
                "patientId",
                "age",
                "birthDate",
                "gender",
                "givenName",
                "surname",
                "secrecy",
                "insuranceInfo"
            ],
            "properties": {
                "patientId": {"type": "string"},
                "age": {"type": "integer"},
                "birthDate": {"type": "string"},
                "gender": {"type": "string"},
                "givenName": {"type": "string"},
                "surname": {"type": "string"},
                "secrecy": {"type": "string"},
                "insuranceInfo": {
                    "type": ["object", "null"]
                }
            }
        }
    }
}