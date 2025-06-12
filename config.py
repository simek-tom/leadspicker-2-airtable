import os
from dotenv import load_dotenv

load_dotenv()

AIRTABLE_API_KEY = os.getenv("AIRTABLE_API_KEY")
LEADSPICKER_API_KEY = os.getenv("LEADSPICKER_API_KEY")