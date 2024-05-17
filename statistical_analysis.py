import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from ipywidgets import widgets
import functions

def display_five_point_summary(data_frame, column_name):
    """
    Display the five-point summary for a given column in the DataFrame.
    
    Parameters:
    - data_frame: The DataFrame containing the data
    - column_name: The column for which to display the five-point summary
    """
    five_point_summary = data_frame[column_name].describe()
    print("Five-Point Summary:")
    print(five_point_summary)
    
    
def display_box_plot(data_frame, column_name):
    """
    Display a box plot for a given column in the DataFrame.
    
    Parameters:
    - data_frame: The DataFrame containing the data
    - column_name: The column for which to display the box plot
    """
    plt.figure(figsize=(8, 6))
    sns.boxplot(y=data_frame[column_name])
    plt.title(f"Box Plot of {column_name}")
    plt.ylabel(column_name)
    plt.show()

def display_histogram(data_frame, column_name):
    """
    Display a histogram for a given column in the DataFrame.
    
    Parameters:
    - data_frame: The DataFrame containing the data
    - column_name: The column for which to display the histogram
    """
    plt.figure(figsize=(8, 6))
    sns.histplot(data_frame[column_name], kde=True)
    plt.title(f"Histogram of {column_name}")
    plt.xlabel(column_name)
    plt.ylabel("Frequency")
    plt.show()

def display_summary_and_box_plot(data_frame, column_name):
    """
    Display both the five-point summary and box plot for a given column in the DataFrame.
    
    Parameters:
    - data_frame: The DataFrame containing the data
    - column_name: The column for which to display the summary and box plot
    """
    display_five_point_summary(data_frame, column_name)
    display_box_plot(data_frame, column_name)

def display_summary_box_plot_histogram(data_frame, column_name):
    """
    Display the five-point summary, box plot, and histogram for a given column in the DataFrame.
    
    Parameters:
    - data_frame: The DataFrame containing the data
    - column_name: The column for which to display the summary, box plot, and histogram
    """
    display_five_point_summary(data_frame, column_name)
    display_box_plot(data_frame, column_name)
    display_histogram(data_frame, column_name)

def display_summary_histogram(data_frame, column_name):
    display_five_point_summary(data_frame, column_name)
    display_histogram(data_frame, column_name)
    
    
def display_histogram_box_plot(data_frame, column_name):
    display_box_plot(data_frame, column_name)
    display_histogram(data_frame, column_name)
    
    
def stats_analyzer(data_frame, user_choice):
    """
    Main function to prompt user for input and display five-point summary and/or box plot.
    
    Parameters:
    - data_frame: The DataFrame containing the data
    """
    copy_of_data_frame = data_frame.copy()
    numeric_df = copy_of_data_frame[['popularity', 'duration_ms', 'danceability', 'energy', 'loudness', 
                                     'speechiness', 'acousticness', 'instrumentalness', 'liveness', 
                                     'valence', 'tempo']]
    
    wants_fps = True
    while wants_fps:
        wants_fps_input = input("Do You Want to See Any Five-Point Summaries/Box Plots of Musical Data Based on a Genre? (yes/no): ")
        while wants_fps_input.lower() not in ['yes', 'y', 'no', 'n']:
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
            filtered_feature = numeric_df.columns[filtered_feature_index]
            if user_choice == 'Summary':
                display_five_point_summary(numeric_df, filtered_feature)
            elif user_choice == 'Box Plot':
                display_box_plot(numeric_df, filtered_feature)
            elif user_choice == 'Summary Box Plot':
                display_summary_and_box_plot(numeric_df, filtered_feature)
            elif user_choice == 'Histogram':
                display_histogram(numeric_df, filtered_feature)
            elif user_choice == "Histogram Box Plot":
                display_histogram_box_plot(numeric_df, filtered_feature)   
            elif user_choice == "Summary Histogram":
                display_summary_histogram(numeric_df, filtered_feature)
            elif user_choice == "Everything":
                display_summary_box_plot_histogram(numeric_df, filtered_feature)

def popularity_filter(meta_data):
    print("Filter popularity:")
    for i in range(1, 11):
        print(f"Select {i} for {i * 10 - 9}-{i * 10}")

    input_valid = False
    while not input_valid:
        popularity_input = input("Please enter the corresponding number for popularity you want to filter: ")
        if not popularity_input.isnumeric():
            print("Please enter numbers only.")
        elif not 1 <= int(popularity_input) <= 10:
            print("Please enter numbers between 1 and 10 only.")
        else:
            input_valid = True

    # Define the bins for popularity ranges
    popularity_bins = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    popularity_labels = ['0-10', '11-20', '21-30', '31-40', '41-50', '51-60', '61-70', '71-80', '81-90', '91-100']

    # Categorize songs based on their popularity
    meta_data['popularity_category'] = pd.cut(meta_data['popularity'], bins=popularity_bins, labels=popularity_labels,
                                               include_lowest=True)
    # Filter the DataFrame based on user-selected popularity category
    selected_popularity_category = popularity_labels[int(popularity_input) - 1]
    filtered_data = meta_data[meta_data['popularity_category'] == selected_popularity_category]

    # Print the filtered DataFrame
    print("Songs in the selected popularity category:")
    print(filtered_data[['track_name', 'popularity']])