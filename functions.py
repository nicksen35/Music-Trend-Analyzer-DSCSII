import pandas as pd
#Import Pandas


def yes_or_no(input_str): #Yes or No Function
    if input_str.lower() in ['yes', 'y', 'no', 'n']:
        return True
    else:
        return False


# Selecting relevant attributes
attributes = ['danceability', 'energy', 'loudness', 'speechiness', 'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo']

def genre_selector(meta_data): #Genre Selector - Display the 10 most popular songs from the selected genre
    
    unique_genres = meta_data['track_genre'].unique()
    
    print("Search and select a genre from the options:")
    
    search_valid = True
    
    while search_valid: #Search Loop for Key Word then Actual Genre
        
        genre_input = input("Please enter a keyword to search for a genre: ").lower()
        
        matched_genres = [genre for genre in unique_genres if genre_input in genre.lower()]
        
        if not matched_genres:
            print("No genres matched your search. Please try again.")
            
        else:
            print("\nMatching genres:")
            for genre in matched_genres:
                print(f"- {genre}")

            input_valid = False
            while not input_valid: #Filtering Feature
                selected_genre_input = input("Please enter the exact genre you want to filter: ").lower()
                if selected_genre_input in (genre.lower() for genre in matched_genres):
                    selected_genre = next(genre for genre in matched_genres if genre.lower() == selected_genre_input)
                    input_valid = True
                else:
                    print("The entered genre is not in the matched list. Please try again.")

            genre_songs = meta_data[meta_data['track_genre'] == selected_genre]

            # Sort by popularity and get the top 10
            top_10_songs = genre_songs.sort_values(by='popularity', ascending=False).head(10)
            
            print(f"\nTop 10 most popular songs in the genre '{selected_genre}':\n")
            
            for idx, song in top_10_songs.iterrows(): #Displaying the Songs of the Genres through Iterrows
                print(f"{idx + 1}. {song['track_name']} by {song['artists']} (Popularity: {song['popularity']})")
            search_valid = False #Ending the Loop

def duration_filter(meta_data): #Filtering by Durations
    print("Filter duration:")
    for i in range(7): #Loop from 0-7 Minutes
        print(f"Select {i + 1} for {i}:00-{i}:59")

    input_valid = False
    while not input_valid: #User Input for Duration
        duration_input = input("Please enter the corresponding number for duration you want to filter: ")
        if not duration_input.isnumeric():
            print("Please enter numbers only.")
        elif not 1 <= int(duration_input) <= 7:
            print("Please enter numbers between 1 and 7 only.")
        else:
            input_valid = True

    # Define the bins for duration ranges
    duration_bins = [0, 60000, 120000, 180000, 240000, 300000, 360000, 420000]

    # Define the labels for the bins
    duration_labels = ['0:00-0:59', '1:00-1:59', '2:00-2:59', '3:00-3:59', '4:00-4:59', '5:00-5:59', '6:00-6:59']

    # Categorize songs based on their duration
    meta_data['duration_category'] = pd.cut(meta_data['duration_ms'], bins=duration_bins, labels=duration_labels,
                                            include_lowest=True)

    # Filter the DataFrame based on user-selected duration category
    selected_duration_category = duration_labels[int(duration_input) - 1]
    filtered_data = meta_data[meta_data['duration_category'] == selected_duration_category]

    # Sort by popularity and get the top 10
    top_10_songs = filtered_data.sort_values(by='popularity', ascending=False).head(10)

    # Print the filtered DataFrame
    print(f"\nTop 10 most popular songs in the duration category '{selected_duration_category}':\n")
    for idx, song in top_10_songs.iterrows():
        print(f"{idx + 1}. {song['track_name']} by {song['artists']} (Duration: {song['duration_ms']} ms, Popularity: {song['popularity']})")

def popularity_filter(meta_data): #Fiilter by Popularity
    print("Filter popularity:")
    for i in range(1, 11): #Popularities from 0-100
        print(f"Select {i} for {i * 10 - 9}-{i * 10}")

    input_valid = False
    while not input_valid: #User Input
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

    # Sort by popularity and get the top 10
    top_10_songs = filtered_data.sort_values(by='popularity', ascending=False).head(10)

    # Print the filtered DataFrame
    print(f"\nTop 10 most popular songs in the popularity category '{selected_popularity_category}':\n")
    for idx, song in top_10_songs.iterrows():
        print(f"{idx + 1}. {song['track_name']} by {song['artists']} (Popularity: {song['popularity']})")

# Function to filter songs by genre
def filter_songs_genre(meta_data):
    unique_genres = meta_data['track_genre'].unique()
    print("Select a genre from the options:")
    for index, genre in enumerate(unique_genres, start=1):
        print(f"{index}. {genre}")

    input_valid = False
    while not input_valid: #User Input
        genre_input = input("Please enter the number corresponding to the genre you want to filter: ").lower()
        if not genre_input.isnumeric():
            print("Please enter numbers only.")
        elif not 1 <= int(genre_input) <= len(unique_genres):
            print(f"Please enter a number between 1 and {len(unique_genres)}.")
        else:
            input_valid = True

    selected_genre = unique_genres[int(genre_input) - 1]
    genre_songs = meta_data[meta_data['track_genre'] == selected_genre]

    # Sort by popularity and get the top 10
    top_10_songs = genre_songs.sort_values(by='popularity', ascending=False).head(10)

    print(f"\nTop 10 most popular songs in the genre '{selected_genre}':\n")
    for idx, song in top_10_songs.iterrows(): #Iterate Through All Songs
        print(f"{idx + 1}. {song['track_name']} by {song['artists']} (Popularity: {song['popularity']})")

# Function to filter songs by artist
def filter_songs_artist(artist, meta_data):
    songs_with_artist = meta_data[meta_data['artists'] == artist]

    # Sort by popularity and get the top 10
    top_10_songs = songs_with_artist.sort_values(by='popularity', ascending=False).head(10)

    print(f"\nTop 10 most popular songs by artist '{artist}':\n")
    for idx, song in top_10_songs.iterrows(): #Iterate Through All Songs
        print(f"{idx + 1}. {song['track_name']} from the album '{song['album_name']}' (Popularity: {song['popularity']}, Duration: {song['duration_ms']} ms)")

# Function to filter songs by album
def filter_songs_albums(album, meta_data):
    songs_with_album = meta_data[meta_data['album_name'] == album]

    # Sort by popularity and get the top 10
    top_10_songs = songs_with_album.sort_values(by='popularity', ascending=False).head(10)

    print(f"\nTop 10 most popular songs in the album '{album}':\n")
    for idx, song in top_10_songs.iterrows(): #Iterate through all Songs
        print(f"{idx + 1}. {song['track_name']} by {song['artists']} (Popularity: {song['popularity']}, Duration: {song['duration_ms']} ms)")

def filter_songs_by_attributes(meta_data): #Interface for Filtering
    input_valid = False
    while not input_valid: #All Functions Present in Interface
        filter_attribute = input("Please enter which attribute you wish to filter the songs by:\n"
                                 "1 for artists\n"
                                 "2 for track name\n"
                                 "3 for album name\n"
                                 "4 for popularity\n"
                                 "5 for duration\n"
                                 "6 for track genre\n"
                                 "Enter your choice: ")
        if not filter_attribute.isnumeric(): #Number Check
            print("Please enter numbers only.")
        elif not 1 <= int(filter_attribute) <= 6: #Numbers 1 through 6 Only
            print("Please enter numbers between 1 and 6 only.")
        else:
            input_valid = True

    # Filter songs based on user's choice
    
    if int(filter_attribute) == 1: #Artist Filtering
        unique_artists = meta_data['artists'].unique()
        input_valid = False
        
        while not input_valid:
            artist_input = input("Please enter the artist you want to filter: ")
            
            if artist_input not in unique_artists:
                print("The entered artist is not present in the dataset.")
                
            else:
                input_valid = True
                
        filter_songs_artist(artist_input, meta_data)
        
    elif int(filter_attribute) == 2: #Track Name Filtering
        unique_track_names = meta_data['track_name'].unique()
        input_valid = False
        
        while not input_valid:
            track_names_input = input("Please enter the track names you want to filter (Part of a Word or Whole Track): ")
            if track_names_input not in unique_track_names:
                print("The entered track name is not present in the dataset.")
                
            else:
                input_valid = True
                
        find_tracks_with_word(meta_data, track_names_input)
        
    elif int(filter_attribute) == 3: #Album Name Filtering
        
        unique_albums = meta_data['album_name'].unique()
        print("Select an album from the options:")

        input_valid = False
        while not input_valid:
            album_input = input("Please enter the album you want to filter: ")
            
            if album_input not in unique_albums:
                print("The entered album is not present in the dataset.")
                
            else:
                input_valid = True
                
        filter_songs_albums(album_input, meta_data)

    elif int(filter_attribute) == 4: #Popularity Filtering
        popularity_filter(meta_data)

    elif int(filter_attribute) == 5: #Duration Filtering
        duration_filter(meta_data)

    elif int(filter_attribute) == 6: #Genre Selector 
        genre_selector(meta_data)
        
        
def find_tracks_with_word(meta_data, select_word): #Searching Albums based on Track Name either Part of the Name or Full Name
    """
    Finds the top 10 tracks with titles containing the specified word, sorted by popularity.

    Args:
        meta_data (DataFrame): DataFrame containing track metadata, including 'track_name' and 'popularity'.
        select_word (str): Word to search for within the track titles.

    Returns:
        DataFrame: DataFrame of the top 10 tracks containing the specified word, sorted by popularity.
    """
    # Filter tracks containing the specified word in their titles
    filtered_tracks = meta_data[meta_data['track_name'].str.contains(select_word, case=False, na=False)]
    
    # Sort by popularity and get the top 10
    top_10_tracks = filtered_tracks.sort_values(by='popularity', ascending=False).head(10)
    
    # Display the top 10 tracks
    print(f"\nTop 10 most popular songs with the word '{select_word}' in the title:\n")
    for idx, song in top_10_tracks.iterrows():
        print(f"{idx + 1}. {song['track_name']} by {song['artists']} (Popularity: {song['popularity']})")
    
    return top_10_tracks


def get_valid_string(prompt): #Valid String Check
    
    while True:
        user_input = input(prompt)
        if isinstance(user_input, str) and user_input.isalpha():
            return user_input
        else:
            print("Invalid input. Please enter a valid word (alphabetic characters only).")
