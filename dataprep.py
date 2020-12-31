import pickle
import pandas as pd

class TP2EAC(object):
    def __init__(self):
        self.scaler = pickle.load(open('preparation/scaler.pkl','rb'))

    def data_preparation(self, df):
        scaler = pickle.load(open('preparation/scaler.pkl','rb'))
        df_scaled = scaler.transform(df)
        columns = ["age","education","capital_gain","capital_loss","hours_per_week","status_civic"]
        df_result = pd.DataFrame(df_scaled, columns=columns)
        return df_result

