import pandas as pd
from google.cloud import bigquery

client = bigquery.Client()

def make_prediction(inputs): 

    inputs_df = pd.DataFrame(
        inputs, 
        columns=["sepal_length", "sepal_width", "petal_length", "petal_width"]
        )
    
    QUERY = (
            'SELECT predicted_species FROM ML.PREDICT(MODEL `msds-434-final-377902.iris.model_log`, ('
                'SELECT '
                    'NULL AS id,'
                    +f'{inputs_df.loc[0, "sepal_length"]} AS sepal_length,'
                    +f'{inputs_df.loc[0, "sepal_width"]} AS sepal_width,'
                    +f'{inputs_df.loc[0, "petal_length"]} AS petal_length,'
                    +f'{inputs_df.loc[0, "petal_width"]} AS petal_width'

    +'))')
    query_job = client.query(QUERY)
    predictions = query_job.result()
    
    return predictions
