from flask import Blueprint, render_template
from flask import Flask, request, redirect, session, flash, render_template

from ..models import Blog

blog_post = Blueprint(
    'blog_post',
    __name__,
    template_folder='templates',
    static_folder='static'
    )

@blog_post.route('/blog-post', methods=['GET'])
def render_blog_post():
    blog_post_id = request.args.get("blog_post_id")   
    blog_post = Blog.query.filter_by(id=blog_post_id).first()

    return render_template('blog_post.html', blog_post=blog_post)