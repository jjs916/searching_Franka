import pandas as pd

# Replace 'file1.xlsx' and 'file2.xlsx' with the paths to your Excel files
file1_path = 'scholar_results_2023.xlsx'
file2_path = 'venues_data.xlsx'

# Read Excel files into DataFrames
df1 = pd.read_excel(file1_path)
df2 = pd.read_excel(file2_path)

# Convert the relevant columns to lowercase for case-insensitive comparison
df1[df1.columns[0]] = df1[df1.columns[0]].str.lower()
df2[df2.columns[0]] = df2[df2.columns[0]].str.lower()

# Merge DataFrames on the lowercase version of the first column
common_data = pd.merge(df1, df2, how='inner', left_on=df1.columns[0], right_on=df2.columns[0])

# Save the result to a new Excel file including the desired columns by their indices
columns_to_save = [0, 1, 3]  # Adjust these indices based on your actual DataFrame structure
common_data.iloc[:, columns_to_save].to_excel('common_data.xlsx', index=False)

print("Common data saved to 'common_data.xlsx'")
