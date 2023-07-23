import requests
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# 1. Get Bitcoin price data from Coingecko API
url = "https://api.coingecko.com/api/v3/coins/bitcoin/market_chart"
params = {"vs_currency": "usd", "days": 10}
response = requests.get(url, params=params)
data = response.json()
#print(data)

# Extract the price data from the API response
prices = [p[1] for p in data["prices"]]

# Prepare the training data and labels
X = np.array(prices[:-1]).reshape(-1, 1)
y = np.array(prices[1:]).reshape(-1, 1)

# 2. Build and train the neural network
model = Sequential()
model.add(Dense(10, input_shape=(1,), activation="relu"))
model.add(Dense(10, activation="relu"))
model.add(Dense(1))
model.compile(optimizer="adam", loss="mse")
model.fit(X, y, epochs=100, verbose=0)

# 3. Use regression to predict the next day's price
last_price = np.array(prices[-1]).reshape(-1, 1)
predicted_price = model.predict(last_price)[0][0]

# 4. Print out the minimum and maximum predicted prices for the next day
print("Minimum predicted price:", predicted_price - 10)
print("Maximum predicted price:", predicted_price + 10)