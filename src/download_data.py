# author: Lennon Au-Yeung
# date: 2023-01-09

"""Downloads data from the web to the raw data file as csv file format.
Usage: src/download_data.py --url=<url> --out_file=<out_file>
Options:
--url=<url>              URL from where to download the data (must be in standard csv format)
--out_file=<out_file>    Path (including filename) of where to locally write the file
"""

from docopt import docopt
import requests
import os
import pandas as pd

opt = docopt(__doc__)

def main(url, out_file):
    '''
    Dowload the data from the url and save it in the desired location
    
    Parameters
    ----------    
    url: str
        url where the data can be extracted
    
    out_file: str
        location and file name for the data extracted
    '''
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

if __name__ == "__main__":
    main(opt["--url"], opt["--out_file"])

#adopted from https://github.com/ttimbers/breast_cancer_predictor/blob/master/src/download_data.py