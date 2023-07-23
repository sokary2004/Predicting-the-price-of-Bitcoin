import requests
import numpy as np
import tensorflow as tf

# 1. Get Bitcoin price data from Coingecko API
response = requests.get('https://api.coingecko.com/api/v3/coins/bitcoin/market_chart?vs_currency=usd&days=30')
prices = [price[1] for price in response.json()['prices']]

# Prepare data for training
X = []
y = []

for i in range(len(prices)-30):
    X.append(prices[i:i+30])
    y.append(prices[i+30])

X = np.array(X)
y = np.array(y)

# 2. Build and train the neural network
model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(10, activation='relu'),
    tf.keras.layers.Dense(10, activation='relu'),
    tf.keras.layers.Dense(1)
])

model.compile(optimizer='adam', loss='mse')
model.fit(X, y, epochs=200, verbose=0)

# 3. Use regression to predict the next 7 days' prices
last_30_days = prices[-30:]
predicted_prices = []

for i in range(7):
    next_day_price = model.predict(np.array([last_30_days]))
    predicted_prices.append(next_day_price[0][0])
    last_30_days = np.append(last_30_days[1:], [next_day_price])

# 4. Print out the predicted prices and their minimum/maximum values for the next 7 days
for i, price in enumerate(predicted_prices):
    min_price = price * 0.95  # 5% lower than the predicted price
    max_price = price * 1.05  # 5% higher than the predicted price
    print(f"Predicted price for day {i+1}: {price:.2f} USD (min: {min_price:.2f} USD, max: {max_price:.2f} USD)")