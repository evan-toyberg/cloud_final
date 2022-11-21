from flask import Flask, render_template, request, flash, redirect,url_for, jsonify, session
from flask import Response,send_file

app = Flask(__name__)

import rds as db

@app.route('/')
def index():

    return render_template('index.html')

@app.route('/insert',methods = ['post'])
def insert():

    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        title = request.form['title']
        comment = request.form['comment']
        db.insert_details(name,email,title,comment)
        #posts = db.get_posts()
        #print(posts)
        #for post in posts:
        #    var = post
        #return render_template('index.html',var=var)
    posts = db.get_posts()
    print(posts)
    var = []
    for post in posts:
        var.append(post)
    return render_template('index.html',var=var)

if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0",port=5000)
