from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydb.db'

db = SQLAlchemy(app)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(300), nullable=False)
    text = db.Column(db.Text, nullable=False)


@app.route("/")
def index():
    posts = Post.query.all()
    return render_template('index.html', posts=posts)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/add", methods=['POST', 'GET'])
def add():
    if request.method == 'POST':
        title = request.form['title']
        text = request.form['text']

        post = Post(text=text, title=title)

        try:
            db.session.add(post)
            db.session.commit()
            return redirect("/")
        except:
            return "An error occured while adding Article"
        
    else:
        return render_template("create.html")


if __name__=="__main__":
    app.run(debug=True)
