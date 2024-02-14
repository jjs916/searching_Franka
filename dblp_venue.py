import dblp
import pandas as pd

conflist = ['icra', 'iros', 'humanoids', 'case', 'rss']  # corl does not have 2023 data
jourlist = ['ral']

# Create an empty list to store DataFrames
dfs = []

# Iterate through conference list
for conf in conflist:
    venues = dblp.venuesearch('conf', conf, '2023')

    # Load data for each venue
    for venue in venues:
        venue.load_data()

    # Assuming venue.data is a list of strings
    for venue in venues:
        venue.data = [item.rstrip('.') if item.endswith('.') else item for item in venue.data]

        # Create a DataFrame with two columns: Venue and Conference
        df = pd.DataFrame({
            'Venue': venue.data,
            'Conference': [conf] * len(venue.data)
        })

        # Append the DataFrame to the list
        dfs.append(df)

# Concatenate the list of DataFrames into a single DataFrame
df_combined = pd.concat(dfs, ignore_index=True)

# Save DataFrame to Excel file
df_combined.to_excel('venues_data.xlsx', index=False)

print("Data saved to 'venues_data.xlsx'")
