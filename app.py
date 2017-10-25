from flask import Flask, jsonify
from flask import request
from util import DateConverter
from util import ListStringConverter
from util import ListIntConverter

app = Flask(__name__)


app.url_map.converters['date'] = DateConverter
app.url_map.converters['listofstrings'] = ListStringConverter
app.url_map.converters['listofints'] = ListIntConverter

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


@app.route('/cities', methods=['GET'])
def cities():
    city = request.args.getlist('name')
    return jsonify({'cities': city})

@app.route('/date/<date:dates>', methods=['GET'])
def date(dates):
	date = dates
	date = str(date)
	return jsonify({'date': date})


@app.route('/planner/startCity/<string:cityName>/startDate/<date:dates>/cities/<listofstrings:cities>/days/<listofints:days>', methods=['GET'])
def getStart(dates,cityName,cities,days):
	city = request.args.get('name')
	date = dates
	date = str(date)
	#http://localhost:5000/planner/startCity/MADRID/startDate/2017-02-03/cities/GRECE-LISBONNE/days/2-3
	return jsonify({'startDate': date,'startCity':cityName,'cities':cities,'days':days})




if __name__ == '__main__':
    app.run(debug=True)

