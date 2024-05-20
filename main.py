import pandas as pd

#Importing Pandas

import statistical_analysis
import functions
import radarchart
import filter_visual
import music_att_plot

#All Custom Made Modules Imported

import time

#Time Module Imported to Aesthetics

data = pd.read_csv('./Data/dataset.csv')

#Reading Data into Pandas Dataframe

meta_data = data[['artists', 'track_name', 'album_name', 'popularity', 'duration_ms', 'track_genre']]
music_data = data[['danceability', 'energy', 'key', 'loudness', 'mode', 'speechiness', 'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo', 'time_signature']]


#Splitting Dataframe into Meta Data and Music Data


primary_options = ["Music Data (Text)", "General Visualizations", "Visuals and Text", 'Quit']
music_data_options = ["Show Data by Filter", "Search for Song Information", "Song Comparisons"]
general_visualization_options = ["Search for Song Information", "Song Comparisons", "Five-Point Summary", "Genre Histogram", "Feature on Popularity"]
visuals_and_text_options = ["Search for Song Information", "Song Comparisons", "Five-Point Summary"]

song_comparison_filter_visualizations = ["Scatter Plots", "Radar Chart"]
five_ps_visualization = ["Histogram", "Box-Plot", "Both Histogram and Box-Plot"]

#Options for the Interface

def enumerate_options(options_list): #For Outputting the Options
    for index, option in enumerate(options_list, 1):
        print(f"{index}. {option}")



def ask_user_input(options_list): #Asking for the User Input of the Options
    
    # Print options for the user
    enumerate_options(options_list)
    
    input_valid = True
    # Prompt user for input
    while input_valid:
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

def interface(): #Interface Function with Full Foolproofing
    interface_loop = True
    
    print("------- Welcome to Sanify 🎵🎵 -------")
    time.sleep(2)
    
    while interface_loop: #Interface Loop
        
        primary_choice = ask_user_input(primary_options)
        
        if primary_choice == 1:  # Music Data (Text)
            music_data_choice = ask_user_input(music_data_options)
            
            if music_data_choice == 1:  # Show Data by Filter
                functions.filter_songs_by_attributes(meta_data)
                
            elif music_data_choice == 2:  # Search for Song Information
                word_to_search = functions.get_valid_string("What word do you wish to search a song with? ")
                songs_with_words = functions.find_tracks_with_word(meta_data, word_to_search)
                for i in songs_with_words:
                    print("Song Title:", i)
                print(f"Amount of Songs with Word '{word_to_search.capitalize()}':", len(songs_with_words))
                
            elif music_data_choice == 3:  # Song Comparisons
                radarchart.main("Compare Songs Text")
                
        elif primary_choice == 2:  # General Visualizations
            
            visualization_choice = ask_user_input(general_visualization_options)
            
            if visualization_choice == 1:  # Spider Chart for a Single Song
                radarchart.main('Spider Chart')
                
            elif visualization_choice == 2:  # Song Comparisons
                radarchart.main("Compare Songs")
                
            elif visualization_choice == 3:  # Five-Point Summary
                summary_type = ask_user_input(five_ps_visualization)
                
                if summary_type == 1: #Histogram
                    statistical_analysis.stats_analyzer(data, 'Histogram')
                    
                elif summary_type == 2: #Boxplot
                    print("Box Plot")
                    statistical_analysis.stats_analyzer(data, 'Box Plot')
                    
                elif summary_type == 3: #Histogram and Box Plot
                    statistical_analysis.stats_analyzer(data, 'Histogram Box Plot')
                    
            elif visualization_choice == 4: #Barchart of Genres of Songs
                filter_visual.plot_genre_barchart(meta_data)
                
                
            elif visualization_choice == 5: #Popularity against Musical Attributes
                music_att_plot.attribute_popularity_plot(meta_data, music_data)
                
                
        elif primary_choice == 3:  # Visuals and Text
            
            visuals_text_choice = ask_user_input(visuals_and_text_options)
            
            if visuals_text_choice == 1: #Radarchart and Text
                radarchart.main("Plot Everything")
                
                
            elif visuals_text_choice == 2: #Compare Songs and Text
                radarchart.main("Compare Songs Both")
                
                
            elif visuals_text_choice == 3: #Five Point Summaries
                box_plot_choice = ask_user_input(five_ps_visualization)
                
                if box_plot_choice == 1: #Histogram with Text
                    statistical_analysis.stats_analyzer(data, "Summary Histogram")
                    
                elif box_plot_choice == 2: #Box Plot with Text
                    statistical_analysis.stats_analyzer(data, "Summary Box Plot")
                    
                elif box_plot_choice == 3: #Histogram, Box Plot, Text
                    statistical_analysis.stats_analyzer(data, "Everything")
                    
                    
        elif primary_choice == 4: #Exiting the Application
            interface_loop = False
            print("\n------- Exiting -------")
            time.sleep(3)
            print("\n Thank you for Viewing Sanify :) ")
        else:
            print("Invalid choice. Please choose a valid option.")
        
        

interface()

#Load Interface