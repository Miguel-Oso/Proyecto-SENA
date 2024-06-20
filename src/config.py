class Config():
    SECRET_KEY = 'mysecret'

class DevelopmentConfig(Config):
    DEBUG = True
    # mysql+pymysql://root@localhost/proyecto-sena
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root@localhost/proyecto-sena'
    

    
config = {
    'development': DevelopmentConfig
}