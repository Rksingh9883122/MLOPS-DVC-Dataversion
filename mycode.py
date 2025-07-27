import pandas as pd
import os

# Convert dictionary to DataFrame
data = pd.DataFrame({'Name': ['Alice', 'Bob', 'Charlie'],
                     'Age': [25, 30, 35],
                     'City': ['New York', 'Los Angeles', 'Chicago']})



df = pd.DataFrame(data)

# Append new row for 2nd version
new_row = {'Name': 'David', 'Age': 28, 'City': 'San Francisco'}
df.loc[len(df.index)] = new_row
print("DataFrame after appending new row:")

# Append new row for 3rd version
new_row = {'Name': 'Eve', 'Age': 22, 'City': 'Seattle'}
df.loc[len(df.index)] = new_row

# Ensure directory exist
data_dir = 'data'
os.makedirs(data_dir, exist_ok=True)

#Define file path
file_path = os.path.join(data_dir, 'people.csv')

#Save DataFrame to CSV
df.to_csv(file_path, index=False)   
print(f'DataFrame saved to {file_path}')

        