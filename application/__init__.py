# Third party
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Custom
from .Home.routes import home
from .CreateBlogPost.routes import create_blog_post
from .BlogPost.routes import blog_post


db = SQLAlchemy()
app = Flask(__name__, instance_relative_config=True)
app.config.from_object('config')
app.config.from_pyfile('config.py')
app.register_blueprint(home)
app.register_blueprint(create_blog_post)
app.register_blueprint(blog_post)
db.init_app(app)