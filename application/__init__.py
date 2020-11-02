# Third party
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Custom
from .Home.routes import home
from .CreateBlog.routes import create_blog

db = SQLAlchemy()
app = Flask(__name__, instance_relative_config=True)
app.config.from_object('config')
app.config.from_pyfile('config.py')
app.register_blueprint(home)
app.register_blueprint(create_blog)
db.init_app(app)