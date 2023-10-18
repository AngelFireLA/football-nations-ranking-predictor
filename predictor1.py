import pandas as pd
import numpy as np
from statsmodels.tsa.arima.model import ARIMA
import random

# Load your data
df = pd.read_csv('merged_fifa_rankings.csv')

# Define forecast length
forecast_length = 15

# Create a dictionary to store predictions
pred_dict = {}

for _, row in df.iterrows():
    country = row['name']

    # Drop countries with no data
    if row.dropna().count() < 2:
        continue

    country_series = row.drop('name').dropna().astype('float32')

    # Create a history list
    history = [x for x in country_series]

    # Create a list for predictions
    predictions = list()

    # Forecasting
    for t in range(forecast_length):
        model = ARIMA(history, order=(1, 1, 1))
        model_fit = model.fit()

        # Add one-step forecast to predictions
        yhat = model_fit.forecast()[0]

        # Add random noise to yhat
        random_noise = random.gauss(0, 1)
        yhat += random_noise

        # Round off to nearest tenth and append
        predictions.append(round(yhat, 1))

        # Add true observation to history for the next loop
        if t < len(country_series) - 1:
            history.append(country_series[t + 1])
        else:
            # Append predicted value to history as well
            history.append(yhat)

    # Add predictions to the dictionary
    pred_dict[country] = predictions

# Create a dataframe from dictionary and transpose
df_pred = pd.DataFrame(pred_dict).transpose()

# Create a datetime index for these forecasts
forecast_index = pd.date_range(start=df.columns[-1], periods=forecast_length + 1, freq='MS')[1:]

df_pred.columns = forecast_index

# Concatenate with the original dataframe
df.set_index('name', inplace=True)

output_df = pd.concat([df, df_pred], axis=1)

output_df.reset_index(inplace=True)
output_df.rename(columns={'index': 'name'}, inplace=True)

# Save to a CSV file
output_df.to_csv('output.csv', index=False)