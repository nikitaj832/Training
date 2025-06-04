# Import a module with a different name using as
import pandas as pd

# Create a simple DataFrame using the alias 'pd'
data = {'Name': ['Amit', 'Neha'], 'Age': [24, 28]}
df = pd.DataFrame(data)

print(df)