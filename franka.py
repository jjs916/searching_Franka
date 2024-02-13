from scholarly import scholarly
import pandas as pd

def get_google_scholar_results(query, source):
    search_query = scholarly.search_pubs(f"{query} {source}", True, True, 2023, 2023)

    data_list = []

    for i, result in enumerate(search_query):
        data = result['bib']
        title = data.get('title', 'Title not available')
        venue = data.get('venue', 'Venue not available')

        print(f"Result {i + 1}:")
        print(f"Title: {title}")
        print(f"Venue: {venue}")
        print("------")

        data_list.append({'Title': title, 'Venue': venue})

    return data_list

if __name__ == "__main__":
    search_query = "franka emika"

    # List of possible sources
    possible_sources = ['source:ICRA site:ieee.org', 'source:IROS site:ieee.org', 'source:"Robotics and automation letters" site:ieee.org',
                        'source:"Transactions on Robotics" site:ieee.org', 'source:"Conference on Robot Learning" site:mlr.press',
                        'franka emika source:"case" site:ieee.org', 'source:"Humanoids" site:ieee.org', 'source:"IEEE Sensors" site:ieee.org']

    all_data = []

    for source in possible_sources:
        print(f"Results for source: {source}")
        data_list = get_google_scholar_results(search_query, source)
        all_data.extend(data_list)
        print("\n---\n")

    # Convert the list of dictionaries to a DataFrame
    df = pd.DataFrame(all_data)

    # Save the DataFrame to an Excel file
    excel_filename = "scholar_results.xlsx"
    df.to_excel(excel_filename, index=False)
    print(f"Data saved to {excel_filename}")

# from scholarly import scholarly

# def get_google_scholar_results(query, source):
#     search_query = scholarly.search_pubs(f"{query} {source}", True, True, 2023, 2023)

#     for i, result in enumerate(search_query):
#         data = result['bib']
#         title = data['title']
#         venue = data['venue']
#         print(f"Result {i + 1}:")
#         print("------")

# if __name__ == "__main__":
#     search_query = "franka emika"

#     # List of possible sources
#     possible_sources = ['source:ICRA site:ieee.org', 'source:IROS site:ieee.org', 'source:"Robotics and automation letters" site:ieee.org',
#                         'source:"Transactions on Robotics" site:ieee.org', 'source:"Conference on Robot Learning" site:mlr.press',
#                         'franka emika source:"case" site:ieee.org', 'source:"Humanoids" site:ieee.org', 'source:"IEEE Sensors" site:ieee.org']

#     for source in possible_sources:
#         print(f"Results for source: {source}")
#         get_google_scholar_results(search_query, source)
#         print("\n---\n")
