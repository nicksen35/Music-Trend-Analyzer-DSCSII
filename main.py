import numpy as np
import pandas as pd
import statistical_analysis
import functions
import radarchart
import filter_visual
import music_att_plot

# Read data
import pandas as pd

data = pd.read_csv('./Data/dataset.csv')

print(data.columns.tolist())
#statistical_analysis.stats_analyzer(data)
meta_data = data[['track_id', 'artists', 'track_name', 'album_name', 'popularity', 'duration_ms', 'track_genre']]


data = pd.read_csv('./data/dataset.csv')
meta_data = data[['artists', 'track_name', 'album_name', 'popularity', 'duration_ms', 'track_genre']]
music_data = data[['danceability', 'energy', 'key', 'loudness', 'mode', 'speechiness', 'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo', 'time_signature']]

primary_options = ["Music Data (Text)", "General Visualizations", "Visuals and Text"]
music_data_options = ["Show Data by Filter", "Search for Song Information", "Song Comparisons"]
general_visualization_options = ["Search for Song Information", "Song Comparisons", "Five-Point Summary", "Genre Histogram", "Feature on Popularity"]
visuals_and_text_options = ["Search for Song Information", "Song Comparisons", "Five-Point Summary"]

song_comparison_filter_visualizations = ["Scatter Plots", "Radar Chart"]
five_ps_visualization = ["Histogram", "Box-Plot", "Both Histogram and Box-Plot"]

def enumerate_options(options_list):
    for index, option in enumerate(options_list, 1):
        print(f"{index}. {option}")

def ask_user_input(options_list):
    """
    Prompt the user to choose an option from a list.
    
    Parameters:
    - options_list: List containing the options to choose from
    
    Returns:
    - choice: The chosen option (index + 1)
    """
    # Print options for the user
    enumerate_options(options_list)
    
    # Prompt user for input
    while True:
        choice_input = input("Please choose an option by entering the corresponding number: ").strip()
        
        # Check if input is not blank
        if choice_input:
            # Check if input is numeric
            if choice_input.isdigit():
                choice = int(choice_input)
                # Check if choice is within range
                if choice in range(1, len(options_list) + 1):
                    return choice
                else:
                    print("Invalid choice. Please choose a valid option.")
            else:
                print("Invalid input. Please enter a number.")
        else:
            print("Input cannot be blank. Please enter a number.")
        
        # Reprint options for the user
        enumerate_options(options_list)

def interface():
    interface_loop = True
    while interface_loop:
        primary_choice = ask_user_input(primary_options)
        if primary_choice == 1:  # Music Data (Text)
            music_data_choice = ask_user_input(music_data_options)
            if music_data_choice == 1:  # Show Data by Filter
                music_data_filter = functions.filter_songs_by_attributes(meta_data)
                
                pass
            elif music_data_choice == 2:  # Search for Song Information
                word_to_search = functions.get_valid_string("What word do you wish to search a song with? ")
                songs_with_words = functions.find_tracks_with_word(meta_data, word_to_search)
                for i in songs_with_words:
                    print("Song Title:", i)
                print(f"Amount of Songs with Word '{word_to_search.capitalize()}':", len(songs_with_words))
            elif music_data_choice == 3:  # Song Comparisons
                #Implement Functionality
                pass
        elif primary_choice == 2:  # General Visualizations
            visualization_choice = ask_user_input(general_visualization_options)
            if visualization_choice == 1:  # Show Data by Filter
                radarchart.main('Spider Chart')
            elif visualization_choice == 2:  # Song Comparisons
                comparison_type = ask_user_input(song_comparison_filter_visualizations)
                # Perform comparison visualization (e.g., Scatter Plots, Radar Chart)
            elif visualization_choice == 3:  # Five-Point Summary
                summary_type = ask_user_input(five_ps_visualization)
                if summary_type == 1:
                    statistical_analysis.stats_analyzer(data, 'Histogram')
                elif summary_type == 2:
                    print("Box Plot")
                    statistical_analysis.stats_analyzer(data, 'Box Plot')
                elif summary_type == 3:
                    statistical_analysis.stats_analyzer(data, 'Histogram Box Plot')
            elif visualization_choice == 4:
                filter_visual.plot_genre_barchart(meta_data)
            elif visualization_choice == 5:
                music_att_plot.attribute_popularity_plot()
        elif primary_choice == 3:  # Visuals and Text
            visuals_text_choice = ask_user_input(visuals_and_text_options)
            if visuals_text_choice == 1:
                radarchart.main("Plot Everything")
            elif visuals_text_choice == 2:
                pass
            elif visuals_text_choice == 3:
                box_plot_choice = ask_user_input(five_ps_visualization)
                if box_plot_choice == 1:
                    statistical_analysis.stats_analyzer(data, "Summary Histogram")
                elif box_plot_choice == 2:
                    statistical_analysis.stats_analyzer(data, "Summary Box Plot")
                elif box_plot_choice == 3:
                    statistical_analysis.stats_analyzer(data, "Everything")
                pass
            # Implement functionality based on chosen option (similar to the above cases)
        else:
            print("Invalid choice. Please choose a valid option.")

interface()