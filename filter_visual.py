import matplotlib.pyplot as plt

#Import Plotting


def plot_genre_barchart(meta_data): #Plotting the Genre Histogram which Maps out How Many Songs in a Certain Genre
    
    unique_genres = meta_data['track_genre'].unique()
    
    input_valid = False
    
    while input_valid == False: #Genre Number Input (How Many?) (Min 1, Max 10)
        num_of_genres= input("Please enter the number of genres you want to enter")
        if not num_of_genres.isnumeric():
            print("Please enter numbers only.")
        elif not 1 <= int(num_of_genres) <= 10:
            print("You must have minimum 2 genres and maximum 10 genres.")
        else:
            input_valid = True  
            
    genres_to_compare = []
    #Initialize Empty List
    
    
    for _ in range(0,int(num_of_genres)): #Loop Through all the Genres and ask For Each Genre and Append it to the Input
        input_valid = False
        while not input_valid:
            genre_input = input("Please enter one of the genres you want to filter ").lower()
            
            if genre_input not in unique_genres:
                print("The entered genre is not present in the dataset.")
            else:
                genres_to_compare.append(genre_input)
                input_valid = True        
                
        #Make a Counter for the Genres (How Many Songs in Each Genre)
        genre_counts = meta_data[meta_data['track_genre'].isin(genres_to_compare)]['track_genre'].value_counts() 
    
    #Plot it in a histogram
    plt.figure(figsize=(10, 6))
    genre_counts.plot(kind='bar')
    
    
    plt.title('Number of Songs in Each Genre')
    plt.xlabel('Genre')
    plt.ylabel('Number of Songs')
    plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for better readability
    plt.tight_layout()
    
    #Show Histogram
    plt.show()