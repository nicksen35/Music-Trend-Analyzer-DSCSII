import numpy as np
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

def attribute_popularity_plot(meta_data, music_data): #Plotting Attributes Alongside Popularity 
    
    combined_data = pd.concat([meta_data, music_data], axis=1) #Combining Our Data

    print("Music attributes:", music_data.columns.tolist()) #Displaying all Musical Attributes to User

    input_valid = False
    while input_valid == False: #Selection of Musical Attribute
        music_attribute_input= input("Please enter a music attribute that you want to compare with popularity.")
        if  music_attribute_input not in music_data.columns:
            print("The entered genre is not present in the dataset.")
        else:
            input_valid = True        
            
    # Create scatter plot with a line of best fit
    plt.figure(figsize=(10, 6))
    
    #Seaborn Scatterplot with Regression
    sns.scatterplot(x=combined_data[music_attribute_input], y=combined_data['popularity'])
    sns.regplot(x=combined_data[music_attribute_input], y=combined_data['popularity'], scatter=False, color='r')
    
    #Labels and Titles
    plt.xlabel(music_attribute_input.capitalize())
    plt.ylabel('Popularity')
    plt.title(f'Effect of {music_attribute_input.capitalize()} on Popularity')
    
    #Displaying
    plt.show()    