import numpy as np
import pandas as pd


data = pd.read_csv('./Data/dataset.csv')
meta_data = data[['track_id', 'artists', 'track_name', 'album_name', 'popularity', 'duration_ms']]
music_data = data[['danceability', 'energy', 'key', 'loudness', 'mode', 'speechiness', 'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo', 'time_signature']]
print(meta_data.head())
print(music_data.head())
print(data.columns.tolist)