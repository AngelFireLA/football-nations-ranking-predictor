import pandas as pd
import os

# List of CSV files and the dates
file_names = [f'fifa_rankings{i}.csv' for i in range(105, 143)]
dates = {
    'fifa_rankings105.csv': '2018-08-16', 'fifa_rankings106.csv': '2018-09-20', 'fifa_rankings107.csv': '2018-10-25',
    'fifa_rankings108.csv': '2018-11-29', 'fifa_rankings109.csv': '2018-12-20', 'fifa_rankings110.csv': '2019-02-08',
    'fifa_rankings111.csv': '2019-04-04', 'fifa_rankings112.csv': '2019-07-25', 'fifa_rankings113.csv': '2019-09-10',
    'fifa_rankings114.csv': '2019-09-11', 'fifa_rankings115.csv': '2019-10-24', 'fifa_rankings116.csv': '2019-11-28',
    'fifa_rankings117.csv': '2020-02-20', 'fifa_rankings118.csv': '2020-03-24', 'fifa_rankings119.csv': '2020-07-23',
    'fifa_rankings120.csv': '2020-09-17', 'fifa_rankings121.csv': '2020-10-22', 'fifa_rankings122.csv': '2020-11-27',
    'fifa_rankings123.csv': '2020-12-10', 'fifa_rankings124.csv': '2021-02-03', 'fifa_rankings125.csv': '2021-02-18',
    'fifa_rankings126.csv': '2021-06-15', 'fifa_rankings127.csv': '2021-08-12', 'fifa_rankings128.csv': '2021-10-20',
    'fifa_rankings129.csv': '2021-10-21', 'fifa_rankings130.csv': '2021-11-19', 'fifa_rankings131.csv': '2021-12-23',
    'fifa_rankings132.csv': '2022-02-10', 'fifa_rankings133.csv': '2022-03-31', 'fifa_rankings134.csv': '2022-06-06',
    'fifa_rankings135.csv': '2022-06-23', 'fifa_rankings136.csv': '2022-09-20', 'fifa_rankings137.csv': '2022-10-06',
    'fifa_rankings138.csv': '2023-01-09', 'fifa_rankings139.csv': '2023-04-06', 'fifa_rankings140.csv': '2023-06-29',
    'fifa_rankings141.csv': '2023-07-20', 'fifa_rankings142.csv': '2023-09-21'
}

# Initialize an empty DataFrame
merged_data = pd.DataFrame()

# Loop through the files and merge them
for file_name in file_names:
    file_path = os.path.join('post_aout_2018', file_name)
    data = pd.read_csv(file_path)
    data = data.rename(columns={"points": dates[file_name]})
    data = data.set_index('name')
    if merged_data.empty:
        merged_data = data
    else:
        merged_data = merged_data.join(data, how='outer')

# Save the merged data to a new CSV file
merged_data.to_csv('merged_fifa_rankings.csv')

print("Merged CSV file has been created as 'merged_fifa_rankings.csv'")
