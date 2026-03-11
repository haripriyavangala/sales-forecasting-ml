### Create Visualization Script

import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_csv("data/sales_data.csv")

# Convert Date column
data["Date"] = pd.to_datetime(data["Date"])

# Sort values
data = data.sort_values("Date")

# Plot sales trend
plt.figure()

plt.plot(data["Date"], data["Weekly_Sales"])

plt.title("Sales Trend Over Time")
plt.xlabel("Date")
plt.ylabel("Sales")

plt.xticks(rotation=45)

plt.tight_layout()

# Save figure
plt.savefig("images/sales_trend_visualization.png")

plt.show()
