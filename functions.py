import pandas as pd

def yes_or_no(input_str):
    if input_str.lower() in ['yes', 'y', 'no', 'n']:
        return True
    else:
        return False
    
def genre_selector():
    pass

def duration_filter(meta_data):
    print("Filter duration:")
    for i in range(7):
        print(f"Select {i + 1} for {i}:{i+59}")

    input_valid = False
    while not input_valid:
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

    # Print the filtered DataFrame
    print("Songs in the selected duration category:")
    print(filtered_data[['track_name', 'duration_ms']])


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

# Function to filter songs by genre
def filter_songs_genre(meta_data):
    unique_genres = meta_data['track_genre'].unique()
    print("Select a genre from the options:")
    for index, genre in enumerate(unique_genres, start=1):
        print(f"{index}. {genre}")

    input_valid = False
    while not input_valid:
        genre_input = input("Please enter the genre you want to filter: ").lower()
        if genre_input not in unique_genres:
            print("The entered genre is not present in the dataset.")
        else:
            input_valid = True

    songs_with_genre = meta_data[meta_data['track_genre'] == genre_input]['track_name']
    for song in songs_with_genre:
        print(song)

# Function to filter songs by artist
def filter_songs_artist(artist, meta_data):
    songs_with_artist = meta_data[meta_data['artists'] == artist]
    songs_with_artist = songs_with_artist[['artists', 'track_name', 'album_name', 'popularity', 'duration_ms', 'track_genre']]
    print(songs_with_artist)

# Function to filter songs by album
def filter_songs_albums(album, meta_data):
    songs_with_album = meta_data[meta_data['album_name'] == album]['track_name']
    for song in songs_with_album:
        print(song)



def filter_songs_by_attributes(meta_data):
    input_valid = False
    while not input_valid:
        filter_attribute = input("Please enter which attribute you wish to filter the songs by: "
                                "1 for artists, 2 for track_name, 3 for album_name, 4 for popularity, "
                                "5 for duration_ms, or 6 for track_genre: ")
        if not filter_attribute.isnumeric():
            print("Please enter numbers only.")
        elif not 1 <= int(filter_attribute) <= 6:
            print("Please enter numbers between 1 and 6 only.")
        else:
            input_valid = True

    # Filter songs based on user's choice
    if int(filter_attribute) == 1:
        unique_artists = meta_data['artists'].unique()
        input_valid = False
        while not input_valid:
            artist_input = input("Please enter the artist you want to filter: ")
            if artist_input not in unique_artists:
                print("The entered artist is not present in the dataset.")
            else:
                input_valid = True
        filter_songs_artist(artist_input, meta_data)
    elif int(filter_attribute) == 2:
        unique_track_names = meta_data['track_name'].unique()
        input_valid = False
        while not input_valid:
            track_names_input = input("Please enter the track names you want to filter (Part of a Word or Whole Track): ")
            if track_names_input not in unique_track_names:
                print("The entered track name is not present in the dataset.")
            else:
                input_valid = True
        tracks = find_tracks_with_word(meta_data, track_names_input)
    elif int(filter_attribute) == 3:
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

    elif int(filter_attribute) == 4:
        popularity_filter(meta_data)

    elif int(filter_attribute) == 5:
        duration_filter(meta_data)

    elif int(filter_attribute) == 6:
        filter_songs_genre(meta_data)


def find_tracks_with_word(meta_data, select_word):
    """
    Finds tracks with titles containing the specified word.

    Args:
        meta_data (DataFrame): DataFrame containing track metadata, including 'track_name'.
        select_word (str): Word to search for within the track titles.

    Returns:
        list: List of track titles containing the specified word.
    """
    unique_tracks = meta_data['track_name'].unique()
    selected_tracks = []
    
    for track_name in unique_tracks:
        if not isinstance(track_name, float):  # Ensure the track name is not NaN
            if select_word.lower() in track_name.lower():
                selected_tracks.append(track_name)
    
    return selected_tracks



def get_valid_string(prompt):
    while True:
        user_input = input(prompt)
        if isinstance(user_input, str) and user_input.isalpha():
            return user_input
        else:
            print("Invalid input. Please enter a valid word (alphabetic characters only).")