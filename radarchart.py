import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from math import pi
import time

# Read the CSV file
data = pd.read_csv('./Data/dataset.csv')

# Selecting relevant attributes
attributes = ['danceability', 'energy', 'loudness', 'speechiness', 'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo']

def get_song_data(track_name): #Get the name of the song for radar chart
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


def format_song_data(song_data): #Format the Song Data into a Readable Format
    
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

def normalize_data(song_data, attributes): #Normalize the Attributes into acceptable data (Between 0 and 1)
    
    
    normalized_values = []
    for attr in attributes: #Handle Loudness Separately
        if attr == 'loudness':  # Normalizing loudness separately
            max_value = data[attr].max()
            min_value = data[attr].min()
            normalized_value = (song_data[attr].values[0] - min_value) / (max_value - min_value) #Min Max Normalization
        else:
            max_value = data[attr].max()
            min_value = data[attr].min()
            normalized_value = (song_data[attr].values[0] - min_value) / (max_value - min_value) #Min-Max Normalization
        normalized_values.append(normalized_value) #Append the Values to All Normalized Values
        
    return normalized_values

def plot_spider_chart(song_data): #Plotting the Spider Chart Given Song Data
    
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


def plot_compare_spider_chart(song_data1, song_data2): #Plots Two Points of Data on a Single Spider Chart
    
    
    # Normalize the values for the relevant attributes
    values1 = normalize_data(song_data1, attributes)
    values2 = normalize_data(song_data2, attributes)
    
    # Number of variables
    num_vars = len(attributes)

    # Compute angle of each axis
    angles = [n / float(num_vars) * 2 * pi for n in range(num_vars)]
    angles += angles[:1]  # Complete the loop

    # Append the first value to values to close the loop
    values1 += values1[:1]
    values2 += values2[:1]

    # Initialise the spider plot
    fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

    # Draw one axe per variable + add labels
    plt.xticks(angles[:-1], attributes)

    # Draw y-labels
    plt.yticks([0.2, 0.4, 0.6, 0.8, 1.0], ['0.2', '0.4', '0.6', '0.8', '1.0'], color='grey', size=7)
    plt.ylim(0, 1)

    # Plot data for song 1
    ax.plot(angles, values1, linewidth=1, linestyle='solid', label=song_data1['track_name'].values[0])
    ax.fill(angles, values1, 'b', alpha=0.1)

    # Plot data for song 2
    ax.plot(angles, values2, linewidth=1, linestyle='solid', label=song_data2['track_name'].values[0])
    ax.fill(angles, values2, 'r', alpha=0.1)

    # Show the plot
    plt.title("Comparison of Song Attributes")
    plt.legend(loc='upper right')
    plt.show()


def main(option): #Main File, Running all the Code --> Option Determines what to Output
    # Prompt user to input a track name
    input_valid = False
    while not input_valid: #Single Track Name Input
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
    elif option == 'Compare Songs' or option == 'Compare Songs Text' or option == 'Compare Songs Both': #If we are comparing, get second song data
        # Get data for second song
        input_valid = False
        while not input_valid:
            track_name_input_2 = input("Please enter the second track name: ")
            
            # Validate the input track name
            if track_name_input_2 not in data['track_name'].values:
                print("The entered second track name is not present in the dataset. Please try again.")
            else:
                input_valid = True
                song_data_2 = get_song_data(track_name_input_2)
        
        if option == 'Compare Songs Text' or option == 'Compare Songs Both': #Interface for Both Songs for Comparison
            print("--------- Song Data 1 ------- ")
            time.sleep(1)
            print(format_song_data(song_data))
            time.sleep(2)
            print("--------- Song Data 2 ------- ")
            time.sleep(1)
            print(format_song_data(song_data_2))
            time.sleep(2)
        if option == 'Compare Songs' or option == 'Compare Songs Both': #If we are not only displaying text, Display the rest
            plot_compare_spider_chart(song_data, song_data_2)
            
        
    else: #If we are not comparing, display the spider chart and the text
        print(format_song_data(song_data))
        plot_spider_chart(song_data)


