from flask import Flask, jsonify

app = Flask(__name__)

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

@app.route('/todo/api/v1.0/planner', methods=['GET'])
def get_tasks():
    return jsonify({'route': route,"details":details})

if __name__ == '__main__':
    app.run(debug=True)

