# Using the pandas module to create a simple DataFrame from a dictionary.

import pandas as pd

# Create a dictionary
data = {
    'Name': ['Ali', 'ram', 'Cherry'],
    'Age': [25, 30, 22],
    'City': ['New York', 'India', 'Chicago']
}

# Convert dictionary to DataFrame
df = pd.DataFrame(data)

# Display the DataFrame
print(df)