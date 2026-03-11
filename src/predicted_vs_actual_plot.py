import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor

# Load dataset
data = pd.read_csv("data/sales_data.csv")

data["Date"] = pd.to_datetime(data["Date"])

# Feature engineering
data["Month"] = data["Date"].dt.month
data["Year"] = data["Date"].dt.year

# Features
X = data[["Month", "Year"]]

# Target
y = data["Weekly_Sales"]

# Train model
model = RandomForestRegressor()

model.fit(X, y)

# Predictions
predictions = model.predict(X)

# Plot
plt.figure()

plt.plot(data["Date"], y, label="Actual Sales")
plt.plot(data["Date"], predictions, label="Predicted Sales")

plt.title("Actual vs Predicted Sales")
plt.xlabel("Date")
plt.ylabel("Sales")

plt.xticks(rotation=45)

plt.legend()

plt.tight_layout()

plt.savefig("images/predicted_vs_actual_sales.png")

plt.show()
