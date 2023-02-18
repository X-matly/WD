HOST = '106.14.123.5'
PORT = '3306'
USERNAME = '106.14.123.5'
PASSWORD = 'NJUnetwork'
DATABASE = '106.14.123.5'

DB_URI = "mysql+pymysql://{username}:{password}@{host}:{port}/{db}?charset=utf8".format(
    username=USERNAME,
    password=PASSWORD,
    host=HOST,
    port=PORT,
    db=DATABASE)

SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_ECHO = True
JSON_AS_ASCII = False

