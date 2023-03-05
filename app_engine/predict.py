import joblib 
import pandas as pd
import tensorflow as tf


model = tf.keras.models.load_model("gs://msds-434-final-377902.appspot.com/model_log/saved_model.pb")

def make_prediction(inputs): 
    """
    Make a prediction using the trained model 
    """
    inputs_df = pd.DataFrame(
        inputs, 
        columns=["sepal_length", "sepal_width", "petal_length", "petal_width"]
        )
    predictions = model.predict(inputs_df)
    
    return predictions
