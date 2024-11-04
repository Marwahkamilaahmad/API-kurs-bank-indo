from flask import Flask, jsonify, request
import pandas as pd

app = Flask(__name__)

data = pd.read_excel('kurs_transaksi.xlsx')

# get all data
@app.route('/api/kurs', methods=['GET'])
def get_all_data():
    return jsonify(data.to_dict(orient='records'))

#filter data by date (for example)
@app.route('/api/kurs', methods=['GET'])
def get_data_by_date():
    date = request.args.get('date')
    if date:
        filtered_data = data[data['Tanggal'] == date]
        return jsonify(filtered_data.to_dict(orient='records'))
    return jsonify(data.to_dict(orient='records'))

# render
if __name__ == '__main__':
    app.run(debug=True)
