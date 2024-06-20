from flask import Flask
from src.models import Base, engine
from flask_controller import FlaskControllerRegister
from src.config import config

app = Flask(__name__)
register = FlaskControllerRegister(app)
register.register_package("src.controllers")

Base.metadata.create_all(engine)

if __name__ == "__main__":
    app.config.from_object(config['development'])
    app.run()