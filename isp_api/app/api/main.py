import pickle
from fastapi import FastAPI
from model_training.features import featureExtraction

def pr(url):
    
    # load model from file
    loaded_model = pickle.load(open("model_training\XGBoostClassifier.pickle.dat", "rb"))

    X = featureExtraction(url)
    print(X)

    # X eke values model ekata yanaw widiha wradi eka balanna
    predict = loaded_model.predict(X)
    
    return predict

app = FastAPI()

@app.post("/predict")
async def predict(url: str):
    
    return pr(url)