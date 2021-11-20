import os
import flask
import arrow
import acp_times
from flask import Flask, redirect, url_for, request, render_template
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient(os.environ['DB_PORT_27017_TCP_ADDR'], 27017)
db = client.tododb

OPEN_LIST = []
CLOSE_LIST = []


@app.route("/")
@app.route("/index")
def index():
    app.logger.debug("Main page entry")
    return render_template('calc.html')


@app.route("/_calc_times")
def _calc_times():
    """
    Calculates open/close times from miles, using rules
    described at https://rusa.org/octime_alg.html.
    Expects one URL-encoded argument, the number of miles.
    """
    app.logger.debug("Got a JSON request")
    km = request.args.get('km', 999, type=float)
    distance = request.args.get('distance', type=int)
    begin_date = request.args.get('begin_date', type=str)
    begin_time = request.args.get('begin_time', type=str)
    beginning_date_time = begin_date + " " + begin_time
    time = arrow.get(beginning_date_time, 'YYYY-MM-DD HH:mm')
    app.logger.debug("km={}".format(km))
    app.logger.debug("request.args: {}".format(request.args))
    open_time = acp_times.open_time(km, distance, time.isoformat())
    close_time = acp_times.close_time(km, distance, time.isoformat())
    OPEN_LIST.append(str(open_time))
    CLOSE_LIST.append(str(close_time))
    result = {"open": open_time, "close": close_time}
    return flask.jsonify(result=result)


@app.route('/display', methods=['POST'])
def display():
    db_items = list(db.tododb.find())
    if not db_items:
        return render_template('nodisplay.html')
    else:
        return render_template('displaytimes.html', items=db_items)


@app.route('/new', methods=['POST'])
def new():
    list_length = len(OPEN_LIST)
    for i in range(list_length):
        item_doc = {
            'open_times': OPEN_LIST[i],
            'close_times': CLOSE_LIST[i]
        }
        db.tododb.insert_one(item_doc)
    db_items = list(db.tododb.find())
    OPEN_LIST.clear()
    CLOSE_LIST.clear()
    if not db_items:
        return render_template('noinput.html')
    else:
        return redirect(url_for('index'))


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
