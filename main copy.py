import numpy as np
import pandas as pd

def filter_songs_genre(meta_data):
    unique_genres = meta_data['track_genre'].unique()
    print("Select a genre from the options:")
    
    # Printing numbered list of genres
    for index, genre in enumerate(unique_genres, start=1):
        print(f"{index}. {genre}")

    input_valid = False
    while not input_valid:
        genre_input = input("Please enter the genre you want to filter: ").lower()
        
        if genre_input not in unique_genres:
            print("The entered genre is not present in the dataset.")
        else:
            input_valid = True
    
    songs_with_genre = meta_data[meta_data['track_genre'] == genre_input]['track_name'].tolist()
    
    return songs_with_genre

def filter_songs_artist(meta_data):
    unique_artists = meta_data['artists'].unique()
    print("Select an artist from the options:")
    # Printing numbered list of artists
    for index, artist in enumerate(unique_artists, start=1):
        print(f"{index}. {artist}")

    input_valid = False
    while not input_valid:
        artist_input = input("Please enter the artist you want to filter: ")
        
        if artist_input not in unique_artists:
            print("The entered artist is not present in the dataset.")
        else:
            input_valid = True
            
    songs_with_artist = meta_data[meta_data['artists'] == artist_input]['track_name'].tolist()
    
    return songs_with_artist

def filter_songs_albums(meta_data):
    unique_albums = meta_data['album_name'].unique()
    print("Select an album from the options:")
    # Printing numbered list of albums
    for index, album in enumerate(unique_albums, start=1):
        print(f"{index}. {album}")

    input_valid = False
    while not input_valid:
        album_input = input("Please enter the album you want to filter: ")
        
        if album_input not in unique_albums:
            print("The entered album is not present in the dataset.")
        else:
            input_valid = True
        
    songs_with_album = meta_data[meta_data['album_name'] == album_input]['track_name'].tolist()
    
    return songs_with_album

        
data = pd.read_csv('downloads/dataset.csv')
meta_data = data[['track_id', 'artists', 'track_name', 'album_name', 'popularity', 'duration_ms', 'track_genre']]
music_data = data[['danceability', 'energy', 'key', 'loudness', 'mode', 'speechiness', 'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo', 'time_signature']]
print(meta_data.head())
print(music_data.head())

input_valid=False
while not input_valid:
    filter_attribute = input("Please enter which attribute you wish to filter the songs by: 1 for artists, 2 for track_name, 3 for album_name, 4 for popularity, 5 for duration_ms or 6 for track_genre: ")
    
    if not filter_attribute.isnumeric():
        print("Please enter numbers only.")
    elif not 1 <= int(filter_attribute) <= 6:
        print("Please enter numbers between 1 and 6 only.")
    else:
        input_valid = True

if int(filter_attribute)==1:
    filter_songs_artist()

if int(filter_attribute)==3:
    filter_songs_albums(album_input)
    
if int(filter_attribute)==4: 
    
    print(f"""Filter popularity:
    Select 1 for 0-10
    Select 2 for 11-20
    Select 3 for 21-30
    Select 4 for 31-40
    Select 5 for 41-50
    Select 6 for 51-60
    Select 7 for 61-70
    Select 8 for 71-80
    Select 9 for 81-90
    Select 10 for 91-100
""")
    
    input_valid=False
    while not input_valid:
        popularity_input=input("Please enter the corresponding number for popularity you want to filter.")
        
        if not popularity_input.isnumeric():
            print("Please enter numbers only.")
        elif not 1 <= int(popularity_input) <= 10:
            print("Please enter numbers between 1 and 10 only.")
        else:
            input_valid = True
    
# Define the bins for popularity ranges
    popularity_bins = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]  

    # Define the labels for the bins
    popularity_labels = ['0-10', '11-20', '21-30', '31-40', '41-50', '51-60', '61-70', '71-80', '81-90', '91-100']

    # Categorize songs based on their popularity
    meta_data['popularity_category'] = pd.cut(meta_data['popularity'], bins=popularity_bins, labels=popularity_labels, include_lowest=True)

    # Filter the DataFrame based on user-selected duration category
    selected_popularity_category = popularity_labels[int(popularity_input) - 1]
    filtered_data = meta_data[meta_data['popularity_category'] == selected_popularity_category]

    # Print the filtered DataFrame
    print("Songs in the selected popularity category:")
    print(filtered_data[['track_name', 'popularity']])
    
if int(filter_attribute)==5: 

    meta_data['duration_min_sec'] = pd.to_datetime(meta_data['duration_ms'], unit='ms').dt.strftime('%M:%S')
    
    #print(meta_data[['track_name', 'duration_min_sec']])   
    print(f"""Filter duration:
    Select 1 for 0:00 to 0:59
    Select 2 for 1:00 to 1:59
    Select 3 for 2:00 to 2:59
    Select 4 for 3:00 to 3:59
    Select 5 for 4:00 to 4:59
    Select 6 for 5:00 to 5:59
    Select 7 for 6:00 to 6:59""")
    
    input_valid=False
    while not input_valid:
        duration_input=input("Please enter the corresponding number for duration you want to filter.")
        
        if not duration_input.isnumeric():
            print("Please enter numbers only.")
        elif not 1 <= int(duration_input) <= 7:
            print("Please enter numbers between 1 and 7 only.")
        else:
            input_valid = True
    
# Define the bins for duration ranges
    duration_bins = [0, 60000, 120000, 180000, 240000, 300000, 360000, 420000]  # Assuming milliseconds

    # Define the labels for the bins
    duration_labels = ['0:00-0:59', '1:00-1:59', '2:00-2:59', '3:00-3:59', '4:00-4:59', '5:00-5:59', '6:00-6:59']

    # Categorize songs based on their duration
    meta_data['duration_category'] = pd.cut(meta_data['duration_ms'], bins=duration_bins, labels=duration_labels, include_lowest=True)

    # Filter the DataFrame based on user-selected duration category
    selected_duration_category = duration_labels[int(duration_input) - 1]
    filtered_data = meta_data[meta_data['duration_category'] == selected_duration_category]

    # Print the filtered DataFrame
    print("Songs in the selected duration category:")
    print(filtered_data[['track_name', 'duration_min_sec']])
    
if int(filter_attribute)==6:
    filter_songs_genre()