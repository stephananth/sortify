# Stephanie K. Ananth (sananth)

# Adapted from Paul Lamere's examples
# https://github.com/plamere/spotipy

import os

import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyClientCredentials

# Client Credentials from Spotify Developer
os.environ['SPOTIPY_CLIENT_ID'] = '5c14698fcf8e41adb4f39b5518e55100'
os.environ['SPOTIPY_CLIENT_SECRET'] = '355d085eaf6049a1bda2e8dff93bdefd'
os.environ['SPOTIPY_REDIRECT_URI'] = 'https://www.cs.cmu.edu/~112/index.html'


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


print(list_playlists('shadykoopa'))
