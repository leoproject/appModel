import os
import pandas as pd
from flask import Flask, jsonify, request
import pickle
from dataprep import TP2EAC 

# load model
model = pickle.load(open('model/modelo.pkl','rb'))

# app
app = Flask(__name__)

# routes
@app.route('/predict', methods=['POST'])

def predict():
    # get data
    data = request.get_json(force=True)

    # convert data into dataframe

    #data_df = pd.DataFrame(eval(data))
    # data_df = pd.DataFrame.from_dict(data, orient='columns')
    query_df = pd.DataFrame(data)
    query = pd.get_dummies(query_df)
    # instanciar a preparação
    pipeline = TP2EAC()
    data1 = pipeline.data_preparation(query)
    # predictions
    result = model.predict(data1)
    data1['prediction'] = result

    # send back to browser
    output = {'results': int(result[0])}

    # return data
    return jsonify(data1.to_json( orient = 'records'))


if __name__ == '__main__':
    port = os.environ.get('PORT', 5000)
    app.run(host='0.0.0.0',port = port, debug=True)