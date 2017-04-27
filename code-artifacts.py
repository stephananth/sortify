# Stephanie K. Ananth (sananth)

# Adapted from Paul Lamere's examples
# https://github.com/plamere/spotipy

import os

import spotipy
import spotipy.util as util

# Client Credentials from Spotify Developer
os.environ['SPOTIPY_CLIENT_ID'] = '5c14698fcf8e41adb4f39b5518e55100'
os.environ['SPOTIPY_CLIENT_SECRET'] = '355d085eaf6049a1bda2e8dff93bdefd'
os.environ['SPOTIPY_REDIRECT_URI'] = 'https://www.cs.cmu.edu/~112/index.html'


# Takes a username and term (short_term, medium_term, long_term) in strings
# Returns a list of the user's top songs' URIs of number of songs in an int
def list_top_songs_by_term(username, term, n=100):
    result = []
    # Scope is the level of authentification to execute the desired function
    scope = 'user-top-read'
    token = util.prompt_for_user_token(username, scope)
    sp = spotipy.Spotify(auth=token)
    sp.trace = False
    results = sp.current_user_top_tracks(time_range=term, limit=n)
    for item in results['items']:
        result += [item['uri']]
    return result


# Takes a username and term (short_term, medium_term, long_term) in strings
# Returns a list of the user's top artists' URIs of n artists in an integer
def list_top_artists_by_term(username, term, n=10):
    result = []
    scope = 'user-top-read'
    token = util.prompt_for_user_token(username, scope)
    sp = spotipy.Spotify(auth=token)
    sp.trace = False
    results = sp.current_user_top_artists(time_range=term, limit=n)
    for item in results['items']:
        result += [item['uri']]
    return result


# Takes an artist URI in a string
# Returns a list of their n (up to 10) top songs' URIs
def list_top_songs_by_artist(artist_uri, n=10):
    result = []
    sp = spotipy.Spotify()
    results = sp.artist_top_tracks(artist_uri)
    for track in results['tracks']:
        result += [track['uri']]
    return result[:n]


# Takes a username in a string and a name for the new playlist in a string
# Creates empty Spotify playlist for the user in the playlist name
# Returns the playlist's URI in a string
def create_playlist(username, playlist_name):
    scope = 'user-library-modify'
    token = util.prompt_for_user_token(username, scope)
    sp = spotipy.Spotify(auth=token)
    sp.trace = False
    playlist = sp.user_playlist_create(username, playlist_name)
    return playlist['uri']


# Takes a username and a playlist URI in a string and song URIs in a list
# Adds the song to the user's playlist, returns None
def add_songs_to_playlist(username, playlist_uri, song_uris):
    scope = 'playlist-modify-public'
    token = util.prompt_for_user_token(username, scope)
    sp = spotipy.Spotify(auth=token)
    sp.trace = False
    results = sp.user_playlist_add_tracks(username, playlist_uri, song_uris)


# Takes a username and a term (short, medium, long) in a string
# Creates a new playlist for the user of their top songs for that term
def create_playlist_top_songs_by_term(username, term, n=100):
    playlist = create_playlist(username, term + '_top_songs')
    songs = list_top_songs_by_term(username, term, n)
    add_songs_to_playlist(username, playlist, songs)


# Takes a username and a term (short, medium, long) in a string
# Creates a new playlist for the user of their top artists' songs for that term
def create_playlist_top_artists_by_term(username, term, n=20, m=5):
    playlist = create_playlist(username, term + '_artist_top_songs')
    artists = list_top_artists_by_term(username, term, 20)
    songs = []
    for artist in artists:
        songs += list_top_songs_by_artist(artist, 5)
    add_songs_to_playlist(username, playlist, songs)


# Takes a username in a string
# Creates playlists for their top songs for each term
# And for their top artists' top songs for each term
def create_playlists_top_songs(username, n=100, m=20, l=5):
    for term in ['short_term', 'medium_term', 'long_term']:
        create_playlist_top_songs_by_term(username, term, n)
        create_playlist_top_artists_by_term(username, term, m, l)


# Takes a username in a string
# Returns a list of the user's top songs that are unique to short term
def list_new_favorites(username):
    result = []
    new = list_top_songs_by_term(username, 'short_term', 100)
    mid = list_top_songs_by_term(username, 'medium_term', 100)
    old = list_top_songs_by_term(username, 'long_term', 100)
    for song in new:
        if ((song not in mid) and (song not in old)):
            result += [song]
    return result


# Takes a username in a string
# Creates a playlist for a user's top songs unique to short term
def create_playlist_new_favorites(username):
    playlist = create_playlist(username, 'new_favorites')
    songs = list_new_favorites(username)
    add_songs_to_playlist(username, playlist, songs)


# Takes a username in a string
# Returns a list of the user's top songs that are unique to long term
def list_old_favorites(username):
    result = []
    new = list_top_songs_by_term(username, 'short_term', 100)
    mid = list_top_songs_by_term(username, 'medium_term', 100)
    old = list_top_songs_by_term(username, 'long_term', 100)
    for song in old:
        if ((song not in mid) and (song not in new)):
            result += [song]
    return result


# Takes a username in a string
# Creates a playlist of the user's top songs unique to long term
def create_playlist_old_favorites(username):
    playlist = create_playlist(username, 'old_favorites')
    songs = list_old_favorites(username)
    add_songs_to_playlist(username, playlist, songs)


# Takes a username in a string
# Returns a list of songs common to all terms
def list_alltime_favorites(username):
    result = []
    new = list_top_songs_by_term(username, 'short_term', 100)
    mid = list_top_songs_by_term(username, 'medium_term', 100)
    old = list_top_songs_by_term(username, 'long_term', 100)
    for song in mid:
        if ((song in new) and (song in old)):
            result += [song]
    return result


# Takes a username in a string
# Creates a playlist of the top songs common to all terms
def create_playlist_alltime_favorites(username):
    playlist = create_playlist(username, 'all_time_favorites')
    songs = list_alltime_favorites(username)
    add_songs_to_playlist(username, playlist, songs)


# Takes a username in a string
# Returns a list of top artists common to all terms
def list_alltime_favorite_artists(username, n=20):
    result = []
    new = list_top_artists_by_term(username, 'short_term', n)
    mid = list_top_artists_by_term(username, 'medium_term', n)
    old = list_top_artists_by_term(username, 'long_term', n)
    for artist in old:
        if ((artist in new) or (artist in mid)):
            result += [artist]
    return result


# Takes a username in a string
# Returns an artists' top songs of top artists common to all terms
def list_alltime_favorite_artists_songs(username, n=20):
    result = []
    artists = list_alltime_favorite_artists(username)
    for artist in artists:
        result += list_top_songs_by_artist(artist, n)
    return result


# Takes a username in a string
# Creates a playlist of top artists for all terms' top songs
def create_playlist_alltime_favorite_artists(username, n=10):
    playlist = create_playlist(username, 'all_time_favorite_artists')
    songs = list_alltime_favorite_artists_songs(username, n)
    add_songs_to_playlist(username, playlist, songs)


# Takes a username in a string
# Returns the list of the user's playlists' URIs
def list_playlists(username):
    result = []
    scope = 'playlist-read-private'
    token = util.prompt_for_user_token(username, scope)
    sp = spotipy.Spotify(auth=token)
    playlists = sp.user_playlists(username)
    playlist_ids = []
    for playlist in playlists['items']:
        uri = playlist['uri']
        username = uri.split(':')[2]
        playlist_id = uri.split(':')[4]
        results = sp.user_playlist(username, playlist_id)
        client_credentials_manager = SpotifyClientCredentials()
        sp = spotipy.Spotify(
            client_credentials_manager=client_credentials_manager)
        results = sp.user_playlist(username, playlist_id)
        songs = []
        for item in results['tracks']['items']:
            songs += [item['track']['id']]
        scope = 'playlist-read-private'
        token = util.prompt_for_user_token(username, scope)
        sp = spotipy.Spotify(auth=token)
        try:
            known = sp.current_user_saved_tracks_contains(songs)
        except:
            known = []
            for song in songs:
                known += sp.current_user_saved_tracks_contains([song])
        result += [(sum(known) / len(known), playlist['name'])]
        print(round(sum(known) / len(known), 2), playlist['name'])
    return sorted(result)[::-1]
