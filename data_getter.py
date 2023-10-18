import requests
from bs4 import BeautifulSoup
import csv
import time

dates = ['2018-08-16', '2018-09-20', '2018-10-25', '2018-11-29', '2018-12-20', '2019-02-08', '2019-04-04', '2019-07-25', '2019-09-10', '2019-09-11', '2019-10-24', '2019-11-28', '2020-02-20', '2020-03-24', '2020-07-23', '2020-09-17', '2020-10-22', '2020-11-27', '2020-12-10', '2021-02-03', '2021-02-18', '2021-06-15', '2021-08-12', '2021-10-20', '2021-10-21', '2021-11-19', '2021-12-23', '2022-02-10', '2022-03-31', '2022-06-06', '2022-06-23', '2022-09-20', '2022-10-06', '2023-01-09', '2023-04-06', '2023-06-29', '2023-07-20', '2023-09-21']
i = 0
for date in dates:
    i+=1
    for u in range(1, 10):
        url = f'https://www.transfermarkt.com/statistik/weltrangliste/statistik/stat/ajax/yw1/datum/{date}/plus/0/galerie/0/page/{u}'

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')

        table = soup.find('table', class_='items')

        rows = table.find_all('tr')

        rankings = []

        for row in rows[1:]:
            cols = row.find_all('td')
            name = cols[1].text.strip()
            points_firstyear = cols[3].text.strip()

            rankings.append([name, points_firstyear])

        with open(f'fifa_rankings{i}_{u}.csv', 'w') as f:
            writer = csv.writer(f)
            writer.writerow(['name', 'points'])
            writer.writerows(rankings)
        time.sleep(0.01)