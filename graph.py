import pandas as pd
import matplotlib.pyplot as plt

# Read data from CSV file
data = pd.read_csv('data.csv')

# Extract the data
categories = data['Category']
values = data['Value']

# Create a bar graph
plt.bar(categories, values, color='blue')

# Add titles and labels
plt.title('Simple Bar Graph')
plt.xlabel('Category')
plt.ylabel('Value')

# Display the bar graph
plt.show()
