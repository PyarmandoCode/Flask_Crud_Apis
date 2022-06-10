from flask import Flask
from Apis_Clientes.config import Config
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)
app.config.from_object(Config)
db = SQLAlchemy(app)

from Apis_Clientes import routes, models
