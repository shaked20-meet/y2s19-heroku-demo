from flask import Flask
from flask import Flask, request, redirect, render_template, url_for
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('shady.html')



if __name__ == '__main__':
    app.run(debug=True)

