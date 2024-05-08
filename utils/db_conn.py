from sqlalchemy import create_engine
from utils.environment import db_name, db_user, db_password, db_host, db_port
from langchain_community.utilities.sql_database import SQLDatabase

def get_connection():
	return create_engine(
		url="mysql+pymysql://{0}:{1}@{2}:{3}/{4}".format(
			db_user, db_password, db_host, db_port, db_name
		)
	)

try:
    engine = get_connection()

except Exception as ex:
    print("Connection could not be made due to the following error: \n", ex)

db = SQLDatabase(engine=engine, view_support=True)
