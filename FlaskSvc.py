from flask import Flask
from flask import jsonify
from flask import request
import isindb

app = Flask(__name__)

isins = [
    {'isin': 'EZ123456789',
     'asset_class': 'Equity',
     'expiry':'2021-03-31'
     },
    {'isin': 'EZ987654321',
     'asset_class': 'Rates',
     'expiry': '2022-06-30'
     }
]

@app.route('/')
def index():
    return 'Hello World!'


@app.route('/isins/class=<asset_class>', methods=['GET'])
def get_isin_by_class(asset_class):
    print(asset_class)
    #ilist2 = [x['isin'] for x in isins if x['asset_class'] == asset_class]
    irecord = isindb.get_isin_by_asset_class(asset_class)
    #return jsonify({'isins': ilist2})
    return jsonify({'isin': irecord})


@app.route('/isins', methods=['GET', 'POST'])
def handle_isins():
    if request.method == 'GET':
        ilist = [x['isin'] for x in isins]
        return jsonify({'isins': ilist})
    elif request.method == 'POST':
        record = request.json
        record['_id'] = record['ISIN']['ISIN']
        isindb.create_isin(record)
        return jsonify({'isin':record['_id']}), 200


@app.route('/isins/<isin_id>', methods=['GET'])
def isin_by_id(isin_id):
    irecord = isindb.get_isin(isin_id)
    return jsonify({'isin': irecord})


if __name__== '__main__':
    app.run(debug=True)
