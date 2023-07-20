from dotenv import load_dotenv
import os

load_dotenv()

DB_HOST = os.environ.get('DB_HOST')
DB_NAME = os.environ.get('DB_NAME')
DB_USER = os.environ.get('DB_USER')
DB_PORT = os.environ.get('DB_PORT')
DB_PASSWORD = os.environ.get('DB_PASSWORD')
GOOGLE_PROJECT_ID = os.environ.get('GOOGLE_PROJECT_ID')
