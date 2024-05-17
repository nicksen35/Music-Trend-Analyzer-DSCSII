import numpy as np
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('./Data/dataset.csv')
meta_data = data[['track_id', 'artists', 'track_name', 'album_name', 'popularity', 'duration_ms', 'track_genre']]
music_data = data[['danceability', 'energy', 'key', 'loudness', 'mode', 'speechiness', 'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo', 'time_signature']]
combined_data = pd.concat([meta_data, music_data], axis=1)

def attribute_popularity_plot():    
    print("Music attributes:", music_data.columns.tolist())

    input_valid=False
    while input_valid==False:
        music_attribute_input= input("Please enter a music attribute that you want to compare with popularity.")
        if  music_attribute_input not in music_data.columns:
            print("The entered genre is not present in the dataset.")
        else:
            input_valid = True        
            
        # Create scatter plot with a line of best fit
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x=combined_data[music_attribute_input], y=combined_data['popularity'])
    
    sns.regplot(x=combined_data[music_attribute_input], y=combined_data['popularity'], scatter=False, color='r')
    plt.xlabel(music_attribute_input.capitalize())
    plt.ylabel('Popularity')
    plt.title(f'Effect of {music_attribute_input.capitalize()} on Popularity')
    plt.show()    