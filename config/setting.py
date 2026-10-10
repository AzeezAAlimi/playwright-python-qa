import os

BASE_URL_DEV = os.getenv(
    "BASE_URL_DEV",
    "https://doktor24.app.dev.platform24.se"
)

BASE_URL_STAGE = os.getenv(
    "BASE_URL_STAGE",
    "https://doktor24.app.staging.platform24.se"
)