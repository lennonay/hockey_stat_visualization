# Hockey Stat Visualization

## Authors

- Lennon Au-Yeung

## Data

The full data set was sourced from Hockey-Statistics and can be found [here](https://hockey-statistics.com/ls-gaa-2/). The xlsx format of the data can be directly downloaded using [this link](https://hockeystatisticscom.files.wordpress.com/2022/10/game_statistics.xlsx?force_download=true).


## Usage
To replicate the analysis done in this project, you can follow the steps below:

1. Create the environment using the following command
```
conda env create -f hockeystat.yaml
```

2. Clone the repository
```
git clone https://github.com/lennonay/hockey_stat_visualization.git
```

3. Downlaod Data
```
python src/download_data.py --url='https://hockeystatisticscom.files.wordpress.com/2022/10/game_statistics.xlsx?force_download=true' --out_file='data/raw/game_statistics.csv'
```

4. Preprocess data
```
python src/pen_preprocessing.py --data_location='data/raw/game_statistic∂s.csv' --output_location='data/processed/game_stat_2122.csv'
```
