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
