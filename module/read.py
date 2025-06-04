# Use pandas to read a CSV file and display the first few rows.

import pandas as pd

df = pd.read_csv("covid_toy.csv")

# Display the first 5 rows
print(df.head())


