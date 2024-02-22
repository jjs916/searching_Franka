# searching_Franka
Before run.
Install requirements
1. scholarly
2. pandas
3. openpyxl
4. xlsxwriter


Howto:
1. Run 'franka.py': check 'search_query', 'year' and 'possible_sources'.
2. It will collect data from google scholar. !Warning - frequent run of the code will block you. Also if there are too many results, you can be blocked.
3. Result will be in 'scholar_results_{year}.xlsx'
====
- If needed, 'dblp_venue.py' can crawl the list of titles from a specific conference/journal. The result will be in 'venues_data.xlsx'.
- 'duplication.py' will check and merge same titles from 'scholar_results_{year}.xlsx' and 'venues_data.xlsx'
