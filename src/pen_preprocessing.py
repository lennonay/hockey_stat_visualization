# author: Lennon Au-Yeung
# date: 2023-01-09

"""Filter the data to only 21-22 NHL season
Usage: src/pen_preprocessing.py --data_location=<data_location> --output_location=<output_location>
Options:
--data_location=<data_location>    Location of the data to be preprocessed
output_location=<output_location>  Location to output the train and test file
"""
from docopt import docopt
import pandas as pd

opt = docopt(__doc__)

def main(data_location, output_location):
    
    game_stat = pd.read_excel(data_location)
    game_stat_2122 = game_stat[(game_stat['Season']==20212022)&(game_stat['Pos.']!='G')]
    game_stat_2122['TOI_All'] = game_stat_2122['TOI_All']/60

    game_stat_2122.to_csv(output_location)
    
if __name__ == "__main__":
    main(opt["--data_location"], opt["--output_location"])