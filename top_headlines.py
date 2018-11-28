from flask import Flask,render_template
import requests
from secrets import nyt_key

app = Flask(__name__)

@app.route('/user/<nm>')
def hello_name(nm):
    return render_template('user.html', name=nm)

if __name__ == '__main__':
    app.run(debug=True)