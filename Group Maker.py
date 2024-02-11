import pandas as pd
import random

# Read the Excel file
file_path = "dataset.xlsx"
df = pd.read_excel(file_path)

# Shuffle the rows
shuffled_index = list(df.index)
random.shuffle(shuffled_index)

# Create a new DataFrame with shuffled rows
shuffled_df = df.iloc[shuffled_index]

# Group a few rows together
num_rows_per_group = 5
grouped_data = []
for group_num, i in enumerate(range(0, len(shuffled_df), num_rows_per_group), start=1):
    group = shuffled_df.iloc[i:i+num_rows_per_group]
    group['Group'] = group_num
    grouped_data.append(group)
    grouped_data.append(pd.DataFrame(index=[''] * 1, columns=group.columns))

grouped_df = pd.concat(grouped_data, ignore_index=True)

# output file
output_file_path = "grouped_data.xlsx"
grouped_df.to_excel(output_file_path, index=False)
