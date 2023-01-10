import pandas as pd

game_stat = pd.read_excel('data/game_statistics.xlsx')
game_stat_2122 = game_stat[(game_stat['Season']==20212022)&(game_stat['Pos.']!='G')]
game_stat_2122['TOI_All'] = game_stat_2122['TOI_All']/60

game_stat_2122.to_csv('data/game_stat_2122.csv')