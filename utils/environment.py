import os
from urllib.parse import quote_plus
from dotenv import load_dotenv
load_dotenv()

api_key=os.getenv("OPENAI_API_KEY")
open_ai_model=os.getenv("OPENAI_MODEL")
db_name=os.getenv("DB_NAME")
db_user=os.getenv("DB_USER")
db_password=quote_plus(os.getenv("DB_PASSWORD"))
db_host=os.getenv("DB_HOST")
db_port=int(os.getenv("DB_PORT"))
langchain_api_key=os.getenv("LANGCHAIN_API_KEY")
