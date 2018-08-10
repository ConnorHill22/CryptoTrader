from flask import Flask, render_template, jsonify
from threading import Thread
import json
from app.backend.main import fiveMin, fifteenMin, oneHour, fourHour, oneDay
import os

template_dir = os.path.dirname(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
template_dir = os.path.join(template_dir, 'Signals')
template_dir = os.path.join(template_dir, 'dist')
static_dir = os.path.join(template_dir, 'static')
print(template_dir)
app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)

@app.before_first_request
def activate_job():
    class five(Thread):
        def __init__(self):
            Thread.__init__(self)
            self.daemon = True
            self.start()
        def run(self):
            while True:
                fiveMin()
    class fifteen(Thread):
        def __init__(self):
            Thread.__init__(self)
            self.daemon = True
            self.start()
        def run(self):
            while True:
                fifteenMin()
    class oneH(Thread):
        def __init__(self):
            Thread.__init__(self)
            self.daemon = True
            self.start()
        def run(self):
            while True:
                oneHour()
    class fourH(Thread):
        def __init__(self):
            Thread.__init__(self)
            self.daemon = True
            self.start()
        def run(self):
            while True:
                fourHour()
    class oneD(Thread):
        def __init__(self):
            Thread.__init__(self)
            self.daemon = True
            self.start()
        def run(self):
            while True:
                oneDay()
    five()
    fifteen()
    oneH()
    fourH()
    oneD()

@app.route('/api/<timeFrame>/<indicator>')
def RSIdata(timeFrame, indicator):
    file_name = 'data/%s/%s.json' %(timeFrame, indicator)
    json_in = open(file_name, 'r')
    data = json.load(json_in)
    return jsonify(data)


@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=False, use_reloader=True)