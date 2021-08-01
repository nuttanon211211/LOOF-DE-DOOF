from tensorflow.keras.models import model_from_json
import numpy as np
import pickle

class CardEffectModel(object):    
    
    EFFECT_LIST = ["DRAW", "HEAL",
                    "DAMAGE"]    
    
    def __init__(self, model_json_file, model_weights_file):
        # load model from JSON file
        with open(model_json_file, "r") as json_file:
            loaded_model_json = json_file.read()
            self.loaded_model = model_from_json(loaded_model_json)        
            
            # load weights into the new model
            self.loaded_model.load_weights(model_weights_file)
            self.loaded_model.make_predict_function()    
            
    def predict_effect(self, text):
        self.preds = self.loaded_model.predict(text)
        return CardEffectModel.EFFECT_LIST[np.argmax(self.preds)]
        
        
model = CardEffectModel("model.json", "model_weights.h5")

filename = 'vectorizer.sav'
loaded_vectorizer = pickle.load(open(filename, 'rb'))

def predictEffect(text):
    effects = np.array([text])
    X = loaded_vectorizer.transform(effects)
    results = model.predict_effect(X)
    return results
    
