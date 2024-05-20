import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from ipywidgets import widgets
import functions

def display_five_point_summary(data_frame, column_name): #Display the five-point summary for a given column in the DataFrame.
    five_point_summary = data_frame[column_name].describe()
    print("Five-Point Summary:")
    print(five_point_summary)
    
    
def display_box_plot(data_frame, column_name): #Display the Box Plot
    plt.figure(figsize=(8, 6))
    sns.boxplot(y=data_frame[column_name])
    plt.title(f"Box Plot of {column_name}")
    plt.ylabel(column_name)
    plt.show()

def display_histogram(data_frame, column_name): #Display a Histogram
    plt.figure(figsize=(8, 6))
    sns.histplot(data_frame[column_name], kde=True)
    plt.title(f"Histogram of {column_name}")
    plt.xlabel(column_name)
    plt.ylabel("Frequency")
    plt.show()

def display_summary_and_box_plot(data_frame, column_name): #Output both the Five-Point Summary and Box Plot
    display_five_point_summary(data_frame, column_name)
    display_box_plot(data_frame, column_name)

def display_summary_box_plot_histogram(data_frame, column_name): #Output both the Five-Point Summary and Histogram and Box Plot

    display_five_point_summary(data_frame, column_name)
    display_box_plot(data_frame, column_name)
    display_histogram(data_frame, column_name)

def display_summary_histogram(data_frame, column_name): #Output both the Five-Point Summary and Histogram
    
    display_five_point_summary(data_frame, column_name)
    display_histogram(data_frame, column_name)
    
    
def display_histogram_box_plot(data_frame, column_name): #Output the Histogram and Box Plot
    display_box_plot(data_frame, column_name)
    display_histogram(data_frame, column_name)
    
    
def stats_analyzer(data_frame, user_choice): #Interface for all of these Functions
    
    #Work with Copy of Data Frame
    copy_of_data_frame = data_frame.copy()
    numeric_df = copy_of_data_frame[['popularity', 'duration_ms', 'danceability', 'energy', 'loudness', 
                                     'speechiness', 'acousticness', 'instrumentalness', 'liveness', 
                                     'valence', 'tempo']]
    
    wants_fps = True
    while wants_fps: #Input for Five-Point Summaries and Box Plot (Yes or No)
        wants_fps_input = input("Do You Want to See Any Five-Point Summaries/Box Plots of Musical Data Based on a Genre? (yes/no): ")
        while wants_fps_input.lower() not in ['yes', 'y', 'no', 'n']:
            wants_fps_input = input("Not a Valid Response, Answer Yes or No If You Want to See a Five-Point Summary/Box Plot or Not (yes/no): ")
        wants_fps = wants_fps_input.lower() in ['yes', 'y']

        if wants_fps: #If they want to see the information pick a statistic to see the analysis of it
        
            print("Which Statistic Do You Want to Show a Boxplot and Generate a 5-Point Summary of?")
            for i, column_name in enumerate(numeric_df.columns):
                print(f"{i+1}: {column_name}")

            valid_input = False
            while not valid_input: #Valid Input Checker
                filtered_feature_index = input(f"Please Pick a Valid Number Between 1-{len(numeric_df.columns)} to Choose Your Musical Feature: ")
                if filtered_feature_index.isdigit() and 1 <= int(filtered_feature_index) <= len(numeric_df.columns):
                    valid_input = True
                else:
                    print("Invalid input. Please enter a valid number.")
                    
            #Makes it an Index but Turns it into the Column Name for Filtering
            filtered_feature_index = int(filtered_feature_index) - 1
            filtered_feature = numeric_df.columns[filtered_feature_index]
            
            if user_choice == 'Summary': #5-Point Summary 
                display_five_point_summary(numeric_df, filtered_feature)
            elif user_choice == 'Box Plot': #Box Plot
                display_box_plot(numeric_df, filtered_feature)
            elif user_choice == 'Summary Box Plot': #5-Point Summary + Box Plot
                display_summary_and_box_plot(numeric_df, filtered_feature)
            elif user_choice == 'Histogram': #Histogram
                display_histogram(numeric_df, filtered_feature)
            elif user_choice == "Histogram Box Plot": #Histogram and Box Plot
                display_histogram_box_plot(numeric_df, filtered_feature)   
            elif user_choice == "Summary Histogram": #5-Point Summary + Histogram
                display_summary_histogram(numeric_df, filtered_feature)
            elif user_choice == "Everything": #Display Everything
                display_summary_box_plot_histogram(numeric_df, filtered_feature)