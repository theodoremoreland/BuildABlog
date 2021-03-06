from flask import Blueprint, render_template
from flask import Flask, request, redirect, session, flash, render_template

from ...models import db, Blog

create_blog_post = Blueprint(
    'create_blog_post',
    __name__, 
    template_folder='templates',
    static_folder='static'
    )


@create_blog_post.route('/create-blog-post', methods=['POST', 'GET'])
def create_post():
    if request.method == 'POST':
        entry = request.form['entry']
        title = request.form['title']

        if title == "" or entry == "":
            flash('Please fill both fields')
        else:
            blog = Blog(title, entry)
            db.session.add(blog)
            db.session.commit()
            blog_id = Blog.query.filter_by(title=title, entry=entry).first().id

            return redirect("/blog-post?blog_post_id=" + str(blog_id))
    
    return render_template('create_blog_post.html')