import requests
import os
import pandas as pd

url = 'https://hockeystatisticscom.files.wordpress.com/2022/10/game_statistics.xlsx?force_download=true'

try: 
    request = requests.get(url)
    request.status_code == 200
except Exception as req:
    print("Website at the provided url does not exist.")
    print(req)

data = pd.read_excel(url)

out_file = 'data/raw/game_statistics.csv'

try:
    data.to_csv(out_file, index = False)
except:
    os.makedirs(os.path.dirname(out_file))
    data.to_csv(out_file, index = False)
 