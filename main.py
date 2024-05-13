import numpy as np
import pandas as pd
import statistical_analysis


data = pd.read_csv('./Data/dataset.csv')

print(data.columns.tolist())
#statistical_analysis.stats_analyzer(data)
meta_data = data[['track_id', 'artists', 'track_name', 'album_name', 'popularity', 'duration_ms', 'track_genre']]

unique_tracks = meta_data['track_name'].unique()
select_word = input("Type a word that you want the following song titles to contain:")
selected_tracks = []
for track_name in unique_tracks:
    if not type(track_name) is float:
        if select_word.lower() in track_name.lower():
            selected_tracks.append(track_name)

print("Songs containing the word '{}' in their title:".format(select_word))
for track_name in selected_tracks:
    print(track_name)
