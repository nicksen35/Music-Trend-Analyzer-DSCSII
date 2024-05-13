import numpy as np
import pandas as pd
import statistical_analysis
import functions

# Read data
import pandas as pd

data = pd.read_csv('./data/dataset.csv')
meta_data = data[['artists', 'track_name', 'album_name', 'popularity', 'duration_ms', 'track_genre']]
music_data = data[['danceability', 'energy', 'key', 'loudness', 'mode', 'speechiness', 'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo', 'time_signature']]

primary_options = ["Music Data (Text)", "General Visualizations", "Visuals and Text"]
music_data_options = ["Show Data by Filter", "Search for Song Information", "Song Comparisons"]
general_visualization_options = ["Show Data by Filter", "Song Comparisons", "Five-Point Summary"]
visuals_and_text_options = ["Show Data by Filter", "Search for Song Information", "Song Comparisons"]

show_data_by_filter_visualization = ["Bar Chart", "Pie Chart", "Heatmap"]
song_comparison_filter_visualizations = ["Scatter Plots", "Radar Chart"]
five_ps_visualization = ["Histogram", "Box-Plot"]

def enumerate_options(options_list):
    for index, option in enumerate(options_list, 1):
        print(f"{index}. {option}")

def ask_user_input(options_list):
    enumerate_options(options_list)
    choice = int(input("Please choose an option by entering the corresponding number: "))
    while choice not in range(1, len(options_list) + 1):
        print("Invalid choice. Please choose a valid option.")
        enumerate_options(options_list)
        choice = int(input("Please choose an option by entering the corresponding number: "))
    return choice

def interface():
    interface_loop = True
    while interface_loop:
        primary_choice = ask_user_input(primary_options)
        if primary_choice == 1:  # Music Data (Text)
            music_data_choice = ask_user_input(music_data_options)
            if music_data_choice == 1:  # Show Data by Filter
                #music_data_filter = music_data_filter(meta_data)
                pass
            elif music_data_choice == 2:  # Search for Song Information
                # Implement search functionality for song information
                pass
            elif music_data_choice == 3:  # Song Comparisons
                #Implement Functionality
                pass
        elif primary_choice == 2:  # General Visualizations
            visualization_choice = ask_user_input(general_visualization_options)
            if visualization_choice == 1:  # Show Data by Filter
                visualization_type = ask_user_input(show_data_by_filter_visualization)
            elif visualization_choice == 2:  # Song Comparisons
                comparison_type = ask_user_input(song_comparison_filter_visualizations)
                # Perform comparison visualization (e.g., Scatter Plots, Radar Chart)
            elif visualization_choice == 3:  # Five-Point Summary
                summary_type = ask_user_input(five_ps_visualization)
                # Perform visualization for Five-Point Summary (e.g., Histogram, Box-Plot)
        elif primary_choice == 3:  # Visuals and Text
            visuals_text_choice = ask_user_input(visuals_and_text_options)
            # Implement functionality based on chosen option (similar to the above cases)
        else:
            print("Invalid choice. Please choose a valid option.")

interface()



interface()
#functions.filter_songs_by_attributes(meta_data)
#functions.statistical_analysis.stats_analyzer(data)
