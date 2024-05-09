import numpy as np
import pandas as pd


data = pd.read_csv('./Data/dataset.csv')
meta_data = data[['track_id', 'artists', 'track_name', 'album_name', 'popularity', 'duration_ms']]
music_data = data[['danceability', 'energy', 'key', 'loudness', 'mode', 'speechiness', 'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo', 'time_signature']]
print(meta_data.head())
print(music_data.head())
<<<<<<< HEAD
print(data.columns.tolist)

=======

print("Hello")
print("ByeBye")


print("this is surya")
>>>>>>> 59de579b9bdba337b03187d14abbf2c40067d0d9
