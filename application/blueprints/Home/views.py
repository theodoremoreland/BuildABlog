from flask import Blueprint, render_template
from flask import Flask, request, redirect, session, flash, render_template

from ...models import db, Blog

home = Blueprint(
    'home',
    __name__,
    template_folder='templates',
    static_folder='static'
    )

@home.route('/', methods=['GET'])
def render_blog():
    blog_id = request.args.get("id")
    
    if blog_id:
        blog = Blog.query.filter_by(id=blog_id).all()
    else: 
        blog = Blog.query.all()

    return render_template('blog.html', blog=blog)