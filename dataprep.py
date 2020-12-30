import pickle

class TP2EAC(object):
    def __init__(self):
        self.age = pickle.load(open('preparation/age.pkl','rb'))
        self.capital_gain = pickle.load(open('preparation/capital_gain.pkl','rb'))
        self.capital_loss = pickle.load(open('preparation/capital_loss.pkl','rb'))
        self.education = pickle.load(open('preparation/education.pkl','rb'))
        self.hours = pickle.load(open('preparation/hours_per_week.pkl','rb'))
        self.status = pickle.load(open('preparation/status_civic.pkl','rb'))
        self.status_encoder = pickle.load(open('preparation/status_civic_encoder.pkl','rb'))

    def data_preparation(self, df):
        df['age'] = self.age.transform(df[['age']].values)
        df['capital_gain'] = self.capital_gain.transform(df[['capital_gain']].values)
        df['capital_loss'] = self.capital_loss.transform(df[['capital_loss']].values)
        df['education'] = self.education.transform( df[['education']].values )
        df['hours_per_week'] = self.hours.transform(df[['hours_per_week']].values)
        df['status_civic'] = self.status.transform(df[['status_civic']].values)

        return df

