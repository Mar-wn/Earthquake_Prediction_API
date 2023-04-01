from fastapi import FastAPI
from models import Donor
import pickle


app = FastAPI(title= 'Blood Donation Prediction')

# load the scaler

with open('scaler.pkl', 'rb') as f:

    min_max_scaler = pickle.load(f)
    f.close()

# load the classifier

with open('model.pkl', 'rb') as f:

    classifier = pickle.load(f)
    f.close()


@app.get('/')
def root():
    return 'Welcome to blood donation prediction API! Now head over to http://localhost:80/docs to try it out'

@app.post('/predict')
def predict(donor: Donor):

    donor = donor.transform(min_max_scaler)

    if classifier.predict(donor)[0] == '1':

        return 'This donor will donate blood! Call him'
    else:
        return "Unfortunately, this donor won't donate now. Look for another."