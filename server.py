from flask import Flask, render_template, redirect, request
# import the class from friend.py
from models.model_user import User
app = Flask(__name__)
@app.route("/")
def index():
    # call the get all classmethod to get all friends
    users = User.get_all()
    print(users)
    return render_template("index.html", users=users)

@app.route('/create')
def create():
    return render_template('create.html')
            

@app.route('/create_user', methods=['POST'])
def create_user():
    data = {
        'fname': request.form['fname'],
        'lname': request.form['lname'],
        'email': request.form['email']
    }
    id = User.save(data)
    return redirect(f"/users/{id}")

@app.route('/users/<int:id>')
def show_user(id):
    data = {
        'id' : id
    }
    return render_template('kms.html', one_user = User.get_one(data))

@app.route('/edit/<int:id>')
def edit(id):
    data = {
        'id' : id
    }
    return render_template('edit.html', one_user = User.get_one(data))

@app.route('/edit_user', methods=['POST'])
def edit_user():
    User.edit(request.form)
    id = request.form['id']
    return redirect(f"/users/{id}")

@app.route('/delete_user/<int:id>')
def delete_user(id):
    data = {
        'id' : id
    }
    User.delete(data)
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)