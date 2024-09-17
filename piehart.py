import pandas as pd
import matplotlib.pyplot as plt

# Read data from CSV file
data = pd.read_csv('data.csv')

# Extract the data
categories = data['Category']
values = data['Value']

# Create a pie chart
plt.pie(values, labels=categories, autopct='%1.1f%%', startangle=140)
plt.title('Simple Pie Chart')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

# Display the pie chart
plt.show()
