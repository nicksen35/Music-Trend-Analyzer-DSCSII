import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from math import pi

# Read the CSV file
data = pd.read_csv('./Data/dataset.csv')

# Selecting relevant attributes
attributes = ['danceability', 'energy', 'loudness', 'speechiness', 'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo']

def get_song_data(track_name):
    """
    Retrieve the music attributes for a given track name and prompt the user to select 
    if multiple songs are found.
    
    Parameters:
    - track_name: The name of the track to retrieve data for
    
    Returns:
    - song_data: DataFrame containing the song data if found, otherwise None
    """
    # Check if the track name exists in the dataset
    song_data = data[data['track_name'].str.lower() == track_name.lower()]
    
    if song_data.empty:
        print(f"No data found for track: {track_name}")
        return None

    if len(song_data) == 1:
        return song_data

    # If multiple songs found, display choices to the user
    print("Multiple songs found. Please select one:")
    for idx, row in song_data.iterrows():
        print(f"{idx}: {row['track_name']} by {row['artists']} from {row['album_name']}")

    # Prompt the user for a choice
    while True:
        try:
            choice = int(input("Enter the number corresponding to your choice: "))
            if choice in song_data.index:
                selected_song = song_data.loc[[choice]]  # Return as DataFrame
                print(selected_song)
                return selected_song
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def format_song_data(song_data):
    """
    Format the song data into a clean and formatted string.
    
    Parameters:
    - song_data: DataFrame row containing the song data
    
    Returns:
    - formatted_data: String containing the formatted song data
    """
    formatted_data = (
        f"\nSong Data:\n"
        f"Track Name: {song_data['track_name'].values[0]}\n"
        f"Artist(s): {song_data['artists'].values[0]}\n"
        f"Album: {song_data['album_name'].values[0]}\n"
        f"Danceability: {song_data['danceability'].values[0]}\n"
        f"Energy: {song_data['energy'].values[0]}\n"
        f"Loudness: {song_data['loudness'].values[0]}\n"
        f"Speechiness: {song_data['speechiness'].values[0]}\n"
        f"Acousticness: {song_data['acousticness'].values[0]}\n"
        f"Instrumentalness: {song_data['instrumentalness'].values[0]}\n"
        f"Liveness: {song_data['liveness'].values[0]}\n"
        f"Valence: {song_data['valence'].values[0]}\n"
        f"Tempo: {song_data['tempo'].values[0]}\n"
    )
    return formatted_data

def normalize_data(song_data, attributes):
    """
    Normalize the song data attributes to be between 0 and 1.
    
    Parameters:
    - song_data: DataFrame row containing the song data
    - attributes: List of attributes to normalize
    
    Returns:
    - normalized_values: List of normalized attribute values
    """
    normalized_values = []
    for attr in attributes:
        if attr == 'loudness':  # Normalizing loudness separately
            max_value = data[attr].max()
            min_value = data[attr].min()
            normalized_value = (song_data[attr].values[0] - min_value) / (max_value - min_value)
        else:
            max_value = data[attr].max()
            min_value = data[attr].min()
            normalized_value = (song_data[attr].values[0] - min_value) / (max_value - min_value)
        normalized_values.append(normalized_value)
    return normalized_values

def plot_spider_chart(song_data):
    """
    Plot a spider chart for the given song data.
    
    Parameters:
    - song_data: DataFrame row containing the song data
    """
    # Normalize the values for the relevant attributes
    values = normalize_data(song_data, attributes)
    
    # Number of variables
    num_vars = len(attributes)

    # Compute angle of each axis
    angles = [n / float(num_vars) * 2 * pi for n in range(num_vars)]
    angles += angles[:1]  # Complete the loop

    # Append the first value to values to close the loop
    values += values[:1]

    # Initialise the spider plot
    fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

    # Draw one axe per variable + add labels
    plt.xticks(angles[:-1], attributes)

    # Draw y-labels
    plt.yticks([0.2, 0.4, 0.6, 0.8, 1.0], ['0.2', '0.4', '0.6', '0.8', '1.0'], color='grey', size=7)
    plt.ylim(0, 1)

    # Plot data
    ax.plot(angles, values, linewidth=1, linestyle='solid')

    # Fill area
    ax.fill(angles, values, 'b', alpha=0.1)

    # Show the plot
    plt.title(f"Attributes of '{song_data['track_name'].values[0]}'")
    plt.show()

def main(option):
    # Prompt user to input a track name
    input_valid = False
    while not input_valid:
        track_name_input = input("Please enter the track name: ")
        
        # Validate the input track name
        if track_name_input not in data['track_name'].values:
            print("The entered track name is not present in the dataset. Please try again.")
        else:
            input_valid = True
            song_data = get_song_data(track_name_input)
    # Plot spider chart for the valid song data
    
    
    if option == 'Spider Chart':
        plot_spider_chart(song_data)
    else:
        print(format_song_data(song_data))
        plot_spider_chart(song_data)

