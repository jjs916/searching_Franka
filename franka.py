from scholarly import scholarly
import pandas as pd


def get_google_scholar_results(query, source, year_low, year_high):
    # search_query = scholarly.search_pubs(f"{query} {source}", True, True, year_low, year_high)#if you want to add specific venue, use this
    search_query = scholarly.search_pubs(f"{query}", True, True, year_low, year_high)#w/o venue

    data_list = []

    for i, result in enumerate(search_query):
        data = result['bib']
        title = data.get('title', 'Title not available')
        venue = data.get('venue', 'Venue not available')

        print(f"Result {i + 1}:")

        data_list.append({'Title': title, 'Venue': venue})

    return i + 1, data_list  # Return the count of results (i)

if __name__ == "__main__":
    # search_query = 'franka OR emika OR "panda arm" OR "panda robot" OR "panda gripper" OR "7 DOF panda" OR "panda manipulator" OR "panda cobot"'
    search_query = 'franka OR emika OR "panda arm" OR "panda gripper" OR "7 DOF panda" OR "panda manipulator" OR "panda cobot" "robot" -site:mlr.press -site:ieee.org'
    year = 2023

    # List of possible sources
    # possible_sources = ['-workshop source:ICRA', '-workshop source:IROS', 'source:"Robotics and automation letters"',
    #                     'source:"Transactions on Robotics" site:ieee.org', '-workshop source:"Conference on Robot Learning"',
    #                     '-workshop source:2023 IEEE "19th International Conference on Automation Science and Engineering (CASE)"',
    #                     '-workshop source:"Humanoids"', 'source:"IEEE Sensors journal"', 'source:arxiv']
    possible_sources = ['']
    
    # possible_sources = ['source:ICRA site:ieee.org', 'source:IROS site:ieee.org', 'source:"Robotics and automation letters" site:ieee.org',
    #                     'source:"Transactions on Robotics" site:ieee.org', 'source:"Conference on Robot Learning" site:mlr.press',
    #                     'source:"case" site:ieee.org', 'source:"Humanoids" site:ieee.org', 'source:"IEEE Sensors" site:ieee.org']

    all_data = []
    counts = {}

    for source in possible_sources:
        print(f"Results for source: {source}")
        count, data_list = get_google_scholar_results(search_query, source, year, year)
        all_data.extend(data_list)
        counts[source] = count
        print(f"Total results for {source}: {count}\n---\n")

    # Convert the list of dictionaries to a DataFrame
    df = pd.DataFrame(all_data)

    # Save the DataFrame to an Excel file
    excel_filename = f"scholar_results_{year}.xlsx"
    with pd.ExcelWriter(excel_filename, engine='xlsxwriter') as writer:
        df.to_excel(writer, sheet_name='Sheet1', index=False)
        # Create a new sheet for counts
        pd.DataFrame(list(counts.items()), columns=['Source', 'Result Count']).to_excel(writer, sheet_name='Sheet2', index=False)

    print(f"Data saved to {excel_filename}")