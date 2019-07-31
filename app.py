from flask import Flask
from flask import Flask, request, redirect, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('shady.html')
@app.route('/login', methods=['POST'])
def login():
    user = get_user(request.form['username'])
    if user.password == request.form['password']:
        login_session['name'] = user.username


if __name__ == '__main__':
    app.run(debug=True)

