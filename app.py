from flask import Flask, jsonify
from flask import request
from util import DateConverter

app = Flask(__name__)


app.url_map.converters['date'] = DateConverter

route = [
    {
        'title': u'MADRID-LISBONNE-GRECE',
        'price': u'250$'
    }
]

details = [
    {
        'title': u'MADRID-LISBONNE',
        'price': u'100$'
    },
    {
        'title': u'LISBONNE-GRECE',
        'price': u'100$'
    },
    {
        'title': u'GRECE-MADRID',
        'price': u'100$'
    }
]

@app.route('/planner', methods=['GET'])
def get_planner():
    return jsonify({'route': route,"details":details})


@app.route('/ville', methods=['GET'])
def ville():
    ville = request.args.getlist('ville')
    return jsonify({'ville': ville})


@app.route('/date/<date:dates>', methods=['GET'])
def date(dates):
	date = dates
	date = str(date)
	return jsonify({'date': date})


if __name__ == '__main__':
    app.run(debug=True)

