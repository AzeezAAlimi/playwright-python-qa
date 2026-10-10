import os
from dotenv import load_dotenv

load_dotenv()

TEST_USER = {
    "surname": "Lund",
    "given_name": "Peter",
    "national_personal_id": os.getenv("TEST_USER_PERSONAL_ID"),
    "personal_id_type": "SWEDISH_PERSONAL_IDENTITY_NUMBER",
}