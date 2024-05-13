import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from ipywidgets import widgets
import functions

def stats_analyzer(data_frame):
    copy_of_data_frame = data_frame.copy()
    print(copy_of_data_frame)
    numeric_df = copy_of_data_frame[['popularity', 'duration_ms', 'danceability', 'energy', 'loudness', 
                    'speechiness', 'acousticness', 'instrumentalness', 'liveness', 
                    'valence', 'tempo']]
    
    wants_fps = True
    while wants_fps:
        wants_fps_input = input("Do You Want to See Any Five-Point Summaries/Box Plots of Musical Data Based on a Genre? (yes/no): ")
        while not functions.yes_or_no(wants_fps_input):
            wants_fps_input = input("Not a Valid Response, Answer Yes or No If You Want to See a Five-Point Summary/Box Plot or Not (yes/no): ")
        wants_fps = wants_fps_input.lower() in ['yes', 'y']

        if wants_fps:
            print("Which Statistic Do You Want to Show a Boxplot and Generate a 5-Point Summary of?")
            for i, column_name in enumerate(numeric_df.columns):
                print(f"{i+1}: {column_name}")

            valid_input = False
            while not valid_input:
                filtered_feature_index = input(f"Please Pick a Valid Number Between 1-{len(numeric_df.columns)} to Choose Your Musical Feature: ")
                if filtered_feature_index.isdigit() and 1 <= int(filtered_feature_index) <= len(numeric_df.columns):
                    valid_input = True
                else:
                    print("Invalid input. Please enter a valid number.")

            filtered_feature_index = int(filtered_feature_index) - 1
            filtered_feature = numeric_df.iloc[:, filtered_feature_index]
            
            five_point_summary = filtered_feature.describe()
            print("Five-Point Summary:")
            print(five_point_summary)
            
            plt.figure(figsize=(8, 6))
            sns.boxplot(y=filtered_feature)
            plt.title(f"Box Plot of {numeric_df.columns[filtered_feature_index]}")
            plt.ylabel(numeric_df.columns[filtered_feature_index])
            plt.show()

             # Asks User if they want to compare two specific songs
            compare_songs = input("Do you want to compare specific songs? (yes/no): ")
            while not functions.yes_or_no(compare_songs):
                compare_songs = input("Invalid response. Please answer with yes or no: ")
            if compare_songs.lower() in ['yes', 'y']:
                valid_songs = False
                while not valid_songs:
                    song1 = input("Enter the name of the first song: ")
                    song2 = input("Enter the name of the second song: ")

                    # Check if the songs exist in the DataFrame
                    if (song1 in data_frame['song_name'].values) and (song2 in data_frame['song_name'].values):
                        valid_songs = True
                    else:
                        print("One or both of the songs are not in the dataset. Please choose again.")
                
                # Fetch details of the songs
                song1_details = data_frame[data_frame['song_name'] == song1].iloc[0]
                song2_details = data_frame[data_frame['song_name'] == song2].iloc[0]

                # Plot spider chart for comparison
                categories = list(numeric_df.columns)
                values_song1 = list(song1_details[numeric_df.columns])
                values_song2 = list(song2_details[numeric_df.columns])

                num_categories = len(categories)
                angles = [n / float(num_categories) * 2 * pi for n in range(num_categories)]
                angles += angles[:1]

                ax = plt.subplot(111, polar=True)
                plt.xticks(angles[:-1], categories, color='grey', size=8)
                ax.plot(angles, values_song1, linewidth=1, linestyle='solid', label=song1)
                ax.fill(angles, values_song1, 'b', alpha=0.1)
                ax.plot(angles, values_song2, linewidth=1, linestyle='solid', label=song2)
                ax.fill(angles, values_song2, 'r', alpha=0.1)
                plt.title(f"Comparison of {song1} and {song2}")
                plt.legend(loc='upper right', bbox_to_anchor=(0.1, 0.1))
                plt.show()

                print("\nComparison:")
                for i, category in enumerate(categories):
                    if values_song1[i] > values_song2[i]:
                        print(f"{song1} prevails in {category}")
                    elif values_song1[i] < values_song2[i]:
                        print(f"{song2} prevails in {category}")
                    else:
                        print(f"{song1} and {song2} have the same {category}")
