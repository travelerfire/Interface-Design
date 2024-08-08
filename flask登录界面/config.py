HOST = "127.0.0.1"
PORT = "3306"
DB = "flasklogin"
USER = "root"
PASS = "123456"
CHARSET = "utf8"
DB_URI = "mysql+pymysql://{}:{}@{}:{}/{}?charset={}".format(
    USER, PASS, HOST, PORT, DB, CHARSET
)
SQLALCHEMY_DATABASE_URI = DB_URI
