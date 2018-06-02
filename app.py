from flask import Flask
from datetime import datetime
import requests
app = Flask(__name__)

@app.route('/')
def homepage():
    the_time = datetime.now().strftime("%A, %d %b %Y %l:%M %p")
    r = requests.get('http://httpbin.org/status/418')

    return """
    <h1>Hello heroku</h1>
    <p>It is currently {time}.</p>
    <p>{r}</p>

    """.format(time=the_time r=r)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)