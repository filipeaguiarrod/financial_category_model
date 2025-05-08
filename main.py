from fastapi import FastAPI
from pydantic import BaseModel
import os
import joblib
app = FastAPI()

# Load the count vectorizer and the classifier model.
loaded_cv_path = os.path.join('model/', 'count_vectorizer.pkl')
loaded_model_path = os.path.join('model/', 'nn_classifier.pkl')

loaded_cv = joblib.load(loaded_cv_path)
loaded_model = joblib.load(loaded_model_path)


# Definir o formato do input usando Pydantic
class UserInput(BaseModel):
    lancamentos: list[str]  # Lista de strings

# Criar um endpoint que recebe um JSON no POST
@app.post("/greet/")
def greet_user(user: UserInput):

    predictions = []
    for lancamento in user.lancamentos:
        predict = loaded_model.predict(loaded_cv.transform([lancamento]))
        predictions.append(predict[0])
    return {'classifications': predictions, 'model':'nn_classifier'}