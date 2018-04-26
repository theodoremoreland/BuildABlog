from flask import Flask, request, redirect, render_template, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://build-a-blog:bproductive@localhost:8889/build-a-blog'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)






class Blog(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    entry = db.Column(db.String(1000))

    def __init__(self, title, entry):
        self.title = title
        self.entry = entry

@app.route('/blog', methods=['POST', 'GET'])
def userblog():

    blog_id = request.args.get("id")
    
    if blog_id:
        blog = Blog.query.filter_by(id=blog_id).all()

    else: 
        blog = Blog.query.all()

    return render_template('blog.html', blogs=blog)

@app.route('/newpost', methods=['POST', 'GET'])
def new_post():

    blog_id = request.args.get("id")


    if request.method == 'POST':
        entry = request.form['entry']
        title = request.form['title']
        if title == "" or entry == "":
            flash('Please fill both fields')
        else:
            blog = Blog(title, entry)
            db.session.add(blog)
            db.session.commit()
        
        
            return render_template('newblog.html', blog=blog)
    

    return render_template('newpost.html')



        



if __name__ == '__main__':
    app.run()