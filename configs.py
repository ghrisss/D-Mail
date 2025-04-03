from os import getenv

from dotenv import load_dotenv

load_dotenv()

EMAIL_PASSWORD = getenv("EMAIL_PASSWORD")
DEBUG = True
