import pandas as pd
import os

data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'City': ['New York', 'Los Angeles', 'Chicago']}

df = pd.DataFrame(data)

# Ensure directory exist
data_dir = 'data'
os.makedirs(data_dir, exist_ok=True)

#Define file path
file_path = os.path.join(data_dir, 'people.csv')

#Save DataFrame to CSV
df.to_csv(file_path, index=False)   
print(f'DataFrame saved to {file_path}')

        