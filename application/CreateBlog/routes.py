from flask import Blueprint, render_template
from flask import Flask, request, redirect, session, flash, render_template

from ..models import db, Blog

create_blog = Blueprint(
    'create_blog',
    __name__, 
    template_folder='templates',
    static_folder='static'
    )


@create_blog.route('/create-blog', methods=['POST', 'GET'])
def new_post():
    if request.method == 'POST':
        entry = request.form['entry']
        title = request.form['title']

        if title == "" or entry == "":
            flash('Please fill both fields')
        else:
            blog = Blog(title, entry)
            db.session.add(blog)
            db.session.commit()
            blogs = Blog.query.all()
            blog_id = len(blogs)

            return redirect("/blog?id=" + str(blog_id))
    
    return render_template('newpost.html')