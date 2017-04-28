################################################################################

# Stephanie K. Ananth (sananth)

<<<<<<< HEAD
=======
################################################################################

>>>>>>> origin/master
import copy
import os
import unicodedata
import webbrowser
from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog

import spotipy
import spotipy.oauth2 as oauth2
from spotipy.oauth2 import SpotifyClientCredentials

import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

################################################################################

# Credentials obtained from developer.spotify.com

os.environ['SPOTIPY_CLIENT_ID'] = '5c14698fcf8e41adb4f39b5518e55100'
os.environ['SPOTIPY_CLIENT_SECRET'] = '355d085eaf6049a1bda2e8dff93bdefd'
os.environ['SPOTIPY_REDIRECT_URI'] = 'https://www.spotify.com/us/'


################################################################################

# cs.cmu.edu/~112/notes/keyEventsDemo.py
# cs.cmu.edu/~112/notes/mouseEventsDemo.py
# cs.cmu.edu/~112/notes/resizableDemo.py

def run(width=1200, height=700):
    def redraw_all_wrapper(canvas, data):
        canvas.delete(ALL)
        canvas.create_rectangle(0, 0, data.width, data.height, fill=white,
                                width=0)
        redraw_all(canvas, data)
        canvas.update()

    def mouse_wrapper(mouse_function, event, canvas, data):
        mouse_function(event, data)
        redraw_all_wrapper(canvas, data)

    def key_wrapper(key_function, event, canvas, data):
        key_function(event, data)
        redraw_all_wrapper(canvas, data)

    def timer_fired_wrapper(canvas, data):
        timer_fired(data)
        redraw_all_wrapper(canvas, data)
        canvas.after(data.timer_delay, timer_fired_wrapper, canvas, data)

    # Initialized before data because data contains an image
    root = Tk()

    class Struct(object):
        pass

    data = Struct()
    data.width = width
    data.height = height
    data.timer_delay = 150
    init(data)

    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.pack(fill=BOTH, expand=YES)

    root.bind('<Button-1>',
              lambda event: mouse_wrapper(left_pressed, event, canvas, data))
    root.bind('<Button-3>',
              lambda event: mouse_wrapper(right_pressed, event, canvas, data))
    canvas.bind('<Motion>',
                lambda event: mouse_wrapper(mouse_moved, event, canvas, data))
    canvas.bind('<B1-Motion>',
                lambda event: mouse_wrapper(left_moved, event, canvas, data))
    canvas.bind('<B3-Motion>',
                lambda event: mouse_wrapper(right_moved, event, canvas, data))
    root.bind('<B1-ButtonRelease>',
              lambda event: mouse_wrapper(left_released, event, canvas, data))
    root.bind('<B3-ButtonRelease>',
              lambda event: mouse_wrapper(right_released, event, canvas, data))
    root.bind('<KeyPress>',
              lambda event: key_wrapper(key_pressed, event, canvas, data))
    root.bind('<KeyRelease>',
              lambda event: key_wrapper(key_released, event, canvas, data))

    def size_changed(event):
        data.width = event.width
        data.height = event.height
        redraw_all_wrapper(canvas, data)

    root.bind('<Configure>', size_changed)
    root.minsize(800, 600)

    timer_fired_wrapper(canvas, data)
    root.mainloop()
    print('Bye!')


###############################################################################

def init(data):
<<<<<<< HEAD
    data.mode = ''
    data.ctrl = False
    data.shift = False
    data.scale = 0 
    data.mouse_moved_x = 0
    data.mouse_moved_y = 0
    data.left_moved_x = 0
    data.left_moved_y = 0
    data.left_pressed_x = 0
    data.left_pressed_y = 0
    data.left_released_x = 0
    data.left_released_y = 0
    data.username = ''
    data.keysym_pressed = ''
    data.buttons = []
    data.headers = []
    data.top_songs_all = []
    data.top_artists_all = []
    data.top_songs_all_set = set()
    data.top_artists_all_set = set()
    data.tokens = {}
    data.all_songs_features = {}
    data.all_artists_features = {}
    data.top_songs = {'short_term': [], 'medium_term': [], 'long_term': []}
    data.top_artists = {'short_term': [], 'medium_term': [], 'long_term': []}

    # login
    data.logo = None
    data.logo_scale = 0

    # organize
    data.vertical1_scale = 0
    data.vertical2_scale = 0

    # organize and analyze
    data.is_overall = False
    data.is_songs = False
    data.is_artists = False
    data.is_artist_top_songs = False
    data.start = 0
    data.source_start = 0
    data.sort_mode = 0
    data.sort_mode_inner = 0
    data.artist_top_songs_end = 10
    data.stage = []
    data.songs = []
    data.stage_id = []
    data.songs_id = []
    data.songs_id_original = []
    data.songs_id_selected = []
    data.artists = []
    data.artists_id = []
    data.artists_id_original = []
    data.artists_id_selected = []
    data.artist_top_songs = []
    data.artist_top_songs_id = []
    data.artist_top_songs_id_original = []
    data.artist_top_songs_id_selected = []
    data.left_sidebar_buttons = []

    # analyze
    data.parameter = ''
    data.source = []
    data.sources = []
    data.charts = []
    data.values = []
    data.parameters = []

    # None
    data.right_moved_x = 0
    data.right_moved_y = 0
    data.right_pressed_x = 0
    data.right_pressed_y = 0
    data.right_released_x = 0
    data.right_released_y = 0
    data.keysym_released = ''

    # <REMOVE> #
=======
    data.mode = data.username = ''
    data.scale = data.logo_scale = 0
    data.vertical1_scale = data.vertical2_scale = 0

    data.ctrl = data.shift = False
    data.mouse_moved_x = data.mouse_moved_y = 0
    data.left_moved_x = data.left_moved_y = 0
    data.left_pressed_x = data.left_pressed_y = 0
    data.left_released_x = data.left_released_y = 0
    data.right_moved_x = data.right_moved_y = 0
    data.right_pressed_x = data.right_pressed_y = 0
    data.right_released_x = data.right_released_y = 0
    data.keysym_pressed = data.keysym_released = ''

    data.logo = None
    data.tokens = {}

    data.top_songs = {'short_term': [], 'medium_term': [], 'long_term': []}
    data.top_songs_all = []
    data.top_songs_all_set = set()
    data.all_songs_features = {}

    data.top_artists = {'short_term': [], 'medium_term': [], 'long_term': []}
    data.top_artists_all = []
    data.top_artists_all_set = set()
    data.all_artists_features = {}

    data.is_overall = data.is_viewing_songs = data.is_analyze_songs = False
    data.is_viewing_artists = data.is_viewing_artist_top_songs = False
    data.is_analyze_artists = data.is_analyze_artist_top_songs = False
    data.viewing_songs_start = data.viewing_artists_start = 0
    data.analyze_songs_start = data.analyze_artists_start = 0
    data.sort_mode = data.inner_sort_mode = 0

    data.original_viewing_songs = data.original_analyze_songs = []
    data.original_viewing_artists = data.original_analyze_artists = []
    data.original_viewing_top_songs = data.original_analyze_top_songs = []

    data.viewing_songs_id = data.analyze_songs_id = []
    data.viewing_songs = data.analyze_songs = []

    data.viewing_artists_id = data.analyze_artists_id = []
    data.viewing_artists = data.analyze_artists = []

    data.viewing_artist_top_songs_end = data.analyze_artist_top_songs_end = 10
    data.viewing_artist_top_songs_id = data.analyze_artist_top_songs_id = []
    data.viewing_artist_top_songs = data.analyze_artist_top_songs = []

    data.selected_songs = []
    data.selected_artists = []
    data.selected_artist_top_songs = []

    data.stage_end = 50
    data.stage_id = []
    data.stage = []

    data.left_sidebar_buttons = []
    data.buttons = []
    data.headers = []

    data.sources = []
    data.parameters = []
    data.charts = []
    data.values = []
    
    data.source = []
    data.source_start = 0
    data.parameter = ''

    # TEST #
>>>>>>> origin/master
    data.all_songs_features = {'2BBb3UMJBNlofpC25pbSp4': {'name': 'Call Me In The Afternoon', 'artist_id': '3ceQN2NVlLg1hgTzljDE4n', 'artist_name': 'Half Moon Run', 'album_name': 'Spotify Sessions', 'track_number': 1, 'duration_ms': 193240, 'popularity': 59, 'danceability': 0.536, 'energy': 0.946, 'loudness': -7.932, 'speechiness': 0.0436, 'acousticness': 0.131, 'instrumentalness': 0.00645, 'liveness': 0.103, 'valence': 0.631, 'tempo': 88.554}, '1Wdj4wRDYS7aT4CoPS0mAH': {'name': 'You Are Enough', 'artist_id': '0MeLMJJcouYXCymQSHPn8g', 'artist_name': 'Sleeping At Last', 'album_name': 'Atlas: Year One', 'track_number': 7, 'duration_ms': 180086, 'popularity': 50, 'danceability': 0.593, 'energy': 0.5, 'loudness': -8.532, 'speechiness': 0.029, 'acousticness': 0.707, 'instrumentalness': 1.24e-05, 'liveness': 0.0837, 'valence': 0.442, 'tempo': 117.996}, '5jQQSl7Uae4S8mlRkR4W8j': {'name': 'Green Eyes and a Heart of Gold', 'artist_id': '7JFtD8KnbAADBBDleIMuH7', 'artist_name': 'The Lone Bellow', 'album_name': 'The Lone Bellow', 'track_number': 1, 'duration_ms': 252853, 'popularity': 45, 'danceability': 0.321, 'energy': 0.895, 'loudness': -6.087, 'speechiness': 0.12, 'acousticness': 0.0314, 'instrumentalness': 0, 'liveness': 0.364, 'valence': 0.394, 'tempo': 127.082}, '6pOFkf24NgrPlf3YV1ESfq': {'name': 'Sing Loud', 'artist_id': '5fhX5cgW9CIJ363zTqAP3a', 'artist_name': 'Alpha Rev', 'album_name': 'Bloom', 'track_number': 3, 'duration_ms': 278360, 'popularity': 35, 'danceability': 0.508, 'energy': 0.669, 'loudness': -8.617, 'speechiness': 0.0377, 'acousticness': 0.0534, 'instrumentalness': 4.07e-05, 'liveness': 0.0836, 'valence': 0.282, 'tempo': 139.989}, '1WeF1b9XrQZpZ8IIEfYYJ5': {'name': 'You Are What You Are', 'artist_id': '5r2ltbRmBrS2c0J4oTwfGo', 'artist_name': 'Matt Hires', 'album_name': 'American Wilderness', 'track_number': 4, 'duration_ms': 191720, 'popularity': 19, 'danceability': 0.352, 'energy': 0.911, 'loudness': -5.401, 'speechiness': 0.109, 'acousticness': 0.038, 'instrumentalness': 0, 'liveness': 0.229, 'valence': 0.557, 'tempo': 166.007}, '4vRuPvw2HQi1ukIaKu107k': {'name': 'Nothing Stays The Same', 'artist_id': '3Lw97gGh8bp1MftsYmwJHG', 'artist_name': 'Luke Sital-Singh', 'album_name': 'The Fire Inside', 'track_number': 1, 'duration_ms': 241386, 'popularity': 46, 'danceability': 0.508, 'energy': 0.835, 'loudness': -5.722, 'speechiness': 0.0376, 'acousticness': 0.0473, 'instrumentalness': 0, 'liveness': 0.11, 'valence': 0.422, 'tempo': 144.952}, '3bEmTTBl5I5cMkelx9foEK': {'name': 'Into the Storm', 'artist_id': '6tK77FerjTNLS5EEhI0zGM', 'artist_name': 'The Brevet', 'album_name': 'Into the Storm', 'track_number': 1, 'duration_ms': 278000, 'popularity': 28, 'danceability': 0.54, 'energy': 0.792, 'loudness': -5.963, 'speechiness': 0.0349, 'acousticness': 0.337, 'instrumentalness': 7.48e-06, 'liveness': 0.0915, 'valence': 0.302, 'tempo': 137.09}, '4YyhCfbXfeVrEjtj5LCO09': {'name': 'Start to Begin', 'artist_id': '6tK77FerjTNLS5EEhI0zGM', 'artist_name': 'The Brevet', 'album_name': 'Battle of the Heart', 'track_number': 1, 'duration_ms': 278613, 'popularity': 35, 'danceability': 0.522, 'energy': 0.603, 'loudness': -8.013, 'speechiness': 0.0293, 'acousticness': 0.0244, 'instrumentalness': 0.000204, 'liveness': 0.085, 'valence': 0.152, 'tempo': 118.007}, '5wTw73gergejPQEvWe5Lqv': {'name': 'On the Road in a Storm', 'artist_id': '4xuWl9MpICwyNQIIlsUPNT', 'artist_name': 'Side Saddle', 'album_name': 'The Postcard - EP', 'track_number': 4, 'duration_ms': 169500, 'popularity': 4, 'danceability': 0.556, 'energy': 0.65, 'loudness': -6.641, 'speechiness': 0.0291, 'acousticness': 0.0783, 'instrumentalness': 0.000788, 'liveness': 0.112, 'valence': 0.341, 'tempo': 169.988}, '0rCcpuqlviUhA8TnBZGC9C': {'name': 'Where the West Wind Blows', 'artist_id': '6Yuow6YoiBaVPFNjZ5BQi7', 'artist_name': 'Green River Ordinance', 'album_name': 'The Morning Passengers EP - Acoustic Sessions', 'track_number': 6, 'duration_ms': 230208, 'popularity': 24, 'danceability': 0.634, 'energy': 0.499, 'loudness': -6.874, 'speechiness': 0.0314, 'acousticness': 0.264, 'instrumentalness': 0, 'liveness': 0.0921, 'valence': 0.347, 'tempo': 144.946}, '06QdJtEtHOckzHhq5EbTfo': {'name': "Don't Ask Me Why", 'artist_id': '4R2xkQL6chRRTgUQ1Xgaf1', 'artist_name': 'Great Caesar', 'album_name': "Don't Ask Me Why", 'track_number': 1, 'duration_ms': 356307, 'popularity': 41, 'danceability': 0.377, 'energy': 0.569, 'loudness': -5.702, 'speechiness': 0.0695, 'acousticness': 0.521, 'instrumentalness': 0, 'liveness': 0.0838, 'valence': 0.489, 'tempo': 80.088}, '0zf3DZPSvyOvGJ6PpsJKBE': {'name': 'Wherever I Go', 'artist_id': '2JMtxA2S9SNUlqBlkDtXm6', 'artist_name': 'The National Parks', 'album_name': 'Until I Live', 'track_number': 9, 'duration_ms': 258533, 'popularity': 33, 'danceability': 0.453, 'energy': 0.301, 'loudness': -9.248, 'speechiness': 0.031, 'acousticness': 0.686, 'instrumentalness': 7.73e-05, 'liveness': 0.101, 'valence': 0.135, 'tempo': 137.824}, '5bE0gN3bXWh8rcWttcvMto': {'name': 'Time to Run', 'artist_id': '6ltzsmQQbmdoHHbLZ4ZN25', 'artist_name': 'Lord Huron', 'album_name': 'Lonesome Dreams', 'track_number': 2, 'duration_ms': 323973, 'popularity': 56, 'danceability': 0.539, 'energy': 0.856, 'loudness': -7.939, 'speechiness': 0.0372, 'acousticness': 0.507, 'instrumentalness': 0.437, 'liveness': 0.114, 'valence': 0.321, 'tempo': 109.022}, '0wfbD5rAksdXUzRvMfM3x5': {'name': 'The One', 'artist_id': '69GGBxA162lTqCwzJG5jLp', 'artist_name': 'The Chainsmokers', 'album_name': 'Memories...Do Not Open', 'track_number': 1, 'duration_ms': 177573, 'popularity': 86, 'danceability': 0.76, 'energy': 0.303, 'loudness': -11.362, 'speechiness': 0.0284, 'acousticness': 0.238, 'instrumentalness': 8.09e-06, 'liveness': 0.294, 'valence': 0.157, 'tempo': 99.991}, '4yRlTvPVfEyhXfp6GZurq9': {'name': 'Never Come Back Again', 'artist_id': '6AMV5iw09ZrX1h3o4x7uVN', 'artist_name': 'Austin Plaine', 'album_name': 'Austin Plaine', 'track_number': 1, 'duration_ms': 196240, 'popularity': 54, 'danceability': 0.593, 'energy': 0.694, 'loudness': -8.858, 'speechiness': 0.0265, 'acousticness': 0.192, 'instrumentalness': 1.96e-06, 'liveness': 0.119, 'valence': 0.159, 'tempo': 105.002}, '1dNIEtp7AY3oDAKCGg2XkH': {'name': 'Something Just Like This', 'artist_id': '69GGBxA162lTqCwzJG5jLp', 'artist_name': 'The Chainsmokers', 'album_name': 'Something Just Like This', 'track_number': 1, 'duration_ms': 247626, 'popularity': 99, 'danceability': 0.607, 'energy': 0.649, 'loudness': -6.695, 'speechiness': 0.0362, 'acousticness': 0.0306, 'instrumentalness': 2.46e-05, 'liveness': 0.174, 'valence': 0.47, 'tempo': 102.996}, '5f9Y4fa3y4mR6Lg1fifz86': {'name': 'Bridge Burn', 'artist_id': '7cfhZmKaLWzNLwHDxzugUH', 'artist_name': 'Little Comets', 'album_name': 'Life Is Elsewhere', 'track_number': 13, 'duration_ms': 164760, 'popularity': 50, 'danceability': 0.634, 'energy': 0.446, 'loudness': -10.345, 'speechiness': 0.041, 'acousticness': 0.765, 'instrumentalness': 0, 'liveness': 0.109, 'valence': 0.496, 'tempo': 102.977}, '5OiaAaIMYlCZONyDBxqk4G': {'name': 'First Day Of My Life', 'artist_id': '5o206eFLx38glA2bb4zqIU', 'artist_name': 'Bright Eyes', 'album_name': "I'm Wide Awake, It's Morning", 'track_number': 6, 'duration_ms': 188800, 'popularity': 73, 'danceability': 0.468, 'energy': 0.201, 'loudness': -17.024, 'speechiness': 0.0388, 'acousticness': 0.915, 'instrumentalness': 8.28e-05, 'liveness': 0.0952, 'valence': 0.384, 'tempo': 94.422}, '2tux1s5FVabQQKpz7GEXbI': {'name': 'Lost, Scared & Tired', 'artist_id': '0GklSybv01PPje5GlXFq2i', 'artist_name': 'Jared & The Mill', 'album_name': 'Orme Dugas', 'track_number': 1, 'duration_ms': 292173, 'popularity': 36, 'danceability': 0.479, 'energy': 0.713, 'loudness': -7.47, 'speechiness': 0.0288, 'acousticness': 0.00499, 'instrumentalness': 1.91e-06, 'liveness': 0.102, 'valence': 0.236, 'tempo': 106.498}, '77KyKfXIATnLVAougyvpBT': {'name': 'I Know', 'artist_id': '2txHhyCwHjUEpJjWrEyqyX', 'artist_name': 'Tom Odell', 'album_name': 'Long Way Down', 'track_number': 4, 'duration_ms': 232626, 'popularity': 40, 'danceability': 0.533, 'energy': 0.697, 'loudness': -7.34, 'speechiness': 0.0349, 'acousticness': 0.296, 'instrumentalness': 0, 'liveness': 0.0664, 'valence': 0.473, 'tempo': 148.031}, '0K90HGijiM6RpytZYyjbJB': {'name': "Don't Wait for Him", 'artist_id': '4xuWl9MpICwyNQIIlsUPNT', 'artist_name': 'Side Saddle', 'album_name': 'The Postcard - EP', 'track_number': 3, 'duration_ms': 190000, 'popularity': 30, 'danceability': 0.603, 'energy': 0.83, 'loudness': -5.263, 'speechiness': 0.0322, 'acousticness': 0.016, 'instrumentalness': 3.2e-05, 'liveness': 0.0754, 'valence': 0.765, 'tempo': 104.995}, '6k7HtqyhIYJMg6DgUwZc6M': {'name': 'Restless Heart', 'artist_id': '5r2ltbRmBrS2c0J4oTwfGo', 'artist_name': 'Matt Hires', 'album_name': "This World Won't Last Forever, But Tonight We Can Pretend", 'track_number': 3, 'duration_ms': 200829, 'popularity': 29, 'danceability': 0.556, 'energy': 0.774, 'loudness': -4.635, 'speechiness': 0.0309, 'acousticness': 0.00169, 'instrumentalness': 0, 'liveness': 0.192, 'valence': 0.654, 'tempo': 139.903}, '30qdwcNJ4n2iJqh75hmWak': {'name': 'Diamond Dreams', 'artist_id': '1qXuwKQR0iK6HBmJO3n0SZ', 'artist_name': 'Castro', 'album_name': 'Diamond Dreams', 'track_number': 1, 'duration_ms': 195266, 'popularity': 54, 'danceability': 0.608, 'energy': 0.668, 'loudness': -6.106, 'speechiness': 0.047, 'acousticness': 0.167, 'instrumentalness': 0, 'liveness': 0.511, 'valence': 0.576, 'tempo': 120.046}, '2j9z9hejHzVbcRUyYM7PZ1': {'name': 'Dear Fellow Traveller', 'artist_id': '3ZllGjNdP5pS8UFnT5Jj2x', 'artist_name': 'Sea Wolf', 'album_name': 'Old World Romance', 'track_number': 8, 'duration_ms': 221000, 'popularity': 39, 'danceability': 0.673, 'energy': 0.654, 'loudness': -8.929, 'speechiness': 0.0306, 'acousticness': 0.339, 'instrumentalness': 8.86e-05, 'liveness': 0.125, 'valence': 0.509, 'tempo': 92.005}, '2ATtrAE0jDv6QYJgL3CHQD': {'name': 'Second Best - Bonus Track', 'artist_id': '4DX2G1URzfEiRg2wBfv4ub', 'artist_name': 'Hudson Taylor', 'album_name': 'Singing For Strangers', 'track_number': 20, 'duration_ms': 226764, 'popularity': 26, 'danceability': 0.522, 'energy': 0.542, 'loudness': -7.353, 'speechiness': 0.0323, 'acousticness': 0.468, 'instrumentalness': 1.75e-06, 'liveness': 0.0931, 'valence': 0.127, 'tempo': 80.962}, '2eAv6wtp8l1GPJWUY4k7Ep': {'name': 'Beautiful Mistake', 'artist_id': '4DX2G1URzfEiRg2wBfv4ub', 'artist_name': 'Hudson Taylor', 'album_name': 'Singing For Strangers', 'track_number': 16, 'duration_ms': 162000, 'popularity': 20, 'danceability': 0.514, 'energy': 0.244, 'loudness': -9.341, 'speechiness': 0.0308, 'acousticness': 0.927, 'instrumentalness': 0, 'liveness': 0.244, 'valence': 0.348, 'tempo': 102.754}, '3CuscN8itbT86pQFKQMIk7': {'name': 'Where The Skies Are Blue', 'artist_id': '16oZKvXb6WkQlVAjwo2Wbg', 'artist_name': 'The Lumineers', 'album_name': 'Cleopatra (Deluxe)', 'track_number': 12, 'duration_ms': 140120, 'popularity': 61, 'danceability': 0.569, 'energy': 0.477, 'loudness': -6.577, 'speechiness': 0.0277, 'acousticness': 0.861, 'instrumentalness': 0.000485, 'liveness': 0.0644, 'valence': 0.558, 'tempo': 132.423}, '1KkFmmhPyIwPDM3tzWgqT8': {'name': 'Ledges', 'artist_id': '34482S5nfxR441wcnVfrHi', 'artist_name': 'Noah Gundersen', 'album_name': 'Ledges', 'track_number': 5, 'duration_ms': 258440, 'popularity': 48, 'danceability': 0.386, 'energy': 0.601, 'loudness': -5.294, 'speechiness': 0.0296, 'acousticness': 0.0235, 'instrumentalness': 1.9e-05, 'liveness': 0.104, 'valence': 0.416, 'tempo': 159.468}, '1DIg9155AY65dpR5Lf5Vg4': {'name': 'Honest', 'artist_id': '4BxCuXFJrSWGi1KHcVqaU4', 'artist_name': 'Kodaline', 'album_name': 'Coming Up for Air (Deluxe)', 'track_number': 1, 'duration_ms': 218933, 'popularity': 55, 'danceability': 0.389, 'energy': 0.758, 'loudness': -5.662, 'speechiness': 0.0485, 'acousticness': 0.00389, 'instrumentalness': 0, 'liveness': 0.167, 'valence': 0.329, 'tempo': 154.919}, '3UR1mTBpLALt8cQGzfTbRz': {'name': 'World Without You', 'artist_id': '4DX2G1URzfEiRg2wBfv4ub', 'artist_name': 'Hudson Taylor', 'album_name': 'Singing For Strangers', 'track_number': 5, 'duration_ms': 223909, 'popularity': 33, 'danceability': 0.43, 'energy': 0.733, 'loudness': -5.848, 'speechiness': 0.0337, 'acousticness': 0.144, 'instrumentalness': 0, 'liveness': 0.101, 'valence': 0.216, 'tempo': 112.963}, '4hVJIlulH29qKVYGCT6cky': {'name': 'Warmth', 'artist_id': '7EQ0qTo7fWT7DPxmxtSYEc', 'artist_name': 'Bastille', 'album_name': 'Wild World (Complete Edition)', 'track_number': 4, 'duration_ms': 229627, 'popularity': 54, 'danceability': 0.636, 'energy': 0.874, 'loudness': -3.577, 'speechiness': 0.0562, 'acousticness': 0.046, 'instrumentalness': 0, 'liveness': 0.844, 'valence': 0.886, 'tempo': 140.045}, '67mjxSBrj9tMfz5aJdatcU': {'name': 'Brother', 'artist_id': '5AVJt6VYXT4hMRP8D3MRAC', 'artist_name': 'Mighty Oaks', 'album_name': 'Howl', 'track_number': 1, 'duration_ms': 195320, 'popularity': 40, 'danceability': 0.507, 'energy': 0.803, 'loudness': -6.152, 'speechiness': 0.0371, 'acousticness': 0.255, 'instrumentalness': 0, 'liveness': 0.0825, 'valence': 0.371, 'tempo': 181.736}, '3pvTrpsqbBF3OduTOPOkii': {'name': 'Old Friend', 'artist_id': '3ZllGjNdP5pS8UFnT5Jj2x', 'artist_name': 'Sea Wolf', 'album_name': 'Old World Romance', 'track_number': 1, 'duration_ms': 237160, 'popularity': 53, 'danceability': 0.658, 'energy': 0.647, 'loudness': -8.157, 'speechiness': 0.029, 'acousticness': 0.248, 'instrumentalness': 0.00019, 'liveness': 0.0837, 'valence': 0.82, 'tempo': 147.419}, '75DtJBMwCXqjLz1bXS1tVr': {'name': 'Blame', 'artist_id': '2Oboq4Pq88TcC9eUn2HSW9', 'artist_name': 'Air Traffic Controller', 'album_name': 'NORDO', 'track_number': 6, 'duration_ms': 272320, 'popularity': 34, 'danceability': 0.417, 'energy': 0.513, 'loudness': -8.819, 'speechiness': 0.0325, 'acousticness': 0.454, 'instrumentalness': 0.00111, 'liveness': 0.126, 'valence': 0.187, 'tempo': 133.691}, '4yyg2J2uXOjCtCyT64984C': {'name': 'Ends of the Earth', 'artist_id': '6ltzsmQQbmdoHHbLZ4ZN25', 'artist_name': 'Lord Huron', 'album_name': 'Lonesome Dreams', 'track_number': 1, 'duration_ms': 284146, 'popularity': 66, 'danceability': 0.55, 'energy': 0.579, 'loudness': -8.622, 'speechiness': 0.0297, 'acousticness': 0.267, 'instrumentalness': 0.0289, 'liveness': 0.358, 'valence': 0.427, 'tempo': 120.991}, '78aRLjDiQx6jo0GVW7aDA4': {'name': "Another Travelin' Song", 'artist_id': '5o206eFLx38glA2bb4zqIU', 'artist_name': 'Bright Eyes', 'album_name': "I'm Wide Awake, It's Morning", 'track_number': 7, 'duration_ms': 256600, 'popularity': 45, 'danceability': 0.523, 'energy': 0.888, 'loudness': -8.099, 'speechiness': 0.0478, 'acousticness': 0.0133, 'instrumentalness': 0.00187, 'liveness': 0.121, 'valence': 0.962, 'tempo': 110.778}, '6cPyTS0Kk2sc4xQwC93kOg': {'name': 'Break Up Every Night', 'artist_id': '69GGBxA162lTqCwzJG5jLp', 'artist_name': 'The Chainsmokers', 'album_name': 'Memories...Do Not Open', 'track_number': 2, 'duration_ms': 207520, 'popularity': 84, 'danceability': 0.624, 'energy': 0.806, 'loudness': -5.957, 'speechiness': 0.0437, 'acousticness': 0.00411, 'instrumentalness': 0, 'liveness': 0.0872, 'valence': 0.536, 'tempo': 149.999}, '6fitB3zIBx8UybcuZg2ADv': {'name': 'Walden Pond', 'artist_id': '3RcaUsjj5gt1x2QK3TSNS2', 'artist_name': 'Atta Boy', 'album_name': 'Out of Sorts', 'track_number': 4, 'duration_ms': 282173, 'popularity': 44, 'danceability': 0.602, 'energy': 0.466, 'loudness': -11.393, 'speechiness': 0.108, 'acousticness': 0.584, 'instrumentalness': 0.000651, 'liveness': 0.0964, 'valence': 0.0355, 'tempo': 96.304}, '0dj1CtyRxZ4bnIT4Q20jNT': {'name': 'Wake Up Alone', 'artist_id': '69GGBxA162lTqCwzJG5jLp', 'artist_name': 'The Chainsmokers', 'album_name': 'Memories...Do Not Open', 'track_number': 10, 'duration_ms': 215720, 'popularity': 79, 'danceability': 0.643, 'energy': 0.52, 'loudness': -5.968, 'speechiness': 0.0334, 'acousticness': 0.0102, 'instrumentalness': 0, 'liveness': 0.11, 'valence': 0.212, 'tempo': 75.168}, '1pJQAHpD51J7GYaFrrFO9S': {'name': "Don't Say", 'artist_id': '69GGBxA162lTqCwzJG5jLp', 'artist_name': 'The Chainsmokers', 'album_name': 'Memories...Do Not Open', 'track_number': 4, 'duration_ms': 228480, 'popularity': 81, 'danceability': 0.567, 'energy': 0.464, 'loudness': -9.66, 'speechiness': 0.0302, 'acousticness': 0.0199, 'instrumentalness': 9.31e-06, 'liveness': 0.269, 'valence': 0.31, 'tempo': 99.806}, '26AuyrZGzWWiYZPSd3XBIg': {'name': 'Bloodstream', 'artist_id': '69GGBxA162lTqCwzJG5jLp', 'artist_name': 'The Chainsmokers', 'album_name': 'Memories...Do Not Open', 'track_number': 3, 'duration_ms': 224280, 'popularity': 81, 'danceability': 0.62, 'energy': 0.627, 'loudness': -5.889, 'speechiness': 0.0259, 'acousticness': 0.0317, 'instrumentalness': 0, 'liveness': 0.172, 'valence': 0.16, 'tempo': 90.955}, '4PMR2XYY8V8MVPRBxyeoxd': {'name': 'Lost Kid', 'artist_id': '62pBNClOEZJEyRXrzC2CtI', 'artist_name': 'The Apache Relay', 'album_name': 'American Nomad', 'track_number': 6, 'duration_ms': 168520, 'popularity': 30, 'danceability': 0.676, 'energy': 0.64, 'loudness': -9.463, 'speechiness': 0.065, 'acousticness': 0.572, 'instrumentalness': 0.000325, 'liveness': 0.0975, 'valence': 0.824, 'tempo': 120.026}, '5xhJmd0I15jFcEdqxfCzKk': {'name': "It Won't Kill Ya", 'artist_id': '69GGBxA162lTqCwzJG5jLp', 'artist_name': 'The Chainsmokers', 'album_name': 'Memories...Do Not Open', 'track_number': 7, 'duration_ms': 217613, 'popularity': 80, 'danceability': 0.572, 'energy': 0.53, 'loudness': -8.521, 'speechiness': 0.0654, 'acousticness': 0.0647, 'instrumentalness': 0.000169, 'liveness': 0.127, 'valence': 0.135, 'tempo': 170.138}, '6KjbNLbRjuoa8rEq5yNA6H': {'name': 'Honest', 'artist_id': '69GGBxA162lTqCwzJG5jLp', 'artist_name': 'The Chainsmokers', 'album_name': 'Memories...Do Not Open', 'track_number': 9, 'duration_ms': 208000, 'popularity': 81, 'danceability': 0.673, 'energy': 0.514, 'loudness': -10.772, 'speechiness': 0.0465, 'acousticness': 0.0121, 'instrumentalness': 8.5e-05, 'liveness': 0.385, 'valence': 0.34, 'tempo': 100.035}, '6V9kwssTrwkKT72imgowj9': {'name': 'My Type', 'artist_id': '69GGBxA162lTqCwzJG5jLp', 'artist_name': 'The Chainsmokers', 'album_name': 'Memories...Do Not Open', 'track_number': 6, 'duration_ms': 217413, 'popularity': 80, 'danceability': 0.604, 'energy': 0.603, 'loudness': -6.324, 'speechiness': 0.0389, 'acousticness': 0.0357, 'instrumentalness': 0, 'liveness': 0.126, 'valence': 0.137, 'tempo': 94.989}, '72jbDTw1piOOj770jWNeaG': {'name': 'Paris', 'artist_id': '69GGBxA162lTqCwzJG5jLp', 'artist_name': 'The Chainsmokers', 'album_name': 'Memories...Do Not Open', 'track_number': 8, 'duration_ms': 221506, 'popularity': 85, 'danceability': 0.653, 'energy': 0.658, 'loudness': -6.428, 'speechiness': 0.0304, 'acousticness': 0.0215, 'instrumentalness': 1.66e-06, 'liveness': 0.0939, 'valence': 0.212, 'tempo': 99.99}, '4gAgdhTIx6T76baPfbXHQX': {'name': 'Specks', 'artist_id': '3JVgWZxQa78cVa2cUuAUQ4', 'artist_name': 'Matt Pond PA', 'album_name': 'The Dark Leaves', 'track_number': 3, 'duration_ms': 229800, 'popularity': 42, 'danceability': 0.466, 'energy': 0.552, 'loudness': -7.474, 'speechiness': 0.031, 'acousticness': 0.651, 'instrumentalness': 0.00326, 'liveness': 0.102, 'valence': 0.142, 'tempo': 91.461}, '4ngv7whSPSAwD8ZP3zMHsd': {'name': 'The Worth Of The Wait', 'artist_id': '3D1IyJznpDnWnnFrzjuWnh', 'artist_name': 'Ivan & Alyosha', 'album_name': 'The Worth Of The Wait', 'track_number': 1, 'duration_ms': 171800, 'popularity': 56, 'danceability': 0.48, 'energy': 0.618, 'loudness': -7.335, 'speechiness': 0.0501, 'acousticness': 0.844, 'instrumentalness': 8.93e-05, 'liveness': 0.325, 'valence': 0.339, 'tempo': 82.051}, '3Hvg5tRKsQlX25wYwgMF9p': {'name': 'Flowers in Your Hair', 'artist_id': '16oZKvXb6WkQlVAjwo2Wbg', 'artist_name': 'The Lumineers', 'album_name': 'The Lumineers', 'track_number': 1, 'duration_ms': 109735, 'popularity': 66, 'danceability': 0.67, 'energy': 0.609, 'loudness': -10.088, 'speechiness': 0.0333, 'acousticness': 0.749, 'instrumentalness': 6.74e-05, 'liveness': 0.227, 'valence': 0.571, 'tempo': 127.463}, '6ItGPha13j36IiQlvubGrT': {'name': 'Here Tonight', 'artist_id': '2S8ft2HNlQ2Ox9ltQZM1A5', 'artist_name': 'Sam Burchfield', 'album_name': 'Where to Run', 'track_number': 1, 'duration_ms': 252146, 'popularity': 46, 'danceability': 0.471, 'energy': 0.464, 'loudness': -7.941, 'speechiness': 0.0301, 'acousticness': 0.702, 'instrumentalness': 5.59e-05, 'liveness': 0.115, 'valence': 0.284, 'tempo': 186.875}, '4MgLY30kpo4vJTB29mhH1R': {'name': 'The Middle One', 'artist_id': '3sva1UjOJOx6cGISZOpItl', 'artist_name': 'The Collection', 'album_name': 'Ars Moriendi', 'track_number': 7, 'duration_ms': 331869, 'popularity': 24, 'danceability': 0.395, 'energy': 0.425, 'loudness': -9.444, 'speechiness': 0.0282, 'acousticness': 0.462, 'instrumentalness': 0.00215, 'liveness': 0.0946, 'valence': 0.084, 'tempo': 145.137}, '723paR6LrVISFCXFPf5z57': {'name': 'Above The Clouds Of Pompeii', 'artist_id': '0nJaMZM8paoA5HEUTUXPqi', 'artist_name': "Bear's Den", 'album_name': 'Islands', 'track_number': 3, 'duration_ms': 279453, 'popularity': 56, 'danceability': 0.581, 'energy': 0.372, 'loudness': -12.403, 'speechiness': 0.0333, 'acousticness': 0.838, 'instrumentalness': 0.000327, 'liveness': 0.0836, 'valence': 0.14, 'tempo': 100.771}, '7Hc1dKzCDzVqvlI8XaMZwH': {'name': 'Boy', 'artist_id': '7JhOzFlNJjcRrFan1wlwYB', 'artist_name': 'John Mark Nelson', 'album_name': 'Sings the Moon', 'track_number': 6, 'duration_ms': 256486, 'popularity': 32, 'danceability': 0.638, 'energy': 0.408, 'loudness': -11.745, 'speechiness': 0.0307, 'acousticness': 0.735, 'instrumentalness': 4.13e-05, 'liveness': 0.106, 'valence': 0.464, 'tempo': 89.976}, '0ewrI06EIDMGXvgJxuyF3U': {'name': 'Dearly Departed (feat. Esme Patterson)', 'artist_id': '1fZpYWNWdL5Z3wrDtISFUH', 'artist_name': 'Shakey Graves', 'album_name': 'And The War Came', 'track_number': 3, 'duration_ms': 212800, 'popularity': 65, 'danceability': 0.576, 'energy': 0.609, 'loudness': -5.921, 'speechiness': 0.107, 'acousticness': 0.303, 'instrumentalness': 0, 'liveness': 0.164, 'valence': 0.74, 'tempo': 86.703}, '6obkbpih6pYSgjPyoI75Xp': {'name': 'Psalm 46 (Lord of Hosts)', 'artist_id': '2LFbgsbEhfilNpQYW7mied', 'artist_name': 'Shane & Shane', 'album_name': 'Psalms, Vol. 2', 'track_number': 1, 'duration_ms': 302817, 'popularity': 48, 'danceability': 0.435, 'energy': 0.458, 'loudness': -10.148, 'speechiness': 0.0332, 'acousticness': 0.05, 'instrumentalness': 0, 'liveness': 0.0799, 'valence': 0.221, 'tempo': 137.595}, '54CtOOuhXdUKGpG0KsEVDD': {'name': 'Here and Heaven', 'artist_id': '53pmIwVqcTM68qW6PVhjW2', 'artist_name': 'Stuart Duncan', 'album_name': 'The Goat Rodeo Sessions', 'track_number': 5, 'duration_ms': 233413, 'popularity': 42, 'danceability': 0.515, 'energy': 0.222, 'loudness': -12.798, 'speechiness': 0.0351, 'acousticness': 0.929, 'instrumentalness': 0.0157, 'liveness': 0.132, 'valence': 0.388, 'tempo': 123.481}, '13p3U002Sv8z722mFjTuWi': {'name': 'I Surrender', 'artist_id': '44LPOpECjnIlnwH91wo2ir', 'artist_name': 'All Sons & Daughters', 'album_name': 'Poets & Saints', 'track_number': 2, 'duration_ms': 253706, 'popularity': 58, 'danceability': 0.412, 'energy': 0.567, 'loudness': -7.494, 'speechiness': 0.0321, 'acousticness': 0.426, 'instrumentalness': 0, 'liveness': 0.0737, 'valence': 0.257, 'tempo': 149.525}, '2SYvX2G6D5SD6BpijIOBpG': {'name': 'Things Happen', 'artist_id': '0CDUUM6KNRvgBFYIbWxJwV', 'artist_name': 'Dawes', 'album_name': 'All Your Favorite Bands', 'track_number': 1, 'duration_ms': 243319, 'popularity': 65, 'danceability': 0.522, 'energy': 0.531, 'loudness': -7.78, 'speechiness': 0.0293, 'acousticness': 0.387, 'instrumentalness': 0, 'liveness': 0.202, 'valence': 0.729, 'tempo': 79.252}, '0FqK5zRZm46125vbLR7K6v': {'name': 'Far Kingdom', 'artist_id': '4gzyIFii6fWdCiLsP0bocC', 'artist_name': 'The Gray Havens', 'album_name': 'Fire and Stone', 'track_number': 10, 'duration_ms': 264480, 'popularity': 38, 'danceability': 0.462, 'energy': 0.258, 'loudness': -10.548, 'speechiness': 0.0299, 'acousticness': 0.695, 'instrumentalness': 0, 'liveness': 0.0811, 'valence': 0.215, 'tempo': 150.052}, '3NXMZPpfTtiyteVW87c5EC': {'name': 'I Am Set Free', 'artist_id': '44LPOpECjnIlnwH91wo2ir', 'artist_name': 'All Sons & Daughters', 'album_name': 'Brokenness Aside EP No. 1', 'track_number': 5, 'duration_ms': 289493, 'popularity': 43, 'danceability': 0.451, 'energy': 0.562, 'loudness': -6.926, 'speechiness': 0.0335, 'acousticness': 0.0653, 'instrumentalness': 0, 'liveness': 0.108, 'valence': 0.168, 'tempo': 156.104}, '2yEtO5IzwNttQ4SG38PDnF': {'name': 'Ghost of a King', 'artist_id': '4gzyIFii6fWdCiLsP0bocC', 'artist_name': 'The Gray Havens', 'album_name': 'Ghost of a King', 'track_number': 3, 'duration_ms': 281635, 'popularity': 41, 'danceability': 0.515, 'energy': 0.501, 'loudness': -10.861, 'speechiness': 0.0398, 'acousticness': 0.517, 'instrumentalness': 1.87e-05, 'liveness': 0.385, 'valence': 0.269, 'tempo': 135.89}, '7H60aEC32oOX4Fy4Ug2l0r': {'name': 'The Tide', 'artist_id': '3d7YNQ39OxBxWOn1VX4J26', 'artist_name': 'The Lonely Heartstring Band', 'album_name': 'Deep Waters', 'track_number': 4, 'duration_ms': 258453, 'popularity': 36, 'danceability': 0.561, 'energy': 0.428, 'loudness': -10.149, 'speechiness': 0.0302, 'acousticness': 0.828, 'instrumentalness': 2.85e-05, 'liveness': 0.12, 'valence': 0.405, 'tempo': 117.914}, '73Iyy1U5QR96t7YPPDrEKb': {'name': 'Be Okay', 'artist_id': '3yQxGz288i3AqOxq7LYHUU', 'artist_name': 'Oh Honey', 'album_name': 'With Love - EP', 'track_number': 2, 'duration_ms': 198674, 'popularity': 52, 'danceability': 0.656, 'energy': 0.92, 'loudness': -4.443, 'speechiness': 0.0588, 'acousticness': 0.00434, 'instrumentalness': 0, 'liveness': 0.173, 'valence': 0.643, 'tempo': 116.99}, '1AtwsVXr1zaZf4YgIEOlDK': {'name': 'Holy Spirit', 'artist_id': '7bvAtcPT3evvSeHDyu2zBC', 'artist_name': 'Bryan & Katie Torwalt', 'album_name': 'Here On Earth', 'track_number': 2, 'duration_ms': 348800, 'popularity': 58, 'danceability': 0.403, 'energy': 0.494, 'loudness': -8.636, 'speechiness': 0.0376, 'acousticness': 0.0203, 'instrumentalness': 0, 'liveness': 0.0998, 'valence': 0.0627, 'tempo': 144.142}, '06wxyCQFJOT0bjvSPMQj7x': {'name': 'Beautiful Things', 'artist_id': '4J4o73Oun7v0XXRjN8DPif', 'artist_name': 'Gungor', 'album_name': 'Beautiful Things', 'track_number': 2, 'duration_ms': 310293, 'popularity': 59, 'danceability': 0.558, 'energy': 0.408, 'loudness': -8.235, 'speechiness': 0.0253, 'acousticness': 0.05, 'instrumentalness': 0.013, 'liveness': 0.125, 'valence': 0.147, 'tempo': 82.021}, '1RJFyMZOQhHCE26iixvM4Y': {'name': 'You Hold It All Together', 'artist_id': '44LPOpECjnIlnwH91wo2ir', 'artist_name': 'All Sons & Daughters', 'album_name': 'Poets & Saints', 'track_number': 9, 'duration_ms': 282106, 'popularity': 44, 'danceability': 0.24, 'energy': 0.286, 'loudness': -10.013, 'speechiness': 0.0355, 'acousticness': 0.539, 'instrumentalness': 0, 'liveness': 0.0965, 'valence': 0.0718, 'tempo': 100.134}, '1YhFtqwcN138S6ng3MT1nN': {'name': 'Rain Is a Good Thing', 'artist_id': '0BvkDsjIUla7X0k6CSWh1I', 'artist_name': 'Luke Bryan', 'album_name': "Doin' My Thing", 'track_number': 1, 'duration_ms': 176160, 'popularity': 64, 'danceability': 0.622, 'energy': 0.932, 'loudness': -4.66, 'speechiness': 0.0498, 'acousticness': 0.105, 'instrumentalness': 2.37e-06, 'liveness': 0.328, 'valence': 0.522, 'tempo': 108.051}, '4dI4oscajpdtjpg2dP1x28': {'name': 'Shake, Shake, Shake', 'artist_id': '2ic4xySjQ39N7DJ0HZemeG', 'artist_name': 'Bronze Radio Return', 'album_name': 'Shake! Shake! Shake!', 'track_number': 3, 'duration_ms': 163236, 'popularity': 51, 'danceability': 0.727, 'energy': 0.678, 'loudness': -5.136, 'speechiness': 0.0625, 'acousticness': 0.0797, 'instrumentalness': 0.000564, 'liveness': 0.115, 'valence': 0.21, 'tempo': 119.955}, '3E3I7DBGCIsIgT1a1UJEFK': {'name': 'Budding Trees', 'artist_id': '35fFUv2850L9CQjjNrLBpb', 'artist_name': 'Nahko and Medicine for the People', 'album_name': 'Dark As Night', 'track_number': 6, 'duration_ms': 384250, 'popularity': 52, 'danceability': 0.604, 'energy': 0.563, 'loudness': -7.661, 'speechiness': 0.0371, 'acousticness': 0.565, 'instrumentalness': 0, 'liveness': 0.283, 'valence': 0.648, 'tempo': 116.026}, '1irfge2G36vfmvs97KV6T0': {'name': 'Glory & Grace', 'artist_id': '5LfJyJ9ZnWxRWawuGFIMMh', 'artist_name': 'Erik Nieder', 'album_name': 'Valley of the Shadow', 'track_number': 7, 'duration_ms': 256127, 'popularity': 33, 'danceability': 0.518, 'energy': 0.277, 'loudness': -9.432, 'speechiness': 0.0293, 'acousticness': 0.227, 'instrumentalness': 4.59e-05, 'liveness': 0.103, 'valence': 0.15, 'tempo': 113.866}, '2wXbVH6oQtUPMcZrlUqnPs': {'name': 'Psalm 98 (Sing Unto the Lord)', 'artist_id': '2LFbgsbEhfilNpQYW7mied', 'artist_name': 'Shane & Shane', 'album_name': 'Psalms, Vol. 2', 'track_number': 6, 'duration_ms': 223207, 'popularity': 40, 'danceability': 0.364, 'energy': 0.678, 'loudness': -7.206, 'speechiness': 0.0407, 'acousticness': 0.000374, 'instrumentalness': 0, 'liveness': 0.333, 'valence': 0.35, 'tempo': 123.17}, '7f6YUhXC4jknHbvhbqK4U4': {'name': 'Rest In You', 'artist_id': '44LPOpECjnIlnwH91wo2ir', 'artist_name': 'All Sons & Daughters', 'album_name': 'Poets & Saints', 'track_number': 8, 'duration_ms': 304400, 'popularity': 46, 'danceability': 0.331, 'energy': 0.185, 'loudness': -13.726, 'speechiness': 0.0294, 'acousticness': 0.678, 'instrumentalness': 7.21e-06, 'liveness': 0.105, 'valence': 0.106, 'tempo': 131.838}, '5gTvQeSZbSFJdh7dxF71e0': {'name': 'Getting Ready to Get Down', 'artist_id': '6igfLpd8s6DBBAuwebRUuo', 'artist_name': 'Josh Ritter', 'album_name': 'Sermon on the Rocks', 'track_number': 4, 'duration_ms': 196195, 'popularity': 56, 'danceability': 0.836, 'energy': 0.757, 'loudness': -6.168, 'speechiness': 0.0322, 'acousticness': 0.137, 'instrumentalness': 0, 'liveness': 0.0812, 'valence': 0.903, 'tempo': 107.001}, '1yLENA7X3q7xVEk57UjXY7': {'name': 'After Many Miles', 'artist_id': '30fXKjFrJ6I9tfwia1ZZMG', 'artist_name': 'The Ghost of Paul Revere', 'album_name': 'Believe', 'track_number': 1, 'duration_ms': 150413, 'popularity': 40, 'danceability': 0.875, 'energy': 0.309, 'loudness': -7.905, 'speechiness': 0.11, 'acousticness': 0.772, 'instrumentalness': 0, 'liveness': 0.109, 'valence': 0.423, 'tempo': 73.611}, '2CdNHP8DJ5tfbRoIRdcTeE': {'name': 'Quesadilla', 'artist_id': '6DIS6PRrLS3wbnZsf7vYic', 'artist_name': 'WALK THE MOON', 'album_name': 'Walk The Moon', 'track_number': 1, 'duration_ms': 195280, 'popularity': 56, 'danceability': 0.551, 'energy': 0.732, 'loudness': -6.081, 'speechiness': 0.0627, 'acousticness': 0.0019, 'instrumentalness': 0, 'liveness': 0.0764, 'valence': 0.628, 'tempo': 145.107}, '23AX1TW2CCpmqXtktvYe42': {'name': 'Called Me Higher', 'artist_id': '44LPOpECjnIlnwH91wo2ir', 'artist_name': 'All Sons & Daughters', 'album_name': 'The Longing EP No. 3', 'track_number': 4, 'duration_ms': 355320, 'popularity': 54, 'danceability': 0.367, 'energy': 0.507, 'loudness': -8.76, 'speechiness': 0.0321, 'acousticness': 0.43, 'instrumentalness': 5.43e-05, 'liveness': 0.102, 'valence': 0.199, 'tempo': 171.957}, '5MMZJtHOiH1RmQSSe3DJdg': {'name': 'Sleep On The Floor', 'artist_id': '16oZKvXb6WkQlVAjwo2Wbg', 'artist_name': 'The Lumineers', 'album_name': 'Cleopatra', 'track_number': 1, 'duration_ms': 211851, 'popularity': 67, 'danceability': 0.389, 'energy': 0.431, 'loudness': -8.061, 'speechiness': 0.0344, 'acousticness': 0.249, 'instrumentalness': 0, 'liveness': 0.13, 'valence': 0.279, 'tempo': 142.14}, '0eLkNeny2GaXvu4VQiHtxG': {'name': 'God With Us', 'artist_id': '44LPOpECjnIlnwH91wo2ir', 'artist_name': 'All Sons & Daughters', 'album_name': 'All Sons & Daughters', 'track_number': 3, 'duration_ms': 248035, 'popularity': 45, 'danceability': 0.453, 'energy': 0.401, 'loudness': -8.757, 'speechiness': 0.0267, 'acousticness': 0.234, 'instrumentalness': 0, 'liveness': 0.0977, 'valence': 0.26, 'tempo': 135.977}, '7LPNlKR6P8CYWEWJh1tg6K': {'name': 'Nothing Is Holding Me Back', 'artist_id': '7bvAtcPT3evvSeHDyu2zBC', 'artist_name': 'Bryan & Katie Torwalt', 'album_name': 'Here On Earth', 'track_number': 8, 'duration_ms': 264120, 'popularity': 52, 'danceability': 0.39, 'energy': 0.45, 'loudness': -9.129, 'speechiness': 0.0336, 'acousticness': 0.0377, 'instrumentalness': 1.26e-06, 'liveness': 0.14, 'valence': 0.19, 'tempo': 156.166}, '7HLTfpgbqC85BayqViMHmU': {'name': 'Television', 'artist_id': '5lBYzBQdFqhcJRc30cPHa9', 'artist_name': "You Won't", 'album_name': 'Skeptic Goodbye', 'track_number': 10, 'duration_ms': 150400, 'popularity': 50, 'danceability': 0.541, 'energy': 0.458, 'loudness': -7.105, 'speechiness': 0.222, 'acousticness': 0.846, 'instrumentalness': 0, 'liveness': 0.13, 'valence': 0.674, 'tempo': 78.922}, '7w5cxTEzp1rfV3KCy0Bd5N': {'name': 'Home', 'artist_id': '7giUHu5pv6YTZgSkxxCcgh', 'artist_name': 'Edward Sharpe & The Magnetic Zeros', 'album_name': 'Up from Below', 'track_number': 6, 'duration_ms': 303200, 'popularity': 73, 'danceability': 0.542, 'energy': 0.589, 'loudness': -6.623, 'speechiness': 0.0318, 'acousticness': 0.292, 'instrumentalness': 0.000522, 'liveness': 0.177, 'valence': 0.139, 'tempo': 111.665}, '3Nby7PH0S2jJpwDMRkIfcb': {'name': 'All the Poor and Powerless', 'artist_id': '44LPOpECjnIlnwH91wo2ir', 'artist_name': 'All Sons & Daughters', 'album_name': 'Season One', 'track_number': 3, 'duration_ms': 342893, 'popularity': 30, 'danceability': 0.363, 'energy': 0.308, 'loudness': -8.335, 'speechiness': 0.0304, 'acousticness': 0.389, 'instrumentalness': 2.43e-06, 'liveness': 0.0872, 'valence': 0.0765, 'tempo': 147.635}, '2F2zpDLZwxdGzT9soOfSZf': {'name': 'Scala Naturae', 'artist_id': '3sva1UjOJOx6cGISZOpItl', 'artist_name': 'The Collection', 'album_name': 'Ars Moriendi', 'track_number': 2, 'duration_ms': 334989, 'popularity': 24, 'danceability': 0.48, 'energy': 0.344, 'loudness': -8.226, 'speechiness': 0.028, 'acousticness': 0.212, 'instrumentalness': 8.09e-05, 'liveness': 0.297, 'valence': 0.176, 'tempo': 112.967}, '0Fu5Kgcj85v1n4pPs5CHUz': {'name': 'The Earth Is Yours', 'artist_id': '4J4o73Oun7v0XXRjN8DPif', 'artist_name': 'Gungor', 'album_name': 'Beautiful Things', 'track_number': 7, 'duration_ms': 188266, 'popularity': 41, 'danceability': 0.576, 'energy': 0.788, 'loudness': -7.084, 'speechiness': 0.0282, 'acousticness': 0.0879, 'instrumentalness': 0, 'liveness': 0.19, 'valence': 0.701, 'tempo': 135.983}, '1tmYNUQaDTffVpBT9IASk0': {'name': 'I Wait', 'artist_id': '44LPOpECjnIlnwH91wo2ir', 'artist_name': 'All Sons & Daughters', 'album_name': 'Poets & Saints', 'track_number': 7, 'duration_ms': 246106, 'popularity': 42, 'danceability': 0.267, 'energy': 0.389, 'loudness': -9.648, 'speechiness': 0.0281, 'acousticness': 0.382, 'instrumentalness': 0.00763, 'liveness': 0.0816, 'valence': 0.225, 'tempo': 95.54}, '32yiDCLJUdqYoaDR46z9gD': {'name': 'Stella', 'artist_id': '3zt4I5TLIb0Z9RigaiHe5G', 'artist_name': 'Cereus Bright', 'album_name': 'Happier Than Me', 'track_number': 2, 'duration_ms': 172866, 'popularity': 52, 'danceability': 0.602, 'energy': 0.744, 'loudness': -6.352, 'speechiness': 0.0319, 'acousticness': 0.0485, 'instrumentalness': 1.43e-06, 'liveness': 0.111, 'valence': 0.616, 'tempo': 116.905}, '4F9jpNQDKRFoyM4Ebpni6S': {'name': 'Amadeus', 'artist_id': '2AmW5LU0vqfHoN2qvghRFe', 'artist_name': 'Family and Friends', 'album_name': 'XOXO', 'track_number': 2, 'duration_ms': 207519, 'popularity': 62, 'danceability': 0.428, 'energy': 0.724, 'loudness': -7.264, 'speechiness': 0.0434, 'acousticness': 0.183, 'instrumentalness': 0.000136, 'liveness': 0.251, 'valence': 0.176, 'tempo': 146.917}, '7z6pDIQFv510mRKfyEjHR1': {'name': 'Codeine', 'artist_id': '3GjVVVcFmUgEJEAAsbGkf4', 'artist_name': 'Trampled By Turtles', 'album_name': 'Blue Sky and the Devil', 'track_number': 3, 'duration_ms': 189474, 'popularity': 50, 'danceability': 0.488, 'energy': 0.796, 'loudness': -8.63, 'speechiness': 0.036, 'acousticness': 0.0991, 'instrumentalness': 0.0574, 'liveness': 0.239, 'valence': 0.647, 'tempo': 137.016}, '2Cx61IzUXPJyhv3GzGtsZ3': {'name': 'Tiger Striped Sky', 'artist_id': '0XHM5ZNJDU8e4CfbWMeSzC', 'artist_name': 'Roo Panes', 'album_name': 'Little Giant', 'track_number': 6, 'duration_ms': 241720, 'popularity': 67, 'danceability': 0.473, 'energy': 0.317, 'loudness': -10.324, 'speechiness': 0.0318, 'acousticness': 0.944, 'instrumentalness': 0.0124, 'liveness': 0.11, 'valence': 0.125, 'tempo': 139.899}, '3Htx5VpJjmftQjaC3O9Tre': {'name': 'Battles', 'artist_id': '4DX2G1URzfEiRg2wBfv4ub', 'artist_name': 'Hudson Taylor', 'album_name': 'Singing For Strangers', 'track_number': 9, 'duration_ms': 207000, 'popularity': 41, 'danceability': 0.582, 'energy': 0.737, 'loudness': -7.795, 'speechiness': 0.0599, 'acousticness': 0.22, 'instrumentalness': 0, 'liveness': 0.0869, 'valence': 0.349, 'tempo': 127.589}, '2im8Pxe6JuPf6dhpxhl2nX': {'name': 'Shine', 'artist_id': '7D5oTJSXSHf51auG0106CQ', 'artist_name': 'Benjamin Francis Leftwich', 'album_name': 'Last Smoke Before the Snowstorm', 'track_number': 7, 'duration_ms': 182613, 'popularity': 58, 'danceability': 0.714, 'energy': 0.533, 'loudness': -10.405, 'speechiness': 0.0293, 'acousticness': 0.64, 'instrumentalness': 1.7e-06, 'liveness': 0.162, 'valence': 0.633, 'tempo': 118.107}, '6y468DyY1V67RBNCwzrMrC': {'name': 'L.I.F.E.G.O.E.S.O.N.', 'artist_id': '0aeLcja6hKzb7Uz2ou7ulP', 'artist_name': 'Noah And The Whale', 'album_name': 'Last Night On Earth', 'track_number': 3, 'duration_ms': 228000, 'popularity': 50, 'danceability': 0.603, 'energy': 0.745, 'loudness': -5.79, 'speechiness': 0.0368, 'acousticness': 0.207, 'instrumentalness': 0, 'liveness': 0.348, 'valence': 0.607, 'tempo': 81.981}, '13PUJCvdTSCT1dn70tlGdm': {'name': 'Welcome Home, Son', 'artist_id': '5EM6xJN2QNk0cL7EEm9HR9', 'artist_name': 'Radical Face', 'album_name': 'Ghost', 'track_number': 2, 'duration_ms': 285320, 'popularity': 69, 'danceability': 0.601, 'energy': 0.537, 'loudness': -9.464, 'speechiness': 0.0296, 'acousticness': 0.743, 'instrumentalness': 0.732, 'liveness': 0.143, 'valence': 0.39, 'tempo': 144.994}, '44tlexN3Rxgake8xlZePPI': {'name': 'Make You Mine (feat. Ricky Skaggs)', 'artist_id': '5sQqZtsAbXAoAnvA8iN9kN', 'artist_name': 'High Valley', 'album_name': 'County Line', 'track_number': 2, 'duration_ms': 211198, 'popularity': 0, 'danceability': 0.532, 'energy': 0.906, 'loudness': -2.99, 'speechiness': 0.0418, 'acousticness': 0.051, 'instrumentalness': 0, 'liveness': 0.133, 'valence': 0.572, 'tempo': 123.101}, '72zmwnbXjx9fMUjw3mbDSs': {'name': 'All We Ever Knew', 'artist_id': '0n94vC3S9c3mb2HyNAOcjg', 'artist_name': 'The Head and the Heart', 'album_name': 'Signs of Light', 'track_number': 1, 'duration_ms': 225560, 'popularity': 73, 'danceability': 0.487, 'energy': 0.724, 'loudness': -5.905, 'speechiness': 0.0289, 'acousticness': 0.00224, 'instrumentalness': 1.03e-05, 'liveness': 0.213, 'valence': 0.531, 'tempo': 102.03}, '3HaiZ4gVk7BnYpayCvHIRO': {'name': 'Why God Made a River', 'artist_id': '5sQqZtsAbXAoAnvA8iN9kN', 'artist_name': 'High Valley', 'album_name': 'County Line', 'track_number': 5, 'duration_ms': 178440, 'popularity': 31, 'danceability': 0.586, 'energy': 0.873, 'loudness': -3.303, 'speechiness': 0.0637, 'acousticness': 0.0698, 'instrumentalness': 0, 'liveness': 0.11, 'valence': 0.648, 'tempo': 111.888}, '4XXkAMGVUz8Txq3m8MoIAR': {'name': 'Northern Sky', 'artist_id': '7ewhxhtYBkaKtWsilZIqPd', 'artist_name': 'Kevin William', 'album_name': 'Current Fears', 'track_number': 2, 'duration_ms': 223825, 'popularity': 5, 'danceability': 0.444, 'energy': 0.563, 'loudness': -5.856, 'speechiness': 0.0469, 'acousticness': 0.373, 'instrumentalness': 0, 'liveness': 0.099, 'valence': 0.446, 'tempo': 69.275}, '2sE61ZmvYH8wiOx5jygkHH': {'name': 'Say You Do', 'artist_id': '7x8nK0m0cP2ksQf0mjWdPS', 'artist_name': 'Dierks Bentley', 'album_name': 'RISER', 'track_number': 2, 'duration_ms': 219360, 'popularity': 60, 'danceability': 0.477, 'energy': 0.737, 'loudness': -8.166, 'speechiness': 0.0345, 'acousticness': 0.122, 'instrumentalness': 0.00167, 'liveness': 0.105, 'valence': 0.475, 'tempo': 147.959}, '0BGM5wPT4L0KNKrf3WsMkn': {'name': 'Make This Leap', 'artist_id': '1fFdRZK1GDGXL7vRxxUWLH', 'artist_name': 'The Hunts', 'album_name': 'Those Younger Days', 'track_number': 5, 'duration_ms': 226426, 'popularity': 46, 'danceability': 0.704, 'energy': 0.412, 'loudness': -7.623, 'speechiness': 0.0332, 'acousticness': 0.896, 'instrumentalness': 2.88e-05, 'liveness': 0.103, 'valence': 0.697, 'tempo': 138.109}, '4KANJH1baadr3U7XsVbM17': {'name': 'Something I Need', 'artist_id': '5Pwc4xIPtQLFEnJriah9YJ', 'artist_name': 'OneRepublic', 'album_name': 'Native', 'track_number': 11, 'duration_ms': 241266, 'popularity': 59, 'danceability': 0.686, 'energy': 0.59, 'loudness': -6.923, 'speechiness': 0.03, 'acousticness': 0.168, 'instrumentalness': 0, 'liveness': 0.118, 'valence': 0.638, 'tempo': 98.991}, '25pHcckhIot8apIQn6NN8F': {'name': 'Hoax', 'artist_id': '7ewhxhtYBkaKtWsilZIqPd', 'artist_name': 'Kevin William', 'album_name': 'Current Fears', 'track_number': 1, 'duration_ms': 271482, 'popularity': 5, 'danceability': 0.335, 'energy': 0.523, 'loudness': -6.114, 'speechiness': 0.0294, 'acousticness': 0.132, 'instrumentalness': 0, 'liveness': 0.115, 'valence': 0.445, 'tempo': 96.384}, '47zl5FL7ue5ez0zgXXg2gZ': {'name': 'Midnight', 'artist_id': '7ewhxhtYBkaKtWsilZIqPd', 'artist_name': 'Kevin William', 'album_name': 'Midnight', 'track_number': 1, 'duration_ms': 239424, 'popularity': 5, 'danceability': 0.28, 'energy': 0.34, 'loudness': -8.263, 'speechiness': 0.0299, 'acousticness': 0.0278, 'instrumentalness': 0.00021, 'liveness': 0.117, 'valence': 0.14, 'tempo': 131.493}, '6OtCIsQZ64Vs1EbzztvAv4': {'name': 'Good Life', 'artist_id': '5Pwc4xIPtQLFEnJriah9YJ', 'artist_name': 'OneRepublic', 'album_name': 'Waking Up', 'track_number': 6, 'duration_ms': 253306, 'popularity': 64, 'danceability': 0.636, 'energy': 0.699, 'loudness': -7.687, 'speechiness': 0.0551, 'acousticness': 0.0929, 'instrumentalness': 0, 'liveness': 0.115, 'valence': 0.642, 'tempo': 94.966}, '5ITmuvjtUUdxVQCCsaKBDx': {'name': 'As We Ran', 'artist_id': '2JMtxA2S9SNUlqBlkDtXm6', 'artist_name': 'The National Parks', 'album_name': 'As We Ran', 'track_number': 1, 'duration_ms': 200321, 'popularity': 53, 'danceability': 0.431, 'energy': 0.588, 'loudness': -6.855, 'speechiness': 0.0348, 'acousticness': 0.0169, 'instrumentalness': 0.00689, 'liveness': 0.368, 'valence': 0.186, 'tempo': 143.975}, '2c62Xf5Po1YSa1N6LOjPHy': {'name': 'Hello My Old Heart', 'artist_id': '3Fe3pszR2t4TOBVz41B1WR', 'artist_name': 'The Oh Hellos', 'album_name': 'The Oh Hellos EP', 'track_number': 1, 'duration_ms': 256006, 'popularity': 64, 'danceability': 0.557, 'energy': 0.299, 'loudness': -10.634, 'speechiness': 0.0266, 'acousticness': 0.624, 'instrumentalness': 0.0308, 'liveness': 0.0914, 'valence': 0.282, 'tempo': 90.081}, '7CEV9VwA8XO9wwxTXgYKvY': {'name': 'I And Love And You', 'artist_id': '196lKsA13K3keVXMDFK66q', 'artist_name': 'The Avett Brothers', 'album_name': 'I And Love And You', 'track_number': 1, 'duration_ms': 300840, 'popularity': 63, 'danceability': 0.494, 'energy': 0.268, 'loudness': -10.063, 'speechiness': 0.0315, 'acousticness': 0.816, 'instrumentalness': 9.74e-05, 'liveness': 0.076, 'valence': 0.16, 'tempo': 70.223}, '3LbvNFkqDTrE1liGMmZBDL': {'name': 'Shotgun Rider', 'artist_id': '6roFdX1y5BYSbp60OTJWMd', 'artist_name': 'Tim McGraw', 'album_name': 'Sundown Heaven Town', 'track_number': 3, 'duration_ms': 235386, 'popularity': 62, 'danceability': 0.458, 'energy': 0.903, 'loudness': -4.589, 'speechiness': 0.0493, 'acousticness': 0.136, 'instrumentalness': 8.06e-06, 'liveness': 0.146, 'valence': 0.695, 'tempo': 167.847}, '4y0Lt1KOuyhKGkGKFZjSlS': {'name': 'Opening Titles', 'artist_id': '0YC192cP3KPCRWx8zr8MfZ', 'artist_name': 'Hans Zimmer', 'album_name': 'Call of Duty: Modern Warfare 2', 'track_number': 1, 'duration_ms': 205333, 'popularity': 50, 'danceability': 0.303, 'energy': 0.401, 'loudness': -13.932, 'speechiness': 0.0375, 'acousticness': 0.0228, 'instrumentalness': 0.768, 'liveness': 0.113, 'valence': 0.0962, 'tempo': 155.822}, '0qcPs4kTUmCMCsGcj7E1Ze': {'name': 'Arrival Time', 'artist_id': '7ewhxhtYBkaKtWsilZIqPd', 'artist_name': 'Kevin William', 'album_name': 'Current Fears', 'track_number': 3, 'duration_ms': 252605, 'popularity': 7, 'danceability': 0.457, 'energy': 0.696, 'loudness': -6.01, 'speechiness': 0.0504, 'acousticness': 0.334, 'instrumentalness': 1.28e-06, 'liveness': 0.0887, 'valence': 0.365, 'tempo': 183.052}, '0tcLy28fz77slArBF9e2k1': {'name': 'Idols', 'artist_id': '7ewhxhtYBkaKtWsilZIqPd', 'artist_name': 'Kevin William', 'album_name': 'Current Fears', 'track_number': 5, 'duration_ms': 212793, 'popularity': 2, 'danceability': 0.335, 'energy': 0.329, 'loudness': -7.367, 'speechiness': 0.0395, 'acousticness': 0.558, 'instrumentalness': 0, 'liveness': 0.103, 'valence': 0.304, 'tempo': 185.112}, '0px0N4hIsQg1ITVi4Nee5c': {'name': 'County Line', 'artist_id': '5sQqZtsAbXAoAnvA8iN9kN', 'artist_name': 'High Valley', 'album_name': 'County Line', 'track_number': 1, 'duration_ms': 209734, 'popularity': 36, 'danceability': 0.503, 'energy': 0.959, 'loudness': -2.538, 'speechiness': 0.0387, 'acousticness': 0.0195, 'instrumentalness': 1.12e-06, 'liveness': 0.197, 'valence': 0.688, 'tempo': 150.069}, '6ho8nmo2Z0y1tSCAdbjRE6': {'name': 'Close Your Eyes', 'artist_id': '4TshyQDihSYXSWqvclXl3I', 'artist_name': 'Parmalee', 'album_name': 'Feels Like Carolina', 'track_number': 4, 'duration_ms': 214933, 'popularity': 54, 'danceability': 0.548, 'energy': 0.849, 'loudness': -3.499, 'speechiness': 0.0323, 'acousticness': 0.0159, 'instrumentalness': 0, 'liveness': 0.0845, 'valence': 0.804, 'tempo': 143.973}, '4bcUaD52IBY6VRYxfCiuYt': {'name': 'Man of Doubt', 'artist_id': '7ewhxhtYBkaKtWsilZIqPd', 'artist_name': 'Kevin William', 'album_name': 'Current Fears', 'track_number': 6, 'duration_ms': 224464, 'popularity': 2, 'danceability': 0.409, 'energy': 0.396, 'loudness': -7.498, 'speechiness': 0.0294, 'acousticness': 0.738, 'instrumentalness': 0, 'liveness': 0.167, 'valence': 0.326, 'tempo': 87.834}, '33y3ks1NgN9qCnKPLU3BTo': {'name': 'Love You for a Long Time', 'artist_id': '5sQqZtsAbXAoAnvA8iN9kN', 'artist_name': 'High Valley', 'album_name': 'Rescue You', 'track_number': 6, 'duration_ms': 181420, 'popularity': 30, 'danceability': 0.593, 'energy': 0.765, 'loudness': -4.869, 'speechiness': 0.032, 'acousticness': 0.00151, 'instrumentalness': 0, 'liveness': 0.0852, 'valence': 0.394, 'tempo': 125.054}, '3wx2kQWPn9p5UppQbNhPAk': {'name': 'Leave The Night On', 'artist_id': '2kucQ9jQwuD8jWdtR9Ef38', 'artist_name': 'Sam Hunt', 'album_name': 'Montevallo', 'track_number': 2, 'duration_ms': 192160, 'popularity': 73, 'danceability': 0.516, 'energy': 0.953, 'loudness': -3.828, 'speechiness': 0.0624, 'acousticness': 0.0996, 'instrumentalness': 0, 'liveness': 0.349, 'valence': 0.849, 'tempo': 171.971}, '0gbpvYtk6nMyLa5nwUjPkJ': {'name': 'Be You', 'artist_id': '5sQqZtsAbXAoAnvA8iN9kN', 'artist_name': 'High Valley', 'album_name': 'County Line', 'track_number': 2, 'duration_ms': 187507, 'popularity': 35, 'danceability': 0.509, 'energy': 0.878, 'loudness': -3.227, 'speechiness': 0.049, 'acousticness': 0.0198, 'instrumentalness': 0, 'liveness': 0.15, 'valence': 0.336, 'tempo': 144.048}, '3T7KFsyl6n3UklWgfn0Lnp': {'name': 'Cross My Mind', 'artist_id': '6GwNGuDRNbx5XwoHQA3QiD', 'artist_name': 'Twin Forks', 'album_name': 'Twin Forks', 'track_number': 2, 'duration_ms': 214613, 'popularity': 49, 'danceability': 0.613, 'energy': 0.84, 'loudness': -5.084, 'speechiness': 0.0287, 'acousticness': 0.367, 'instrumentalness': 0, 'liveness': 0.244, 'valence': 0.504, 'tempo': 90.984}, '0ABHhxQTaluB94ohp2RLSr': {'name': 'Feelin It', 'artist_id': '6ZV6lGY0prbqpTD0Md8i29', 'artist_name': 'Scotty McCreery', 'album_name': 'See You Tonight', 'track_number': 4, 'duration_ms': 198226, 'popularity': 56, 'danceability': 0.584, 'energy': 0.771, 'loudness': -5.322, 'speechiness': 0.0514, 'acousticness': 0.107, 'instrumentalness': 0, 'liveness': 0.0844, 'valence': 0.686, 'tempo': 184.114}, '4B6vZwJl0PJ42nD5bHUQeM': {'name': 'Children', 'artist_id': '7ewhxhtYBkaKtWsilZIqPd', 'artist_name': 'Kevin William', 'album_name': 'Current Fears', 'track_number': 4, 'duration_ms': 213456, 'popularity': 2, 'danceability': 0.49, 'energy': 0.487, 'loudness': -7.774, 'speechiness': 0.0327, 'acousticness': 0.0485, 'instrumentalness': 0, 'liveness': 0.112, 'valence': 0.194, 'tempo': 120.142}, '4q0SB41tm7eFqnAODPM8C6': {'name': 'Take It On Back', 'artist_id': '7io3MyhMxDZoBYXp4rlRFA', 'artist_name': 'Chase Bryant', 'album_name': 'Chase Bryant', 'track_number': 5, 'duration_ms': 244453, 'popularity': 53, 'danceability': 0.558, 'energy': 0.815, 'loudness': -5.352, 'speechiness': 0.067, 'acousticness': 0.0122, 'instrumentalness': 0, 'liveness': 0.0705, 'valence': 0.649, 'tempo': 157.954}, '6DEaND0SHv3sC11xobZLiy': {'name': 'Take Your Time', 'artist_id': '2kucQ9jQwuD8jWdtR9Ef38', 'artist_name': 'Sam Hunt', 'album_name': 'Montevallo', 'track_number': 1, 'duration_ms': 243706, 'popularity': 74, 'danceability': 0.551, 'energy': 0.719, 'loudness': -5.631, 'speechiness': 0.0416, 'acousticness': 0.0869, 'instrumentalness': 0, 'liveness': 0.219, 'valence': 0.456, 'tempo': 158.08}, '7hIRQZhDjab4YgqkkkehV9': {'name': 'If I Lose Myself', 'artist_id': '5Pwc4xIPtQLFEnJriah9YJ', 'artist_name': 'OneRepublic', 'album_name': 'Native', 'track_number': 3, 'duration_ms': 241640, 'popularity': 59, 'danceability': 0.484, 'energy': 0.715, 'loudness': -6.005, 'speechiness': 0.0478, 'acousticness': 0.0923, 'instrumentalness': 0, 'liveness': 0.112, 'valence': 0.294, 'tempo': 140.073}, '5misaMDzoPWVxvjBTVwx7v': {'name': 'Come on Down', 'artist_id': '5sQqZtsAbXAoAnvA8iN9kN', 'artist_name': 'High Valley', 'album_name': 'County Line', 'track_number': 6, 'duration_ms': 202064, 'popularity': 40, 'danceability': 0.684, 'energy': 0.902, 'loudness': -3.018, 'speechiness': 0.0412, 'acousticness': 0.134, 'instrumentalness': 0, 'liveness': 0.0908, 'valence': 0.671, 'tempo': 106.015}, '1gRZZ2BQZ9XFu3t2lXvynZ': {'name': 'Lay It On Me', 'artist_id': '78YqeIji3mgAS2K1Maca6x', 'artist_name': 'Dylan Scott', 'album_name': 'Dylan Scott', 'track_number': 1, 'duration_ms': 178346, 'popularity': 54, 'danceability': 0.49, 'energy': 0.879, 'loudness': -4.909, 'speechiness': 0.0355, 'acousticness': 0.0105, 'instrumentalness': 0, 'liveness': 0.0809, 'valence': 0.693, 'tempo': 75.032}, '14s1A7gCghXIt7LXYYdYdp': {'name': 'Rescue You', 'artist_id': '5sQqZtsAbXAoAnvA8iN9kN', 'artist_name': 'High Valley', 'album_name': 'Rescue You', 'track_number': 2, 'duration_ms': 159399, 'popularity': 32, 'danceability': 0.451, 'energy': 0.793, 'loudness': -4.894, 'speechiness': 0.0268, 'acousticness': 0.188, 'instrumentalness': 0, 'liveness': 0.115, 'valence': 0.651, 'tempo': 107.86}, '359krpyCKcFF8SFvqWES9L': {'name': 'Wagon Wheel', 'artist_id': '4DBi4EYXgiqbkxvWUXUzMi', 'artist_name': 'Old Crow Medicine Show', 'album_name': 'O.C.M.S.', 'track_number': 11, 'duration_ms': 232133, 'popularity': 64, 'danceability': 0.621, 'energy': 0.403, 'loudness': -8.211, 'speechiness': 0.0359, 'acousticness': 0.58, 'instrumentalness': 0, 'liveness': 0.114, 'valence': 0.643, 'tempo': 145.525}, '0IsjGDAqohBEdZWVoTaMjI': {'name': 'Raised by a Good Time', 'artist_id': '5MW08rvyz59mdceF4urxXO', 'artist_name': 'Steven Lee Olsen', 'album_name': 'Raised by a Good Time', 'track_number': 1, 'duration_ms': 192986, 'popularity': 51, 'danceability': 0.583, 'energy': 0.859, 'loudness': -4.495, 'speechiness': 0.0402, 'acousticness': 0.0579, 'instrumentalness': 0, 'liveness': 0.11, 'valence': 0.587, 'tempo': 142.071}, '1crbFuCkGL4kXnAGd63RXq': {'name': 'Crooked Teeth', 'artist_id': '0YrtvWJMgSdVrk3SfNjTbx', 'artist_name': 'Death Cab for Cutie', 'album_name': 'Plans', 'track_number': 8, 'duration_ms': 203733, 'popularity': 54, 'danceability': 0.579, 'energy': 0.662, 'loudness': -6.885, 'speechiness': 0.0245, 'acousticness': 0.000625, 'instrumentalness': 3.89e-06, 'liveness': 0.117, 'valence': 0.583, 'tempo': 102.951}, '1VklQ1e01s84jFTRD9np7n': {'name': 'Farm Girl', 'artist_id': '5sQqZtsAbXAoAnvA8iN9kN', 'artist_name': 'High Valley', 'album_name': 'County Line', 'track_number': 4, 'duration_ms': 189164, 'popularity': 33, 'danceability': 0.564, 'energy': 0.957, 'loudness': -3.203, 'speechiness': 0.0679, 'acousticness': 0.0342, 'instrumentalness': 0, 'liveness': 0.329, 'valence': 0.866, 'tempo': 152.049}, '0W4Kpfp1w2xkY3PrV714B7': {'name': 'Ho Hey', 'artist_id': '16oZKvXb6WkQlVAjwo2Wbg', 'artist_name': 'The Lumineers', 'album_name': 'The Lumineers', 'track_number': 5, 'duration_ms': 163133, 'popularity': 72, 'danceability': 0.685, 'energy': 0.466, 'loudness': -9.074, 'speechiness': 0.0304, 'acousticness': 0.794, 'instrumentalness': 2.06e-06, 'liveness': 0.0915, 'valence': 0.37, 'tempo': 79.936}, '3d8y0t70g7hw2FOWl9Z4Fm': {'name': 'Ophelia', 'artist_id': '16oZKvXb6WkQlVAjwo2Wbg', 'artist_name': 'The Lumineers', 'album_name': 'Cleopatra', 'track_number': 2, 'duration_ms': 160097, 'popularity': 71, 'danceability': 0.664, 'energy': 0.573, 'loudness': -6.519, 'speechiness': 0.0277, 'acousticness': 0.613, 'instrumentalness': 0.000363, 'liveness': 0.0857, 'valence': 0.573, 'tempo': 76.023}, '2ToW7zhGCrVrLU4fiKj9U1': {'name': 'Cleopatra', 'artist_id': '16oZKvXb6WkQlVAjwo2Wbg', 'artist_name': 'The Lumineers', 'album_name': 'Cleopatra', 'track_number': 3, 'duration_ms': 201413, 'popularity': 69, 'danceability': 0.536, 'energy': 0.775, 'loudness': -6.765, 'speechiness': 0.0394, 'acousticness': 0.228, 'instrumentalness': 0.000143, 'liveness': 0.0947, 'valence': 0.501, 'tempo': 151.393}, '3ekNuTF3UpOvIZCfiejpnC': {'name': 'Stubborn Love', 'artist_id': '16oZKvXb6WkQlVAjwo2Wbg', 'artist_name': 'The Lumineers', 'album_name': 'The Lumineers', 'track_number': 7, 'duration_ms': 279000, 'popularity': 69, 'danceability': 0.598, 'energy': 0.56, 'loudness': -11.679, 'speechiness': 0.0375, 'acousticness': 0.607, 'instrumentalness': 0.0432, 'liveness': 0.196, 'valence': 0.225, 'tempo': 115.01}, '66nJBHV6WtQI3IiU6n8fY5': {'name': 'Slow It Down', 'artist_id': '16oZKvXb6WkQlVAjwo2Wbg', 'artist_name': 'The Lumineers', 'album_name': 'The Lumineers', 'track_number': 6, 'duration_ms': 307000, 'popularity': 66, 'danceability': 0.428, 'energy': 0.064, 'loudness': -14.42, 'speechiness': 0.0374, 'acousticness': 0.929, 'instrumentalness': 0, 'liveness': 0.0859, 'valence': 0.108, 'tempo': 142.436}, '5bodDpPolC3xlame0SVcDY': {'name': 'Angela', 'artist_id': '16oZKvXb6WkQlVAjwo2Wbg', 'artist_name': 'The Lumineers', 'album_name': 'Cleopatra', 'track_number': 5, 'duration_ms': 201785, 'popularity': 65, 'danceability': 0.668, 'energy': 0.563, 'loudness': -8.23, 'speechiness': 0.0305, 'acousticness': 0.649, 'instrumentalness': 0.000347, 'liveness': 0.11, 'valence': 0.299, 'tempo': 130.366}, '5kGBSOrKYmhRfdPBw4xD8D': {'name': 'Angela (Single Version)', 'artist_id': '16oZKvXb6WkQlVAjwo2Wbg', 'artist_name': 'The Lumineers', 'album_name': 'Angela (Single Version)', 'track_number': 1, 'duration_ms': 178840, 'popularity': 61, 'danceability': 0.652, 'energy': 0.601, 'loudness': -7.988, 'speechiness': 0.0317, 'acousticness': 0.625, 'instrumentalness': 0.000165, 'liveness': 0.17, 'valence': 0.274, 'tempo': 130.308}, '0QZ5yyl6B6utIWkxeBDxQN': {'name': 'The Night We Met', 'artist_id': '6ltzsmQQbmdoHHbLZ4ZN25', 'artist_name': 'Lord Huron', 'album_name': 'Strange Trails', 'track_number': 14, 'duration_ms': 208226, 'popularity': 77, 'danceability': 0.441, 'energy': 0.379, 'loudness': -9.545, 'speechiness': 0.0449, 'acousticness': 0.968, 'instrumentalness': 0.262, 'liveness': 0.639, 'valence': 0.107, 'tempo': 174.118}, '77x96TdWdkIia82QqU35SD': {'name': 'Fool for Love', 'artist_id': '6ltzsmQQbmdoHHbLZ4ZN25', 'artist_name': 'Lord Huron', 'album_name': 'Strange Trails', 'track_number': 6, 'duration_ms': 274706, 'popularity': 61, 'danceability': 0.619, 'energy': 0.758, 'loudness': -6.285, 'speechiness': 0.0367, 'acousticness': 0.598, 'instrumentalness': 0.192, 'liveness': 0.113, 'valence': 0.223, 'tempo': 90.993}, '0zCckv4tx3KzJ5GGTRbbLf': {'name': 'She Lit a Fire', 'artist_id': '6ltzsmQQbmdoHHbLZ4ZN25', 'artist_name': 'Lord Huron', 'album_name': 'Lonesome Dreams', 'track_number': 5, 'duration_ms': 270666, 'popularity': 59, 'danceability': 0.484, 'energy': 0.734, 'loudness': -6.674, 'speechiness': 0.0283, 'acousticness': 0.259, 'instrumentalness': 0.000215, 'liveness': 0.0997, 'valence': 0.431, 'tempo': 84.958}, '1bqrRn1pJWowNLA5N9L6uW': {'name': 'Meet Me in the Woods', 'artist_id': '6ltzsmQQbmdoHHbLZ4ZN25', 'artist_name': 'Lord Huron', 'album_name': 'Strange Trails', 'track_number': 8, 'duration_ms': 262213, 'popularity': 59, 'danceability': 0.543, 'energy': 0.907, 'loudness': -6.698, 'speechiness': 0.0427, 'acousticness': 0.36, 'instrumentalness': 0.622, 'liveness': 0.0689, 'valence': 0.602, 'tempo': 80.5}, '4UGoW08gaqIEWNTam1UNen': {'name': 'Love Like Ghosts', 'artist_id': '6ltzsmQQbmdoHHbLZ4ZN25', 'artist_name': 'Lord Huron', 'album_name': 'Strange Trails', 'track_number': 1, 'duration_ms': 224053, 'popularity': 56, 'danceability': 0.476, 'energy': 0.551, 'loudness': -7.228, 'speechiness': 0.0273, 'acousticness': 0.767, 'instrumentalness': 0.00126, 'liveness': 0.123, 'valence': 0.182, 'tempo': 137.049}, '3NNimGud58iHka1LHkda6D': {'name': 'The World Ender', 'artist_id': '6ltzsmQQbmdoHHbLZ4ZN25', 'artist_name': 'Lord Huron', 'album_name': 'Strange Trails', 'track_number': 7, 'duration_ms': 270053, 'popularity': 54, 'danceability': 0.547, 'energy': 0.934, 'loudness': -5.6, 'speechiness': 0.0346, 'acousticness': 0.59, 'instrumentalness': 0.384, 'liveness': 0.804, 'valence': 0.744, 'tempo': 157.033}, '3SVSjlirwiGk5cepW66iBS': {'name': 'Lonesome Dreams', 'artist_id': '6ltzsmQQbmdoHHbLZ4ZN25', 'artist_name': 'Lord Huron', 'album_name': 'Lonesome Dreams', 'track_number': 3, 'duration_ms': 255573, 'popularity': 52, 'danceability': 0.548, 'energy': 0.786, 'loudness': -7.421, 'speechiness': 0.0284, 'acousticness': 0.861, 'instrumentalness': 0.0197, 'liveness': 0.261, 'valence': 0.467, 'tempo': 140.352}, '5IleMdgH4wAm6MnWLLjEra': {'name': 'La Belle Fleur Sauvage', 'artist_id': '6ltzsmQQbmdoHHbLZ4ZN25', 'artist_name': 'Lord Huron', 'album_name': 'Strange Trails', 'track_number': 5, 'duration_ms': 341133, 'popularity': 52, 'danceability': 0.531, 'energy': 0.655, 'loudness': -6.993, 'speechiness': 0.0296, 'acousticness': 0.83, 'instrumentalness': 0.123, 'liveness': 0.381, 'valence': 0.2, 'tempo': 87.523}, '0eQBlLMUunP21spx6MeMts': {'name': 'Called On - Bonus Track', 'artist_id': '4DX2G1URzfEiRg2wBfv4ub', 'artist_name': 'Hudson Taylor', 'album_name': 'Singing For Strangers', 'track_number': 19, 'duration_ms': 210000, 'popularity': 35, 'danceability': 0.463, 'energy': 0.44, 'loudness': -7.702, 'speechiness': 0.029, 'acousticness': 0.791, 'instrumentalness': 0, 'liveness': 0.0977, 'valence': 0.385, 'tempo': 86.059}, '1sKZ2ZXYlWmnEr8yJF1u21': {'name': 'Chasing Rubies', 'artist_id': '4DX2G1URzfEiRg2wBfv4ub', 'artist_name': 'Hudson Taylor', 'album_name': 'Singing For Strangers', 'track_number': 3, 'duration_ms': 226600, 'popularity': 28, 'danceability': 0.633, 'energy': 0.662, 'loudness': -9.183, 'speechiness': 0.0309, 'acousticness': 0.0337, 'instrumentalness': 0, 'liveness': 0.202, 'valence': 0.609, 'tempo': 144.025}, '6KmnJh5FpFOJHPXAIJ6M2J': {'name': 'Weapons', 'artist_id': '4DX2G1URzfEiRg2wBfv4ub', 'artist_name': 'Hudson Taylor', 'album_name': 'Singing For Strangers', 'track_number': 7, 'duration_ms': 177000, 'popularity': 27, 'danceability': 0.506, 'energy': 0.504, 'loudness': -8.677, 'speechiness': 0.0406, 'acousticness': 0.486, 'instrumentalness': 0, 'liveness': 0.111, 'valence': 0.367, 'tempo': 154.594}, '5dSdEPRHR4c8v5fxS2F4Z6': {'name': 'Just A Thought', 'artist_id': '4DX2G1URzfEiRg2wBfv4ub', 'artist_name': 'Hudson Taylor', 'album_name': 'Singing For Strangers', 'track_number': 1, 'duration_ms': 192500, 'popularity': 34, 'danceability': 0.369, 'energy': 0.746, 'loudness': -8.279, 'speechiness': 0.0592, 'acousticness': 0.0125, 'instrumentalness': 0, 'liveness': 0.354, 'valence': 0.512, 'tempo': 79.15}, '4cwivYcdU7K1cc8XmTvf82': {'name': 'Chasing Rubies - Acoustic', 'artist_id': '4DX2G1URzfEiRg2wBfv4ub', 'artist_name': 'Hudson Taylor', 'album_name': 'Chasing Rubies', 'track_number': 4, 'duration_ms': 259466, 'popularity': 35, 'danceability': 0.54, 'energy': 0.552, 'loudness': -4.297, 'speechiness': 0.0285, 'acousticness': 0.655, 'instrumentalness': 0, 'liveness': 0.0967, 'valence': 0.523, 'tempo': 144.107}, '739iJdEQSZWC0IV12uoK4T': {'name': 'Drop Of Smoke', 'artist_id': '4DX2G1URzfEiRg2wBfv4ub', 'artist_name': 'Hudson Taylor', 'album_name': 'Chasing Rubies', 'track_number': 2, 'duration_ms': 181586, 'popularity': 30, 'danceability': 0.503, 'energy': 0.818, 'loudness': -6.487, 'speechiness': 0.0398, 'acousticness': 0.302, 'instrumentalness': 2.25e-05, 'liveness': 0.29, 'valence': 0.389, 'tempo': 96.483}, '2l0Q3cp5Ua1br9Sq1wCTRY': {'name': 'Butterflies', 'artist_id': '4DX2G1URzfEiRg2wBfv4ub', 'artist_name': 'Hudson Taylor', 'album_name': 'Singing For Strangers', 'track_number': 2, 'duration_ms': 177546, 'popularity': 23, 'danceability': 0.543, 'energy': 0.598, 'loudness': -8.547, 'speechiness': 0.0337, 'acousticness': 0.0805, 'instrumentalness': 0, 'liveness': 0.111, 'valence': 0.328, 'tempo': 95.966}, '6xBv2Rlq9DiYeTBFno0uR5': {'name': 'Cedarsmoke', 'artist_id': '3ZllGjNdP5pS8UFnT5Jj2x', 'artist_name': 'Sea Wolf', 'album_name': 'Song Spells, No.1: Cedarsmoke', 'track_number': 5, 'duration_ms': 214093, 'popularity': 50, 'danceability': 0.168, 'energy': 0.368, 'loudness': -17.304, 'speechiness': 0.0608, 'acousticness': 0.77, 'instrumentalness': 0.938, 'liveness': 0.312, 'valence': 0.372, 'tempo': 85.377}, '4cFMT3DwTYChrjBT71hqGy': {'name': "You're a Wolf", 'artist_id': '3ZllGjNdP5pS8UFnT5Jj2x', 'artist_name': 'Sea Wolf', 'album_name': 'Leaves in the River', 'track_number': 6, 'duration_ms': 215560, 'popularity': 50, 'danceability': 0.676, 'energy': 0.671, 'loudness': -7.636, 'speechiness': 0.027, 'acousticness': 0.69, 'instrumentalness': 0.183, 'liveness': 0.138, 'valence': 0.544, 'tempo': 121.008}, '4BhEQsifqbzCdknLf52O1G': {'name': 'Young Bodies', 'artist_id': '3ZllGjNdP5pS8UFnT5Jj2x', 'artist_name': 'Sea Wolf', 'album_name': 'Song Spells, No.1: Cedarsmoke', 'track_number': 6, 'duration_ms': 209266, 'popularity': 50, 'danceability': 0.694, 'energy': 0.237, 'loudness': -16.391, 'speechiness': 0.0413, 'acousticness': 0.938, 'instrumentalness': 0.296, 'liveness': 0.109, 'valence': 0.345, 'tempo': 136.866}, '2tJ5nxeNIFTNGSqyFvG8Ov': {'name': 'Intro', 'artist_id': '3ZllGjNdP5pS8UFnT5Jj2x', 'artist_name': 'Sea Wolf', 'album_name': 'Song Spells, No.1: Cedarsmoke', 'track_number': 1, 'duration_ms': 140000, 'popularity': 46, 'danceability': 0.234, 'energy': 0.333, 'loudness': -18.284, 'speechiness': 0.0425, 'acousticness': 0.704, 'instrumentalness': 0.868, 'liveness': 0.334, 'valence': 0.148, 'tempo': 184.839}, '26yoPdmJ5K44quYeTzxcsT': {'name': 'Middle Distance Runner', 'artist_id': '3ZllGjNdP5pS8UFnT5Jj2x', 'artist_name': 'Sea Wolf', 'album_name': 'Leaves in the River', 'track_number': 5, 'duration_ms': 207666, 'popularity': 45, 'danceability': 0.751, 'energy': 0.527, 'loudness': -10.933, 'speechiness': 0.0274, 'acousticness': 0.54, 'instrumentalness': 0.00066, 'liveness': 0.0978, 'valence': 0.71, 'tempo': 103.03}, '73wwgXHDgUkF5foFy3oyuU': {'name': 'The Garden You Planted', 'artist_id': '3ZllGjNdP5pS8UFnT5Jj2x', 'artist_name': 'Sea Wolf', 'album_name': 'Get to the River Before It Runs Too Low', 'track_number': 2, 'duration_ms': 241773, 'popularity': 44, 'danceability': 0.597, 'energy': 0.303, 'loudness': -15.028, 'speechiness': 0.0251, 'acousticness': 0.744, 'instrumentalness': 0.137, 'liveness': 0.139, 'valence': 0.323, 'tempo': 88.245}, '5H7PvgENZHanmlrJyolIzK': {'name': 'Bergamot Morning', 'artist_id': '3ZllGjNdP5pS8UFnT5Jj2x', 'artist_name': 'Sea Wolf', 'album_name': 'Song Spells, No.1: Cedarsmoke', 'track_number': 3, 'duration_ms': 208946, 'popularity': 42, 'danceability': 0.651, 'energy': 0.702, 'loudness': -11.115, 'speechiness': 0.0285, 'acousticness': 0.421, 'instrumentalness': 0.0034, 'liveness': 0.124, 'valence': 0.516, 'tempo': 131.962}, '1aMiDQtbZlTAq93SsbG1wN': {'name': 'Leaves in the River', 'artist_id': '3ZllGjNdP5pS8UFnT5Jj2x', 'artist_name': 'Sea Wolf', 'album_name': 'Leaves in the River', 'track_number': 1, 'duration_ms': 300080, 'popularity': 39, 'danceability': 0.587, 'energy': 0.34, 'loudness': -14.614, 'speechiness': 0.0349, 'acousticness': 0.852, 'instrumentalness': 0.000224, 'liveness': 0.364, 'valence': 0.512, 'tempo': 135.775}, '3gbBpTdY8lnQwqxNCcf795': {'name': 'Pompeii', 'artist_id': '7EQ0qTo7fWT7DPxmxtSYEc', 'artist_name': 'Bastille', 'album_name': 'Bad Blood', 'track_number': 1, 'duration_ms': 214147, 'popularity': 71, 'danceability': 0.681, 'energy': 0.715, 'loudness': -6.318, 'speechiness': 0.0388, 'acousticness': 0.078, 'instrumentalness': 0, 'liveness': 0.275, 'valence': 0.587, 'tempo': 127.429}, '1oxOiOjsi7plNOZEhoPLPj': {'name': 'Good Grief', 'artist_id': '7EQ0qTo7fWT7DPxmxtSYEc', 'artist_name': 'Bastille', 'album_name': 'Wild World (Complete Edition)', 'track_number': 1, 'duration_ms': 206493, 'popularity': 64, 'danceability': 0.727, 'energy': 0.768, 'loudness': -4.849, 'speechiness': 0.068, 'acousticness': 0.18, 'instrumentalness': 0, 'liveness': 0.204, 'valence': 0.885, 'tempo': 120.047}, '4Wg7VfvO7NVG57R8cSPDQG': {'name': 'Send Them Off!', 'artist_id': '7EQ0qTo7fWT7DPxmxtSYEc', 'artist_name': 'Bastille', 'album_name': 'Wild World (Complete Edition)', 'track_number': 8, 'duration_ms': 200987, 'popularity': 61, 'danceability': 0.605, 'energy': 0.811, 'loudness': -3.508, 'speechiness': 0.0594, 'acousticness': 0.121, 'instrumentalness': 0, 'liveness': 0.253, 'valence': 0.413, 'tempo': 100.001}, '6ZeQp2XTOiPCePWRfCHSo5': {'name': 'Oblivion', 'artist_id': '7EQ0qTo7fWT7DPxmxtSYEc', 'artist_name': 'Bastille', 'album_name': 'Bad Blood', 'track_number': 8, 'duration_ms': 196346, 'popularity': 63, 'danceability': 0.419, 'energy': 0.331, 'loudness': -9.013, 'speechiness': 0.03, 'acousticness': 0.723, 'instrumentalness': 1.41e-06, 'liveness': 0.426, 'valence': 0.216, 'tempo': 78.501}, '7BNDyzwDboNRR2wmd7GSew': {'name': 'Of The Night', 'artist_id': '7EQ0qTo7fWT7DPxmxtSYEc', 'artist_name': 'Bastille', 'album_name': 'All This Bad Blood', 'track_number': 9, 'duration_ms': 214205, 'popularity': 59, 'danceability': 0.668, 'energy': 0.826, 'loudness': -7.18, 'speechiness': 0.0398, 'acousticness': 0.0209, 'instrumentalness': 0.000249, 'liveness': 0.0886, 'valence': 0.36, 'tempo': 125.007}, '7yrx5A6zDOsd7Bn02WvbLH': {'name': 'Blame', 'artist_id': '7EQ0qTo7fWT7DPxmxtSYEc', 'artist_name': 'Bastille', 'album_name': 'Wild World (Complete Edition)', 'track_number': 11, 'duration_ms': 175880, 'popularity': 62, 'danceability': 0.37, 'energy': 0.771, 'loudness': -3.988, 'speechiness': 0.0447, 'acousticness': 0.000865, 'instrumentalness': 0, 'liveness': 0.287, 'valence': 0.336, 'tempo': 169.995}, '5dSFlPDHjAuYU1apyrRgqV': {'name': 'Good Grief - Don Diablo Remix', 'artist_id': '7EQ0qTo7fWT7DPxmxtSYEc', 'artist_name': 'Bastille', 'album_name': 'Good Grief (Don Diablo Remix)', 'track_number': 1, 'duration_ms': 239000, 'popularity': 58, 'danceability': 0.747, 'energy': 0.793, 'loudness': -3.482, 'speechiness': 0.0956, 'acousticness': 0.0207, 'instrumentalness': 0, 'liveness': 0.121, 'valence': 0.731, 'tempo': 125.986}, '2oTdiDj4AawNeeYFz8bipG': {'name': 'Things We Lost In The Fire', 'artist_id': '7EQ0qTo7fWT7DPxmxtSYEc', 'artist_name': 'Bastille', 'album_name': 'Bad Blood', 'track_number': 2, 'duration_ms': 240746, 'popularity': 55, 'danceability': 0.587, 'energy': 0.916, 'loudness': -4.879, 'speechiness': 0.0605, 'acousticness': 0.063, 'instrumentalness': 0, 'liveness': 0.25, 'valence': 0.646, 'tempo': 134.029}, '6ezPXXacQCCz2wIzg4sEAj': {'name': 'Four Walls (The Ballad Of Perry Smith)', 'artist_id': '7EQ0qTo7fWT7DPxmxtSYEc', 'artist_name': 'Bastille', 'album_name': 'Wild World (Complete Edition)', 'track_number': 10, 'duration_ms': 252146, 'popularity': 54, 'danceability': 0.704, 'energy': 0.565, 'loudness': -5.314, 'speechiness': 0.0459, 'acousticness': 0.616, 'instrumentalness': 0, 'liveness': 0.0551, 'valence': 0.367, 'tempo': 120.006}, '67wABU4SjBlnDHB0KiU3HL': {'name': 'Flaws', 'artist_id': '7EQ0qTo7fWT7DPxmxtSYEc', 'artist_name': 'Bastille', 'album_name': 'Bad Blood', 'track_number': 9, 'duration_ms': 218800, 'popularity': 58, 'danceability': 0.573, 'energy': 0.653, 'loudness': -6.985, 'speechiness': 0.0371, 'acousticness': 0.398, 'instrumentalness': 0, 'liveness': 0.0751, 'valence': 0.433, 'tempo': 144.187}, '099TPpEaCSjEwysWZeTZv1': {'name': 'You Know Me', 'artist_id': '2Oboq4Pq88TcC9eUn2HSW9', 'artist_name': 'Air Traffic Controller', 'album_name': 'NORDO', 'track_number': 3, 'duration_ms': 240680, 'popularity': 49, 'danceability': 0.519, 'energy': 0.861, 'loudness': -6.413, 'speechiness': 0.0404, 'acousticness': 0.000665, 'instrumentalness': 1.21e-06, 'liveness': 0.134, 'valence': 0.833, 'tempo': 138.048}, '0sF4M6WIH6yqzR8ijc8nON': {'name': 'People Watching', 'artist_id': '2Oboq4Pq88TcC9eUn2HSW9', 'artist_name': 'Air Traffic Controller', 'album_name': 'Black Box', 'track_number': 1, 'duration_ms': 243093, 'popularity': 40, 'danceability': 0.557, 'energy': 0.945, 'loudness': -6.374, 'speechiness': 0.115, 'acousticness': 0.31, 'instrumentalness': 0, 'liveness': 0.0745, 'valence': 0.327, 'tempo': 140.017}, '5uyRkr9cH64kAGh632Sj1T': {'name': 'Hurry, Hurry', 'artist_id': '2Oboq4Pq88TcC9eUn2HSW9', 'artist_name': 'Air Traffic Controller', 'album_name': 'Nordo', 'track_number': 1, 'duration_ms': 203266, 'popularity': 40, 'danceability': 0.612, 'energy': 0.913, 'loudness': -4.668, 'speechiness': 0.0492, 'acousticness': 0.0015, 'instrumentalness': 0, 'liveness': 0.117, 'valence': 0.806, 'tempo': 120.001}, '0iXuj965YYNsSAaRaWpBRI': {'name': 'The House', 'artist_id': '2Oboq4Pq88TcC9eUn2HSW9', 'artist_name': 'Air Traffic Controller', 'album_name': 'Black Box', 'track_number': 4, 'duration_ms': 205000, 'popularity': 35, 'danceability': 0.457, 'energy': 0.846, 'loudness': -4.678, 'speechiness': 0.0569, 'acousticness': 0.0663, 'instrumentalness': 0, 'liveness': 0.733, 'valence': 0.82, 'tempo': 169.041}, '0HsmznKa8h9AlqOrsBNkh4': {'name': 'What You Do to My Soul (Ronson Remix)', 'artist_id': '2Oboq4Pq88TcC9eUn2HSW9', 'artist_name': 'Air Traffic Controller', 'album_name': 'Black Box', 'track_number': 13, 'duration_ms': 193440, 'popularity': 34, 'danceability': 0.506, 'energy': 0.868, 'loudness': -4.03, 'speechiness': 0.149, 'acousticness': 0.00254, 'instrumentalness': 0, 'liveness': 0.371, 'valence': 0.727, 'tempo': 124.073}, '79uuGIdXuzA5yeSx6vNzij': {'name': 'Pick Me Up', 'artist_id': '2Oboq4Pq88TcC9eUn2HSW9', 'artist_name': 'Air Traffic Controller', 'album_name': 'Nordo', 'track_number': 4, 'duration_ms': 244640, 'popularity': 33, 'danceability': 0.425, 'energy': 0.839, 'loudness': -5.577, 'speechiness': 0.0663, 'acousticness': 0.000677, 'instrumentalness': 0.000102, 'liveness': 0.301, 'valence': 0.508, 'tempo': 214.052}, '6bRu0aqwBqwoSRZpGaIL8C': {'name': 'On the Wire', 'artist_id': '2Oboq4Pq88TcC9eUn2HSW9', 'artist_name': 'Air Traffic Controller', 'album_name': 'Black Box', 'track_number': 10, 'duration_ms': 230760, 'popularity': 24, 'danceability': 0.223, 'energy': 0.772, 'loudness': -6.095, 'speechiness': 0.0981, 'acousticness': 0.0382, 'instrumentalness': 0.0869, 'liveness': 0.105, 'valence': 0.304, 'tempo': 118.779}, '09qyIW5B7MuNUxQnDIZfVG': {'name': 'What You Do to My Soul', 'artist_id': '2Oboq4Pq88TcC9eUn2HSW9', 'artist_name': 'Air Traffic Controller', 'album_name': 'Black Box', 'track_number': 5, 'duration_ms': 193853, 'popularity': 30, 'danceability': 0.519, 'energy': 0.86, 'loudness': -4.41, 'speechiness': 0.0895, 'acousticness': 0.0155, 'instrumentalness': 0.000115, 'liveness': 0.367, 'valence': 0.706, 'tempo': 124.084}, '0xHTTy2xujEwvjT3fqHN5t': {'name': 'Test 1, 2', 'artist_id': '2Oboq4Pq88TcC9eUn2HSW9', 'artist_name': 'Air Traffic Controller', 'album_name': 'The One', 'track_number': 12, 'duration_ms': 253506, 'popularity': 27, 'danceability': 0.618, 'energy': 0.452, 'loudness': -9.602, 'speechiness': 0.0448, 'acousticness': 0.455, 'instrumentalness': 2.66e-06, 'liveness': 0.222, 'valence': 0.521, 'tempo': 150.063}, '3gvAGvbMCRvVDDp8ZaIPV5': {'name': 'Lost in My Mind', 'artist_id': '0n94vC3S9c3mb2HyNAOcjg', 'artist_name': 'The Head and the Heart', 'album_name': 'The Head and the Heart', 'track_number': 7, 'duration_ms': 259120, 'popularity': 70, 'danceability': 0.375, 'energy': 0.546, 'loudness': -8.16, 'speechiness': 0.0294, 'acousticness': 0.451, 'instrumentalness': 0.000312, 'liveness': 0.278, 'valence': 0.361, 'tempo': 95.361}, '4Q6Kuze3wNMQRjamyBjHUR': {'name': 'Rivers and Roads', 'artist_id': '0n94vC3S9c3mb2HyNAOcjg', 'artist_name': 'The Head and the Heart', 'album_name': 'The Head and the Heart', 'track_number': 5, 'duration_ms': 284000, 'popularity': 69, 'danceability': 0.494, 'energy': 0.194, 'loudness': -8.965, 'speechiness': 0.0352, 'acousticness': 0.699, 'instrumentalness': 2.98e-05, 'liveness': 0.0803, 'valence': 0.154, 'tempo': 135.753}, '5Gtn8HgCAo0TUiaKKgP6us': {'name': 'Down in the Valley', 'artist_id': '0n94vC3S9c3mb2HyNAOcjg', 'artist_name': 'The Head and the Heart', 'album_name': 'The Head and the Heart', 'track_number': 4, 'duration_ms': 303653, 'popularity': 66, 'danceability': 0.418, 'energy': 0.403, 'loudness': -10.53, 'speechiness': 0.0294, 'acousticness': 0.555, 'instrumentalness': 0.024, 'liveness': 0.108, 'valence': 0.142, 'tempo': 105.801}, '5bAJhDTVCWVScr5Ev4LnB2': {'name': 'Rhythm & Blues', 'artist_id': '0n94vC3S9c3mb2HyNAOcjg', 'artist_name': 'The Head and the Heart', 'album_name': 'Signs of Light', 'track_number': 3, 'duration_ms': 240253, 'popularity': 65, 'danceability': 0.433, 'energy': 0.863, 'loudness': -4.452, 'speechiness': 0.0296, 'acousticness': 0.00148, 'instrumentalness': 0.00107, 'liveness': 0.351, 'valence': 0.537, 'tempo': 82.998}, '5m1L3o7fOfLFyw6VwumROL': {'name': 'Shake', 'artist_id': '0n94vC3S9c3mb2HyNAOcjg', 'artist_name': 'The Head and the Heart', 'album_name': "Let's Be Still", 'track_number': 6, 'duration_ms': 241706, 'popularity': 63, 'danceability': 0.48, 'energy': 0.79, 'loudness': -7.775, 'speechiness': 0.0353, 'acousticness': 0.472, 'instrumentalness': 0.713, 'liveness': 0.155, 'valence': 0.434, 'tempo': 111.025}, '4HjEsfSpWo8gvZMr9SA3a1': {'name': 'Library Magic', 'artist_id': '0n94vC3S9c3mb2HyNAOcjg', 'artist_name': 'The Head and the Heart', 'album_name': 'Signs of Light', 'track_number': 6, 'duration_ms': 193786, 'popularity': 62, 'danceability': 0.425, 'energy': 0.616, 'loudness': -7.585, 'speechiness': 0.0381, 'acousticness': 0.248, 'instrumentalness': 0, 'liveness': 0.0978, 'valence': 0.522, 'tempo': 89.705}, '1JxNWpK9xTWKRPoYTIX4Qk': {'name': 'Another Story', 'artist_id': '0n94vC3S9c3mb2HyNAOcjg', 'artist_name': 'The Head and the Heart', 'album_name': "Let's Be Still", 'track_number': 2, 'duration_ms': 274200, 'popularity': 61, 'danceability': 0.352, 'energy': 0.45, 'loudness': -9.881, 'speechiness': 0.0293, 'acousticness': 0.546, 'instrumentalness': 0.127, 'liveness': 0.283, 'valence': 0.111, 'tempo': 86.937}, '0PHm9MrfZdEUasfd1XC0n2': {'name': 'All We Ever Knew - Recorded at Spotify Studios NYC', 'artist_id': '0n94vC3S9c3mb2HyNAOcjg', 'artist_name': 'The Head and the Heart', 'album_name': 'Spotify Singles', 'track_number': 1, 'duration_ms': 228586, 'popularity': 57, 'danceability': 0.46, 'energy': 0.825, 'loudness': -5.203, 'speechiness': 0.031, 'acousticness': 0.0695, 'instrumentalness': 1.52e-05, 'liveness': 0.337, 'valence': 0.451, 'tempo': 100.137}, '01NSrsQkOZ3PgRcGLGrOT5': {'name': 'Winter Song', 'artist_id': '0n94vC3S9c3mb2HyNAOcjg', 'artist_name': 'The Head and the Heart', 'album_name': 'The Head and the Heart', 'track_number': 8, 'duration_ms': 163973, 'popularity': 56, 'danceability': 0.54, 'energy': 0.253, 'loudness': -14.274, 'speechiness': 0.032, 'acousticness': 0.837, 'instrumentalness': 0.00139, 'liveness': 0.117, 'valence': 0.308, 'tempo': 171.949}, '6ZFbXIJkuI1dVNWvzJzown': {'name': 'Time', 'artist_id': '0YC192cP3KPCRWx8zr8MfZ', 'artist_name': 'Hans Zimmer', 'album_name': 'Inception (Music From The Motion Picture)', 'track_number': 12, 'duration_ms': 275546, 'popularity': 71, 'danceability': 0.221, 'energy': 0.0879, 'loudness': -16.996, 'speechiness': 0.0381, 'acousticness': 0.155, 'instrumentalness': 0.698, 'liveness': 0.0869, 'valence': 0.0396, 'tempo': 126.622}, '18z7tK7u9DcDw85LYRR5Fe': {'name': 'Cornfield Chase', 'artist_id': '0YC192cP3KPCRWx8zr8MfZ', 'artist_name': 'Hans Zimmer', 'album_name': 'Interstellar: Original Motion Picture Soundtrack', 'track_number': 2, 'duration_ms': 126959, 'popularity': 66, 'danceability': 0.33, 'energy': 0.229, 'loudness': -16.442, 'speechiness': 0.0375, 'acousticness': 0.948, 'instrumentalness': 0.973, 'liveness': 0.0998, 'valence': 0.062, 'tempo': 96.158}, '2H4zwjbv0D0ggDhf0E8j8j': {'name': 'Day One', 'artist_id': '0YC192cP3KPCRWx8zr8MfZ', 'artist_name': 'Hans Zimmer', 'album_name': 'Interstellar: Original Motion Picture Soundtrack', 'track_number': 4, 'duration_ms': 199422, 'popularity': 66, 'danceability': 0.132, 'energy': 0.0176, 'loudness': -27.762, 'speechiness': 0.0362, 'acousticness': 0.927, 'instrumentalness': 0.964, 'liveness': 0.0729, 'valence': 0.0639, 'tempo': 95.979}, '1elGwF4VwkwglV4nCBPJtv': {'name': 'Now We Are Free', 'artist_id': '3C4MmUJYQN9svNdedAR2BK', 'artist_name': 'Lisa Gerrard', 'album_name': 'Gladiator - Music From The Motion Picture', 'track_number': 17, 'duration_ms': 254293, 'popularity': 58, 'danceability': 0.311, 'energy': 0.234, 'loudness': -18.374, 'speechiness': 0.0349, 'acousticness': 0.634, 'instrumentalness': 0.0484, 'liveness': 0.104, 'valence': 0.039, 'tempo': 138.272}, '6WVRhBxRMW9fn6sRkt2gWn': {'name': 'Mountains', 'artist_id': '0YC192cP3KPCRWx8zr8MfZ', 'artist_name': 'Hans Zimmer', 'album_name': 'Interstellar: Original Motion Picture Soundtrack', 'track_number': 8, 'duration_ms': 219092, 'popularity': 62, 'danceability': 0.251, 'energy': 0.0575, 'loudness': -16.985, 'speechiness': 0.0293, 'acousticness': 0.605, 'instrumentalness': 0.922, 'liveness': 0.098, 'valence': 0.0374, 'tempo': 95.947}, '5xKVYMxOHB2XRLCUafFrz6': {'name': 'Dream Is Collapsing', 'artist_id': '0YC192cP3KPCRWx8zr8MfZ', 'artist_name': 'Hans Zimmer', 'album_name': 'Inception (Music From The Motion Picture)', 'track_number': 3, 'duration_ms': 143800, 'popularity': 61, 'danceability': 0.518, 'energy': 0.434, 'loudness': -12.232, 'speechiness': 0.0314, 'acousticness': 0.0708, 'instrumentalness': 0.748, 'liveness': 0.421, 'valence': 0.104, 'tempo': 126.02}, '1olO0IZxJUM6COX6i57RGe': {'name': 'S.T.A.Y.', 'artist_id': '0YC192cP3KPCRWx8zr8MfZ', 'artist_name': 'Hans Zimmer', 'album_name': 'Interstellar: Original Motion Picture Soundtrack', 'track_number': 15, 'duration_ms': 383513, 'popularity': 59, 'danceability': 0.12, 'energy': 0.0306, 'loudness': -30.798, 'speechiness': 0.0468, 'acousticness': 0.932, 'instrumentalness': 0.942, 'liveness': 0.073, 'valence': 0.0249, 'tempo': 191.841}, '1uyB4BHbIicheenh3BgeQ3': {'name': 'Dust', 'artist_id': '0YC192cP3KPCRWx8zr8MfZ', 'artist_name': 'Hans Zimmer', 'album_name': 'Interstellar: Original Motion Picture Soundtrack', 'track_number': 3, 'duration_ms': 341395, 'popularity': 57, 'danceability': 0.167, 'energy': 0.122, 'loudness': -23.045, 'speechiness': 0.0456, 'acousticness': 0.964, 'instrumentalness': 0.655, 'liveness': 0.102, 'valence': 0.0297, 'tempo': 129.618}, '1PyEOnj3tdaHAcDcsqTYbv': {'name': 'Stay', 'artist_id': '0YC192cP3KPCRWx8zr8MfZ', 'artist_name': 'Hans Zimmer', 'album_name': 'Interstellar: Original Motion Picture Soundtrack', 'track_number': 5, 'duration_ms': 412424, 'popularity': 57, 'danceability': 0.149, 'energy': 0.0482, 'loudness': -15.953, 'speechiness': 0.0474, 'acousticness': 0.00619, 'instrumentalness': 0.904, 'liveness': 0.124, 'valence': 0.0223, 'tempo': 105.333}, '1TBJRUEWgRCKvcaVtojDad': {'name': "Where We're Going", 'artist_id': '0YC192cP3KPCRWx8zr8MfZ', 'artist_name': 'Hans Zimmer', 'album_name': 'Interstellar: Original Motion Picture Soundtrack', 'track_number': 16, 'duration_ms': 461268, 'popularity': 56, 'danceability': 0.119, 'energy': 0.0231, 'loudness': -23.521, 'speechiness': 0.0483, 'acousticness': 0.866, 'instrumentalness': 0.944, 'liveness': 0.371, 'valence': 0.0269, 'tempo': 96.052}, '4o0NjemqhmsYLIMwlcosvW': {'name': 'The Funeral', 'artist_id': '0OdUWJ0sBjDrqHygGUXeCF', 'artist_name': 'Band of Horses', 'album_name': 'Everything All The Time', 'track_number': 4, 'duration_ms': 321146, 'popularity': 73, 'danceability': 0.316, 'energy': 0.769, 'loudness': -5.283, 'speechiness': 0.0422, 'acousticness': 0.0142, 'instrumentalness': 0, 'liveness': 0.0928, 'valence': 0.112, 'tempo': 122.507}, '5MYfpFJYm8WNFGssR6H2Oz': {'name': "No One's Gonna Love You - Live from Spotify Sweden", 'artist_id': '0OdUWJ0sBjDrqHygGUXeCF', 'artist_name': 'Band of Horses', 'album_name': 'Spotify Sessions', 'track_number': 5, 'duration_ms': 239080, 'popularity': 67, 'danceability': 0.547, 'energy': 0.188, 'loudness': -10.676, 'speechiness': 0.036, 'acousticness': 0.929, 'instrumentalness': 1.2e-06, 'liveness': 0.714, 'valence': 0.194, 'tempo': 135.657}, '3LeNQIGi0zwmQm8WShZB95': {'name': "No One's Gonna Love You", 'artist_id': '0OdUWJ0sBjDrqHygGUXeCF', 'artist_name': 'Band of Horses', 'album_name': 'Cease To Begin', 'track_number': 3, 'duration_ms': 217333, 'popularity': 63, 'danceability': 0.313, 'energy': 0.894, 'loudness': -3.579, 'speechiness': 0.0294, 'acousticness': 0.121, 'instrumentalness': 0, 'liveness': 0.0925, 'valence': 0.372, 'tempo': 149.043}, '1jKvrkkZxtQ7ZDiXdITOis': {'name': 'The Funeral - Live Acoustic', 'artist_id': '0OdUWJ0sBjDrqHygGUXeCF', 'artist_name': 'Band of Horses', 'album_name': 'Acoustic at The Ryman (Live)', 'track_number': 9, 'duration_ms': 307760, 'popularity': 56, 'danceability': 0.457, 'energy': 0.321, 'loudness': -12.126, 'speechiness': 0.0309, 'acousticness': 0.949, 'instrumentalness': 0.000815, 'liveness': 0.905, 'valence': 0.103, 'tempo': 128.008}, '5qWgGPylB0Al9IVq2HKTHE': {'name': 'Is There A Ghost', 'artist_id': '0OdUWJ0sBjDrqHygGUXeCF', 'artist_name': 'Band of Horses', 'album_name': 'Cease To Begin', 'track_number': 1, 'duration_ms': 179666, 'popularity': 55, 'danceability': 0.3, 'energy': 0.843, 'loudness': -3.841, 'speechiness': 0.0354, 'acousticness': 0.0049, 'instrumentalness': 4.86e-06, 'liveness': 0.079, 'valence': 0.127, 'tempo': 135.648}, '7sMcFdVYcwucGVtoV7r9lZ': {'name': 'Casual Party', 'artist_id': '0OdUWJ0sBjDrqHygGUXeCF', 'artist_name': 'Band of Horses', 'album_name': 'Why Are You OK', 'track_number': 4, 'duration_ms': 233573, 'popularity': 54, 'danceability': 0.48, 'energy': 0.795, 'loudness': -4.726, 'speechiness': 0.0354, 'acousticness': 9.16e-05, 'instrumentalness': 2.14e-05, 'liveness': 0.316, 'valence': 0.508, 'tempo': 130.068}, '3MNTXYdBLLeBJjbihvTjOJ': {'name': 'The General Specific', 'artist_id': '0OdUWJ0sBjDrqHygGUXeCF', 'artist_name': 'Band of Horses', 'album_name': 'Cease To Begin', 'track_number': 5, 'duration_ms': 187053, 'popularity': 52, 'danceability': 0.752, 'energy': 0.695, 'loudness': -5.776, 'speechiness': 0.0279, 'acousticness': 0.204, 'instrumentalness': 0.00484, 'liveness': 0.146, 'valence': 0.616, 'tempo': 118.144}, '3wNti9PJJPrP9nF2ccsQvw': {'name': 'Factory', 'artist_id': '0OdUWJ0sBjDrqHygGUXeCF', 'artist_name': 'Band of Horses', 'album_name': 'Infinite Arms', 'track_number': 1, 'duration_ms': 275360, 'popularity': 50, 'danceability': 0.314, 'energy': 0.59, 'loudness': -5.865, 'speechiness': 0.0334, 'acousticness': 0.03, 'instrumentalness': 0.00408, 'liveness': 0.16, 'valence': 0.131, 'tempo': 121.186}, '1Z94DVkRor1ZzFPICesOUt': {'name': 'Evening Kitchen', 'artist_id': '0OdUWJ0sBjDrqHygGUXeCF', 'artist_name': 'Band of Horses', 'album_name': 'Infinite Arms', 'track_number': 8, 'duration_ms': 236933, 'popularity': 50, 'danceability': 0.335, 'energy': 0.15, 'loudness': -12.53, 'speechiness': 0.0318, 'acousticness': 0.97, 'instrumentalness': 0.000665, 'liveness': 0.111, 'valence': 0.153, 'tempo': 183.347}, '6DVX4qug0tCQkdlcRT7nUf': {'name': 'In A Drawer', 'artist_id': '0OdUWJ0sBjDrqHygGUXeCF', 'artist_name': 'Band of Horses', 'album_name': 'Why Are You OK', 'track_number': 5, 'duration_ms': 238906, 'popularity': 50, 'danceability': 0.575, 'energy': 0.703, 'loudness': -6.782, 'speechiness': 0.0381, 'acousticness': 0.141, 'instrumentalness': 0.00195, 'liveness': 0.161, 'valence': 0.299, 'tempo': 140.054}, '5nQCeXUXtTFobB8LnOCslX': {'name': 'Light Me Up', 'artist_id': '2ic4xySjQ39N7DJ0HZemeG', 'artist_name': 'Bronze Radio Return', 'album_name': 'Light Me Up', 'track_number': 1, 'duration_ms': 197493, 'popularity': 43, 'danceability': 0.506, 'energy': 0.94, 'loudness': -5.288, 'speechiness': 0.0428, 'acousticness': 0.00148, 'instrumentalness': 0.023, 'liveness': 0.0945, 'valence': 0.626, 'tempo': 171.045}, '2GNFDAYqOl9uJEOTqYDISb': {'name': 'Further On', 'artist_id': '2ic4xySjQ39N7DJ0HZemeG', 'artist_name': 'Bronze Radio Return', 'album_name': 'Up, On & Over', 'track_number': 3, 'duration_ms': 146780, 'popularity': 41, 'danceability': 0.633, 'energy': 0.811, 'loudness': -6.661, 'speechiness': 0.0327, 'acousticness': 0.112, 'instrumentalness': 0.0144, 'liveness': 0.12, 'valence': 0.921, 'tempo': 130.157}, '60SV7HSk7dwgIDvVCi7Ru0': {'name': "Where I'm Coming From", 'artist_id': '2ic4xySjQ39N7DJ0HZemeG', 'artist_name': 'Bronze Radio Return', 'album_name': 'Live from Brooklyn and Then Some', 'track_number': 7, 'duration_ms': 220787, 'popularity': 45, 'danceability': 0.652, 'energy': 0.522, 'loudness': -9.388, 'speechiness': 0.0278, 'acousticness': 0.798, 'instrumentalness': 0.00785, 'liveness': 0.195, 'valence': 0.288, 'tempo': 132.134}, '0VrHcZMvnE3AslLG7lvmJX': {'name': 'Up, On & Over', 'artist_id': '2ic4xySjQ39N7DJ0HZemeG', 'artist_name': 'Bronze Radio Return', 'album_name': 'Up, On & Over', 'track_number': 1, 'duration_ms': 173374, 'popularity': 43, 'danceability': 0.594, 'energy': 0.731, 'loudness': -6.472, 'speechiness': 0.0294, 'acousticness': 0.051, 'instrumentalness': 0.000263, 'liveness': 0.0973, 'valence': 0.405, 'tempo': 125.042}, '1exs6EE3ll55TUNkX3PZAA': {'name': 'Good Company', 'artist_id': '2ic4xySjQ39N7DJ0HZemeG', 'artist_name': 'Bronze Radio Return', 'album_name': 'Light Me Up', 'track_number': 10, 'duration_ms': 226480, 'popularity': 42, 'danceability': 0.538, 'energy': 0.577, 'loudness': -5.428, 'speechiness': 0.0278, 'acousticness': 0.205, 'instrumentalness': 0.00168, 'liveness': 0.191, 'valence': 0.454, 'tempo': 76.98}, '1nDjwLTeKD9f2jt22841U6': {'name': 'Worth Wondering', 'artist_id': '2ic4xySjQ39N7DJ0HZemeG', 'artist_name': 'Bronze Radio Return', 'album_name': 'Old Time Speaker', 'track_number': 7, 'duration_ms': 172773, 'popularity': 41, 'danceability': 0.685, 'energy': 0.511, 'loudness': -12.545, 'speechiness': 0.0284, 'acousticness': 0.61, 'instrumentalness': 0, 'liveness': 0.126, 'valence': 0.302, 'tempo': 105.974}, '5cJfRpdcXzoVEqYEaAseUZ': {'name': 'Before I Get There', 'artist_id': '2ic4xySjQ39N7DJ0HZemeG', 'artist_name': 'Bronze Radio Return', 'album_name': 'Light Me Up', 'track_number': 9, 'duration_ms': 207586, 'popularity': 41, 'danceability': 0.602, 'energy': 0.903, 'loudness': -3.909, 'speechiness': 0.0314, 'acousticness': 0.0214, 'instrumentalness': 0.00623, 'liveness': 0.181, 'valence': 0.496, 'tempo': 106.027}, '1tnUlsPH9pTJKvBZ6TXI69': {'name': 'Melting in My Icebox', 'artist_id': '2ic4xySjQ39N7DJ0HZemeG', 'artist_name': 'Bronze Radio Return', 'album_name': 'Up, On & Over', 'track_number': 5, 'duration_ms': 186118, 'popularity': 39, 'danceability': 0.589, 'energy': 0.864, 'loudness': -5.58, 'speechiness': 0.0271, 'acousticness': 0.00477, 'instrumentalness': 6.25e-05, 'liveness': 0.0815, 'valence': 0.635, 'tempo': 110.009}, '0EjUR5qLuMMilc7bFbrzaa': {'name': 'Say Hello Sometime', 'artist_id': '2ic4xySjQ39N7DJ0HZemeG', 'artist_name': 'Bronze Radio Return', 'album_name': 'Light Me Up', 'track_number': 8, 'duration_ms': 214813, 'popularity': 38, 'danceability': 0.643, 'energy': 0.839, 'loudness': -4.413, 'speechiness': 0.037, 'acousticness': 0.104, 'instrumentalness': 7.03e-06, 'liveness': 0.646, 'valence': 0.758, 'tempo': 109.969}, '2kW59AS9OrpFsuXbi2939R': {'name': 'Forest Whitaker', 'artist_id': '0e9H8oaYYRCKFXOVv848nt', 'artist_name': 'Bad Books', 'album_name': 'II', 'track_number': 3, 'duration_ms': 220600, 'popularity': 48, 'danceability': 0.716, 'energy': 0.726, 'loudness': -5.517, 'speechiness': 0.0406, 'acousticness': 0.352, 'instrumentalness': 4.89e-05, 'liveness': 0.163, 'valence': 0.916, 'tempo': 113.985}, '61hvSzyzdXo4e2rAWmAoV0': {'name': 'Pyotr', 'artist_id': '0e9H8oaYYRCKFXOVv848nt', 'artist_name': 'Bad Books', 'album_name': 'II', 'track_number': 5, 'duration_ms': 222786, 'popularity': 41, 'danceability': 0.495, 'energy': 0.235, 'loudness': -9.638, 'speechiness': 0.0408, 'acousticness': 0.963, 'instrumentalness': 0.000177, 'liveness': 0.104, 'valence': 0.203, 'tempo': 138.375}, '0YJBawdB7HwXmTg4wwWFpu': {'name': 'The After Party', 'artist_id': '0e9H8oaYYRCKFXOVv848nt', 'artist_name': 'Bad Books', 'album_name': 'II', 'track_number': 1, 'duration_ms': 213333, 'popularity': 39, 'danceability': 0.602, 'energy': 0.474, 'loudness': -6.928, 'speechiness': 0.0287, 'acousticness': 0.0359, 'instrumentalness': 0.0106, 'liveness': 0.202, 'valence': 0.0936, 'tempo': 137.044}, '0InFsFgdpCJuDSERgsM2hJ': {'name': 'It Never Stops', 'artist_id': '0e9H8oaYYRCKFXOVv848nt', 'artist_name': 'Bad Books', 'album_name': 'II', 'track_number': 4, 'duration_ms': 200040, 'popularity': 37, 'danceability': 0.59, 'energy': 0.68, 'loudness': -6.079, 'speechiness': 0.0591, 'acousticness': 0.0924, 'instrumentalness': 0, 'liveness': 0.0945, 'valence': 0.152, 'tempo': 150.067}, '4cbHCYCabWrNz25xzH2p8w': {'name': '42', 'artist_id': '0e9H8oaYYRCKFXOVv848nt', 'artist_name': 'Bad Books', 'album_name': 'II', 'track_number': 9, 'duration_ms': 144013, 'popularity': 33, 'danceability': 0.421, 'energy': 0.0992, 'loudness': -13.839, 'speechiness': 0.0448, 'acousticness': 0.851, 'instrumentalness': 1.43e-06, 'liveness': 0.0946, 'valence': 0.3, 'tempo': 77.315}, '5pbXxljyrIYP4xIrRksjE6': {'name': 'Friendly Advice', 'artist_id': '0e9H8oaYYRCKFXOVv848nt', 'artist_name': 'Bad Books', 'album_name': 'II', 'track_number': 6, 'duration_ms': 227493, 'popularity': 31, 'danceability': 0.686, 'energy': 0.638, 'loudness': -6.759, 'speechiness': 0.0294, 'acousticness': 0.0848, 'instrumentalness': 0.0287, 'liveness': 0.0992, 'valence': 0.367, 'tempo': 123.961}, '3rOcOcUJ2O9z5xEtse9d2F': {'name': 'Petite Mort', 'artist_id': '0e9H8oaYYRCKFXOVv848nt', 'artist_name': 'Bad Books', 'album_name': 'II', 'track_number': 8, 'duration_ms': 203000, 'popularity': 30, 'danceability': 0.528, 'energy': 0.665, 'loudness': -7.516, 'speechiness': 0.0329, 'acousticness': 0.466, 'instrumentalness': 0.000374, 'liveness': 0.165, 'valence': 0.546, 'tempo': 107.982}, '1DoxXO4w8FIu87Zztboz14': {'name': 'Lost Creek', 'artist_id': '0e9H8oaYYRCKFXOVv848nt', 'artist_name': 'Bad Books', 'album_name': 'II', 'track_number': 10, 'duration_ms': 283960, 'popularity': 29, 'danceability': 0.595, 'energy': 0.335, 'loudness': -9.988, 'speechiness': 0.0308, 'acousticness': 0.741, 'instrumentalness': 0.000328, 'liveness': 0.128, 'valence': 0.122, 'tempo': 125.873}, '0i1ypxjLSoirkgDTAWLAKa': {'name': 'Ambivalent Peaks', 'artist_id': '0e9H8oaYYRCKFXOVv848nt', 'artist_name': 'Bad Books', 'album_name': 'II', 'track_number': 11, 'duration_ms': 310373, 'popularity': 29, 'danceability': 0.533, 'energy': 0.067, 'loudness': -15.928, 'speechiness': 0.0387, 'acousticness': 0.907, 'instrumentalness': 0.000129, 'liveness': 0.107, 'valence': 0.173, 'tempo': 102.625}, '33d6D40n1ts4qmy5gBFbet': {'name': 'No Reward', 'artist_id': '0e9H8oaYYRCKFXOVv848nt', 'artist_name': 'Bad Books', 'album_name': 'II', 'track_number': 2, 'duration_ms': 202480, 'popularity': 28, 'danceability': 0.436, 'energy': 0.79, 'loudness': -4.537, 'speechiness': 0.0306, 'acousticness': 0.00782, 'instrumentalness': 0, 'liveness': 0.177, 'valence': 0.483, 'tempo': 104.041}, '11TK5KLtLZUdKr1C549bAw': {'name': 'What Would I Do Without You', 'artist_id': '4RwbDag6jWIYJnEGH6Wte9', 'artist_name': 'Drew Holcomb & The Neighbors', 'album_name': 'Good Light', 'track_number': 9, 'duration_ms': 172213, 'popularity': 58, 'danceability': 0.602, 'energy': 0.336, 'loudness': -11.106, 'speechiness': 0.0369, 'acousticness': 0.883, 'instrumentalness': 0.0017, 'liveness': 0.143, 'valence': 0.34, 'tempo': 90.894}, '7K36drJq6lInkW6Kkojucp': {'name': 'American Beauty', 'artist_id': '4RwbDag6jWIYJnEGH6Wte9', 'artist_name': 'Drew Holcomb & The Neighbors', 'album_name': 'Medicine', 'track_number': 1, 'duration_ms': 158013, 'popularity': 49, 'danceability': 0.645, 'energy': 0.169, 'loudness': -15.744, 'speechiness': 0.0317, 'acousticness': 0.844, 'instrumentalness': 0.00019, 'liveness': 0.109, 'valence': 0.174, 'tempo': 167.826}, '1idjvenidUlcO6e7rsqo9P': {'name': 'The Morning Song', 'artist_id': '4RwbDag6jWIYJnEGH6Wte9', 'artist_name': 'Drew Holcomb & The Neighbors', 'album_name': 'Souvenir', 'track_number': 1, 'duration_ms': 278355, 'popularity': 47, 'danceability': 0.598, 'energy': 0.461, 'loudness': -8.895, 'speechiness': 0.026, 'acousticness': 0.274, 'instrumentalness': 0.000651, 'liveness': 0.0899, 'valence': 0.414, 'tempo': 83.931}, '2f9h72MZuU0ZdEnGIfGf5H': {'name': 'Here We Go', 'artist_id': '4RwbDag6jWIYJnEGH6Wte9', 'artist_name': 'Drew Holcomb & The Neighbors', 'album_name': 'Medicine', 'track_number': 3, 'duration_ms': 202171, 'popularity': 45, 'danceability': 0.669, 'energy': 0.695, 'loudness': -9.389, 'speechiness': 0.0335, 'acousticness': 0.0643, 'instrumentalness': 0.02, 'liveness': 0.125, 'valence': 0.883, 'tempo': 151.957}, '1M4AnTxC8qImcRSIooLd7x': {'name': 'Live Forever', 'artist_id': '4RwbDag6jWIYJnEGH6Wte9', 'artist_name': 'Drew Holcomb & The Neighbors', 'album_name': 'Chasing Someday', 'track_number': 3, 'duration_ms': 273120, 'popularity': 26, 'danceability': 0.436, 'energy': 0.337, 'loudness': -7.958, 'speechiness': 0.0322, 'acousticness': 0.371, 'instrumentalness': 0, 'liveness': 0.104, 'valence': 0.0756, 'tempo': 122.99}, '3sWSJmerUoVLaB1w8g07e5': {'name': 'California', 'artist_id': '4RwbDag6jWIYJnEGH6Wte9', 'artist_name': 'Drew Holcomb & The Neighbors', 'album_name': 'Souvenir', 'track_number': 2, 'duration_ms': 170966, 'popularity': 43, 'danceability': 0.651, 'energy': 0.775, 'loudness': -7.497, 'speechiness': 0.0325, 'acousticness': 0.0165, 'instrumentalness': 9.38e-05, 'liveness': 0.301, 'valence': 0.964, 'tempo': 136.959}, '4yVdycF2kVA6ay8UvC1l4c': {'name': 'Black and Blue', 'artist_id': '4RwbDag6jWIYJnEGH6Wte9', 'artist_name': 'Drew Holcomb & The Neighbors', 'album_name': 'Souvenir', 'track_number': 8, 'duration_ms': 251793, 'popularity': 42, 'danceability': 0.575, 'energy': 0.533, 'loudness': -7.663, 'speechiness': 0.0277, 'acousticness': 0.0759, 'instrumentalness': 0.000811, 'liveness': 0.103, 'valence': 0.466, 'tempo': 174.146}, '19TXsT1N9vAoI4O2b92322': {'name': 'Fight for Love', 'artist_id': '4RwbDag6jWIYJnEGH6Wte9', 'artist_name': 'Drew Holcomb & The Neighbors', 'album_name': 'Souvenir', 'track_number': 3, 'duration_ms': 188215, 'popularity': 42, 'danceability': 0.61, 'energy': 0.768, 'loudness': -6.835, 'speechiness': 0.0274, 'acousticness': 0.0014, 'instrumentalness': 0.000912, 'liveness': 0.237, 'valence': 0.666, 'tempo': 109.069}, '0SkvSPb1uQH6OCQOFyA1Mz': {'name': "Mama's Sunshine, Daddy's Rain", 'artist_id': '4RwbDag6jWIYJnEGH6Wte9', 'artist_name': 'Drew Holcomb & The Neighbors', 'album_name': 'Souvenir', 'track_number': 7, 'duration_ms': 200937, 'popularity': 42, 'danceability': 0.674, 'energy': 0.62, 'loudness': -9.136, 'speechiness': 0.159, 'acousticness': 0.448, 'instrumentalness': 0, 'liveness': 0.0792, 'valence': 0.869, 'tempo': 176.923}, '2qURbsi4Mds6xJ8DWanSfX': {'name': 'New Year', 'artist_id': '4RwbDag6jWIYJnEGH6Wte9', 'artist_name': 'Drew Holcomb & The Neighbors', 'album_name': 'Souvenir', 'track_number': 5, 'duration_ms': 257965, 'popularity': 42, 'danceability': 0.771, 'energy': 0.574, 'loudness': -12.12, 'speechiness': 0.0529, 'acousticness': 0.419, 'instrumentalness': 0.336, 'liveness': 0.112, 'valence': 0.797, 'tempo': 143.743}, '5gHR34g8eZzmDWKYmVw0Ye': {'name': 'Back To You', 'artist_id': '6GwNGuDRNbx5XwoHQA3QiD', 'artist_name': 'Twin Forks', 'album_name': 'Twin Forks', 'track_number': 3, 'duration_ms': 170960, 'popularity': 52, 'danceability': 0.56, 'energy': 0.848, 'loudness': -5.529, 'speechiness': 0.0588, 'acousticness': 0.00502, 'instrumentalness': 0, 'liveness': 0.0778, 'valence': 0.419, 'tempo': 129.006}, '2wuFgUPBuzxYtNxsGxq5zj': {'name': "Kiss Me Darlin'", 'artist_id': '6GwNGuDRNbx5XwoHQA3QiD', 'artist_name': 'Twin Forks', 'album_name': 'Twin Forks', 'track_number': 4, 'duration_ms': 179786, 'popularity': 42, 'danceability': 0.541, 'energy': 0.723, 'loudness': -4.812, 'speechiness': 0.0327, 'acousticness': 0.481, 'instrumentalness': 0, 'liveness': 0.116, 'valence': 0.685, 'tempo': 79.959}, '0e1COboAmkFQPNUlpo8Pya': {'name': "Can't Be Broken", 'artist_id': '6GwNGuDRNbx5XwoHQA3QiD', 'artist_name': 'Twin Forks', 'album_name': 'Twin Forks', 'track_number': 1, 'duration_ms': 216666, 'popularity': 34, 'danceability': 0.592, 'energy': 0.587, 'loudness': -6.952, 'speechiness': 0.0356, 'acousticness': 0.111, 'instrumentalness': 0.000254, 'liveness': 0.0575, 'valence': 0.609, 'tempo': 123.478}, '3tY4oBJYB44wTHQjUkP3OZ': {'name': 'Something We Just Know', 'artist_id': '6GwNGuDRNbx5XwoHQA3QiD', 'artist_name': 'Twin Forks', 'album_name': 'Twin Forks', 'track_number': 6, 'duration_ms': 172453, 'popularity': 31, 'danceability': 0.353, 'energy': 0.758, 'loudness': -5.436, 'speechiness': 0.0374, 'acousticness': 0.219, 'instrumentalness': 0, 'liveness': 0.0989, 'valence': 0.563, 'tempo': 118.684}, '1JcGO7CIxm5X4pH2N56cEh': {'name': 'Scraping Up The Pieces', 'artist_id': '6GwNGuDRNbx5XwoHQA3QiD', 'artist_name': 'Twin Forks', 'album_name': 'Twin Forks', 'track_number': 5, 'duration_ms': 168920, 'popularity': 31, 'danceability': 0.557, 'energy': 0.878, 'loudness': -5.783, 'speechiness': 0.0782, 'acousticness': 0.0875, 'instrumentalness': 0, 'liveness': 0.0672, 'valence': 0.782, 'tempo': 132.936}, '46A0QpE6dz0LmwJPv4TekD': {'name': "Who's Looking Out", 'artist_id': '6GwNGuDRNbx5XwoHQA3QiD', 'artist_name': 'Twin Forks', 'album_name': 'Twin Forks', 'track_number': 12, 'duration_ms': 247040, 'popularity': 31, 'danceability': 0.52, 'energy': 0.321, 'loudness': -9.262, 'speechiness': 0.0271, 'acousticness': 0.845, 'instrumentalness': 0.00245, 'liveness': 0.106, 'valence': 0.202, 'tempo': 68.96}, '5kcCAHnf84RmstfEidjtjW': {'name': 'Danger', 'artist_id': '6GwNGuDRNbx5XwoHQA3QiD', 'artist_name': 'Twin Forks', 'album_name': 'Twin Forks', 'track_number': 7, 'duration_ms': 220853, 'popularity': 31, 'danceability': 0.626, 'energy': 0.661, 'loudness': -6.703, 'speechiness': 0.0343, 'acousticness': 0.189, 'instrumentalness': 0.00271, 'liveness': 0.156, 'valence': 0.444, 'tempo': 107.063}, '1UUfaWEtL31BDfwGat1ieE': {'name': 'Done', 'artist_id': '6GwNGuDRNbx5XwoHQA3QiD', 'artist_name': 'Twin Forks', 'album_name': 'Twin Forks', 'track_number': 10, 'duration_ms': 210640, 'popularity': 27, 'danceability': 0.569, 'energy': 0.627, 'loudness': -7.159, 'speechiness': 0.0304, 'acousticness': 0.0581, 'instrumentalness': 0.128, 'liveness': 0.074, 'valence': 0.164, 'tempo': 91.004}, '4B52oKoCXtye9H9LDW3wOI': {'name': 'Plans For Ya', 'artist_id': '6GwNGuDRNbx5XwoHQA3QiD', 'artist_name': 'Twin Forks', 'album_name': 'Twin Forks', 'track_number': 9, 'duration_ms': 216413, 'popularity': 27, 'danceability': 0.401, 'energy': 0.776, 'loudness': -5.4, 'speechiness': 0.0279, 'acousticness': 0.319, 'instrumentalness': 9.78e-05, 'liveness': 0.121, 'valence': 0.599, 'tempo': 171.961}, '1Pp7VoElB9xGZ4BeqUZ0ji': {'name': 'Light', 'artist_id': '2gzH4rGNFJeNg13yv2uI4L', 'artist_name': 'Jon Bryant', 'album_name': 'Twenty Something', 'track_number': 4, 'duration_ms': 267306, 'popularity': 53, 'danceability': 0.512, 'energy': 0.36, 'loudness': -11.589, 'speechiness': 0.028, 'acousticness': 0.568, 'instrumentalness': 0.0219, 'liveness': 0.13, 'valence': 0.131, 'tempo': 129.831}, '3rQqqQef0tVevvbJwgtEM4': {'name': 'Wilderness', 'artist_id': '2gzH4rGNFJeNg13yv2uI4L', 'artist_name': 'Jon Bryant', 'album_name': 'Twenty Something', 'track_number': 9, 'duration_ms': 269986, 'popularity': 45, 'danceability': 0.501, 'energy': 0.211, 'loudness': -16.668, 'speechiness': 0.0303, 'acousticness': 0.88, 'instrumentalness': 0.005, 'liveness': 0.088, 'valence': 0.137, 'tempo': 82.916}, '6bMX6XfA8Bz47vvKxOLCRy': {'name': 'Heroine', 'artist_id': '2gzH4rGNFJeNg13yv2uI4L', 'artist_name': 'Jon Bryant', 'album_name': 'Twenty Something', 'track_number': 7, 'duration_ms': 249960, 'popularity': 43, 'danceability': 0.505, 'energy': 0.295, 'loudness': -11.407, 'speechiness': 0.0288, 'acousticness': 0.806, 'instrumentalness': 2.42e-05, 'liveness': 0.0923, 'valence': 0.168, 'tempo': 147.84}, '23FJw5F8nipFrzkZviz5vQ': {'name': 'Evening Sun', 'artist_id': '2gzH4rGNFJeNg13yv2uI4L', 'artist_name': 'Jon Bryant', 'album_name': 'What Takes You', 'track_number': 5, 'duration_ms': 214702, 'popularity': 43, 'danceability': 0.45, 'energy': 0.254, 'loudness': -13.203, 'speechiness': 0.0299, 'acousticness': 0.756, 'instrumentalness': 0.0177, 'liveness': 0.104, 'valence': 0.191, 'tempo': 77.396}, '5OeQ93epC1lutxGlmqR0AU': {'name': 'Deep Dark Valley', 'artist_id': '2gzH4rGNFJeNg13yv2uI4L', 'artist_name': 'Jon Bryant', 'album_name': 'Twenty Something', 'track_number': 5, 'duration_ms': 163666, 'popularity': 41, 'danceability': 0.487, 'energy': 0.186, 'loudness': -11.656, 'speechiness': 0.0779, 'acousticness': 0.673, 'instrumentalness': 0, 'liveness': 0.109, 'valence': 0.475, 'tempo': 95.621}, '431aJf5rb7MRvRK04Y1pZP': {'name': 'Carolina', 'artist_id': '2gzH4rGNFJeNg13yv2uI4L', 'artist_name': 'Jon Bryant', 'album_name': 'What Takes You', 'track_number': 7, 'duration_ms': 246251, 'popularity': 40, 'danceability': 0.509, 'energy': 0.24, 'loudness': -10.105, 'speechiness': 0.0344, 'acousticness': 0.909, 'instrumentalness': 0, 'liveness': 0.109, 'valence': 0.356, 'tempo': 79.227}, '6ZYdXHZFoumJyBH5kC2QhP': {'name': 'Trenches and Charms', 'artist_id': '2gzH4rGNFJeNg13yv2uI4L', 'artist_name': 'Jon Bryant', 'album_name': 'Twenty Something', 'track_number': 10, 'duration_ms': 249480, 'popularity': 38, 'danceability': 0.57, 'energy': 0.391, 'loudness': -10.9, 'speechiness': 0.0394, 'acousticness': 0.686, 'instrumentalness': 0.000694, 'liveness': 0.0557, 'valence': 0.0967, 'tempo': 116.093}, '4l6y5AjO3aFnvRr3YvqTvS': {'name': "Don't Wait", 'artist_id': '2gzH4rGNFJeNg13yv2uI4L', 'artist_name': 'Jon Bryant', 'album_name': 'Twenty Something', 'track_number': 1, 'duration_ms': 249586, 'popularity': 36, 'danceability': 0.602, 'energy': 0.283, 'loudness': -10.958, 'speechiness': 0.03, 'acousticness': 0.747, 'instrumentalness': 1.09e-06, 'liveness': 0.213, 'valence': 0.201, 'tempo': 126.915}, '59NpCm0lOMObumSe0soohI': {'name': 'Were You There', 'artist_id': '2gzH4rGNFJeNg13yv2uI4L', 'artist_name': 'Jon Bryant', 'album_name': 'Two Coasts for Comfort', 'track_number': 10, 'duration_ms': 205026, 'popularity': 35, 'danceability': 0.525, 'energy': 0.194, 'loudness': -13.614, 'speechiness': 0.031, 'acousticness': 0.833, 'instrumentalness': 0.000104, 'liveness': 0.0949, 'valence': 0.272, 'tempo': 125.154}, '7bJUoMjysndU0HpyBM4AIi': {'name': 'Ontario', 'artist_id': '2gzH4rGNFJeNg13yv2uI4L', 'artist_name': 'Jon Bryant', 'album_name': 'What Takes You', 'track_number': 3, 'duration_ms': 370623, 'popularity': 34, 'danceability': 0.392, 'energy': 0.307, 'loudness': -10.725, 'speechiness': 0.0282, 'acousticness': 0.454, 'instrumentalness': 0.00512, 'liveness': 0.122, 'valence': 0.183, 'tempo': 76.634}, '6uhkZFj3vzLY0FA9ONCM41': {'name': 'Dancing Shoes', 'artist_id': '6Yuow6YoiBaVPFNjZ5BQi7', 'artist_name': 'Green River Ordinance', 'album_name': 'The Morning Passengers EP - Acoustic Sessions', 'track_number': 1, 'duration_ms': 229389, 'popularity': 51, 'danceability': 0.594, 'energy': 0.415, 'loudness': -6.99, 'speechiness': 0.0277, 'acousticness': 0.141, 'instrumentalness': 1.58e-06, 'liveness': 0.105, 'valence': 0.203, 'tempo': 138.032}, '2EaDYb12Pzd0fU8UmQBa4h': {'name': 'Endlessly', 'artist_id': '6Yuow6YoiBaVPFNjZ5BQi7', 'artist_name': 'Green River Ordinance', 'album_name': 'Out Of My Hands', 'track_number': 11, 'duration_ms': 215426, 'popularity': 43, 'danceability': 0.538, 'energy': 0.397, 'loudness': -7.72, 'speechiness': 0.0266, 'acousticness': 0.818, 'instrumentalness': 0, 'liveness': 0.11, 'valence': 0.287, 'tempo': 145.048}, '4JkP8L0inEniMrIXSIj2SK': {'name': 'Red Fire Night', 'artist_id': '6Yuow6YoiBaVPFNjZ5BQi7', 'artist_name': 'Green River Ordinance', 'album_name': 'Fifteen', 'track_number': 2, 'duration_ms': 188466, 'popularity': 34, 'danceability': 0.578, 'energy': 0.836, 'loudness': -3.443, 'speechiness': 0.0502, 'acousticness': 0.26, 'instrumentalness': 0, 'liveness': 0.168, 'valence': 0.863, 'tempo': 141.993}, '663BdiOMzIQglSd7AaMUSN': {'name': "It Ain't Love", 'artist_id': '6Yuow6YoiBaVPFNjZ5BQi7', 'artist_name': 'Green River Ordinance', 'album_name': 'Chasing Down the Wind', 'track_number': 2, 'duration_ms': 247768, 'popularity': 38, 'danceability': 0.521, 'energy': 0.695, 'loudness': -7.529, 'speechiness': 0.0277, 'acousticness': 0.0488, 'instrumentalness': 4.21e-06, 'liveness': 0.102, 'valence': 0.541, 'tempo': 160.023}, '2BVGoBQCnuvOGdeESdvgP2': {'name': 'She Is in the Air', 'artist_id': '6Yuow6YoiBaVPFNjZ5BQi7', 'artist_name': 'Green River Ordinance', 'album_name': 'Chasing Down the Wind', 'track_number': 5, 'duration_ms': 239792, 'popularity': 38, 'danceability': 0.537, 'energy': 0.535, 'loudness': -8.561, 'speechiness': 0.0287, 'acousticness': 0.612, 'instrumentalness': 0.000163, 'liveness': 0.352, 'valence': 0.329, 'tempo': 139.963}, '72BNmHN1KzumgOt0nxEapE': {'name': 'Better Love', 'artist_id': '6Yuow6YoiBaVPFNjZ5BQi7', 'artist_name': 'Green River Ordinance', 'album_name': 'Chasing Down the Wind', 'track_number': 6, 'duration_ms': 177927, 'popularity': 38, 'danceability': 0.525, 'energy': 0.532, 'loudness': -9.386, 'speechiness': 0.0455, 'acousticness': 0.238, 'instrumentalness': 1.36e-05, 'liveness': 0.197, 'valence': 0.328, 'tempo': 145.984}, '7KeSMKp6YTKg6sZqvH3FS8': {'name': 'Flying', 'artist_id': '6Yuow6YoiBaVPFNjZ5BQi7', 'artist_name': 'Green River Ordinance', 'album_name': 'Chasing Down the Wind', 'track_number': 4, 'duration_ms': 205221, 'popularity': 36, 'danceability': 0.596, 'energy': 0.865, 'loudness': -7.82, 'speechiness': 0.0281, 'acousticness': 0.00971, 'instrumentalness': 0.000413, 'liveness': 0.136, 'valence': 0.591, 'tempo': 124.011}, '3td8BqcLSrW71Vi3LlhTsi': {'name': 'Simple Life', 'artist_id': '6Yuow6YoiBaVPFNjZ5BQi7', 'artist_name': 'Green River Ordinance', 'album_name': 'Fifteen', 'track_number': 4, 'duration_ms': 237666, 'popularity': 35, 'danceability': 0.502, 'energy': 0.68, 'loudness': -3.707, 'speechiness': 0.0264, 'acousticness': 0.114, 'instrumentalness': 0, 'liveness': 0.188, 'valence': 0.398, 'tempo': 142.056}, '6Xb7RS9idYr8jzuhyOCtDt': {'name': 'On Your Own', 'artist_id': '6Yuow6YoiBaVPFNjZ5BQi7', 'artist_name': 'Green River Ordinance', 'album_name': 'Out Of My Hands', 'track_number': 4, 'duration_ms': 259760, 'popularity': 33, 'danceability': 0.435, 'energy': 0.831, 'loudness': -4.212, 'speechiness': 0.0436, 'acousticness': 0.125, 'instrumentalness': 0, 'liveness': 0.0801, 'valence': 0.179, 'tempo': 143.989}, '2LaoI1GMcL2fBO4uZfmon7': {'name': 'Heart of Me', 'artist_id': '6Yuow6YoiBaVPFNjZ5BQi7', 'artist_name': 'Green River Ordinance', 'album_name': 'Under Fire', 'track_number': 3, 'duration_ms': 209773, 'popularity': 29, 'danceability': 0.523, 'energy': 0.782, 'loudness': -4.617, 'speechiness': 0.0308, 'acousticness': 0.0378, 'instrumentalness': 0, 'liveness': 0.352, 'valence': 0.583, 'tempo': 122.031}, '2PwXOevGUSkU8qaYZjgLq2': {'name': 'All I Want', 'artist_id': '4BxCuXFJrSWGi1KHcVqaU4', 'artist_name': 'Kodaline', 'album_name': 'In A Perfect World', 'track_number': 2, 'duration_ms': 305746, 'popularity': 71, 'danceability': 0.209, 'energy': 0.412, 'loudness': -9.733, 'speechiness': 0.0443, 'acousticness': 0.172, 'instrumentalness': 0.15, 'liveness': 0.0843, 'valence': 0.154, 'tempo': 86.26}, '5rZXBHUU2qz7huEckTwpqo': {'name': 'High Hopes', 'artist_id': '4BxCuXFJrSWGi1KHcVqaU4', 'artist_name': 'Kodaline', 'album_name': 'In A Perfect World', 'track_number': 4, 'duration_ms': 230266, 'popularity': 60, 'danceability': 0.488, 'energy': 0.487, 'loudness': -6.371, 'speechiness': 0.0307, 'acousticness': 0.577, 'instrumentalness': 0, 'liveness': 0.193, 'valence': 0.235, 'tempo': 77.344}, '0My8NPmENHrN5W7OfgZnZJ': {'name': 'The One', 'artist_id': '4BxCuXFJrSWGi1KHcVqaU4', 'artist_name': 'Kodaline', 'album_name': 'Coming Up for Air (Deluxe)', 'track_number': 2, 'duration_ms': 232520, 'popularity': 66, 'danceability': 0.43, 'energy': 0.587, 'loudness': -8.003, 'speechiness': 0.0348, 'acousticness': 0.654, 'instrumentalness': 8.83e-05, 'liveness': 0.158, 'valence': 0.324, 'tempo': 156.006}, '1VfJeju8B6qP4ZFsYuVW9U': {'name': 'Love Like This - Acoustic', 'artist_id': '4BxCuXFJrSWGi1KHcVqaU4', 'artist_name': 'Kodaline', 'album_name': 'Love Like This', 'track_number': 5, 'duration_ms': 241640, 'popularity': 57, 'danceability': 0.398, 'energy': 0.151, 'loudness': -14.402, 'speechiness': 0.0341, 'acousticness': 0.961, 'instrumentalness': 0.0425, 'liveness': 0.0923, 'valence': 0.0758, 'tempo': 107.072}, '3weT2tgXC6sQ0AKZcj3vwH': {'name': 'Love Like This', 'artist_id': '4BxCuXFJrSWGi1KHcVqaU4', 'artist_name': 'Kodaline', 'album_name': 'In A Perfect World', 'track_number': 3, 'duration_ms': 216346, 'popularity': 50, 'danceability': 0.456, 'energy': 0.815, 'loudness': -4.801, 'speechiness': 0.0411, 'acousticness': 0.0463, 'instrumentalness': 0, 'liveness': 0.266, 'valence': 0.371, 'tempo': 123.996}, '41Tfjvjuw8s61okfqPOV1Z': {'name': 'One Day', 'artist_id': '4BxCuXFJrSWGi1KHcVqaU4', 'artist_name': 'Kodaline', 'album_name': 'In A Perfect World', 'track_number': 1, 'duration_ms': 255560, 'popularity': 48, 'danceability': 0.48, 'energy': 0.749, 'loudness': -5.553, 'speechiness': 0.0282, 'acousticness': 0.0839, 'instrumentalness': 0.00128, 'liveness': 0.111, 'valence': 0.334, 'tempo': 96.015}, '11IYMTXu5Uws1DjmUMLOcP': {'name': 'Love Will Set You Free', 'artist_id': '4BxCuXFJrSWGi1KHcVqaU4', 'artist_name': 'Kodaline', 'album_name': 'Coming Up for Air (Deluxe)', 'track_number': 12, 'duration_ms': 260093, 'popularity': 55, 'danceability': 0.472, 'energy': 0.421, 'loudness': -8.553, 'speechiness': 0.0265, 'acousticness': 0.115, 'instrumentalness': 3.09e-06, 'liveness': 0.167, 'valence': 0.288, 'tempo': 75.017}, '16Lt4xHuWNaMX9JNzEpq9n': {'name': 'Talk', 'artist_id': '4BxCuXFJrSWGi1KHcVqaU4', 'artist_name': 'Kodaline', 'album_name': 'In A Perfect World', 'track_number': 9, 'duration_ms': 268360, 'popularity': 47, 'danceability': 0.541, 'energy': 0.455, 'loudness': -7.305, 'speechiness': 0.0306, 'acousticness': 0.531, 'instrumentalness': 8.71e-05, 'liveness': 0.0689, 'valence': 0.168, 'tempo': 119.985}, '3QFCL0dqEzXFIWlqWiVDJU': {'name': 'Moving on', 'artist_id': '4BxCuXFJrSWGi1KHcVqaU4', 'artist_name': 'Kodaline', 'album_name': 'Coming Up for Air (Deluxe)', 'track_number': 15, 'duration_ms': 265813, 'popularity': 54, 'danceability': 0.536, 'energy': 0.383, 'loudness': -10.582, 'speechiness': 0.0393, 'acousticness': 0.884, 'instrumentalness': 0, 'liveness': 0.0732, 'valence': 0.176, 'tempo': 81.124}, '1595LW73XBxkRk2ciQOHfr': {'name': 'A-Punk', 'artist_id': '5BvJzeQpmsdsFp4HGUYUEx', 'artist_name': 'Vampire Weekend', 'album_name': 'Vampire Weekend', 'track_number': 3, 'duration_ms': 137760, 'popularity': 67, 'danceability': 0.548, 'energy': 0.816, 'loudness': -4.478, 'speechiness': 0.0499, 'acousticness': 0.0104, 'instrumentalness': 0.0543, 'liveness': 0.152, 'valence': 0.858, 'tempo': 174.993}, '7psPPGwhFzP3pyOcb3ivcT': {'name': 'Unbelievers', 'artist_id': '5BvJzeQpmsdsFp4HGUYUEx', 'artist_name': 'Vampire Weekend', 'album_name': 'Modern Vampires of the City', 'track_number': 2, 'duration_ms': 202666, 'popularity': 67, 'danceability': 0.644, 'energy': 0.811, 'loudness': -7.681, 'speechiness': 0.0499, 'acousticness': 0.142, 'instrumentalness': 0.000629, 'liveness': 0.169, 'valence': 0.837, 'tempo': 154.903}, '78J9MBkAoqfvyeEpQKJDzD': {'name': 'Step', 'artist_id': '5BvJzeQpmsdsFp4HGUYUEx', 'artist_name': 'Vampire Weekend', 'album_name': 'Modern Vampires of the City', 'track_number': 3, 'duration_ms': 251626, 'popularity': 66, 'danceability': 0.624, 'energy': 0.724, 'loudness': -7.113, 'speechiness': 0.101, 'acousticness': 0.591, 'instrumentalness': 7.79e-06, 'liveness': 0.101, 'valence': 0.62, 'tempo': 78.008}, '104pmtTQOlmW8Zt2BipGKH': {'name': 'Diane Young', 'artist_id': '5BvJzeQpmsdsFp4HGUYUEx', 'artist_name': 'Vampire Weekend', 'album_name': 'Modern Vampires of the City', 'track_number': 4, 'duration_ms': 160066, 'popularity': 64, 'danceability': 0.419, 'energy': 0.803, 'loudness': -5.498, 'speechiness': 0.246, 'acousticness': 0.032, 'instrumentalness': 3.7e-05, 'liveness': 0.206, 'valence': 0.745, 'tempo': 86.958}, '2Ml0l8YWJLQhPrRDLpQaDM': {'name': 'Oxford Comma', 'artist_id': '5BvJzeQpmsdsFp4HGUYUEx', 'artist_name': 'Vampire Weekend', 'album_name': 'Vampire Weekend', 'track_number': 2, 'duration_ms': 195733, 'popularity': 62, 'danceability': 0.694, 'energy': 0.711, 'loudness': -4.237, 'speechiness': 0.0517, 'acousticness': 0.114, 'instrumentalness': 0.00124, 'liveness': 0.0433, 'valence': 0.974, 'tempo': 119.516}, '3t87C08isN6yw2DnWOorLm': {'name': 'Hannah Hunt', 'artist_id': '5BvJzeQpmsdsFp4HGUYUEx', 'artist_name': 'Vampire Weekend', 'album_name': 'Modern Vampires of the City', 'track_number': 6, 'duration_ms': 237973, 'popularity': 59, 'danceability': 0.345, 'energy': 0.313, 'loudness': -10.098, 'speechiness': 0.0681, 'acousticness': 0.717, 'instrumentalness': 0.000822, 'liveness': 0.1, 'valence': 0.166, 'tempo': 207.969}, '4eE6vZ2vOrceLq4xgz3VmG': {'name': 'Ya Hey', 'artist_id': '5BvJzeQpmsdsFp4HGUYUEx', 'artist_name': 'Vampire Weekend', 'album_name': 'Modern Vampires of the City', 'track_number': 10, 'duration_ms': 312653, 'popularity': 58, 'danceability': 0.584, 'energy': 0.65, 'loudness': -6.481, 'speechiness': 0.0427, 'acousticness': 0.179, 'instrumentalness': 0.000283, 'liveness': 0.0935, 'valence': 0.493, 'tempo': 92.01}, '2gKZXeCTkQjblUQgnKF7Ow': {'name': 'Obvious Bicycle', 'artist_id': '5BvJzeQpmsdsFp4HGUYUEx', 'artist_name': 'Vampire Weekend', 'album_name': 'Modern Vampires of the City', 'track_number': 1, 'duration_ms': 251253, 'popularity': 56, 'danceability': 0.472, 'energy': 0.29, 'loudness': -12.327, 'speechiness': 0.0957, 'acousticness': 0.403, 'instrumentalness': 0.000115, 'liveness': 0.199, 'valence': 0.137, 'tempo': 180.098}, '7q4MJZSiqPC16dbhQWxugv': {'name': 'Cape Cod Kwassa Kwassa', 'artist_id': '5BvJzeQpmsdsFp4HGUYUEx', 'artist_name': 'Vampire Weekend', 'album_name': 'Vampire Weekend', 'track_number': 4, 'duration_ms': 214706, 'popularity': 55, 'danceability': 0.852, 'energy': 0.518, 'loudness': -7.155, 'speechiness': 0.0413, 'acousticness': 0.832, 'instrumentalness': 0.0893, 'liveness': 0.14, 'valence': 0.771, 'tempo': 105.058}, '5y02IcERVgEUItFLeeZDz6': {'name': 'Worship You', 'artist_id': '5BvJzeQpmsdsFp4HGUYUEx', 'artist_name': 'Vampire Weekend', 'album_name': 'Modern Vampires of the City', 'track_number': 9, 'duration_ms': 201240, 'popularity': 55, 'danceability': 0.474, 'energy': 0.919, 'loudness': -5.966, 'speechiness': 0.0779, 'acousticness': 0.00119, 'instrumentalness': 1.82e-06, 'liveness': 0.314, 'valence': 0.309, 'tempo': 149.055}, '2v162mDpVPU2tUhKZtgjpV': {'name': 'Sophie', 'artist_id': '0nJaMZM8paoA5HEUTUXPqi', 'artist_name': "Bear's Den", 'album_name': 'Without/Within', 'track_number': 5, 'duration_ms': 304506, 'popularity': 62, 'danceability': 0.592, 'energy': 0.299, 'loudness': -12.74, 'speechiness': 0.0321, 'acousticness': 0.778, 'instrumentalness': 0.00511, 'liveness': 0.185, 'valence': 0.365, 'tempo': 144.069}, '5V3c00YkpPZQSpGxi50kuu': {'name': 'Berlin', 'artist_id': '0nJaMZM8paoA5HEUTUXPqi', 'artist_name': "Bear's Den", 'album_name': 'Berlin', 'track_number': 1, 'duration_ms': 269233, 'popularity': 57, 'danceability': 0.499, 'energy': 0.406, 'loudness': -13.85, 'speechiness': 0.0336, 'acousticness': 0.876, 'instrumentalness': 0.00767, 'liveness': 0.0994, 'valence': 0.321, 'tempo': 90.91}, '0u3rkZ1Z5f1JIPHlLUX2Mi': {'name': 'Agape', 'artist_id': '0nJaMZM8paoA5HEUTUXPqi', 'artist_name': "Bear's Den", 'album_name': 'Islands', 'track_number': 1, 'duration_ms': 257519, 'popularity': 47, 'danceability': 0.448, 'energy': 0.603, 'loudness': -7.884, 'speechiness': 0.0327, 'acousticness': 0.0157, 'instrumentalness': 0.00473, 'liveness': 0.118, 'valence': 0.175, 'tempo': 149.898}, '5hdyp3FQ2S1TdyFlO630CH': {'name': 'Auld Wives', 'artist_id': '0nJaMZM8paoA5HEUTUXPqi', 'artist_name': "Bear's Den", 'album_name': 'Red Earth & Pouring Rain', 'track_number': 7, 'duration_ms': 278613, 'popularity': 42, 'danceability': 0.55, 'energy': 0.696, 'loudness': -7.723, 'speechiness': 0.0282, 'acousticness': 0.258, 'instrumentalness': 0.0533, 'liveness': 0.0812, 'valence': 0.263, 'tempo': 95.012}, '6RmaaE3i8WpOzjjXwBPGLn': {'name': 'Red Earth & Pouring Rain', 'artist_id': '0nJaMZM8paoA5HEUTUXPqi', 'artist_name': "Bear's Den", 'album_name': 'Red Earth & Pouring Rain', 'track_number': 1, 'duration_ms': 292066, 'popularity': 46, 'danceability': 0.528, 'energy': 0.611, 'loudness': -5.635, 'speechiness': 0.0273, 'acousticness': 0.0182, 'instrumentalness': 0.0006, 'liveness': 0.072, 'valence': 0.0379, 'tempo': 92.086}, '2MaCvfadvDHyrttQen5kv2': {'name': 'When You Break', 'artist_id': '0nJaMZM8paoA5HEUTUXPqi', 'artist_name': "Bear's Den", 'album_name': 'Agape', 'track_number': 4, 'duration_ms': 287933, 'popularity': 53, 'danceability': 0.508, 'energy': 0.504, 'loudness': -10.922, 'speechiness': 0.0491, 'acousticness': 0.605, 'instrumentalness': 0.0025, 'liveness': 0.139, 'valence': 0.176, 'tempo': 141.004}, '4wlTRoeZs9bMr65AmScn2L': {'name': 'Writing On The Wall - Spotify Sessions / Curated By Jim Eno', 'artist_id': '0nJaMZM8paoA5HEUTUXPqi', 'artist_name': "Bear's Den", 'album_name': 'Spotify Sessions (Curated By Jim Eno)', 'track_number': 1, 'duration_ms': 256701, 'popularity': 34, 'danceability': 0.583, 'energy': 0.648, 'loudness': -6.115, 'speechiness': 0.0309, 'acousticness': 0.39, 'instrumentalness': 0.0795, 'liveness': 0.0817, 'valence': 0.596, 'tempo': 65.554}, '40YV3J6bAVimjb4yJf5ieJ': {'name': 'Gabriel', 'artist_id': '0nJaMZM8paoA5HEUTUXPqi', 'artist_name': "Bear's Den", 'album_name': 'Red Earth & Pouring Rain', 'track_number': 11, 'duration_ms': 244600, 'popularity': 42, 'danceability': 0.603, 'energy': 0.417, 'loudness': -10.076, 'speechiness': 0.0346, 'acousticness': 0.708, 'instrumentalness': 0.00224, 'liveness': 0.116, 'valence': 0.259, 'tempo': 139.773}, '7mLcjLqiY9rJUA3BQAywiH': {'name': 'Elysium', 'artist_id': '0nJaMZM8paoA5HEUTUXPqi', 'artist_name': "Bear's Den", 'album_name': 'Islands', 'track_number': 9, 'duration_ms': 206160, 'popularity': 43, 'danceability': 0.304, 'energy': 0.426, 'loudness': -9.739, 'speechiness': 0.0331, 'acousticness': 0.0627, 'instrumentalness': 0.163, 'liveness': 0.106, 'valence': 0.118, 'tempo': 138.258}, '34fJIXIKjz8tbUwzRiD4lj': {'name': 'Wind & Anchor', 'artist_id': '2JMtxA2S9SNUlqBlkDtXm6', 'artist_name': 'The National Parks', 'album_name': 'Young', 'track_number': 11, 'duration_ms': 188493, 'popularity': 52, 'danceability': 0.44, 'energy': 0.324, 'loudness': -9.468, 'speechiness': 0.0307, 'acousticness': 0.777, 'instrumentalness': 1.41e-06, 'liveness': 0.0621, 'valence': 0.313, 'tempo': 79.382}, '7s8slcfStICYWbPUwf983B': {'name': 'Corao', 'artist_id': '2JMtxA2S9SNUlqBlkDtXm6', 'artist_name': 'The National Parks', 'album_name': 'Until I Live', 'track_number': 1, 'duration_ms': 229426, 'popularity': 44, 'danceability': 0.498, 'energy': 0.624, 'loudness': -6.446, 'speechiness': 0.04, 'acousticness': 0.0247, 'instrumentalness': 0.000439, 'liveness': 0.102, 'valence': 0.439, 'tempo': 130.05}, '2AcN6OGdjrnvNNoLTLFSy6': {'name': 'You Are Gold', 'artist_id': '2JMtxA2S9SNUlqBlkDtXm6', 'artist_name': 'The National Parks', 'album_name': 'Until I Live', 'track_number': 7, 'duration_ms': 216653, 'popularity': 42, 'danceability': 0.43, 'energy': 0.133, 'loudness': -13.512, 'speechiness': 0.0311, 'acousticness': 0.874, 'instrumentalness': 0.000322, 'liveness': 0.113, 'valence': 0.156, 'tempo': 107.916}, '0rQDAm42zmL10iTmeQb1Hm': {'name': 'Ba Ba Ra', 'artist_id': '2JMtxA2S9SNUlqBlkDtXm6', 'artist_name': 'The National Parks', 'album_name': 'Until I Live', 'track_number': 10, 'duration_ms': 227520, 'popularity': 39, 'danceability': 0.568, 'energy': 0.571, 'loudness': -8.462, 'speechiness': 0.0327, 'acousticness': 0.0152, 'instrumentalness': 0.0103, 'liveness': 0.181, 'valence': 0.27, 'tempo': 107.069}, '5jR1sFQdmmb0wN0C8jq12F': {'name': 'As We Ran (Bunt. Edit)', 'artist_id': '2JMtxA2S9SNUlqBlkDtXm6', 'artist_name': 'The National Parks', 'album_name': 'As We Ran (Bunt. Edit)', 'track_number': 1, 'duration_ms': 232380, 'popularity': 38, 'danceability': 0.469, 'energy': 0.694, 'loudness': -7.168, 'speechiness': 0.0379, 'acousticness': 0.068, 'instrumentalness': 0.00757, 'liveness': 0.0714, 'valence': 0.437, 'tempo': 126.032}, '6Yx9yDESLdPcpytSmOmltM': {'name': 'Monsters of the North', 'artist_id': '2JMtxA2S9SNUlqBlkDtXm6', 'artist_name': 'The National Parks', 'album_name': 'Until I Live', 'track_number': 3, 'duration_ms': 232853, 'popularity': 38, 'danceability': 0.642, 'energy': 0.617, 'loudness': -8.228, 'speechiness': 0.0632, 'acousticness': 0.0821, 'instrumentalness': 0.000518, 'liveness': 0.232, 'valence': 0.319, 'tempo': 138.059}, '0I073R2LQQrkRNXXptWmdG': {'name': 'Ghosts', 'artist_id': '2JMtxA2S9SNUlqBlkDtXm6', 'artist_name': 'The National Parks', 'album_name': 'Young', 'track_number': 3, 'duration_ms': 260306, 'popularity': 36, 'danceability': 0.29, 'energy': 0.295, 'loudness': -12.937, 'speechiness': 0.0316, 'acousticness': 0.717, 'instrumentalness': 0.00203, 'liveness': 0.0786, 'valence': 0.232, 'tempo': 146.84}, '1cYV9cRRD5GArn8jj5D6Od': {'name': 'Glow', 'artist_id': '2JMtxA2S9SNUlqBlkDtXm6', 'artist_name': 'The National Parks', 'album_name': 'Until I Live', 'track_number': 2, 'duration_ms': 240960, 'popularity': 34, 'danceability': 0.567, 'energy': 0.627, 'loudness': -6.993, 'speechiness': 0.0345, 'acousticness': 0.0334, 'instrumentalness': 0.000283, 'liveness': 0.123, 'valence': 0.193, 'tempo': 128.017}, '139OFhHYDAvIGbl1pxZEm3': {'name': 'Helsinki', 'artist_id': '2JMtxA2S9SNUlqBlkDtXm6', 'artist_name': 'The National Parks', 'album_name': 'Young', 'track_number': 1, 'duration_ms': 237213, 'popularity': 34, 'danceability': 0.381, 'energy': 0.311, 'loudness': -11.856, 'speechiness': 0.0293, 'acousticness': 0.568, 'instrumentalness': 0.000213, 'liveness': 0.0863, 'valence': 0.0515, 'tempo': 106.031}, '2KCqAdd2ad0hpJc5ySoTE8': {'name': 'Coastline', 'artist_id': '7IAFAOtc9kTYNTizhLSWM6', 'artist_name': 'Hollow Coves', 'album_name': 'Wanderlust', 'track_number': 1, 'duration_ms': 233973, 'popularity': 56, 'danceability': 0.67, 'energy': 0.496, 'loudness': -11.23, 'speechiness': 0.0277, 'acousticness': 0.63, 'instrumentalness': 0.00316, 'liveness': 0.0584, 'valence': 0.417, 'tempo': 100.168}, '4fPQ3n56NbnONBtlaPMa82': {'name': 'Home', 'artist_id': '7IAFAOtc9kTYNTizhLSWM6', 'artist_name': 'Hollow Coves', 'album_name': 'Wanderlust', 'track_number': 5, 'duration_ms': 202440, 'popularity': 49, 'danceability': 0.504, 'energy': 0.497, 'loudness': -11.858, 'speechiness': 0.0253, 'acousticness': 0.86, 'instrumentalness': 0.00486, 'liveness': 0.117, 'valence': 0.251, 'tempo': 84.879}, '08bo51XXjxoJRv3O9tuUaj': {'name': 'The Woods', 'artist_id': '7IAFAOtc9kTYNTizhLSWM6', 'artist_name': 'Hollow Coves', 'album_name': 'Wanderlust', 'track_number': 3, 'duration_ms': 241546, 'popularity': 52, 'danceability': 0.802, 'energy': 0.41, 'loudness': -12.793, 'speechiness': 0.0455, 'acousticness': 0.411, 'instrumentalness': 0.000994, 'liveness': 0.0941, 'valence': 0.226, 'tempo': 106.05}, '5q3lFZYp9HLaXATffQSgcj': {'name': 'We Will Run', 'artist_id': '7IAFAOtc9kTYNTizhLSWM6', 'artist_name': 'Hollow Coves', 'album_name': 'Wanderlust', 'track_number': 2, 'duration_ms': 255520, 'popularity': 43, 'danceability': 0.653, 'energy': 0.627, 'loudness': -9.601, 'speechiness': 0.034, 'acousticness': 0.494, 'instrumentalness': 0.0357, 'liveness': 0.166, 'valence': 0.452, 'tempo': 100.109}, '6JcjrO7RInmcq8WNa0TrPn': {'name': 'The Wood (Bass Fly & Laurent L Remix)', 'artist_id': '7IAFAOtc9kTYNTizhLSWM6', 'artist_name': 'Hollow Coves', 'album_name': 'FG Chill Out #1 - The Deep House & Lounge Music Must Have Selection', 'track_number': 26, 'duration_ms': 268120, 'popularity': 37, 'danceability': 0.64, 'energy': 0.68, 'loudness': -7.06, 'speechiness': 0.0312, 'acousticness': 0.081, 'instrumentalness': 0.00395, 'liveness': 0.0923, 'valence': 0.143, 'tempo': 115.025}, '28sWYevC75ZrUMJ0tD4zWM': {'name': 'These Memories', 'artist_id': '7IAFAOtc9kTYNTizhLSWM6', 'artist_name': 'Hollow Coves', 'album_name': 'Wanderlust', 'track_number': 6, 'duration_ms': 313480, 'popularity': 35, 'danceability': 0.537, 'energy': 0.265, 'loudness': -18.229, 'speechiness': 0.0304, 'acousticness': 0.961, 'instrumentalness': 0.131, 'liveness': 0.0676, 'valence': 0.37, 'tempo': 77.471}, '6J2X5zPPmyDG80Nw5x7hQC': {'name': 'Interlude', 'artist_id': '7IAFAOtc9kTYNTizhLSWM6', 'artist_name': 'Hollow Coves', 'album_name': 'Wanderlust', 'track_number': 4, 'duration_ms': 60013, 'popularity': 32, 'danceability': 0.585, 'energy': 0.0831, 'loudness': -21.379, 'speechiness': 0.0395, 'acousticness': 0.988, 'instrumentalness': 0.934, 'liveness': 0.111, 'valence': 0.628, 'tempo': 99.971}, '460VcG8aVLhv8KzTvULfLo': {'name': 'Fighting a Ghost', 'artist_id': '5r2ltbRmBrS2c0J4oTwfGo', 'artist_name': 'Matt Hires', 'album_name': 'American Wilderness', 'track_number': 1, 'duration_ms': 224020, 'popularity': 47, 'danceability': 0.449, 'energy': 0.82, 'loudness': -8.887, 'speechiness': 0.136, 'acousticness': 0.00438, 'instrumentalness': 0, 'liveness': 0.081, 'valence': 0.211, 'tempo': 78.968}, '1AZ3kCJfnyJt5O3broFxAD': {'name': 'A To B', 'artist_id': '5r2ltbRmBrS2c0J4oTwfGo', 'artist_name': 'Matt Hires', 'album_name': 'A to B EP', 'track_number': 2, 'duration_ms': 197093, 'popularity': 36, 'danceability': 0.453, 'energy': 0.619, 'loudness': -6.498, 'speechiness': 0.0295, 'acousticness': 0.288, 'instrumentalness': 0, 'liveness': 0.268, 'valence': 0.83, 'tempo': 90.385}, '2jL97xZFlwpskNvmVIOQn0': {'name': 'Honey, Let Me Sing You A Song', 'artist_id': '5r2ltbRmBrS2c0J4oTwfGo', 'artist_name': 'Matt Hires', 'album_name': 'Take Us To The Start', 'track_number': 1, 'duration_ms': 248533, 'popularity': 34, 'danceability': 0.581, 'energy': 0.844, 'loudness': -3.701, 'speechiness': 0.0326, 'acousticness': 0.124, 'instrumentalness': 0, 'liveness': 0.0942, 'valence': 0.653, 'tempo': 127.056}, '3mgpIfk3tDrfjyY0OoKiX2': {'name': 'Glory Bound', 'artist_id': '5r2ltbRmBrS2c0J4oTwfGo', 'artist_name': 'Matt Hires', 'album_name': 'American Wilderness', 'track_number': 5, 'duration_ms': 252650, 'popularity': 34, 'danceability': 0.509, 'energy': 0.657, 'loudness': -6.331, 'speechiness': 0.045, 'acousticness': 0.438, 'instrumentalness': 0, 'liveness': 0.0537, 'valence': 0.354, 'tempo': 131.922}, '64uVjoozJhPeP4GVlBIFoR': {'name': 'Out Of The Dark', 'artist_id': '5r2ltbRmBrS2c0J4oTwfGo', 'artist_name': 'Matt Hires', 'album_name': 'Take Us To The Start', 'track_number': 10, 'duration_ms': 247133, 'popularity': 33, 'danceability': 0.674, 'energy': 0.462, 'loudness': -7.133, 'speechiness': 0.0292, 'acousticness': 0.523, 'instrumentalness': 0, 'liveness': 0.0757, 'valence': 0.469, 'tempo': 118.955}, '40sRbPxIlHNkDaaC4oFUIR': {'name': 'Hold You Up', 'artist_id': '5r2ltbRmBrS2c0J4oTwfGo', 'artist_name': 'Matt Hires', 'album_name': 'Hold You Up', 'track_number': 1, 'duration_ms': 224637, 'popularity': 28, 'danceability': 0.593, 'energy': 0.674, 'loudness': -7.074, 'speechiness': 0.0334, 'acousticness': 0.0839, 'instrumentalness': 0, 'liveness': 0.0878, 'valence': 0.426, 'tempo': 88.039}, '5aHLzcx8t1KDMnHgU7LNRz': {'name': 'Forever', 'artist_id': '5r2ltbRmBrS2c0J4oTwfGo', 'artist_name': 'Matt Hires', 'album_name': "This World Won't Last Forever, But Tonight We Can Pretend", 'track_number': 1, 'duration_ms': 208480, 'popularity': 27, 'danceability': 0.539, 'energy': 0.856, 'loudness': -5.54, 'speechiness': 0.0439, 'acousticness': 7.78e-05, 'instrumentalness': 0.00307, 'liveness': 0.0937, 'valence': 0.443, 'tempo': 143.089}, '1v83gmu2L9frOvrrT4UMZB': {'name': 'Begin Again', 'artist_id': '5r2ltbRmBrS2c0J4oTwfGo', 'artist_name': 'Matt Hires', 'album_name': 'American Wilderness', 'track_number': 6, 'duration_ms': 176117, 'popularity': 27, 'danceability': 0.637, 'energy': 0.44, 'loudness': -9.172, 'speechiness': 0.0419, 'acousticness': 0.919, 'instrumentalness': 0.000229, 'liveness': 0.109, 'valence': 0.377, 'tempo': 164.756}, '4JUHCikVx6Fav0i9XOOegH': {'name': 'Holy War', 'artist_id': '5r2ltbRmBrS2c0J4oTwfGo', 'artist_name': 'Matt Hires', 'album_name': 'American Wilderness', 'track_number': 2, 'duration_ms': 195436, 'popularity': 26, 'danceability': 0.466, 'energy': 0.889, 'loudness': -5.155, 'speechiness': 0.0635, 'acousticness': 0.00495, 'instrumentalness': 0, 'liveness': 0.0999, 'valence': 0.43, 'tempo': 124.08}, '6GmUVqe73u5YRfUUynZK6I': {'name': 'Let Her Go', 'artist_id': '0gadJ2b9A4SKsB1RFkBb66', 'artist_name': 'Passenger', 'album_name': 'All the Little Lights', 'track_number': 2, 'duration_ms': 252733, 'popularity': 75, 'danceability': 0.479, 'energy': 0.545, 'loudness': -7.346, 'speechiness': 0.0688, 'acousticness': 0.365, 'instrumentalness': 0, 'liveness': 0.0963, 'valence': 0.239, 'tempo': 74.897}, '3V2pTc1zYbZGzHlyd3YtlH': {'name': 'Anywhere', 'artist_id': '0gadJ2b9A4SKsB1RFkBb66', 'artist_name': 'Passenger', 'album_name': 'Young as the Morning Old as the Sea (Deluxe Version)', 'track_number': 4, 'duration_ms': 216200, 'popularity': 57, 'danceability': 0.594, 'energy': 0.635, 'loudness': -6.192, 'speechiness': 0.0295, 'acousticness': 0.0953, 'instrumentalness': 7.05e-05, 'liveness': 0.0917, 'valence': 0.801, 'tempo': 104.507}, '1RNyz1P8eyL5BsCzooCguk': {'name': "What You're Thinking (feat. Josh Pyke)", 'artist_id': '0gadJ2b9A4SKsB1RFkBb66', 'artist_name': 'Passenger', 'album_name': 'Flight of the Crow', 'track_number': 2, 'duration_ms': 174613, 'popularity': 66, 'danceability': 0.467, 'energy': 0.384, 'loudness': -9.968, 'speechiness': 0.0278, 'acousticness': 0.77, 'instrumentalness': 1.98e-06, 'liveness': 0.104, 'valence': 0.494, 'tempo': 78.685}, '3eeIdvZqXaffY0yVRgbGfQ': {'name': 'Shape of Love (feat. Boy & Bear)', 'artist_id': '0gadJ2b9A4SKsB1RFkBb66', 'artist_name': 'Passenger', 'album_name': 'Flight of the Crow', 'track_number': 3, 'duration_ms': 188453, 'popularity': 65, 'danceability': 0.625, 'energy': 0.736, 'loudness': -8.658, 'speechiness': 0.0325, 'acousticness': 0.118, 'instrumentalness': 0, 'liveness': 0.167, 'valence': 0.91, 'tempo': 105.529}, '4tzAf07GCR6DlycQkUKlgN': {'name': 'Let Her Go - Acoustic', 'artist_id': '0gadJ2b9A4SKsB1RFkBb66', 'artist_name': 'Passenger', 'album_name': 'All the Little Lights (Deluxe Version)', 'track_number': 1, 'duration_ms': 266626, 'popularity': 56, 'danceability': 0.546, 'energy': 0.0775, 'loudness': -13.75, 'speechiness': 0.0497, 'acousticness': 0.945, 'instrumentalness': 0, 'liveness': 0.0818, 'valence': 0.242, 'tempo': 143.114}, '6nd9ZMftN6tfm2YAoUvK7f': {'name': 'Beautiful Birds (feat. Birdy)', 'artist_id': '0gadJ2b9A4SKsB1RFkBb66', 'artist_name': 'Passenger', 'album_name': 'Young as the Morning Old as the Sea (Deluxe Version)', 'track_number': 7, 'duration_ms': 213706, 'popularity': 52, 'danceability': 0.318, 'energy': 0.182, 'loudness': -11.91, 'speechiness': 0.0296, 'acousticness': 0.91, 'instrumentalness': 0.00253, 'liveness': 0.116, 'valence': 0.137, 'tempo': 85.863}, '1xUOevQqJdG7ERSLFByT7v': {'name': 'A Kindly Reminder', 'artist_id': '0gadJ2b9A4SKsB1RFkBb66', 'artist_name': 'Passenger', 'album_name': 'A Kindly Reminder', 'track_number': 1, 'duration_ms': 163365, 'popularity': 58, 'danceability': 0.408, 'energy': 0.539, 'loudness': -9.149, 'speechiness': 0.0388, 'acousticness': 0.331, 'instrumentalness': 4.09e-05, 'liveness': 0.339, 'valence': 0.467, 'tempo': 109.284}, '0IknWdl7UzA71oKRQneQ41': {'name': 'Young as the Morning Old as the Sea', 'artist_id': '0gadJ2b9A4SKsB1RFkBb66', 'artist_name': 'Passenger', 'album_name': 'Young as the Morning Old as the Sea (Deluxe Version)', 'track_number': 6, 'duration_ms': 206080, 'popularity': 47, 'danceability': 0.61, 'energy': 0.466, 'loudness': -10.129, 'speechiness': 0.0343, 'acousticness': 0.625, 'instrumentalness': 0.0558, 'liveness': 0.113, 'valence': 0.837, 'tempo': 105.705}, '10D6VJLgBNPJLDCGJH8NKM': {'name': "Somebody's Love - Single Version", 'artist_id': '0gadJ2b9A4SKsB1RFkBb66', 'artist_name': 'Passenger', 'album_name': "Somebody's Love", 'track_number': 1, 'duration_ms': 225413, 'popularity': 56, 'danceability': 0.508, 'energy': 0.61, 'loudness': -6.526, 'speechiness': 0.0379, 'acousticness': 0.237, 'instrumentalness': 4.16e-05, 'liveness': 0.233, 'valence': 0.593, 'tempo': 136.33}, '17VHkJ5zeQBRHL3i0J0jT8': {'name': 'Fear of Fear', 'artist_id': '0gadJ2b9A4SKsB1RFkBb66', 'artist_name': 'Passenger', 'album_name': 'Whispers II', 'track_number': 1, 'duration_ms': 178698, 'popularity': 58, 'danceability': 0.484, 'energy': 0.276, 'loudness': -11.347, 'speechiness': 0.0428, 'acousticness': 0.831, 'instrumentalness': 0, 'liveness': 0.105, 'valence': 0.291, 'tempo': 160.97}, '6t6oULCRS6hnI7rm0h5gwl': {'name': 'Some Nights', 'artist_id': '5nCi3BB41mBaMH9gfr6Su0', 'artist_name': 'fun.', 'album_name': 'Some Nights (Spotify Exclusive)', 'track_number': 2, 'duration_ms': 277040, 'popularity': 72, 'danceability': 0.672, 'energy': 0.738, 'loudness': -7.045, 'speechiness': 0.0506, 'acousticness': 0.0178, 'instrumentalness': 6.75e-05, 'liveness': 0.0927, 'valence': 0.401, 'tempo': 107.938}, '7a86XRg84qjasly9f6bPSD': {'name': 'We Are Young (feat. Janelle Mone) - feat. Janelle Monae', 'artist_id': '5nCi3BB41mBaMH9gfr6Su0', 'artist_name': 'fun.', 'album_name': 'Some Nights (Spotify Exclusive)', 'track_number': 3, 'duration_ms': 250626, 'popularity': 70, 'danceability': 0.378, 'energy': 0.638, 'loudness': -5.576, 'speechiness': 0.075, 'acousticness': 0.02, 'instrumentalness': 7.66e-05, 'liveness': 0.0849, 'valence': 0.762, 'tempo': 184.086}, '7gpy7sfWPNuOKmUNs3XQYE': {'name': 'Carry On', 'artist_id': '5nCi3BB41mBaMH9gfr6Su0', 'artist_name': 'fun.', 'album_name': 'Some Nights (Spotify Exclusive)', 'track_number': 4, 'duration_ms': 278373, 'popularity': 63, 'danceability': 0.388, 'energy': 0.694, 'loudness': -5.769, 'speechiness': 0.0735, 'acousticness': 0.118, 'instrumentalness': 0.000293, 'liveness': 0.082, 'valence': 0.383, 'tempo': 145.434}, '53c9tTEHXWL5GkYNalbXZ3': {'name': "C'mon", 'artist_id': '20JZFwl6HVl6yg8a4H3ZqK', 'artist_name': 'Panic! At The Disco', 'album_name': "C'mon", 'track_number': 1, 'duration_ms': 214430, 'popularity': 60, 'danceability': 0.38, 'energy': 0.489, 'loudness': -7.027, 'speechiness': 0.0362, 'acousticness': 0.0351, 'instrumentalness': 0.00243, 'liveness': 0.081, 'valence': 0.35, 'tempo': 127.097}, '4orHVYvdG5v4G4bmp2Lwdg': {'name': 'Sight Of The Sun', 'artist_id': '5nCi3BB41mBaMH9gfr6Su0', 'artist_name': 'fun.', 'album_name': 'Sight Of The Sun', 'track_number': 1, 'duration_ms': 210373, 'popularity': 59, 'danceability': 0.626, 'energy': 0.703, 'loudness': -5.247, 'speechiness': 0.0306, 'acousticness': 0.0275, 'instrumentalness': 1.66e-06, 'liveness': 0.0903, 'valence': 0.521, 'tempo': 92.054}, '5tbz0VnVwfF3jubvjDGdHo': {'name': 'We Are Young - feat. Janelle Mone [Acoustic]', 'artist_id': '5nCi3BB41mBaMH9gfr6Su0', 'artist_name': 'fun.', 'album_name': 'Some Nights (Spotify Exclusive)', 'track_number': 12, 'duration_ms': 272546, 'popularity': 54, 'danceability': 0.445, 'energy': 0.296, 'loudness': -7.091, 'speechiness': 0.0419, 'acousticness': 0.815, 'instrumentalness': 0, 'liveness': 0.0562, 'valence': 0.283, 'tempo': 169.331}, '1Y5wYXgX9dHwSKZdQNHEhV': {'name': 'The Gambler', 'artist_id': '5nCi3BB41mBaMH9gfr6Su0', 'artist_name': 'fun.', 'album_name': 'Aim and Ignite (Deluxe Version)', 'track_number': 9, 'duration_ms': 251266, 'popularity': 50, 'danceability': 0.612, 'energy': 0.297, 'loudness': -7.571, 'speechiness': 0.0308, 'acousticness': 0.941, 'instrumentalness': 1.45e-06, 'liveness': 0.109, 'valence': 0.447, 'tempo': 99.937}, '5QbQ5iAebksB5Wj5BPazNX': {'name': 'Why Am I the One', 'artist_id': '5nCi3BB41mBaMH9gfr6Su0', 'artist_name': 'fun.', 'album_name': 'Some Nights (Spotify Exclusive)', 'track_number': 6, 'duration_ms': 286706, 'popularity': 49, 'danceability': 0.408, 'energy': 0.499, 'loudness': -7.16, 'speechiness': 0.0547, 'acousticness': 0.44, 'instrumentalness': 4.04e-06, 'liveness': 0.595, 'valence': 0.486, 'tempo': 82.157}, '1TQyRzRnGJflBhUHAwtk1x': {'name': 'All The Pretty Girls', 'artist_id': '5nCi3BB41mBaMH9gfr6Su0', 'artist_name': 'fun.', 'album_name': 'Aim and Ignite (Deluxe Version)', 'track_number': 3, 'duration_ms': 202893, 'popularity': 48, 'danceability': 0.646, 'energy': 0.787, 'loudness': -4.654, 'speechiness': 0.0602, 'acousticness': 0.258, 'instrumentalness': 0, 'liveness': 0.199, 'valence': 0.782, 'tempo': 131.036}, '3xsMa7CA11iRjhmIdEy2N6': {'name': 'All Alright', 'artist_id': '5nCi3BB41mBaMH9gfr6Su0', 'artist_name': 'fun.', 'album_name': 'Some Nights (Spotify Exclusive)', 'track_number': 8, 'duration_ms': 237466, 'popularity': 47, 'danceability': 0.321, 'energy': 0.786, 'loudness': -4.137, 'speechiness': 0.0516, 'acousticness': 0.00158, 'instrumentalness': 0, 'liveness': 0.105, 'valence': 0.371, 'tempo': 107.3}, '2gYiCTytrSRtuaHP1Nac6u': {'name': 'Fast', 'artist_id': '0BvkDsjIUla7X0k6CSWh1I', 'artist_name': 'Luke Bryan', 'album_name': 'Kill The Lights (Deluxe)', 'track_number': 6, 'duration_ms': 206213, 'popularity': 76, 'danceability': 0.548, 'energy': 0.898, 'loudness': -2.561, 'speechiness': 0.0459, 'acousticness': 0.225, 'instrumentalness': 0, 'liveness': 0.1, 'valence': 0.596, 'tempo': 145.953}, '03fT3OHB9KyMtGMt2zwqCT': {'name': 'Play It Again', 'artist_id': '0BvkDsjIUla7X0k6CSWh1I', 'artist_name': 'Luke Bryan', 'album_name': 'Crash My Party', 'track_number': 9, 'duration_ms': 226866, 'popularity': 75, 'danceability': 0.51, 'energy': 0.898, 'loudness': -3.15, 'speechiness': 0.0696, 'acousticness': 0.0832, 'instrumentalness': 0, 'liveness': 0.071, 'valence': 0.595, 'tempo': 144.056}, '0dbzWSYpMcRtwjI1S7Pkql': {'name': "Huntin', Fishin' And Lovin' Every Day", 'artist_id': '0BvkDsjIUla7X0k6CSWh1I', 'artist_name': 'Luke Bryan', 'album_name': 'Kill The Lights (Deluxe)', 'track_number': 12, 'duration_ms': 278613, 'popularity': 74, 'danceability': 0.546, 'energy': 0.805, 'loudness': -4.251, 'speechiness': 0.0348, 'acousticness': 0.125, 'instrumentalness': 9.27e-06, 'liveness': 0.148, 'valence': 0.386, 'tempo': 77.029}, '5XFu5S1vBY7sNHlheCapOz': {'name': 'Strip It Down', 'artist_id': '0BvkDsjIUla7X0k6CSWh1I', 'artist_name': 'Luke Bryan', 'album_name': 'Kill The Lights (Deluxe)', 'track_number': 3, 'duration_ms': 241613, 'popularity': 71, 'danceability': 0.629, 'energy': 0.878, 'loudness': -3.535, 'speechiness': 0.0443, 'acousticness': 0.392, 'instrumentalness': 0, 'liveness': 0.0899, 'valence': 0.721, 'tempo': 137.989}, '5HGibWoxnkYSkl6mHmAlOE': {'name': "That's My Kind Of Night", 'artist_id': '0BvkDsjIUla7X0k6CSWh1I', 'artist_name': 'Luke Bryan', 'album_name': 'Crash My Party', 'track_number': 1, 'duration_ms': 190186, 'popularity': 71, 'danceability': 0.66, 'energy': 0.754, 'loudness': -2.84, 'speechiness': 0.051, 'acousticness': 0.0626, 'instrumentalness': 0, 'liveness': 0.1, 'valence': 0.889, 'tempo': 110.02}, '0yD66650JxhqKbW76C2qCo': {'name': 'Country Girl (Shake It For Me)', 'artist_id': '0BvkDsjIUla7X0k6CSWh1I', 'artist_name': 'Luke Bryan', 'album_name': 'Tailgates & Tanlines', 'track_number': 1, 'duration_ms': 225560, 'popularity': 70, 'danceability': 0.645, 'energy': 0.904, 'loudness': -4.532, 'speechiness': 0.0462, 'acousticness': 0.0293, 'instrumentalness': 0, 'liveness': 0.0834, 'valence': 0.66, 'tempo': 105.97}, '3b7CDTKB0SRTmQ6ytYi5vZ': {'name': 'Drunk On You', 'artist_id': '0BvkDsjIUla7X0k6CSWh1I', 'artist_name': 'Luke Bryan', 'album_name': 'Tailgates & Tanlines', 'track_number': 3, 'duration_ms': 213546, 'popularity': 69, 'danceability': 0.558, 'energy': 0.872, 'loudness': -4.401, 'speechiness': 0.0449, 'acousticness': 0.178, 'instrumentalness': 0, 'liveness': 0.173, 'valence': 0.462, 'tempo': 143.971}, '6qoH2pKeEibNUG1pnJIjmZ': {'name': 'Move', 'artist_id': '0BvkDsjIUla7X0k6CSWh1I', 'artist_name': 'Luke Bryan', 'album_name': 'Kill The Lights (Deluxe)', 'track_number': 7, 'duration_ms': 227413, 'popularity': 69, 'danceability': 0.569, 'energy': 0.946, 'loudness': -0.698, 'speechiness': 0.0808, 'acousticness': 0.00873, 'instrumentalness': 0, 'liveness': 0.0903, 'valence': 0.763, 'tempo': 103.991}, '5g15o2Sm55Hn9ShK5yEXgp': {'name': 'Kick The Dust Up', 'artist_id': '0BvkDsjIUla7X0k6CSWh1I', 'artist_name': 'Luke Bryan', 'album_name': 'Kill The Lights (Deluxe)', 'track_number': 1, 'duration_ms': 190586, 'popularity': 69, 'danceability': 0.596, 'energy': 0.855, 'loudness': -2.255, 'speechiness': 0.0474, 'acousticness': 0.197, 'instrumentalness': 0, 'liveness': 0.11, 'valence': 0.797, 'tempo': 172.082}, '0cV4xwUA4ue2deqq4CZFko': {'name': "I Don't Want This Night to End", 'artist_id': '0BvkDsjIUla7X0k6CSWh1I', 'artist_name': 'Luke Bryan', 'album_name': 'Tailgates & Tanlines', 'track_number': 5, 'duration_ms': 219973, 'popularity': 68, 'danceability': 0.616, 'energy': 0.728, 'loudness': -4.02, 'speechiness': 0.0278, 'acousticness': 0.0275, 'instrumentalness': 0, 'liveness': 0.228, 'valence': 0.375, 'tempo': 111.934}, '0GqfyQKzlUvzfL6rF7LcVg': {'name': 'American Dream', 'artist_id': '3zt4I5TLIb0Z9RigaiHe5G', 'artist_name': 'Cereus Bright', 'album_name': 'Excuses', 'track_number': 4, 'duration_ms': 227946, 'popularity': 20, 'danceability': 0.705, 'energy': 0.504, 'loudness': -11.33, 'speechiness': 0.0323, 'acousticness': 0.18, 'instrumentalness': 0.00393, 'liveness': 0.126, 'valence': 0.186, 'tempo': 133.077}, '38h1mljyMeayECUCx95GPh': {'name': 'River Run', 'artist_id': '3zt4I5TLIb0Z9RigaiHe5G', 'artist_name': 'Cereus Bright', 'album_name': 'Excuses', 'track_number': 2, 'duration_ms': 257640, 'popularity': 29, 'danceability': 0.574, 'energy': 0.592, 'loudness': -10.735, 'speechiness': 0.0752, 'acousticness': 0.175, 'instrumentalness': 0.000334, 'liveness': 0.14, 'valence': 0.21, 'tempo': 159.866}, '5pQ1e9moalBVW4IbUBZ1Rx': {'name': 'Stella - Audiotree Live Version', 'artist_id': '3zt4I5TLIb0Z9RigaiHe5G', 'artist_name': 'Cereus Bright', 'album_name': 'Cereus Bright on Audiotree Live', 'track_number': 4, 'duration_ms': 209278, 'popularity': 37, 'danceability': 0.666, 'energy': 0.674, 'loudness': -7.471, 'speechiness': 0.0322, 'acousticness': 0.447, 'instrumentalness': 0.0925, 'liveness': 0.143, 'valence': 0.635, 'tempo': 110.438}, '06WH4YIbuVcRNEQdiYIj3U': {'name': 'Hindenburg', 'artist_id': '3zt4I5TLIb0Z9RigaiHe5G', 'artist_name': 'Cereus Bright', 'album_name': 'Excuses', 'track_number': 8, 'duration_ms': 262453, 'popularity': 37, 'danceability': 0.539, 'energy': 0.291, 'loudness': -13.534, 'speechiness': 0.0294, 'acousticness': 0.533, 'instrumentalness': 0.119, 'liveness': 0.243, 'valence': 0.091, 'tempo': 159.826}, '2UZG2fnQRvm7mLblQDwrTl': {'name': 'Cereus Bright', 'artist_id': '3zt4I5TLIb0Z9RigaiHe5G', 'artist_name': 'Cereus Bright', 'album_name': 'Excuses', 'track_number': 11, 'duration_ms': 291666, 'popularity': 35, 'danceability': 0.575, 'energy': 0.124, 'loudness': -16.188, 'speechiness': 0.0269, 'acousticness': 0.875, 'instrumentalness': 0.00178, 'liveness': 0.118, 'valence': 0.15, 'tempo': 95.938}, '240SHxowlaqE1jvVe6QEgA': {'name': 'Cereus Bright - Audiotree Live Version', 'artist_id': '3zt4I5TLIb0Z9RigaiHe5G', 'artist_name': 'Cereus Bright', 'album_name': 'Cereus Bright on Audiotree Live', 'track_number': 5, 'duration_ms': 274918, 'popularity': 32, 'danceability': 0.541, 'energy': 0.0738, 'loudness': -17.774, 'speechiness': 0.0281, 'acousticness': 0.834, 'instrumentalness': 0.0119, 'liveness': 0.114, 'valence': 0.0495, 'tempo': 94.095}, '3IHGv6PVQ6qmLa6OML44Xa': {'name': 'Chattanooga', 'artist_id': '3zt4I5TLIb0Z9RigaiHe5G', 'artist_name': 'Cereus Bright', 'album_name': 'Happier Than Me', 'track_number': 4, 'duration_ms': 240573, 'popularity': 30, 'danceability': 0.525, 'energy': 0.574, 'loudness': -8.954, 'speechiness': 0.0389, 'acousticness': 0.0158, 'instrumentalness': 2.05e-06, 'liveness': 0.142, 'valence': 0.459, 'tempo': 97.723}, '5cEACMcaVwmbFTaG8cjYki': {'name': 'Happier Than Me', 'artist_id': '3zt4I5TLIb0Z9RigaiHe5G', 'artist_name': 'Cereus Bright', 'album_name': 'Happier Than Me', 'track_number': 1, 'duration_ms': 184466, 'popularity': 2, 'danceability': 0.596, 'energy': 0.671, 'loudness': -8.527, 'speechiness': 0.0336, 'acousticness': 0.568, 'instrumentalness': 0.00015, 'liveness': 0.0865, 'valence': 0.386, 'tempo': 94.992}, '1hvuxAwZwZDCsB8HnJ06bu': {'name': 'Claustrophobic', 'artist_id': '3zt4I5TLIb0Z9RigaiHe5G', 'artist_name': 'Cereus Bright', 'album_name': 'Excuses', 'track_number': 1, 'duration_ms': 197186, 'popularity': 28, 'danceability': 0.666, 'energy': 0.407, 'loudness': -10.055, 'speechiness': 0.0347, 'acousticness': 0.669, 'instrumentalness': 0, 'liveness': 0.147, 'valence': 0.269, 'tempo': 141.981}, '4TTV7EcfroSLWzXRY6gLv6': {'name': 'Alexander Hamilton', 'artist_id': '3cR4rhS2hBWqI7rJEBacvN', 'artist_name': 'Leslie Odom Jr.', 'album_name': 'Hamilton (Original Broadway Cast Recording)', 'track_number': 1, 'duration_ms': 236737, 'popularity': 73, 'danceability': 0.609, 'energy': 0.435, 'loudness': -7.862, 'speechiness': 0.284, 'acousticness': 0.524, 'instrumentalness': 0, 'liveness': 0.118, 'valence': 0.557, 'tempo': 131.998}, '4cxvludVmQxryrnx1m9FqL': {'name': 'My Shot', 'artist_id': '4aXXDj9aZnlshx7mzj3W1N', 'artist_name': 'Lin-Manuel Miranda', 'album_name': 'Hamilton (Original Broadway Cast Recording)', 'track_number': 3, 'duration_ms': 333154, 'popularity': 72, 'danceability': 0.829, 'energy': 0.649, 'loudness': -6.764, 'speechiness': 0.317, 'acousticness': 0.15, 'instrumentalness': 0, 'liveness': 0.0904, 'valence': 0.588, 'tempo': 90.936}, '71X7bPDljJHrmEGYCe7kQ8': {'name': 'The Schuyler Sisters', 'artist_id': '5VJN4jB6PqqEg4kJiAj6Eu', 'artist_name': 'Rene Elise Goldsberry', 'album_name': 'Hamilton (Original Broadway Cast Recording)', 'track_number': 5, 'duration_ms': 186542, 'popularity': 71, 'danceability': 0.74, 'energy': 0.727, 'loudness': -6.253, 'speechiness': 0.278, 'acousticness': 0.186, 'instrumentalness': 0, 'liveness': 0.627, 'valence': 0.762, 'tempo': 101.408}, '6dr7ekfhlbquvsVY8D7gyk': {'name': 'Aaron Burr, Sir', 'artist_id': '4aXXDj9aZnlshx7mzj3W1N', 'artist_name': 'Lin-Manuel Miranda', 'album_name': 'Hamilton (Original Broadway Cast Recording)', 'track_number': 2, 'duration_ms': 156630, 'popularity': 71, 'danceability': 0.646, 'energy': 0.438, 'loudness': -10.837, 'speechiness': 0.808, 'acousticness': 0.271, 'instrumentalness': 0, 'liveness': 0.0945, 'valence': 0.517, 'tempo': 160.433}, '7EqpEBPOohgk7NnKvBGFWo': {'name': 'Wait For It', 'artist_id': '3cR4rhS2hBWqI7rJEBacvN', 'artist_name': 'Leslie Odom Jr.', 'album_name': 'Hamilton (Original Broadway Cast Recording)', 'track_number': 13, 'duration_ms': 193749, 'popularity': 70, 'danceability': 0.561, 'energy': 0.474, 'loudness': -9.638, 'speechiness': 0.155, 'acousticness': 0.125, 'instrumentalness': 5.07e-06, 'liveness': 0.0922, 'valence': 0.523, 'tempo': 86.897}, '7m9XR7FquXLP1FewdAcNS9': {'name': 'Guns and Ships', 'artist_id': '3cR4rhS2hBWqI7rJEBacvN', 'artist_name': 'Leslie Odom Jr.', 'album_name': 'Hamilton (Original Broadway Cast Recording)', 'track_number': 18, 'duration_ms': 127578, 'popularity': 70, 'danceability': 0.715, 'energy': 0.666, 'loudness': -6.914, 'speechiness': 0.322, 'acousticness': 0.399, 'instrumentalness': 0, 'liveness': 0.0844, 'valence': 0.398, 'tempo': 137.906}, '7qfoq1JFKBUEIvhqOHzuqX': {'name': 'Non-Stop', 'artist_id': '3cR4rhS2hBWqI7rJEBacvN', 'artist_name': 'Leslie Odom Jr.', 'album_name': 'Hamilton (Original Broadway Cast Recording)', 'track_number': 23, 'duration_ms': 385438, 'popularity': 69, 'danceability': 0.772, 'energy': 0.482, 'loudness': -9.529, 'speechiness': 0.351, 'acousticness': 0.211, 'instrumentalness': 0, 'liveness': 0.223, 'valence': 0.446, 'tempo': 92.017}, '3nJYcY9yvKP8Oi2Ml8brXt': {'name': 'Right Hand Man', 'artist_id': '6sLwRSXSUF5JTUnQaFenyj', 'artist_name': 'Christopher Jackson', 'album_name': 'Hamilton (Original Broadway Cast Recording)', 'track_number': 8, 'duration_ms': 321696, 'popularity': 69, 'danceability': 0.68, 'energy': 0.413, 'loudness': -9.41, 'speechiness': 0.492, 'acousticness': 0.177, 'instrumentalness': 0, 'liveness': 0.205, 'valence': 0.386, 'tempo': 158.58}, '2sEq2rC3ynYsT49x7utWnd': {'name': 'Dear Theodosia', 'artist_id': '3cR4rhS2hBWqI7rJEBacvN', 'artist_name': 'Leslie Odom Jr.', 'album_name': 'Hamilton (Original Broadway Cast Recording)', 'track_number': 22, 'duration_ms': 184004, 'popularity': 68, 'danceability': 0.601, 'energy': 0.222, 'loudness': -10.485, 'speechiness': 0.0303, 'acousticness': 0.906, 'instrumentalness': 4.11e-05, 'liveness': 0.0723, 'valence': 0.249, 'tempo': 106.754}, '2yBMVrq96wb9OHbMdBs0lF': {'name': "A Winter's Ball", 'artist_id': '3cR4rhS2hBWqI7rJEBacvN', 'artist_name': 'Leslie Odom Jr.', 'album_name': 'Hamilton (Original Broadway Cast Recording)', 'track_number': 9, 'duration_ms': 69900, 'popularity': 68, 'danceability': 0.856, 'energy': 0.327, 'loudness': -10.834, 'speechiness': 0.452, 'acousticness': 0.41, 'instrumentalness': 0, 'liveness': 0.0889, 'valence': 0.715, 'tempo': 131.352}, '2uhEKg8kIzpdvz4gyy6x8W': {'name': 'Only Love', 'artist_id': '5schNIzWdI9gJ1QRK8SBnc', 'artist_name': 'Ben Howard', 'album_name': 'Every Kingdom', 'track_number': 5, 'duration_ms': 249173, 'popularity': 70, 'danceability': 0.486, 'energy': 0.492, 'loudness': -9.918, 'speechiness': 0.154, 'acousticness': 0.344, 'instrumentalness': 0.00189, 'liveness': 0.117, 'valence': 0.332, 'tempo': 80.444}, '3CAX47TnPqTujLIQTw8nwI': {'name': 'Old Pine', 'artist_id': '5schNIzWdI9gJ1QRK8SBnc', 'artist_name': 'Ben Howard', 'album_name': 'Every Kingdom', 'track_number': 1, 'duration_ms': 328506, 'popularity': 66, 'danceability': 0.413, 'energy': 0.359, 'loudness': -10.843, 'speechiness': 0.0321, 'acousticness': 0.472, 'instrumentalness': 0.116, 'liveness': 0.17, 'valence': 0.219, 'tempo': 129.664}, '5fpEDGQX0Ah3utGnFYulQZ': {'name': 'Keep Your Head Up', 'artist_id': '5schNIzWdI9gJ1QRK8SBnc', 'artist_name': 'Ben Howard', 'album_name': 'Every Kingdom', 'track_number': 7, 'duration_ms': 264546, 'popularity': 62, 'danceability': 0.438, 'energy': 0.566, 'loudness': -9.029, 'speechiness': 0.0352, 'acousticness': 0.476, 'instrumentalness': 9.48e-06, 'liveness': 0.111, 'valence': 0.401, 'tempo': 158.561}, '7gYwIAHB6VxzLJFSZMMv8i': {'name': 'I Forget Where We Were', 'artist_id': '5schNIzWdI9gJ1QRK8SBnc', 'artist_name': 'Ben Howard', 'album_name': 'I Forget Where We Were', 'track_number': 3, 'duration_ms': 281213, 'popularity': 59, 'danceability': 0.299, 'energy': 0.47, 'loudness': -9.542, 'speechiness': 0.0346, 'acousticness': 0.437, 'instrumentalness': 0.176, 'liveness': 0.0919, 'valence': 0.184, 'tempo': 113.506}, '4qyfir5Yr7nfo05g6cyFMT': {'name': 'Promise', 'artist_id': '5schNIzWdI9gJ1QRK8SBnc', 'artist_name': 'Ben Howard', 'album_name': 'Every Kingdom', 'track_number': 10, 'duration_ms': 384080, 'popularity': 60, 'danceability': 0.365, 'energy': 0.181, 'loudness': -15.693, 'speechiness': 0.0392, 'acousticness': 0.88, 'instrumentalness': 0.452, 'liveness': 0.363, 'valence': 0.187, 'tempo': 158.088}, '2Viw81MZJPsOjODAz4A5nW': {'name': 'She Treats Me Well', 'artist_id': '5schNIzWdI9gJ1QRK8SBnc', 'artist_name': 'Ben Howard', 'album_name': 'I Forget Where We Were', 'track_number': 5, 'duration_ms': 317933, 'popularity': 53, 'danceability': 0.62, 'energy': 0.492, 'loudness': -12.618, 'speechiness': 0.0385, 'acousticness': 0.376, 'instrumentalness': 0.197, 'liveness': 0.0739, 'valence': 0.61, 'tempo': 79.619}, '5RySo0AAUR0reTHSCvb6HC': {'name': 'Small Things', 'artist_id': '5schNIzWdI9gJ1QRK8SBnc', 'artist_name': 'Ben Howard', 'album_name': 'I Forget Where We Were', 'track_number': 1, 'duration_ms': 343786, 'popularity': 56, 'danceability': 0.393, 'energy': 0.592, 'loudness': -9.782, 'speechiness': 0.0411, 'acousticness': 0.784, 'instrumentalness': 0.278, 'liveness': 0.116, 'valence': 0.164, 'tempo': 135.696}, '6yPuQr6vjZ7tJ4oq1PEXle': {'name': 'In Dreams', 'artist_id': '5schNIzWdI9gJ1QRK8SBnc', 'artist_name': 'Ben Howard', 'album_name': 'I Forget Where We Were', 'track_number': 4, 'duration_ms': 213440, 'popularity': 56, 'danceability': 0.501, 'energy': 0.594, 'loudness': -13.457, 'speechiness': 0.0395, 'acousticness': 0.613, 'instrumentalness': 0.579, 'liveness': 0.136, 'valence': 0.259, 'tempo': 126.795}, '4dr5sJ1p6mdNpK3fIUz8vR': {'name': 'Oats In The Water', 'artist_id': '5schNIzWdI9gJ1QRK8SBnc', 'artist_name': 'Ben Howard', 'album_name': 'The Burgh Island EP', 'track_number': 2, 'duration_ms': 299381, 'popularity': 54, 'danceability': 0.359, 'energy': 0.47, 'loudness': -9.471, 'speechiness': 0.0286, 'acousticness': 0.29, 'instrumentalness': 0.423, 'liveness': 0.189, 'valence': 0.0932, 'tempo': 130.812}, '2omeRL5Clxg3y8g2kv2enS': {'name': 'These Waters', 'artist_id': '5schNIzWdI9gJ1QRK8SBnc', 'artist_name': 'Ben Howard', 'album_name': 'Every Kingdom (Deluxe Version)', 'track_number': 12, 'duration_ms': 248000, 'popularity': 56, 'danceability': 0.425, 'energy': 0.46, 'loudness': -9.983, 'speechiness': 0.0326, 'acousticness': 0.292, 'instrumentalness': 0.000445, 'liveness': 0.115, 'valence': 0.314, 'tempo': 143.947}, '2hRBqxdkYuFySfyEkcsPOp': {'name': 'Messengers', 'artist_id': '0GklSybv01PPje5GlXFq2i', 'artist_name': 'Jared & The Mill', 'album_name': 'Life We Chose', 'track_number': 4, 'duration_ms': 277613, 'popularity': 47, 'danceability': 0.494, 'energy': 0.47, 'loudness': -7.413, 'speechiness': 0.0313, 'acousticness': 0.739, 'instrumentalness': 0, 'liveness': 0.0774, 'valence': 0.175, 'tempo': 134.334}, '1Gn1Yzgdk0RFq3H0lePlMB': {'name': 'Keep Me Going', 'artist_id': '0GklSybv01PPje5GlXFq2i', 'artist_name': 'Jared & The Mill', 'album_name': 'Keep Me Going', 'track_number': 1, 'duration_ms': 208953, 'popularity': 41, 'danceability': 0.366, 'energy': 0.688, 'loudness': -6.84, 'speechiness': 0.0368, 'acousticness': 0.0137, 'instrumentalness': 2.3e-05, 'liveness': 0.114, 'valence': 0.455, 'tempo': 169.493}, '2qNIaXkc0wlR7IIN5l7KtL': {'name': 'Life We Chose', 'artist_id': '0GklSybv01PPje5GlXFq2i', 'artist_name': 'Jared & The Mill', 'album_name': 'Life We Chose', 'track_number': 6, 'duration_ms': 342013, 'popularity': 40, 'danceability': 0.533, 'energy': 0.582, 'loudness': -6.556, 'speechiness': 0.0304, 'acousticness': 0.765, 'instrumentalness': 0, 'liveness': 0.0859, 'valence': 0.247, 'tempo': 141.87}, '6ewlMqeK1LuFOmNG9x7tma': {'name': 'Song for a Girl', 'artist_id': '0GklSybv01PPje5GlXFq2i', 'artist_name': 'Jared & The Mill', 'album_name': 'Orme Dugas', 'track_number': 5, 'duration_ms': 246557, 'popularity': 39, 'danceability': 0.527, 'energy': 0.332, 'loudness': -11.367, 'speechiness': 0.0329, 'acousticness': 0.844, 'instrumentalness': 0.000135, 'liveness': 0.111, 'valence': 0.291, 'tempo': 87.162}, '5vqjiKUSu9Y9GmUkiUXrj7': {'name': 'Keep Me Going - Audiotree Live Version', 'artist_id': '0GklSybv01PPje5GlXFq2i', 'artist_name': 'Jared & The Mill', 'album_name': 'Jared & The Mill on Audiotree Live', 'track_number': 4, 'duration_ms': 209082, 'popularity': 35, 'danceability': 0.27, 'energy': 0.648, 'loudness': -7.883, 'speechiness': 0.0426, 'acousticness': 0.168, 'instrumentalness': 8.75e-05, 'liveness': 0.17, 'valence': 0.496, 'tempo': 164.353}, '1T0uOwBt4KRVOC1cgbmlNa': {'name': 'Crawl', 'artist_id': '0GklSybv01PPje5GlXFq2i', 'artist_name': 'Jared & The Mill', 'album_name': 'Life We Chose', 'track_number': 1, 'duration_ms': 256333, 'popularity': 32, 'danceability': 0.482, 'energy': 0.558, 'loudness': -6.962, 'speechiness': 0.0312, 'acousticness': 0.429, 'instrumentalness': 5.71e-05, 'liveness': 0.122, 'valence': 0.364, 'tempo': 150.015}, '5dKKgYqiuLLC5xG8Sm9kVr': {'name': 'Still Alone', 'artist_id': '0GklSybv01PPje5GlXFq2i', 'artist_name': 'Jared & The Mill', 'album_name': 'Orme Dugas', 'track_number': 3, 'duration_ms': 228520, 'popularity': 31, 'danceability': 0.562, 'energy': 0.776, 'loudness': -6.789, 'speechiness': 0.0319, 'acousticness': 0.00345, 'instrumentalness': 0.0161, 'liveness': 0.335, 'valence': 0.829, 'tempo': 150.044}, '5kYFOIJ1CUnYJhj9JAqQHF': {'name': 'She', 'artist_id': '0GklSybv01PPje5GlXFq2i', 'artist_name': 'Jared & The Mill', 'album_name': 'Life We Chose', 'track_number': 3, 'duration_ms': 276280, 'popularity': 31, 'danceability': 0.546, 'energy': 0.487, 'loudness': -9.066, 'speechiness': 0.0378, 'acousticness': 0.794, 'instrumentalness': 0, 'liveness': 0.0944, 'valence': 0.326, 'tempo': 86.03}, '39EWzCLWBfkwkZKmJSakjX': {'name': 'Hold On', 'artist_id': '0GklSybv01PPje5GlXFq2i', 'artist_name': 'Jared & The Mill', 'album_name': 'Life We Chose', 'track_number': 2, 'duration_ms': 232093, 'popularity': 30, 'danceability': 0.555, 'energy': 0.594, 'loudness': -6.488, 'speechiness': 0.0294, 'acousticness': 0.444, 'instrumentalness': 0, 'liveness': 0.0665, 'valence': 0.626, 'tempo': 92.105}, '4vb4mFvYsr2h6enhjJsq9Y': {'name': 'Water Under the Bridge', 'artist_id': '4dpARuHxo51G3z768sgnrY', 'artist_name': 'Adele', 'album_name': '25', 'track_number': 6, 'duration_ms': 240426, 'popularity': 79, 'danceability': 0.596, 'energy': 0.838, 'loudness': -6.52, 'speechiness': 0.0704, 'acousticness': 0.0189, 'instrumentalness': 1.54e-05, 'liveness': 0.108, 'valence': 0.479, 'tempo': 94.982}, '4kflIGfjdZJW4ot2ioixTB': {'name': 'Someone Like You', 'artist_id': '4dpARuHxo51G3z768sgnrY', 'artist_name': 'Adele', 'album_name': '21', 'track_number': 11, 'duration_ms': 285040, 'popularity': 77, 'danceability': 0.559, 'energy': 0.33, 'loudness': -8.251, 'speechiness': 0.0285, 'acousticness': 0.892, 'instrumentalness': 0, 'liveness': 0.0975, 'valence': 0.28, 'tempo': 135.109}, '4BHzQ9C00ceJxfG16AlNWb': {'name': 'Send My Love (To Your New Lover)', 'artist_id': '4dpARuHxo51G3z768sgnrY', 'artist_name': 'Adele', 'album_name': '25', 'track_number': 2, 'duration_ms': 223080, 'popularity': 76, 'danceability': 0.69, 'energy': 0.524, 'loudness': -8.39, 'speechiness': 0.103, 'acousticness': 0.0415, 'instrumentalness': 3.16e-06, 'liveness': 0.17, 'valence': 0.561, 'tempo': 164.023}, '7rPLZ8Krm6CZIbraFUlnWZ': {'name': 'Make You Feel My Love', 'artist_id': '4dpARuHxo51G3z768sgnrY', 'artist_name': 'Adele', 'album_name': '19', 'track_number': 9, 'duration_ms': 212040, 'popularity': 70, 'danceability': 0.325, 'energy': 0.18, 'loudness': -10.647, 'speechiness': 0.0311, 'acousticness': 0.91, 'instrumentalness': 0.000633, 'liveness': 0.113, 'valence': 0.0928, 'tempo': 72.416}, '7IWkJwX9C0J7tHurTD7ViL': {'name': 'When We Were Young', 'artist_id': '4dpARuHxo51G3z768sgnrY', 'artist_name': 'Adele', 'album_name': '25', 'track_number': 4, 'duration_ms': 290906, 'popularity': 73, 'danceability': 0.381, 'energy': 0.594, 'loudness': -5.97, 'speechiness': 0.0486, 'acousticness': 0.348, 'instrumentalness': 0, 'liveness': 0.0925, 'valence': 0.275, 'tempo': 143.86}, '4sPmO7WMQUAf45kwMOtONw': {'name': 'Hello', 'artist_id': '4dpARuHxo51G3z768sgnrY', 'artist_name': 'Adele', 'album_name': '25', 'track_number': 1, 'duration_ms': 295493, 'popularity': 74, 'danceability': 0.481, 'energy': 0.451, 'loudness': -6.095, 'speechiness': 0.0347, 'acousticness': 0.336, 'instrumentalness': 0, 'liveness': 0.0872, 'valence': 0.287, 'tempo': 157.966}, '2GblQ918RbkOs4Yo1Rpkcj': {'name': 'Rolling In The Deep', 'artist_id': '4dpARuHxo51G3z768sgnrY', 'artist_name': 'Adele', 'album_name': 'Pay Close Attention : XL Recordings', 'track_number': 18, 'duration_ms': 228141, 'popularity': 60, 'danceability': 0.727, 'energy': 0.76, 'loudness': -5.114, 'speechiness': 0.0297, 'acousticness': 0.13, 'instrumentalness': 0, 'liveness': 0.0584, 'valence': 0.517, 'tempo': 104.941}, '3CKCZ9pfwAfoMZlMncA1Nc': {'name': 'Set Fire to the Rain', 'artist_id': '4dpARuHxo51G3z768sgnrY', 'artist_name': 'Adele', 'album_name': '21', 'track_number': 5, 'duration_ms': 241693, 'popularity': 72, 'danceability': 0.61, 'energy': 0.683, 'loudness': -3.879, 'speechiness': 0.0253, 'acousticness': 0.00382, 'instrumentalness': 1.79e-06, 'liveness': 0.125, 'valence': 0.466, 'tempo': 108.003}, '1wMALZpuqAy7amQsFBWQ8m': {'name': 'All I Ask', 'artist_id': '4dpARuHxo51G3z768sgnrY', 'artist_name': 'Adele', 'album_name': '25', 'track_number': 10, 'duration_ms': 271800, 'popularity': 70, 'danceability': 0.587, 'energy': 0.283, 'loudness': -5.473, 'speechiness': 0.0279, 'acousticness': 0.882, 'instrumentalness': 0, 'liveness': 0.149, 'valence': 0.339, 'tempo': 141.961}, '7GgQi7JTG4b6J4iEF4RTjF': {'name': 'Remedy', 'artist_id': '4dpARuHxo51G3z768sgnrY', 'artist_name': 'Adele', 'album_name': '25', 'track_number': 5, 'duration_ms': 245426, 'popularity': 67, 'danceability': 0.396, 'energy': 0.305, 'loudness': -6.481, 'speechiness': 0.0387, 'acousticness': 0.891, 'instrumentalness': 0, 'liveness': 0.169, 'valence': 0.251, 'tempo': 165.398}, '4n0xztUAbHPUV8G3NQvF30': {'name': 'How Not To', 'artist_id': '7z5WFjZAIYejWy0NI5lv4T', 'artist_name': 'Dan + Shay', 'album_name': 'Obsessed', 'track_number': 5, 'duration_ms': 192000, 'popularity': 76, 'danceability': 0.501, 'energy': 0.836, 'loudness': -3.587, 'speechiness': 0.0491, 'acousticness': 0.208, 'instrumentalness': 0, 'liveness': 0.152, 'valence': 0.627, 'tempo': 159.863}, '0lQJBl9YEsoMtE8D4yTE9g': {'name': 'From the Ground Up', 'artist_id': '7z5WFjZAIYejWy0NI5lv4T', 'artist_name': 'Dan + Shay', 'album_name': 'Obsessed', 'track_number': 3, 'duration_ms': 253933, 'popularity': 64, 'danceability': 0.281, 'energy': 0.58, 'loudness': -5.967, 'speechiness': 0.0323, 'acousticness': 0.333, 'instrumentalness': 0, 'liveness': 0.122, 'valence': 0.281, 'tempo': 151.568}, '4W38RXuQNuoTSwVsQA1OGC': {'name': "Nothin' Like You", 'artist_id': '7z5WFjZAIYejWy0NI5lv4T', 'artist_name': 'Dan + Shay', 'album_name': 'Where It All Began', 'track_number': 7, 'duration_ms': 186253, 'popularity': 68, 'danceability': 0.589, 'energy': 0.704, 'loudness': -4.772, 'speechiness': 0.0303, 'acousticness': 0.151, 'instrumentalness': 0, 'liveness': 0.067, 'valence': 0.429, 'tempo': 84.956}, '16DRIwIBIgZdAgpp0vLh5q': {'name': 'When I Pray For You', 'artist_id': '7z5WFjZAIYejWy0NI5lv4T', 'artist_name': 'Dan + Shay', 'album_name': 'When I Pray For You', 'track_number': 1, 'duration_ms': 209173, 'popularity': 63, 'danceability': 0.382, 'energy': 0.781, 'loudness': -4.243, 'speechiness': 0.0433, 'acousticness': 0.054, 'instrumentalness': 0, 'liveness': 0.23, 'valence': 0.351, 'tempo': 163.815}, '5xdFitc41cUXrRtR5dzwg5': {'name': "Can't Say No", 'artist_id': '7z5WFjZAIYejWy0NI5lv4T', 'artist_name': 'Dan + Shay', 'album_name': 'Where It All Began', 'track_number': 5, 'duration_ms': 174373, 'popularity': 61, 'danceability': 0.742, 'energy': 0.43, 'loudness': -11.373, 'speechiness': 0.0267, 'acousticness': 0.46, 'instrumentalness': 0, 'liveness': 0.172, 'valence': 0.696, 'tempo': 101.982}, '2IOvJJrN6RajoMOd9TyGra': {'name': "Road Trippin'", 'artist_id': '7z5WFjZAIYejWy0NI5lv4T', 'artist_name': 'Dan + Shay', 'album_name': 'Obsessed', 'track_number': 2, 'duration_ms': 212573, 'popularity': 61, 'danceability': 0.545, 'energy': 0.812, 'loudness': -4.652, 'speechiness': 0.049, 'acousticness': 0.00327, 'instrumentalness': 0, 'liveness': 0.286, 'valence': 0.764, 'tempo': 161.107}, '7ongSdLv28Z27WeCrzZXwB': {'name': '19 You + Me', 'artist_id': '7z5WFjZAIYejWy0NI5lv4T', 'artist_name': 'Dan + Shay', 'album_name': 'Where It All Began', 'track_number': 3, 'duration_ms': 217406, 'popularity': 59, 'danceability': 0.493, 'energy': 0.67, 'loudness': -5.131, 'speechiness': 0.0298, 'acousticness': 0.319, 'instrumentalness': 0, 'liveness': 0.102, 'valence': 0.467, 'tempo': 151.989}, '4w9LtJn74XQhsHD1zAHnzY': {'name': 'Show You Off', 'artist_id': '7z5WFjZAIYejWy0NI5lv4T', 'artist_name': 'Dan + Shay', 'album_name': 'Where It All Began', 'track_number': 1, 'duration_ms': 183280, 'popularity': 57, 'danceability': 0.543, 'energy': 0.851, 'loudness': -4.197, 'speechiness': 0.0381, 'acousticness': 0.207, 'instrumentalness': 0, 'liveness': 0.0655, 'valence': 0.779, 'tempo': 166.054}, '4RBmXmZKf76IyNiPzebI55': {'name': 'Obsessed', 'artist_id': '7z5WFjZAIYejWy0NI5lv4T', 'artist_name': 'Dan + Shay', 'album_name': 'Obsessed', 'track_number': 10, 'duration_ms': 302960, 'popularity': 57, 'danceability': 0.563, 'energy': 0.574, 'loudness': -6.354, 'speechiness': 0.0286, 'acousticness': 0.379, 'instrumentalness': 4.66e-05, 'liveness': 0.142, 'valence': 0.806, 'tempo': 171.901}, '2pLw1tu9QEGeidJKBZRaZI': {'name': 'Already Ready', 'artist_id': '7z5WFjZAIYejWy0NI5lv4T', 'artist_name': 'Dan + Shay', 'album_name': 'Obsessed', 'track_number': 4, 'duration_ms': 201613, 'popularity': 56, 'danceability': 0.583, 'energy': 0.56, 'loudness': -8.569, 'speechiness': 0.0297, 'acousticness': 0.148, 'instrumentalness': 0, 'liveness': 0.111, 'valence': 0.577, 'tempo': 80.064}, '6uFSls1Xd3U6Kt8yj3zVR0': {'name': 'Killing Me', 'artist_id': '3Lw97gGh8bp1MftsYmwJHG', 'artist_name': 'Luke Sital-Singh', 'album_name': 'Killing Me', 'track_number': 1, 'duration_ms': 264480, 'popularity': 63, 'danceability': 0.39, 'energy': 0.21, 'loudness': -8.294, 'speechiness': 0.0371, 'acousticness': 0.898, 'instrumentalness': 0.000435, 'liveness': 0.0925, 'valence': 0.0617, 'tempo': 67.989}, '64qdx3vEpshNqch4EC5GMV': {'name': 'Fail For You', 'artist_id': '3Lw97gGh8bp1MftsYmwJHG', 'artist_name': 'Luke Sital-Singh', 'album_name': 'The Fire Inside', 'track_number': 9, 'duration_ms': 256240, 'popularity': 52, 'danceability': 0.275, 'energy': 0.141, 'loudness': -11.623, 'speechiness': 0.0341, 'acousticness': 0.946, 'instrumentalness': 6.77e-06, 'liveness': 0.107, 'valence': 0.0851, 'tempo': 82.955}, '6AmFUEceHzykYXeFAms8Ds': {'name': "This Woman's Work", 'artist_id': '3Lw97gGh8bp1MftsYmwJHG', 'artist_name': 'Luke Sital-Singh', 'album_name': "This Woman's Work / American Girl", 'track_number': 1, 'duration_ms': 224193, 'popularity': 51, 'danceability': 0.592, 'energy': 0.192, 'loudness': -10.209, 'speechiness': 0.0351, 'acousticness': 0.938, 'instrumentalness': 1.74e-05, 'liveness': 0.111, 'valence': 0.12, 'tempo': 107.913}, '67UAImj4r5ZfCwhpsTvn5l': {'name': 'Pure', 'artist_id': '3Lw97gGh8bp1MftsYmwJHG', 'artist_name': 'Luke Sital-Singh', 'album_name': 'Pure', 'track_number': 1, 'duration_ms': 251111, 'popularity': 51, 'danceability': 0.721, 'energy': 0.22, 'loudness': -12.308, 'speechiness': 0.0516, 'acousticness': 0.837, 'instrumentalness': 0, 'liveness': 0.116, 'valence': 0.428, 'tempo': 108.153}, '7cKQE2K6ggLByzlIMtCxzu': {'name': 'Bottled Up Tight', 'artist_id': '3Lw97gGh8bp1MftsYmwJHG', 'artist_name': 'Luke Sital-Singh', 'album_name': 'The Fire Inside', 'track_number': 3, 'duration_ms': 200253, 'popularity': 43, 'danceability': 0.556, 'energy': 0.537, 'loudness': -7.74, 'speechiness': 0.0293, 'acousticness': 0.0499, 'instrumentalness': 9.06e-06, 'liveness': 0.166, 'valence': 0.527, 'tempo': 89.404}, '2bzSwMHkc8XgTpSghMpYFB': {'name': 'Nearly Morning', 'artist_id': '3Lw97gGh8bp1MftsYmwJHG', 'artist_name': 'Luke Sital-Singh', 'album_name': 'The Fire Inside', 'track_number': 6, 'duration_ms': 272106, 'popularity': 47, 'danceability': 0.535, 'energy': 0.261, 'loudness': -10.648, 'speechiness': 0.028, 'acousticness': 0.713, 'instrumentalness': 1.6e-05, 'liveness': 0.0961, 'valence': 0.151, 'tempo': 131.797}, '35D0xUf06Tu3yr1sqr4Vsv': {'name': 'American Girl', 'artist_id': '3Lw97gGh8bp1MftsYmwJHG', 'artist_name': 'Luke Sital-Singh', 'album_name': "This Woman's Work / American Girl", 'track_number': 2, 'duration_ms': 175500, 'popularity': 46, 'danceability': 0.636, 'energy': 0.366, 'loudness': -9.974, 'speechiness': 0.026, 'acousticness': 0.918, 'instrumentalness': 0.000498, 'liveness': 0.136, 'valence': 0.289, 'tempo': 103.002}, '6KtizyqyvJ10bEbm1qNtPa': {'name': 'Benediction', 'artist_id': '3Lw97gGh8bp1MftsYmwJHG', 'artist_name': 'Luke Sital-Singh', 'album_name': 'The Fire Inside', 'track_number': 12, 'duration_ms': 219120, 'popularity': 45, 'danceability': 0.416, 'energy': 0.122, 'loudness': -11.366, 'speechiness': 0.0364, 'acousticness': 0.972, 'instrumentalness': 0.000268, 'liveness': 0.108, 'valence': 0.197, 'tempo': 120.71}, '4jMgRHnKEEHDEBBxU3PBMB': {'name': 'Hunger', 'artist_id': '3Lw97gGh8bp1MftsYmwJHG', 'artist_name': 'Luke Sital-Singh', 'album_name': 'Hunger', 'track_number': 1, 'duration_ms': 199306, 'popularity': 42, 'danceability': 0.56, 'energy': 0.586, 'loudness': -7.033, 'speechiness': 0.0335, 'acousticness': 0.201, 'instrumentalness': 0.0446, 'liveness': 0.111, 'valence': 0.155, 'tempo': 111.828}, '7px4t7HGiuMUvFkEOpZEwp': {'name': 'Song for Another Time', 'artist_id': '6y8XlgIV8BLlIg1tT1R10i', 'artist_name': 'Old Dominion', 'album_name': 'Meat and Candy', 'track_number': 9, 'duration_ms': 191826, 'popularity': 76, 'danceability': 0.497, 'energy': 0.805, 'loudness': -3.995, 'speechiness': 0.0332, 'acousticness': 0.125, 'instrumentalness': 0, 'liveness': 0.167, 'valence': 0.688, 'tempo': 166.048}, '1JupdHkhDzE4XtrFFe9w6o': {'name': 'No Such Thing as a Broken Heart', 'artist_id': '6y8XlgIV8BLlIg1tT1R10i', 'artist_name': 'Old Dominion', 'album_name': 'No Such Thing as a Broken Heart', 'track_number': 1, 'duration_ms': 178840, 'popularity': 74, 'danceability': 0.655, 'energy': 0.785, 'loudness': -4.022, 'speechiness': 0.0697, 'acousticness': 0.279, 'instrumentalness': 0, 'liveness': 0.116, 'valence': 0.931, 'tempo': 171.969}, '5ZManJDV3CexO66nRCkdiV': {'name': 'Break Up with Him', 'artist_id': '6y8XlgIV8BLlIg1tT1R10i', 'artist_name': 'Old Dominion', 'album_name': 'Meat and Candy', 'track_number': 8, 'duration_ms': 207733, 'popularity': 73, 'danceability': 0.615, 'energy': 0.632, 'loudness': -5.382, 'speechiness': 0.0374, 'acousticness': 0.0685, 'instrumentalness': 0, 'liveness': 0.108, 'valence': 0.561, 'tempo': 152.035}, '7I5fYc4qKJddht8Ozhqqdx': {'name': 'Snapback', 'artist_id': '6y8XlgIV8BLlIg1tT1R10i', 'artist_name': 'Old Dominion', 'album_name': 'Meat and Candy', 'track_number': 1, 'duration_ms': 206506, 'popularity': 71, 'danceability': 0.687, 'energy': 0.793, 'loudness': -3.577, 'speechiness': 0.0333, 'acousticness': 0.305, 'instrumentalness': 3.23e-06, 'liveness': 0.1, 'valence': 0.672, 'tempo': 100.991}, '6arLnfArtdWKOcCYzDd4rS': {'name': 'Nowhere Fast', 'artist_id': '6y8XlgIV8BLlIg1tT1R10i', 'artist_name': 'Old Dominion', 'album_name': 'Meat and Candy', 'track_number': 6, 'duration_ms': 188960, 'popularity': 68, 'danceability': 0.788, 'energy': 0.488, 'loudness': -7.319, 'speechiness': 0.0286, 'acousticness': 0.46, 'instrumentalness': 4.52e-06, 'liveness': 0.0751, 'valence': 0.495, 'tempo': 101.974}, '74uXfGRDayyx7UIV1irrhK': {'name': 'Wrong Turns', 'artist_id': '6y8XlgIV8BLlIg1tT1R10i', 'artist_name': 'Old Dominion', 'album_name': 'Meat and Candy', 'track_number': 3, 'duration_ms': 208480, 'popularity': 65, 'danceability': 0.633, 'energy': 0.683, 'loudness': -4.648, 'speechiness': 0.0277, 'acousticness': 0.0902, 'instrumentalness': 0, 'liveness': 0.124, 'valence': 0.56, 'tempo': 131.046}, '1E1LaXgZRkBOljpGXtlR7B': {'name': 'Wake up Loving You', 'artist_id': '6y8XlgIV8BLlIg1tT1R10i', 'artist_name': 'Old Dominion', 'album_name': 'Old Dominion Originals', 'track_number': 1, 'duration_ms': 228013, 'popularity': 60, 'danceability': 0.579, 'energy': 0.499, 'loudness': -8.195, 'speechiness': 0.0425, 'acousticness': 0.0299, 'instrumentalness': 2.51e-06, 'liveness': 0.111, 'valence': 0.425, 'tempo': 147.995}, '3nC688MXGnFDAcL3lU1Ray': {'name': 'Crazy Beautiful Sexy', 'artist_id': '6y8XlgIV8BLlIg1tT1R10i', 'artist_name': 'Old Dominion', 'album_name': 'Meat and Candy', 'track_number': 5, 'duration_ms': 188160, 'popularity': 58, 'danceability': 0.73, 'energy': 0.826, 'loudness': -4.33, 'speechiness': 0.0371, 'acousticness': 0.328, 'instrumentalness': 1.86e-06, 'liveness': 0.0725, 'valence': 0.873, 'tempo': 96.974}, '5dTTvqEs42JMJv98b4SaoE': {'name': 'Half Empty', 'artist_id': '6y8XlgIV8BLlIg1tT1R10i', 'artist_name': 'Old Dominion', 'album_name': 'Meat and Candy', 'track_number': 2, 'duration_ms': 170800, 'popularity': 57, 'danceability': 0.577, 'energy': 0.751, 'loudness': -4.822, 'speechiness': 0.0301, 'acousticness': 0.449, 'instrumentalness': 0, 'liveness': 0.158, 'valence': 0.837, 'tempo': 84.048}, '6CCV2biTOmU2wRBTJzapxX': {'name': "Til It's Over", 'artist_id': '6y8XlgIV8BLlIg1tT1R10i', 'artist_name': 'Old Dominion', 'album_name': 'Meat and Candy', 'track_number': 10, 'duration_ms': 207106, 'popularity': 57, 'danceability': 0.634, 'energy': 0.805, 'loudness': -5.152, 'speechiness': 0.0344, 'acousticness': 0.322, 'instrumentalness': 3.71e-05, 'liveness': 0.112, 'valence': 0.806, 'tempo': 92.543}, '6LIWwxXoHqm7AuOByjFyd2': {'name': 'Speak to a Girl', 'artist_id': '6roFdX1y5BYSbp60OTJWMd', 'artist_name': 'Tim McGraw', 'album_name': 'Speak to a Girl', 'track_number': 1, 'duration_ms': 231920, 'popularity': 73, 'danceability': 0.476, 'energy': 0.527, 'loudness': -6.406, 'speechiness': 0.0399, 'acousticness': 0.661, 'instrumentalness': 0, 'liveness': 0.307, 'valence': 0.205, 'tempo': 152.117}, '4wFUdSCer8bdQsrp1M90sa': {'name': "Highway Don't Care", 'artist_id': '6roFdX1y5BYSbp60OTJWMd', 'artist_name': 'Tim McGraw', 'album_name': 'Two Lanes Of Freedom', 'track_number': 11, 'duration_ms': 276880, 'popularity': 71, 'danceability': 0.47, 'energy': 0.79, 'loudness': -5.352, 'speechiness': 0.039, 'acousticness': 0.0216, 'instrumentalness': 0, 'liveness': 0.0863, 'valence': 0.5, 'tempo': 158.061}, '4Pn0JlCUusD2QHjADuOzuV': {'name': 'Humble And Kind', 'artist_id': '6roFdX1y5BYSbp60OTJWMd', 'artist_name': 'Tim McGraw', 'album_name': 'Damn Country Music', 'track_number': 11, 'duration_ms': 259266, 'popularity': 63, 'danceability': 0.471, 'energy': 0.489, 'loudness': -7.252, 'speechiness': 0.0263, 'acousticness': 0.709, 'instrumentalness': 1.45e-06, 'liveness': 0.12, 'valence': 0.181, 'tempo': 151.454}, '7B1QliUMZv7gSTUGAfMRRD': {'name': 'Live Like You Were Dying', 'artist_id': '6roFdX1y5BYSbp60OTJWMd', 'artist_name': 'Tim McGraw', 'album_name': 'Live Like You Were Dying', 'track_number': 5, 'duration_ms': 300333, 'popularity': 45, 'danceability': 0.416, 'energy': 0.546, 'loudness': -7.728, 'speechiness': 0.0297, 'acousticness': 0.492, 'instrumentalness': 0, 'liveness': 0.0845, 'valence': 0.411, 'tempo': 159.929}, '2op0kDNARK2VHWHntEeH4g': {'name': 'Just To See You Smile', 'artist_id': '6roFdX1y5BYSbp60OTJWMd', 'artist_name': 'Tim McGraw', 'album_name': 'Everywhere', 'track_number': 9, 'duration_ms': 215173, 'popularity': 39, 'danceability': 0.492, 'energy': 0.823, 'loudness': -8.526, 'speechiness': 0.0297, 'acousticness': 0.127, 'instrumentalness': 0, 'liveness': 0.0523, 'valence': 0.704, 'tempo': 94.342}, '2ZekuYUoEIBrUwHOY0gcgB': {'name': "How I'll Always Be", 'artist_id': '6roFdX1y5BYSbp60OTJWMd', 'artist_name': 'Tim McGraw', 'album_name': 'Damn Country Music', 'track_number': 3, 'duration_ms': 213453, 'popularity': 64, 'danceability': 0.456, 'energy': 0.813, 'loudness': -4.676, 'speechiness': 0.0452, 'acousticness': 0.319, 'instrumentalness': 5.42e-06, 'liveness': 0.0946, 'valence': 0.645, 'tempo': 185.993}, '4pdoeoOQSu6DNznlfNc5FP': {'name': 'Top Of The World', 'artist_id': '6roFdX1y5BYSbp60OTJWMd', 'artist_name': 'Tim McGraw', 'album_name': 'Damn Country Music', 'track_number': 7, 'duration_ms': 233973, 'popularity': 61, 'danceability': 0.673, 'energy': 0.795, 'loudness': -5.608, 'speechiness': 0.0391, 'acousticness': 0.296, 'instrumentalness': 0, 'liveness': 0.489, 'valence': 0.961, 'tempo': 141.208}, '503sFkc8Y2eyGnM6cu8kHm': {'name': "It's Your Love", 'artist_id': '6roFdX1y5BYSbp60OTJWMd', 'artist_name': 'Tim McGraw', 'album_name': 'Everywhere', 'track_number': 3, 'duration_ms': 227333, 'popularity': 38, 'danceability': 0.474, 'energy': 0.528, 'loudness': -8.588, 'speechiness': 0.0276, 'acousticness': 0.526, 'instrumentalness': 0, 'liveness': 0.109, 'valence': 0.359, 'tempo': 144.366}, '6leiB1fEsTnVCuPiielde5': {'name': 'Something Like That', 'artist_id': '6roFdX1y5BYSbp60OTJWMd', 'artist_name': 'Tim McGraw', 'album_name': 'A Place In The Sun', 'track_number': 9, 'duration_ms': 183733, 'popularity': 38, 'danceability': 0.507, 'energy': 0.85, 'loudness': -5.679, 'speechiness': 0.0472, 'acousticness': 0.378, 'instrumentalness': 0, 'liveness': 0.0567, 'valence': 0.848, 'tempo': 171.8}, '08YEGpKt2LHJ0URCXKHEie': {'name': '9 Crimes', 'artist_id': '14r9dR01KeBLFfylVSKCZQ', 'artist_name': 'Damien Rice', 'album_name': '9', 'track_number': 1, 'duration_ms': 217946, 'popularity': 67, 'danceability': 0.346, 'energy': 0.139, 'loudness': -15.326, 'speechiness': 0.0321, 'acousticness': 0.913, 'instrumentalness': 7.73e-05, 'liveness': 0.0934, 'valence': 0.112, 'tempo': 136.168}, '4B2lJinAkeNLSJjcq3dg8Q': {'name': "The Blower's Daughter", 'artist_id': '14r9dR01KeBLFfylVSKCZQ', 'artist_name': 'Damien Rice', 'album_name': 'O', 'track_number': 3, 'duration_ms': 286653, 'popularity': 59, 'danceability': 0.342, 'energy': 0.2, 'loudness': -13.569, 'speechiness': 0.0324, 'acousticness': 0.134, 'instrumentalness': 0.000153, 'liveness': 0.341, 'valence': 0.0732, 'tempo': 133.113}, '3BFXgZr628FqwDP3pQCgvk': {'name': "I Don't Want To Change You", 'artist_id': '14r9dR01KeBLFfylVSKCZQ', 'artist_name': 'Damien Rice', 'album_name': 'My Favourite Faded Fantasy', 'track_number': 4, 'duration_ms': 326206, 'popularity': 58, 'danceability': 0.41, 'energy': 0.306, 'loudness': -9.704, 'speechiness': 0.0348, 'acousticness': 0.472, 'instrumentalness': 3.28e-05, 'liveness': 0.12, 'valence': 0.161, 'tempo': 141.565}, '5mb6SzBnxv1ywFSH9V3uxd': {'name': 'Delicate', 'artist_id': '14r9dR01KeBLFfylVSKCZQ', 'artist_name': 'Damien Rice', 'album_name': 'O', 'track_number': 1, 'duration_ms': 307773, 'popularity': 55, 'danceability': 0.351, 'energy': 0.142, 'loudness': -14.556, 'speechiness': 0.0394, 'acousticness': 0.679, 'instrumentalness': 0.000797, 'liveness': 0.107, 'valence': 0.169, 'tempo': 85.87}, '7FCYixd46BlSiO2memrsPo': {'name': 'Older Chests', 'artist_id': '14r9dR01KeBLFfylVSKCZQ', 'artist_name': 'Damien Rice', 'album_name': 'O', 'track_number': 5, 'duration_ms': 282066, 'popularity': 56, 'danceability': 0.507, 'energy': 0.129, 'loudness': -15.846, 'speechiness': 0.031, 'acousticness': 0.894, 'instrumentalness': 0.0026, 'liveness': 0.0983, 'valence': 0.161, 'tempo': 110.887}, '6R0BVRF95vCERjhCabl17q': {'name': 'The Greatest Bastard', 'artist_id': '14r9dR01KeBLFfylVSKCZQ', 'artist_name': 'Damien Rice', 'album_name': 'My Favourite Faded Fantasy', 'track_number': 3, 'duration_ms': 304809, 'popularity': 44, 'danceability': 0.432, 'energy': 0.0773, 'loudness': -14.325, 'speechiness': 0.0443, 'acousticness': 0.768, 'instrumentalness': 4e-06, 'liveness': 0.0791, 'valence': 0.222, 'tempo': 105.044}, '4CVP2pvqUxH9tExsHJnzV9': {'name': 'Coconut Skins', 'artist_id': '14r9dR01KeBLFfylVSKCZQ', 'artist_name': 'Damien Rice', 'album_name': '9', 'track_number': 6, 'duration_ms': 225373, 'popularity': 53, 'danceability': 0.36, 'energy': 0.594, 'loudness': -6.898, 'speechiness': 0.0312, 'acousticness': 0.255, 'instrumentalness': 0, 'liveness': 0.0875, 'valence': 0.471, 'tempo': 107.528}, '7r2az72yWEXzlrQEMJjcsz': {'name': 'My Favourite Faded Fantasy', 'artist_id': '14r9dR01KeBLFfylVSKCZQ', 'artist_name': 'Damien Rice', 'album_name': 'My Favourite Faded Fantasy', 'track_number': 1, 'duration_ms': 371797, 'popularity': 45, 'danceability': 0.35, 'energy': 0.233, 'loudness': -11.832, 'speechiness': 0.0322, 'acousticness': 0.651, 'instrumentalness': 0.00117, 'liveness': 0.262, 'valence': 0.085, 'tempo': 146.663}, '4bdjQvuoDBAsxdUPmEIltt': {'name': 'Lonelily', 'artist_id': '14r9dR01KeBLFfylVSKCZQ', 'artist_name': 'Damien Rice', 'album_name': 'B-Sides', 'track_number': 2, 'duration_ms': 193880, 'popularity': 52, 'danceability': 0.298, 'energy': 0.503, 'loudness': -8.555, 'speechiness': 0.0437, 'acousticness': 0.348, 'instrumentalness': 6.3e-05, 'liveness': 0.118, 'valence': 0.545, 'tempo': 78.951}, '3AkxSspcYOvhWTkaMvqyaD': {'name': 'Volcano', 'artist_id': '14r9dR01KeBLFfylVSKCZQ', 'artist_name': 'Damien Rice', 'album_name': 'O', 'track_number': 2, 'duration_ms': 278426, 'popularity': 48, 'danceability': 0.49, 'energy': 0.293, 'loudness': -12.883, 'speechiness': 0.0512, 'acousticness': 0.593, 'instrumentalness': 2.38e-06, 'liveness': 0.127, 'valence': 0.436, 'tempo': 153.616}, '5sjIhQzNljMVrDklI91ezp': {'name': 'A Guy With a Girl', 'artist_id': '1UTPBmNbXNTittyMJrNkvw', 'artist_name': 'Blake Shelton', 'album_name': "If I'm Honest", 'track_number': 8, 'duration_ms': 189466, 'popularity': 77, 'danceability': 0.552, 'energy': 0.893, 'loudness': -4.593, 'speechiness': 0.0383, 'acousticness': 0.0158, 'instrumentalness': 0, 'liveness': 0.105, 'valence': 0.767, 'tempo': 163.948}, '0c4ICGb0jvszKj3KPR59JU': {'name': 'Every Time I Hear That Song', 'artist_id': '1UTPBmNbXNTittyMJrNkvw', 'artist_name': 'Blake Shelton', 'album_name': "If I'm Honest", 'track_number': 4, 'duration_ms': 214800, 'popularity': 74, 'danceability': 0.523, 'energy': 0.725, 'loudness': -5.448, 'speechiness': 0.0339, 'acousticness': 0.0558, 'instrumentalness': 6.96e-06, 'liveness': 0.0937, 'valence': 0.52, 'tempo': 155.855}, '0p1HtkrNYxv0iDfEKwXSTp': {'name': 'Sangria', 'artist_id': '1UTPBmNbXNTittyMJrNkvw', 'artist_name': 'Blake Shelton', 'album_name': 'BRINGING BACK THE SUNSHINE', 'track_number': 6, 'duration_ms': 233480, 'popularity': 73, 'danceability': 0.646, 'energy': 0.724, 'loudness': -6.96, 'speechiness': 0.0265, 'acousticness': 0.017, 'instrumentalness': 1.39e-06, 'liveness': 0.153, 'valence': 0.541, 'tempo': 115.984}, '1N7qGCKRRnvjoy8MGyHgpS': {'name': 'Came Here to Forget', 'artist_id': '1UTPBmNbXNTittyMJrNkvw', 'artist_name': 'Blake Shelton', 'album_name': "If I'm Honest", 'track_number': 5, 'duration_ms': 220413, 'popularity': 72, 'danceability': 0.613, 'energy': 0.667, 'loudness': -6.874, 'speechiness': 0.029, 'acousticness': 0.356, 'instrumentalness': 1.29e-05, 'liveness': 0.111, 'valence': 0.49, 'tempo': 130.023}, '0gY2iq0xJPRoIB1PScKSw4': {'name': 'Honey Bee', 'artist_id': '1UTPBmNbXNTittyMJrNkvw', 'artist_name': 'Blake Shelton', 'album_name': 'Red River Blue (Deluxe)', 'track_number': 1, 'duration_ms': 210720, 'popularity': 68, 'danceability': 0.481, 'energy': 0.849, 'loudness': -5.131, 'speechiness': 0.0385, 'acousticness': 0.00167, 'instrumentalness': 1.49e-06, 'liveness': 0.121, 'valence': 0.722, 'tempo': 205.57}, '1zvQt99d5oTkEQLmSoO1yu': {'name': 'Mine Would Be You', 'artist_id': '1UTPBmNbXNTittyMJrNkvw', 'artist_name': 'Blake Shelton', 'album_name': 'Based on a True Story... (Deluxe Version)', 'track_number': 9, 'duration_ms': 239506, 'popularity': 67, 'danceability': 0.572, 'energy': 0.529, 'loudness': -6.897, 'speechiness': 0.0282, 'acousticness': 0.146, 'instrumentalness': 0, 'liveness': 0.335, 'valence': 0.332, 'tempo': 139.876}, '6eJBihAzTWRxvvjJWuRQXM': {'name': 'Go Ahead and Break My Heart (feat. Gwen Stefani)', 'artist_id': '1UTPBmNbXNTittyMJrNkvw', 'artist_name': 'Blake Shelton', 'album_name': "If I'm Honest", 'track_number': 9, 'duration_ms': 263800, 'popularity': 67, 'danceability': 0.618, 'energy': 0.731, 'loudness': -5.181, 'speechiness': 0.0321, 'acousticness': 0.0714, 'instrumentalness': 5.05e-05, 'liveness': 0.421, 'valence': 0.325, 'tempo': 116.008}, '39FwE8edwuyiaa4PrGBkP7': {'name': "Boys 'Round Here (feat. Pistol Annies & Friends)", 'artist_id': '1UTPBmNbXNTittyMJrNkvw', 'artist_name': 'Blake Shelton', 'album_name': 'Based on a True Story... (Deluxe Version)', 'track_number': 1, 'duration_ms': 288760, 'popularity': 66, 'danceability': 0.611, 'energy': 0.688, 'loudness': -6.369, 'speechiness': 0.0529, 'acousticness': 0.251, 'instrumentalness': 2.35e-06, 'liveness': 0.248, 'valence': 0.647, 'tempo': 169.895}, '3JffB4CABj9lA0NC63kbCp': {'name': "She's Got a Way With Words", 'artist_id': '1UTPBmNbXNTittyMJrNkvw', 'artist_name': 'Blake Shelton', 'album_name': "If I'm Honest", 'track_number': 2, 'duration_ms': 190986, 'popularity': 66, 'danceability': 0.616, 'energy': 0.697, 'loudness': -5.952, 'speechiness': 0.0295, 'acousticness': 0.326, 'instrumentalness': 2.18e-05, 'liveness': 0.0827, 'valence': 0.686, 'tempo': 148.93}, '5yIiXdLRE85OBiQmCaUenq': {'name': 'Sure Be Cool If You Did', 'artist_id': '1UTPBmNbXNTittyMJrNkvw', 'artist_name': 'Blake Shelton', 'album_name': 'Based on a True Story... (Deluxe Version)', 'track_number': 2, 'duration_ms': 215720, 'popularity': 61, 'danceability': 0.576, 'energy': 0.726, 'loudness': -4.625, 'speechiness': 0.035, 'acousticness': 0.255, 'instrumentalness': 0, 'liveness': 0.108, 'valence': 0.578, 'tempo': 136.802}, '6YH2r9NyEJTjlRmKOCvxgJ': {'name': 'We Know The Way', 'artist_id': '4aXXDj9aZnlshx7mzj3W1N', 'artist_name': 'Lin-Manuel Miranda', 'album_name': 'Moana (Original Motion Picture Soundtrack/Deluxe Edition)', 'track_number': 5, 'duration_ms': 141413, 'popularity': 74, 'danceability': 0.696, 'energy': 0.567, 'loudness': -8.907, 'speechiness': 0.0374, 'acousticness': 0.372, 'instrumentalness': 0, 'liveness': 0.112, 'valence': 0.395, 'tempo': 98.034}, '3HAh7a08YVxEyb8BM645bU': {'name': 'We Know The Way - Finale', 'artist_id': '4aXXDj9aZnlshx7mzj3W1N', 'artist_name': 'Lin-Manuel Miranda', 'album_name': 'Moana (Original Motion Picture Soundtrack/Deluxe Edition)', 'track_number': 12, 'duration_ms': 69120, 'popularity': 69, 'danceability': 0.498, 'energy': 0.829, 'loudness': -8.611, 'speechiness': 0.0511, 'acousticness': 0.552, 'instrumentalness': 0, 'liveness': 0.0705, 'valence': 0.166, 'tempo': 101.034}, '0NJWhm3hUwIZSy5s0TGJ8q': {'name': 'The Story Of Tonight', 'artist_id': '4aXXDj9aZnlshx7mzj3W1N', 'artist_name': 'Lin-Manuel Miranda', 'album_name': 'Hamilton (Original Broadway Cast Recording)', 'track_number': 4, 'duration_ms': 91980, 'popularity': 69, 'danceability': 0.407, 'energy': 0.237, 'loudness': -10.579, 'speechiness': 0.053, 'acousticness': 0.835, 'instrumentalness': 0, 'liveness': 0.648, 'valence': 0.603, 'tempo': 95.111}, '2G9lekfCh83S0lt2yfffBz': {'name': 'Farmer Refuted', 'artist_id': '4lSm9vkdpKSs1O8nKflRaB', 'artist_name': 'Thayne Jasperson', 'album_name': 'Hamilton (Original Broadway Cast Recording)', 'track_number': 6, 'duration_ms': 112742, 'popularity': 68, 'danceability': 0.795, 'energy': 0.409, 'loudness': -8.334, 'speechiness': 0.372, 'acousticness': 0.684, 'instrumentalness': 0, 'liveness': 0.0548, 'valence': 0.587, 'tempo': 77.879}, '5o9LteJdhkA3ndUDz4JVfV': {'name': 'Make You Mine', 'artist_id': '5sQqZtsAbXAoAnvA8iN9kN', 'artist_name': 'High Valley', 'album_name': 'Dear Life', 'track_number': 4, 'duration_ms': 211613, 'popularity': 65, 'danceability': 0.576, 'energy': 0.892, 'loudness': -4.178, 'speechiness': 0.0392, 'acousticness': 0.12, 'instrumentalness': 0, 'liveness': 0.131, 'valence': 0.516, 'tempo': 123.074}, '2p2cCrOaNrIOLk5ArtlHy6': {'name': "She's With Me", 'artist_id': '5sQqZtsAbXAoAnvA8iN9kN', 'artist_name': 'High Valley', 'album_name': 'Dear Life', 'track_number': 1, 'duration_ms': 180301, 'popularity': 56, 'danceability': 0.599, 'energy': 0.931, 'loudness': -3.662, 'speechiness': 0.0517, 'acousticness': 0.0285, 'instrumentalness': 0, 'liveness': 0.102, 'valence': 0.781, 'tempo': 111.012}, '1zMGZrrUG26o0pkfOPfHbo': {'name': 'I Be U Be', 'artist_id': '5sQqZtsAbXAoAnvA8iN9kN', 'artist_name': 'High Valley', 'album_name': 'Dear Life', 'track_number': 8, 'duration_ms': 213093, 'popularity': 46, 'danceability': 0.442, 'energy': 0.746, 'loudness': -5.883, 'speechiness': 0.0335, 'acousticness': 0.0074, 'instrumentalness': 0, 'liveness': 0.0996, 'valence': 0.43, 'tempo': 126.035}, '2dieIRxavIVIC0ZZYNZB5o': {'name': 'Young Forever', 'artist_id': '5sQqZtsAbXAoAnvA8iN9kN', 'artist_name': 'High Valley', 'album_name': 'Dear Life', 'track_number': 11, 'duration_ms': 220240, 'popularity': 46, 'danceability': 0.565, 'energy': 0.898, 'loudness': -4.693, 'speechiness': 0.0372, 'acousticness': 0.000497, 'instrumentalness': 0, 'liveness': 0.208, 'valence': 0.719, 'tempo': 146.025}, '6V647zWTLg2LcfzPzFljZA': {'name': 'Dear Life', 'artist_id': '5sQqZtsAbXAoAnvA8iN9kN', 'artist_name': 'High Valley', 'album_name': 'Dear Life', 'track_number': 2, 'duration_ms': 195000, 'popularity': 45, 'danceability': 0.554, 'energy': 0.88, 'loudness': -6.366, 'speechiness': 0.0425, 'acousticness': 0.0179, 'instrumentalness': 0, 'liveness': 0.0862, 'valence': 0.423, 'tempo': 127.026}, '4JqSjvWYsFIHsnpwSZ0f8W': {'name': "Every Week's Got a Friday", 'artist_id': '5sQqZtsAbXAoAnvA8iN9kN', 'artist_name': 'High Valley', 'album_name': "Every Week's Got a Friday", 'track_number': 1, 'duration_ms': 188669, 'popularity': 42, 'danceability': 0.487, 'energy': 0.966, 'loudness': -3.064, 'speechiness': 0.0623, 'acousticness': 0.0425, 'instrumentalness': 0, 'liveness': 0.442, 'valence': 0.626, 'tempo': 160.033}, '3EV2ZdIDTcZ551RqIRspSw': {'name': 'Soldier', 'artist_id': '5sQqZtsAbXAoAnvA8iN9kN', 'artist_name': 'High Valley', 'album_name': 'Dear Life', 'track_number': 10, 'duration_ms': 203906, 'popularity': 41, 'danceability': 0.619, 'energy': 0.682, 'loudness': -6.036, 'speechiness': 0.0302, 'acousticness': 0.00867, 'instrumentalness': 0, 'liveness': 0.1, 'valence': 0.611, 'tempo': 122.997}, '2uTzK6JPWHlsE8ekkwOFKF': {'name': "Memory Makin'", 'artist_id': '5sQqZtsAbXAoAnvA8iN9kN', 'artist_name': 'High Valley', 'album_name': 'Dear Life', 'track_number': 9, 'duration_ms': 159160, 'popularity': 40, 'danceability': 0.507, 'energy': 0.787, 'loudness': -5.339, 'speechiness': 0.0411, 'acousticness': 0.0101, 'instrumentalness': 0, 'liveness': 0.218, 'valence': 0.352, 'tempo': 104.009}, '1zlFtrl1qpymPGtSQqMsJ9': {'name': 'The Only', 'artist_id': '5sQqZtsAbXAoAnvA8iN9kN', 'artist_name': 'High Valley', 'album_name': 'Dear Life', 'track_number': 6, 'duration_ms': 187720, 'popularity': 40, 'danceability': 0.56, 'energy': 0.832, 'loudness': -4.276, 'speechiness': 0.0281, 'acousticness': 0.00484, 'instrumentalness': 0, 'liveness': 0.263, 'valence': 0.601, 'tempo': 95.99}, '0o9ivTBX7mjTnaUYF4Gk6t': {'name': 'The Imitation Game', 'artist_id': '71jzN72g8qWMCMkWC5p1Z0', 'artist_name': 'Alexandre Desplat', 'album_name': 'The Imitation Game (Original Motion Picture Soundtrack)', 'track_number': 1, 'duration_ms': 157026, 'popularity': 63, 'danceability': 0.318, 'energy': 0.308, 'loudness': -13.676, 'speechiness': 0.0285, 'acousticness': 0.438, 'instrumentalness': 0.889, 'liveness': 0.109, 'valence': 0.0541, 'tempo': 103.925}, '3GiE1hcocpQIEf1gC7fv2o': {'name': "Alan Turing's Legacy", 'artist_id': '71jzN72g8qWMCMkWC5p1Z0', 'artist_name': 'Alexandre Desplat', 'album_name': 'The Imitation Game (Original Motion Picture Soundtrack)', 'track_number': 21, 'duration_ms': 116520, 'popularity': 58, 'danceability': 0.242, 'energy': 0.371, 'loudness': -11.427, 'speechiness': 0.0333, 'acousticness': 0.803, 'instrumentalness': 0.969, 'liveness': 0.0938, 'valence': 0.0982, 'tempo': 102.194}, '2ISjP2XebyGSoKSM6Cnb0m': {'name': "LIly's Theme", 'artist_id': '71jzN72g8qWMCMkWC5p1Z0', 'artist_name': 'Alexandre Desplat', 'album_name': 'Harry Potter and the Deathly Hallows - Part 2: Original Motion Picture Soundtrack', 'track_number': 1, 'duration_ms': 148813, 'popularity': 53, 'danceability': 0.179, 'energy': 0.048, 'loudness': -28.663, 'speechiness': 0.0469, 'acousticness': 0.889, 'instrumentalness': 0.974, 'liveness': 0.0775, 'valence': 0.0276, 'tempo': 72.93}, '0pyCqpKtJFbVvkZ2ATLT2C': {'name': 'Letters', 'artist_id': '71jzN72g8qWMCMkWC5p1Z0', 'artist_name': 'Alexandre Desplat', 'album_name': 'The Light Between Oceans (Original Motion Picture Soundtrack)', 'track_number': 1, 'duration_ms': 120253, 'popularity': 55, 'danceability': 0.492, 'energy': 0.161, 'loudness': -20.062, 'speechiness': 0.0286, 'acousticness': 0.951, 'instrumentalness': 0.966, 'liveness': 0.196, 'valence': 0.0568, 'tempo': 82.036}, '3eoeShZGzmkzqnIpHZfHPn': {'name': 'Extremely Loud and Incredibly Close', 'artist_id': '71jzN72g8qWMCMkWC5p1Z0', 'artist_name': 'Alexandre Desplat', 'album_name': 'Extremely Loud and Incredibly Close: Original Motion Picture Soundtrack', 'track_number': 1, 'duration_ms': 117673, 'popularity': 55, 'danceability': 0.474, 'energy': 0.0118, 'loudness': -31.108, 'speechiness': 0.0318, 'acousticness': 0.991, 'instrumentalness': 0.891, 'liveness': 0.0622, 'valence': 0.0828, 'tempo': 79.1}, '5RKqgLYBUZC4IZrlGH9RuD': {'name': 'Making Gnocchi', 'artist_id': '71jzN72g8qWMCMkWC5p1Z0', 'artist_name': 'Alexandre Desplat', 'album_name': 'Unbroken (Original Motion Picture Soundtrack)', 'track_number': 10, 'duration_ms': 70907, 'popularity': 52, 'danceability': 0.229, 'energy': 0.00507, 'loudness': -30.13, 'speechiness': 0.0404, 'acousticness': 0.981, 'instrumentalness': 0.854, 'liveness': 0.115, 'valence': 0.106, 'tempo': 68.956}, '3jXFtmb3OU9rhytuuT1VT6': {'name': 'Statues', 'artist_id': '71jzN72g8qWMCMkWC5p1Z0', 'artist_name': 'Alexandre Desplat', 'album_name': 'Harry Potter and the Deathly Hallows - Part 2: Original Motion Picture Soundtrack', 'track_number': 9, 'duration_ms': 144200, 'popularity': 47, 'danceability': 0.321, 'energy': 0.241, 'loudness': -20.495, 'speechiness': 0.0373, 'acousticness': 0.442, 'instrumentalness': 0.888, 'liveness': 0.105, 'valence': 0.0792, 'tempo': 128.98}, '6WoCCsRd3ILkGcLm0C2XL8': {'name': 'Alan', 'artist_id': '71jzN72g8qWMCMkWC5p1Z0', 'artist_name': 'Alexandre Desplat', 'album_name': 'The Imitation Game (Original Motion Picture Soundtrack)', 'track_number': 3, 'duration_ms': 177386, 'popularity': 51, 'danceability': 0.137, 'energy': 0.158, 'loudness': -18.14, 'speechiness': 0.0441, 'acousticness': 0.912, 'instrumentalness': 0.975, 'liveness': 0.0852, 'valence': 0.0724, 'tempo': 59.341}, '7wCacjnlvU9ZN3uBNTKycs': {'name': 'Tracking Calls', 'artist_id': '71jzN72g8qWMCMkWC5p1Z0', 'artist_name': 'Alexandre Desplat', 'album_name': 'Zero Dark Thirty (Original Soundtrack)', 'track_number': 14, 'duration_ms': 226106, 'popularity': 49, 'danceability': 0.153, 'energy': 0.141, 'loudness': -31.619, 'speechiness': 0.0534, 'acousticness': 0.918, 'instrumentalness': 0.819, 'liveness': 0.248, 'valence': 0.0343, 'tempo': 75.864}, '3l1bpC1lrAZ911bplYydPb': {'name': 'Courtyard Apocalypse', 'artist_id': '71jzN72g8qWMCMkWC5p1Z0', 'artist_name': 'Alexandre Desplat', 'album_name': 'Harry Potter and the Deathly Hallows - Part 2: Original Motion Picture Soundtrack', 'track_number': 15, 'duration_ms': 120386, 'popularity': 44, 'danceability': 0.137, 'energy': 0.313, 'loudness': -17.088, 'speechiness': 0.0386, 'acousticness': 0.487, 'instrumentalness': 0.918, 'liveness': 0.111, 'valence': 0.125, 'tempo': 97.368}, '1Hv54MWloXiAZDam1ez840': {'name': 'Great Are You Lord', 'artist_id': '44LPOpECjnIlnwH91wo2ir', 'artist_name': 'All Sons & Daughters', 'album_name': 'All Sons & Daughters', 'track_number': 8, 'duration_ms': 296343, 'popularity': 62, 'danceability': 0.472, 'energy': 0.351, 'loudness': -8.996, 'speechiness': 0.0326, 'acousticness': 0.589, 'instrumentalness': 0, 'liveness': 0.0821, 'valence': 0.0584, 'tempo': 144.01}, '23aRQxzv8AbUOAV4czlNmp': {'name': 'All the Poor and Powerless', 'artist_id': '44LPOpECjnIlnwH91wo2ir', 'artist_name': 'All Sons & Daughters', 'album_name': 'Brokenness Aside EP No. 1', 'track_number': 3, 'duration_ms': 342893, 'popularity': 56, 'danceability': 0.363, 'energy': 0.308, 'loudness': -8.335, 'speechiness': 0.0304, 'acousticness': 0.389, 'instrumentalness': 2.43e-06, 'liveness': 0.0872, 'valence': 0.0765, 'tempo': 147.635}, '4PYOh644yKjYyvyVUHqcof': {'name': 'Great Are You Lord - Live', 'artist_id': '44LPOpECjnIlnwH91wo2ir', 'artist_name': 'All Sons & Daughters', 'album_name': 'Live', 'track_number': 4, 'duration_ms': 290413, 'popularity': 53, 'danceability': 0.39, 'energy': 0.457, 'loudness': -7.915, 'speechiness': 0.0327, 'acousticness': 0.0874, 'instrumentalness': 8.9e-06, 'liveness': 0.123, 'valence': 0.142, 'tempo': 143.977}, '19mFt7CznVnV5DH56ZoBTn': {'name': 'Oh How I Need You', 'artist_id': '44LPOpECjnIlnwH91wo2ir', 'artist_name': 'All Sons & Daughters', 'album_name': 'The Longing EP No. 3', 'track_number': 1, 'duration_ms': 243493, 'popularity': 50, 'danceability': 0.52, 'energy': 0.655, 'loudness': -6.854, 'speechiness': 0.0364, 'acousticness': 0.509, 'instrumentalness': 0, 'liveness': 0.087, 'valence': 0.186, 'tempo': 103.966}, '5UgGtoBzu4mmslDkcbLduT': {'name': 'Your Glory / Nothing But The Blood - Live', 'artist_id': '44LPOpECjnIlnwH91wo2ir', 'artist_name': 'All Sons & Daughters', 'album_name': 'Live', 'track_number': 13, 'duration_ms': 537866, 'popularity': 50, 'danceability': 0.384, 'energy': 0.391, 'loudness': -8.141, 'speechiness': 0.0312, 'acousticness': 0.171, 'instrumentalness': 0, 'liveness': 0.701, 'valence': 0.175, 'tempo': 142.107}, '51sy2ohrjo0E2O1lhJw64G': {'name': 'Brokenness Aside', 'artist_id': '44LPOpECjnIlnwH91wo2ir', 'artist_name': 'All Sons & Daughters', 'album_name': 'Brokenness Aside EP No. 1', 'track_number': 4, 'duration_ms': 352026, 'popularity': 50, 'danceability': 0.393, 'energy': 0.277, 'loudness': -9.573, 'speechiness': 0.0296, 'acousticness': 0.497, 'instrumentalness': 0, 'liveness': 0.0941, 'valence': 0.152, 'tempo': 135.784}, '1YJ8qjJQpTZjQZVR2hgWfx': {'name': 'Rising Sun - Live', 'artist_id': '44LPOpECjnIlnwH91wo2ir', 'artist_name': 'All Sons & Daughters', 'album_name': 'Live', 'track_number': 5, 'duration_ms': 340720, 'popularity': 45, 'danceability': 0.378, 'energy': 0.623, 'loudness': -6.663, 'speechiness': 0.0343, 'acousticness': 0.0311, 'instrumentalness': 6.57e-05, 'liveness': 0.238, 'valence': 0.218, 'tempo': 145.964}, '4PMvRfhHAx5j6Bb3XsFLoq': {'name': 'Lua', 'artist_id': '5o206eFLx38glA2bb4zqIU', 'artist_name': 'Bright Eyes', 'album_name': "I'm Wide Awake, It's Morning", 'track_number': 4, 'duration_ms': 271666, 'popularity': 60, 'danceability': 0.603, 'energy': 0.124, 'loudness': -18.301, 'speechiness': 0.0827, 'acousticness': 0.802, 'instrumentalness': 3e-05, 'liveness': 0.0565, 'valence': 0.321, 'tempo': 104.902}, '6QSmeY9pNWnE0fAUrXmYC7': {'name': "We Are Nowhere And It's Now", 'artist_id': '5o206eFLx38glA2bb4zqIU', 'artist_name': 'Bright Eyes', 'album_name': "I'm Wide Awake, It's Morning", 'track_number': 2, 'duration_ms': 252933, 'popularity': 51, 'danceability': 0.413, 'energy': 0.537, 'loudness': -9.957, 'speechiness': 0.0323, 'acousticness': 0.0766, 'instrumentalness': 0.0195, 'liveness': 0.154, 'valence': 0.531, 'tempo': 147.076}, '558BHSecDFS85E2L2aKzP8': {'name': 'Land Locked Blues', 'artist_id': '5o206eFLx38glA2bb4zqIU', 'artist_name': 'Bright Eyes', 'album_name': "I'm Wide Awake, It's Morning", 'track_number': 8, 'duration_ms': 347733, 'popularity': 50, 'danceability': 0.479, 'energy': 0.259, 'loudness': -11.928, 'speechiness': 0.0681, 'acousticness': 0.831, 'instrumentalness': 0, 'liveness': 0.142, 'valence': 0.338, 'tempo': 137.911}, '7C4LTWRsikDhkxXrgc29q0': {'name': 'Poison Oak', 'artist_id': '5o206eFLx38glA2bb4zqIU', 'artist_name': 'Bright Eyes', 'album_name': "I'm Wide Awake, It's Morning", 'track_number': 9, 'duration_ms': 279866, 'popularity': 49, 'danceability': 0.399, 'energy': 0.185, 'loudness': -11.373, 'speechiness': 0.0344, 'acousticness': 0.153, 'instrumentalness': 0.0104, 'liveness': 0.166, 'valence': 0.183, 'tempo': 96.376}, '6588w3GdDxmdtLMLuwf1tO': {'name': 'At The Bottom Of Everything', 'artist_id': '5o206eFLx38glA2bb4zqIU', 'artist_name': 'Bright Eyes', 'album_name': "I'm Wide Awake, It's Morning", 'track_number': 1, 'duration_ms': 274000, 'popularity': 49, 'danceability': 0.495, 'energy': 0.46, 'loudness': -11.221, 'speechiness': 0.0894, 'acousticness': 0.664, 'instrumentalness': 0, 'liveness': 0.325, 'valence': 0.831, 'tempo': 107.326}, '1PW6GA54DjaQDwKU4ATCDE': {'name': 'Road To Joy', 'artist_id': '5o206eFLx38glA2bb4zqIU', 'artist_name': 'Bright Eyes', 'album_name': "I'm Wide Awake, It's Morning", 'track_number': 10, 'duration_ms': 234906, 'popularity': 48, 'danceability': 0.33, 'energy': 0.592, 'loudness': -8.567, 'speechiness': 0.03, 'acousticness': 0.032, 'instrumentalness': 0.00173, 'liveness': 0.115, 'valence': 0.127, 'tempo': 146.599}, '20Lo9M6nfdIAWrzPPV4yY0': {'name': 'Devil Town', 'artist_id': '5o206eFLx38glA2bb4zqIU', 'artist_name': 'Bright Eyes', 'album_name': 'Noise Floor (Rarities: 1998-2005)', 'track_number': 13, 'duration_ms': 183240, 'popularity': 47, 'danceability': 0.216, 'energy': 0.53, 'loudness': -8.456, 'speechiness': 0.0372, 'acousticness': 0.164, 'instrumentalness': 7.4e-05, 'liveness': 0.25, 'valence': 0.361, 'tempo': 84.152}, '1fPLarHjgMC9QlsHfPijbr': {'name': "Lover I Don't Have To Love", 'artist_id': '5o206eFLx38glA2bb4zqIU', 'artist_name': 'Bright Eyes', 'album_name': 'LIFTED Or The Story Is In The Soil, Keep Your Ear To The Ground', 'track_number': 5, 'duration_ms': 240106, 'popularity': 45, 'danceability': 0.516, 'energy': 0.714, 'loudness': -7.772, 'speechiness': 0.0393, 'acousticness': 0.154, 'instrumentalness': 0.00136, 'liveness': 0.106, 'valence': 0.505, 'tempo': 80.614}, '4gSYPXqENGdaJiwm6W0hkQ': {'name': 'Atlas Hands', 'artist_id': '7D5oTJSXSHf51auG0106CQ', 'artist_name': 'Benjamin Francis Leftwich', 'album_name': 'Last Smoke Before the Snowstorm', 'track_number': 5, 'duration_ms': 173080, 'popularity': 55, 'danceability': 0.638, 'energy': 0.308, 'loudness': -11.89, 'speechiness': 0.0301, 'acousticness': 0.889, 'instrumentalness': 0.000853, 'liveness': 0.0543, 'valence': 0.463, 'tempo': 82.527}, '4sVnlrSGaRwnBaj35C2wXu': {'name': 'Tilikum', 'artist_id': '7D5oTJSXSHf51auG0106CQ', 'artist_name': 'Benjamin Francis Leftwich', 'album_name': 'After the Rain', 'track_number': 1, 'duration_ms': 286746, 'popularity': 42, 'danceability': 0.457, 'energy': 0.324, 'loudness': -15.459, 'speechiness': 0.031, 'acousticness': 0.926, 'instrumentalness': 0.00717, 'liveness': 0.108, 'valence': 0.363, 'tempo': 129.131}, '2cEBG31c2Y7mfRlLY8g1ah': {'name': 'Pictures', 'artist_id': '7D5oTJSXSHf51auG0106CQ', 'artist_name': 'Benjamin Francis Leftwich', 'album_name': 'Last Smoke Before the Snowstorm', 'track_number': 1, 'duration_ms': 177533, 'popularity': 49, 'danceability': 0.547, 'energy': 0.313, 'loudness': -10.313, 'speechiness': 0.0352, 'acousticness': 0.935, 'instrumentalness': 6.05e-06, 'liveness': 0.1, 'valence': 0.324, 'tempo': 141.177}, '2PLh0v3da9bVrRE6o8AWT8': {'name': 'Atlas Hands - Thomas Jack Remix', 'artist_id': '7D5oTJSXSHf51auG0106CQ', 'artist_name': 'Benjamin Francis Leftwich', 'album_name': 'Atlas Hands (Thomas Jack Remix)', 'track_number': 1, 'duration_ms': 327476, 'popularity': 41, 'danceability': 0.839, 'energy': 0.484, 'loudness': -9.766, 'speechiness': 0.134, 'acousticness': 0.0251, 'instrumentalness': 0.326, 'liveness': 0.304, 'valence': 0.624, 'tempo': 107.007}, '5FyxzFb5qOTtl9fCMFT20D': {'name': 'Shine (Kygo Remix)', 'artist_id': '7D5oTJSXSHf51auG0106CQ', 'artist_name': 'Benjamin Francis Leftwich', 'album_name': 'Shine (Kygo Remix)', 'track_number': 1, 'duration_ms': 281133, 'popularity': 42, 'danceability': 0.703, 'energy': 0.603, 'loudness': -8.687, 'speechiness': 0.161, 'acousticness': 0.413, 'instrumentalness': 0.00125, 'liveness': 0.141, 'valence': 0.314, 'tempo': 112.015}, '3tF1VBq5c91U1aN2aWrjfP': {'name': 'Just Breathe', 'artist_id': '7D5oTJSXSHf51auG0106CQ', 'artist_name': 'Benjamin Francis Leftwich', 'album_name': 'After the Rain', 'track_number': 6, 'duration_ms': 228093, 'popularity': 38, 'danceability': 0.625, 'energy': 0.535, 'loudness': -9.17, 'speechiness': 0.0279, 'acousticness': 0.773, 'instrumentalness': 0.00016, 'liveness': 0.116, 'valence': 0.369, 'tempo': 118.026}, '4bvtfm8XL26qmM2vliZfMP': {'name': 'Super 8 Eyes', 'artist_id': '7D5oTJSXSHf51auG0106CQ', 'artist_name': 'Benjamin Francis Leftwich', 'album_name': 'Super 8 Eyes', 'track_number': 1, 'duration_ms': 275080, 'popularity': 43, 'danceability': 0.502, 'energy': 0.178, 'loudness': -16.601, 'speechiness': 0.0316, 'acousticness': 0.955, 'instrumentalness': 0.00181, 'liveness': 0.215, 'valence': 0.324, 'tempo': 109.984}, '4E8Zv4wFRUsFJtpnsoT01V': {'name': 'She Will Sing', 'artist_id': '7D5oTJSXSHf51auG0106CQ', 'artist_name': 'Benjamin Francis Leftwich', 'album_name': 'After the Rain', 'track_number': 3, 'duration_ms': 224413, 'popularity': 33, 'danceability': 0.606, 'energy': 0.806, 'loudness': -7.638, 'speechiness': 0.0327, 'acousticness': 0.497, 'instrumentalness': 0.000365, 'liveness': 0.115, 'valence': 0.406, 'tempo': 130.006}, '7IJK1KdKnLNl9fv21eh7h2': {'name': 'Snowship - Thomas Jack Remix', 'artist_id': '7D5oTJSXSHf51auG0106CQ', 'artist_name': 'Benjamin Francis Leftwich', 'album_name': 'Snowship (Thomas Jack Remix)', 'track_number': 1, 'duration_ms': 336000, 'popularity': 38, 'danceability': 0.847, 'energy': 0.587, 'loudness': -8.074, 'speechiness': 0.0581, 'acousticness': 0.0472, 'instrumentalness': 0.00418, 'liveness': 0.175, 'valence': 0.496, 'tempo': 105.026}, '6wycnu8FWXsj68ig7BEot9': {'name': "Blue Ain't Your Color", 'artist_id': '0u2FHSq3ln94y5Q57xazwf', 'artist_name': 'Keith Urban', 'album_name': 'Ripcord', 'track_number': 7, 'duration_ms': 230600, 'popularity': 77, 'danceability': 0.686, 'energy': 0.417, 'loudness': -7.787, 'speechiness': 0.0363, 'acousticness': 0.606, 'instrumentalness': 1.79e-06, 'liveness': 0.0844, 'valence': 0.45, 'tempo': 82.407}, '5OUSPcqhYTOzpbXzoEvKim': {'name': 'The Fighter', 'artist_id': '0u2FHSq3ln94y5Q57xazwf', 'artist_name': 'Keith Urban', 'album_name': 'Ripcord', 'track_number': 8, 'duration_ms': 184040, 'popularity': 76, 'danceability': 0.681, 'energy': 0.845, 'loudness': -5.147, 'speechiness': 0.0525, 'acousticness': 0.0304, 'instrumentalness': 0, 'liveness': 0.197, 'valence': 0.761, 'tempo': 132.023}, '13wYXGimJ5fANFu0y2pqG1': {'name': 'Wasted Time', 'artist_id': '0u2FHSq3ln94y5Q57xazwf', 'artist_name': 'Keith Urban', 'album_name': 'Ripcord', 'track_number': 3, 'duration_ms': 233826, 'popularity': 68, 'danceability': 0.626, 'energy': 0.831, 'loudness': -5.69, 'speechiness': 0.0481, 'acousticness': 0.0628, 'instrumentalness': 0, 'liveness': 0.0799, 'valence': 0.314, 'tempo': 100.009}, '0b9djfiuDIMw1zKH6gV74g': {'name': 'Somebody Like You', 'artist_id': '0u2FHSq3ln94y5Q57xazwf', 'artist_name': 'Keith Urban', 'album_name': 'Golden Road', 'track_number': 1, 'duration_ms': 323040, 'popularity': 44, 'danceability': 0.624, 'energy': 0.84, 'loudness': -5.768, 'speechiness': 0.0337, 'acousticness': 0.108, 'instrumentalness': 0.000546, 'liveness': 0.144, 'valence': 0.649, 'tempo': 111.02}, '72f7jNxopSGvbx3M35i3Zl': {'name': 'John Cougar, John Deere, John 3:16', 'artist_id': '0u2FHSq3ln94y5Q57xazwf', 'artist_name': 'Keith Urban', 'album_name': 'Ripcord', 'track_number': 2, 'duration_ms': 221600, 'popularity': 60, 'danceability': 0.644, 'energy': 0.776, 'loudness': -6.967, 'speechiness': 0.0929, 'acousticness': 0.0606, 'instrumentalness': 3.77e-06, 'liveness': 0.0795, 'valence': 0.596, 'tempo': 170.036}, '0lZxd99ZIjA0zUdQAY3FXr': {'name': "You'll Think Of Me", 'artist_id': '0u2FHSq3ln94y5Q57xazwf', 'artist_name': 'Keith Urban', 'album_name': 'Greatest Hits - 18 Kids', 'track_number': 12, 'duration_ms': 231293, 'popularity': 62, 'danceability': 0.55, 'energy': 0.543, 'loudness': -8.395, 'speechiness': 0.0408, 'acousticness': 0.379, 'instrumentalness': 0, 'liveness': 0.0927, 'valence': 0.575, 'tempo': 82.761}, '3MFV4DgrAOXz6KURPQxRj9': {'name': 'Somewhere In My Car', 'artist_id': '0u2FHSq3ln94y5Q57xazwf', 'artist_name': 'Keith Urban', 'album_name': 'Somewhere In My Car', 'track_number': 1, 'duration_ms': 195973, 'popularity': 62, 'danceability': 0.584, 'energy': 0.866, 'loudness': -5.511, 'speechiness': 0.0419, 'acousticness': 0.00535, 'instrumentalness': 2.92e-05, 'liveness': 0.0858, 'valence': 0.495, 'tempo': 118.005}, '61hmCqoIlTJjcVMMLhcH5n': {'name': 'Tonight I Wanna Cry', 'artist_id': '0u2FHSq3ln94y5Q57xazwf', 'artist_name': 'Keith Urban', 'album_name': 'Be Here', 'track_number': 8, 'duration_ms': 259506, 'popularity': 48, 'danceability': 0.579, 'energy': 0.385, 'loudness': -7.885, 'speechiness': 0.0256, 'acousticness': 0.88, 'instrumentalness': 2.17e-06, 'liveness': 0.164, 'valence': 0.135, 'tempo': 103.779}, '5vCgOg9VqRaAUbnflCO6P3': {'name': 'Cop Car', 'artist_id': '0u2FHSq3ln94y5Q57xazwf', 'artist_name': 'Keith Urban', 'album_name': 'Fuse (Deluxe Edition)', 'track_number': 3, 'duration_ms': 256746, 'popularity': 61, 'danceability': 0.536, 'energy': 0.662, 'loudness': -6.245, 'speechiness': 0.0388, 'acousticness': 0.167, 'instrumentalness': 0, 'liveness': 0.0973, 'valence': 0.377, 'tempo': 154.022}, '7zHKBxCMAc9Qt6OrIaUmyi': {'name': 'Long Hot Summer', 'artist_id': '0u2FHSq3ln94y5Q57xazwf', 'artist_name': 'Keith Urban', 'album_name': 'Get Closer', 'track_number': 4, 'duration_ms': 272230, 'popularity': 38, 'danceability': 0.657, 'energy': 0.785, 'loudness': -8.428, 'speechiness': 0.037, 'acousticness': 0.0301, 'instrumentalness': 4.62e-06, 'liveness': 0.0927, 'valence': 0.759, 'tempo': 127.987}, '4dGJf1SER1T6ooX46vwzRB': {'name': 'Chicken Fried', 'artist_id': '6yJCxee7QumYr820xdIsjo', 'artist_name': 'Zac Brown Band', 'album_name': 'The Foundation', 'track_number': 6, 'duration_ms': 238146, 'popularity': 74, 'danceability': 0.566, 'energy': 0.713, 'loudness': -4.25, 'speechiness': 0.0417, 'acousticness': 0.645, 'instrumentalness': 0, 'liveness': 0.114, 'valence': 0.791, 'tempo': 169.864}, '31lhygAGEsvwcUvhakP6yY': {'name': 'My Old Man', 'artist_id': '6yJCxee7QumYr820xdIsjo', 'artist_name': 'Zac Brown Band', 'album_name': 'My Old Man', 'track_number': 1, 'duration_ms': 227222, 'popularity': 73, 'danceability': 0.64, 'energy': 0.196, 'loudness': -11.478, 'speechiness': 0.0267, 'acousticness': 0.819, 'instrumentalness': 3.63e-05, 'liveness': 0.0978, 'valence': 0.273, 'tempo': 143.919}, '1yEwEiTpsaPhQi9lb5EVV4': {'name': 'Knee Deep (feat. Jimmy Buffett)', 'artist_id': '6yJCxee7QumYr820xdIsjo', 'artist_name': 'Zac Brown Band', 'album_name': 'You Get What You Give (Deluxe)', 'track_number': 2, 'duration_ms': 203173, 'popularity': 70, 'danceability': 0.715, 'energy': 0.584, 'loudness': -8.231, 'speechiness': 0.0296, 'acousticness': 0.432, 'instrumentalness': 1.41e-06, 'liveness': 0.095, 'valence': 0.6, 'tempo': 90.987}, '1qwnPVOIJjAFfCc40Etb1D': {'name': 'Homegrown', 'artist_id': '6yJCxee7QumYr820xdIsjo', 'artist_name': 'Zac Brown Band', 'album_name': 'JEKYLL + HYDE', 'track_number': 4, 'duration_ms': 205000, 'popularity': 69, 'danceability': 0.717, 'energy': 0.796, 'loudness': -3.677, 'speechiness': 0.0303, 'acousticness': 0.0189, 'instrumentalness': 8.94e-05, 'liveness': 0.19, 'valence': 0.949, 'tempo': 105.017}, '5kjyiH6but1t2UDXq15aeS': {'name': 'Toes', 'artist_id': '6yJCxee7QumYr820xdIsjo', 'artist_name': 'Zac Brown Band', 'album_name': 'The Foundation', 'track_number': 1, 'duration_ms': 262773, 'popularity': 69, 'danceability': 0.8, 'energy': 0.759, 'loudness': -5.398, 'speechiness': 0.0378, 'acousticness': 0.655, 'instrumentalness': 0, 'liveness': 0.0897, 'valence': 0.831, 'tempo': 129.979}, '69XcvSymPaTke2Qb6f3W6P': {'name': 'Loving You Easy', 'artist_id': '6yJCxee7QumYr820xdIsjo', 'artist_name': 'Zac Brown Band', 'album_name': 'JEKYLL + HYDE', 'track_number': 2, 'duration_ms': 155653, 'popularity': 66, 'danceability': 0.722, 'energy': 0.593, 'loudness': -3.953, 'speechiness': 0.0269, 'acousticness': 0.017, 'instrumentalness': 1.42e-06, 'liveness': 0.067, 'valence': 0.329, 'tempo': 98.982}, '0vcfOQOvTCv8ckiRs8Xc1Z': {'name': 'Beautiful Drug', 'artist_id': '6yJCxee7QumYr820xdIsjo', 'artist_name': 'Zac Brown Band', 'album_name': 'JEKYLL + HYDE', 'track_number': 1, 'duration_ms': 191600, 'popularity': 64, 'danceability': 0.61, 'energy': 0.857, 'loudness': -5.267, 'speechiness': 0.0877, 'acousticness': 0.0424, 'instrumentalness': 2e-06, 'liveness': 0.128, 'valence': 0.365, 'tempo': 125.838}, '1M2l9ReoabUnvl6Y8jLUe7': {'name': 'Colder Weather', 'artist_id': '6yJCxee7QumYr820xdIsjo', 'artist_name': 'Zac Brown Band', 'album_name': 'You Get What You Give (Deluxe)', 'track_number': 8, 'duration_ms': 273893, 'popularity': 64, 'danceability': 0.667, 'energy': 0.381, 'loudness': -7.494, 'speechiness': 0.0294, 'acousticness': 0.458, 'instrumentalness': 0, 'liveness': 0.116, 'valence': 0.206, 'tempo': 135.979}, '5PNcJn4oFNvlRfrZBHfqWh': {'name': 'Castaway', 'artist_id': '6yJCxee7QumYr820xdIsjo', 'artist_name': 'Zac Brown Band', 'album_name': 'JEKYLL + HYDE', 'track_number': 8, 'duration_ms': 188053, 'popularity': 64, 'danceability': 0.634, 'energy': 0.78, 'loudness': -4.928, 'speechiness': 0.0477, 'acousticness': 0.161, 'instrumentalness': 0, 'liveness': 0.112, 'valence': 0.932, 'tempo': 101.066}, '71zbcnCMLpQ8SPSv6sFlqF': {'name': 'Real Thing', 'artist_id': '6yJCxee7QumYr820xdIsjo', 'artist_name': 'Zac Brown Band', 'album_name': 'Real Thing', 'track_number': 1, 'duration_ms': 230721, 'popularity': 62, 'danceability': 0.533, 'energy': 0.533, 'loudness': -8.266, 'speechiness': 0.0324, 'acousticness': 0.0915, 'instrumentalness': 0, 'liveness': 0.0972, 'valence': 0.506, 'tempo': 159.907}, '3kZC0ZmFWrEHdUCmUqlvgZ': {'name': 'I Will Follow You Into The Dark', 'artist_id': '0YrtvWJMgSdVrk3SfNjTbx', 'artist_name': 'Death Cab for Cutie', 'album_name': 'Plans', 'track_number': 5, 'duration_ms': 189186, 'popularity': 67, 'danceability': 0.517, 'energy': 0.206, 'loudness': -12.233, 'speechiness': 0.0421, 'acousticness': 0.924, 'instrumentalness': 0, 'liveness': 0.118, 'valence': 0.486, 'tempo': 80.401}, '59FC22eN2Syt9bbv2d6393': {'name': 'Black Sun', 'artist_id': '0YrtvWJMgSdVrk3SfNjTbx', 'artist_name': 'Death Cab for Cutie', 'album_name': 'Kintsugi', 'track_number': 2, 'duration_ms': 289160, 'popularity': 61, 'danceability': 0.608, 'energy': 0.642, 'loudness': -7.978, 'speechiness': 0.0251, 'acousticness': 0.17, 'instrumentalness': 0.0667, 'liveness': 0.166, 'valence': 0.607, 'tempo': 87.703}, '5yc59J3MR3tVDPTOgwgRI5': {'name': 'Soul Meets Body', 'artist_id': '0YrtvWJMgSdVrk3SfNjTbx', 'artist_name': 'Death Cab for Cutie', 'album_name': 'Plans', 'track_number': 2, 'duration_ms': 229413, 'popularity': 60, 'danceability': 0.621, 'energy': 0.853, 'loudness': -5.735, 'speechiness': 0.0253, 'acousticness': 0.0767, 'instrumentalness': 3.26e-06, 'liveness': 0.0893, 'valence': 0.725, 'tempo': 128.142}, '7DDRPKLKFIvDbNSQmnz19Y': {'name': 'Transatlanticism', 'artist_id': '0YrtvWJMgSdVrk3SfNjTbx', 'artist_name': 'Death Cab for Cutie', 'album_name': 'Transatlanticism', 'track_number': 7, 'duration_ms': 475093, 'popularity': 59, 'danceability': 0.439, 'energy': 0.469, 'loudness': -9.283, 'speechiness': 0.0311, 'acousticness': 0.395, 'instrumentalness': 0.573, 'liveness': 0.183, 'valence': 0.191, 'tempo': 127.44}, '6wNCdMW82LwJgFrnGqLhpJ': {'name': 'The Ghosts Of Beverly Drive', 'artist_id': '0YrtvWJMgSdVrk3SfNjTbx', 'artist_name': 'Death Cab for Cutie', 'album_name': 'Kintsugi', 'track_number': 3, 'duration_ms': 243253, 'popularity': 59, 'danceability': 0.557, 'energy': 0.859, 'loudness': -6.557, 'speechiness': 0.0582, 'acousticness': 0.00474, 'instrumentalness': 5.79e-05, 'liveness': 0.103, 'valence': 0.745, 'tempo': 154.718}, '77vYwoC7e3pVoPq8BA9CuL': {'name': 'I Will Possess Your Heart', 'artist_id': '0YrtvWJMgSdVrk3SfNjTbx', 'artist_name': 'Death Cab for Cutie', 'album_name': 'Narrow Stairs', 'track_number': 2, 'duration_ms': 505773, 'popularity': 55, 'danceability': 0.605, 'energy': 0.619, 'loudness': -8.971, 'speechiness': 0.0261, 'acousticness': 0.423, 'instrumentalness': 0.313, 'liveness': 0.0732, 'valence': 0.571, 'tempo': 133.074}, '7C1p70Zs3pBZEQGeWMF8sS': {'name': 'Good Help (Is So Hard To Find)', 'artist_id': '0YrtvWJMgSdVrk3SfNjTbx', 'artist_name': 'Death Cab for Cutie', 'album_name': 'Kintsugi', 'track_number': 8, 'duration_ms': 285600, 'popularity': 55, 'danceability': 0.705, 'energy': 0.856, 'loudness': -5.921, 'speechiness': 0.0423, 'acousticness': 0.0414, 'instrumentalness': 0.00228, 'liveness': 0.0666, 'valence': 0.775, 'tempo': 117.005}, '4mCF3EBgGPSqmEm205KBAV': {'name': 'A Lack Of Color', 'artist_id': '0YrtvWJMgSdVrk3SfNjTbx', 'artist_name': 'Death Cab for Cutie', 'album_name': 'Transatlanticism', 'track_number': 11, 'duration_ms': 215933, 'popularity': 53, 'danceability': 0.642, 'energy': 0.339, 'loudness': -11.884, 'speechiness': 0.0291, 'acousticness': 0.81, 'instrumentalness': 0.000751, 'liveness': 0.108, 'valence': 0.35, 'tempo': 135.812}, '7DkTneByAopqOjXFG6XlZK': {'name': 'No Room In Frame', 'artist_id': '0YrtvWJMgSdVrk3SfNjTbx', 'artist_name': 'Death Cab for Cutie', 'album_name': 'Kintsugi', 'track_number': 1, 'duration_ms': 245280, 'popularity': 53, 'danceability': 0.642, 'energy': 0.721, 'loudness': -9.765, 'speechiness': 0.0434, 'acousticness': 0.196, 'instrumentalness': 0.474, 'liveness': 0.0926, 'valence': 0.458, 'tempo': 124.997}, '0d3BJRrklQ6sTfbmrojuZI': {'name': "Don't Take The Money", 'artist_id': '2eam0iDomRHGBypaDQLwWI', 'artist_name': 'Bleachers', 'album_name': "Don't Take The Money", 'track_number': 1, 'duration_ms': 215539, 'popularity': 71, 'danceability': 0.633, 'energy': 0.884, 'loudness': -5.667, 'speechiness': 0.0392, 'acousticness': 0.00036, 'instrumentalness': 1.64e-06, 'liveness': 0.189, 'valence': 0.287, 'tempo': 110.081}, '5L95vS64rG1YMIFm1hLjyZ': {'name': 'Rollercoaster', 'artist_id': '2eam0iDomRHGBypaDQLwWI', 'artist_name': 'Bleachers', 'album_name': 'Strange Desire', 'track_number': 2, 'duration_ms': 188866, 'popularity': 62, 'danceability': 0.421, 'energy': 0.79, 'loudness': -6.227, 'speechiness': 0.0538, 'acousticness': 0.00205, 'instrumentalness': 0.000309, 'liveness': 0.148, 'valence': 0.275, 'tempo': 162.024}, '1BwhFXqoIsePt21WyWIttb': {'name': 'I Wanna Get Better', 'artist_id': '2eam0iDomRHGBypaDQLwWI', 'artist_name': 'Bleachers', 'album_name': 'Strange Desire', 'track_number': 4, 'duration_ms': 204520, 'popularity': 60, 'danceability': 0.446, 'energy': 0.915, 'loudness': -6.221, 'speechiness': 0.141, 'acousticness': 0.00281, 'instrumentalness': 3.87e-05, 'liveness': 0.218, 'valence': 0.402, 'tempo': 190.013}, '5li3FHS5s9V3l4xWsUcmQa': {'name': 'Entropy', 'artist_id': '053q0ukIDRgzwTr4vNSwab', 'artist_name': 'Grimes', 'album_name': 'Entropy', 'track_number': 1, 'duration_ms': 183493, 'popularity': 59, 'danceability': 0.756, 'energy': 0.624, 'loudness': -6.623, 'speechiness': 0.0384, 'acousticness': 0.313, 'instrumentalness': 0.31, 'liveness': 0.0983, 'valence': 0.773, 'tempo': 109.53}, '7tY8crx0ZaIS4yScJcKaiU': {'name': 'Like a River Runs', 'artist_id': '2eam0iDomRHGBypaDQLwWI', 'artist_name': 'Bleachers', 'album_name': 'Terrible Thrills, Vol. 2', 'track_number': 8, 'duration_ms': 237586, 'popularity': 55, 'danceability': 0.255, 'energy': 0.243, 'loudness': -11.194, 'speechiness': 0.0384, 'acousticness': 0.84, 'instrumentalness': 2.36e-06, 'liveness': 0.187, 'valence': 0.136, 'tempo': 89.258}, '6YArGkJUr82ehzRFa2YaRK': {'name': 'Wake Me', 'artist_id': '2eam0iDomRHGBypaDQLwWI', 'artist_name': 'Bleachers', 'album_name': 'Strange Desire', 'track_number': 5, 'duration_ms': 163880, 'popularity': 55, 'danceability': 0.818, 'energy': 0.374, 'loudness': -10.666, 'speechiness': 0.0459, 'acousticness': 0.0951, 'instrumentalness': 0.0139, 'liveness': 0.217, 'valence': 0.455, 'tempo': 117.956}, '3Ao4MeZQu5BA3H3K2QeBl2': {'name': 'Rollercoaster', 'artist_id': '2eam0iDomRHGBypaDQLwWI', 'artist_name': 'Bleachers', 'album_name': 'Terrible Thrills, Vol. 2', 'track_number': 2, 'duration_ms': 187466, 'popularity': 54, 'danceability': 0.543, 'energy': 0.845, 'loudness': -6.384, 'speechiness': 0.0553, 'acousticness': 0.00208, 'instrumentalness': 0.136, 'liveness': 0.248, 'valence': 0.445, 'tempo': 162.005}, '7pK4jm4HiNaYVzL2zbQSoG': {'name': 'Wild Heart', 'artist_id': '2eam0iDomRHGBypaDQLwWI', 'artist_name': 'Bleachers', 'album_name': 'Strange Desire', 'track_number': 1, 'duration_ms': 200386, 'popularity': 52, 'danceability': 0.552, 'energy': 0.941, 'loudness': -8.256, 'speechiness': 0.0415, 'acousticness': 0.318, 'instrumentalness': 0.0655, 'liveness': 0.33, 'valence': 0.558, 'tempo': 159.594}, '06zKjN3gV8JDNQVz9HwQ3C': {'name': 'Hate That You Know Me', 'artist_id': '2eam0iDomRHGBypaDQLwWI', 'artist_name': 'Bleachers', 'album_name': 'Hate That You Know Me', 'track_number': 1, 'duration_ms': 185855, 'popularity': 50, 'danceability': 0.775, 'energy': 0.56, 'loudness': -7.194, 'speechiness': 0.136, 'acousticness': 0.0271, 'instrumentalness': 0, 'liveness': 0.0495, 'valence': 0.536, 'tempo': 109.475}, '0DdJoUPb3VXOZ9zl0vAwHn': {'name': 'Take Me Away', 'artist_id': '2eam0iDomRHGBypaDQLwWI', 'artist_name': 'Bleachers', 'album_name': 'Strange Desire', 'track_number': 7, 'duration_ms': 150453, 'popularity': 50, 'danceability': 0.606, 'energy': 0.312, 'loudness': -11.43, 'speechiness': 0.0332, 'acousticness': 0.767, 'instrumentalness': 0.00803, 'liveness': 0.0508, 'valence': 0.424, 'tempo': 120.074}, '7otCGmgp9h4CsR2LhwB6gt': {'name': 'Another Love', 'artist_id': '2txHhyCwHjUEpJjWrEyqyX', 'artist_name': 'Tom Odell', 'album_name': 'Long Way Down', 'track_number': 3, 'duration_ms': 244360, 'popularity': 63, 'danceability': 0.445, 'energy': 0.537, 'loudness': -8.532, 'speechiness': 0.04, 'acousticness': 0.695, 'instrumentalness': 1.6e-05, 'liveness': 0.0941, 'valence': 0.126, 'tempo': 122.764}, '5snyhxAh55A2wlNRH7VVZJ': {'name': 'Another Love - Zwette Edit', 'artist_id': '2txHhyCwHjUEpJjWrEyqyX', 'artist_name': 'Tom Odell', 'album_name': 'Another Love (Zwette Edit)', 'track_number': 1, 'duration_ms': 394573, 'popularity': 69, 'danceability': 0.87, 'energy': 0.554, 'loudness': -5.828, 'speechiness': 0.0635, 'acousticness': 0.0802, 'instrumentalness': 0.0739, 'liveness': 0.115, 'valence': 0.467, 'tempo': 123.998}, '5baXzOMmD0sf26hayRqfqI': {'name': 'Magnetised - Acoustic', 'artist_id': '2txHhyCwHjUEpJjWrEyqyX', 'artist_name': 'Tom Odell', 'album_name': 'Magnetised (Acoustic)', 'track_number': 1, 'duration_ms': 292186, 'popularity': 67, 'danceability': 0.487, 'energy': 0.0746, 'loudness': -12.952, 'speechiness': 0.0327, 'acousticness': 0.952, 'instrumentalness': 0, 'liveness': 0.108, 'valence': 0.131, 'tempo': 106.328}, '1xVF9wZZ87uAz0bw6jT4sH': {'name': 'Heal', 'artist_id': '2txHhyCwHjUEpJjWrEyqyX', 'artist_name': 'Tom Odell', 'album_name': 'Long Way Down', 'track_number': 13, 'duration_ms': 195240, 'popularity': 61, 'danceability': 0.455, 'energy': 0.179, 'loudness': -12.938, 'speechiness': 0.0389, 'acousticness': 0.952, 'instrumentalness': 0.00056, 'liveness': 0.106, 'valence': 0.113, 'tempo': 73.698}, '1rGxG6Y5OgmSwGPRPJv9Q4': {'name': 'True Colours', 'artist_id': '2txHhyCwHjUEpJjWrEyqyX', 'artist_name': 'Tom Odell', 'album_name': 'True Colours', 'track_number': 1, 'duration_ms': 143706, 'popularity': 62, 'danceability': 0.518, 'energy': 0.126, 'loudness': -12.102, 'speechiness': 0.0431, 'acousticness': 0.942, 'instrumentalness': 0, 'liveness': 0.105, 'valence': 0.159, 'tempo': 75.991}, '4JBNKQg27FoumUSo96r2pk': {'name': 'Magnetised', 'artist_id': '2txHhyCwHjUEpJjWrEyqyX', 'artist_name': 'Tom Odell', 'album_name': 'Wrong Crowd (Deluxe)', 'track_number': 2, 'duration_ms': 235133, 'popularity': 61, 'danceability': 0.606, 'energy': 0.821, 'loudness': -3.946, 'speechiness': 0.0451, 'acousticness': 0.0229, 'instrumentalness': 0, 'liveness': 0.131, 'valence': 0.198, 'tempo': 125.021}, '1DxjoJ2w0K9zQ8KgU9rXhr': {'name': 'Here I Am', 'artist_id': '2txHhyCwHjUEpJjWrEyqyX', 'artist_name': 'Tom Odell', 'album_name': 'Wrong Crowd (Deluxe)', 'track_number': 10, 'duration_ms': 207440, 'popularity': 59, 'danceability': 0.707, 'energy': 0.838, 'loudness': -4.109, 'speechiness': 0.0336, 'acousticness': 0.0903, 'instrumentalness': 0, 'liveness': 0.368, 'valence': 0.622, 'tempo': 116.534}, '0rhJ30qQSus6Ckn3hKZ6Hr': {'name': 'Another Love - Live from Spotify (SXSW)', 'artist_id': '2txHhyCwHjUEpJjWrEyqyX', 'artist_name': 'Tom Odell', 'album_name': 'Spotify Sessions', 'track_number': 4, 'duration_ms': 257266, 'popularity': 59, 'danceability': 0.453, 'energy': 0.586, 'loudness': -6.741, 'speechiness': 0.0395, 'acousticness': 0.86, 'instrumentalness': 0, 'liveness': 0.751, 'valence': 0.145, 'tempo': 119.306}, '3B61es35RhmjeZgFuG6VV2': {'name': 'Grow Old with Me', 'artist_id': '2txHhyCwHjUEpJjWrEyqyX', 'artist_name': 'Tom Odell', 'album_name': 'Long Way Down', 'track_number': 1, 'duration_ms': 182720, 'popularity': 47, 'danceability': 0.474, 'energy': 0.583, 'loudness': -7.488, 'speechiness': 0.0278, 'acousticness': 0.509, 'instrumentalness': 0, 'liveness': 0.25, 'valence': 0.352, 'tempo': 146.007}, '23UCOmWmenFhxFQG71tTKL': {'name': 'Long Way Down', 'artist_id': '2txHhyCwHjUEpJjWrEyqyX', 'artist_name': 'Tom Odell', 'album_name': 'Long Way Down', 'track_number': 9, 'duration_ms': 149773, 'popularity': 52, 'danceability': 0.367, 'energy': 0.121, 'loudness': -13.778, 'speechiness': 0.0335, 'acousticness': 0.972, 'instrumentalness': 0.0322, 'liveness': 0.0871, 'valence': 0.0812, 'tempo': 132.244}, '57FqmzNGTziRPCyuqaUrHo': {'name': 'First Defeat', 'artist_id': '34482S5nfxR441wcnVfrHi', 'artist_name': 'Noah Gundersen', 'album_name': 'Ledges', 'track_number': 7, 'duration_ms': 243773, 'popularity': 56, 'danceability': 0.519, 'energy': 0.214, 'loudness': -11.243, 'speechiness': 0.0298, 'acousticness': 0.858, 'instrumentalness': 0.0021, 'liveness': 0.118, 'valence': 0.22, 'tempo': 144.411}, '4EC81x7yH6ncvo3Fox53C8': {'name': 'Family', 'artist_id': '34482S5nfxR441wcnVfrHi', 'artist_name': 'Noah Gundersen', 'album_name': 'Family', 'track_number': 7, 'duration_ms': 214840, 'popularity': 50, 'danceability': 0.507, 'energy': 0.201, 'loudness': -11.836, 'speechiness': 0.0324, 'acousticness': 0.751, 'instrumentalness': 0.000551, 'liveness': 0.173, 'valence': 0.147, 'tempo': 110.93}, '2CtHCWOxvOL33wm2OyHOtj': {'name': 'Day Is Gone - from Sons of Anarchy', 'artist_id': '34482S5nfxR441wcnVfrHi', 'artist_name': 'Noah Gundersen', 'album_name': 'Songs of Anarchy: Vol. 3 (Music from Sons of Anarchy)', 'track_number': 8, 'duration_ms': 264773, 'popularity': 48, 'danceability': 0.362, 'energy': 0.149, 'loudness': -14.546, 'speechiness': 0.0402, 'acousticness': 0.863, 'instrumentalness': 7.84e-05, 'liveness': 0.116, 'valence': 0.186, 'tempo': 117.064}, '0FvKy8AbNlEniYbmoykuBN': {'name': 'Blossom', 'artist_id': '34482S5nfxR441wcnVfrHi', 'artist_name': 'Noah Gundersen', 'album_name': 'Carry The Ghost (Deluxe Edition)', 'track_number': 10, 'duration_ms': 223853, 'popularity': 48, 'danceability': 0.435, 'energy': 0.279, 'loudness': -11.405, 'speechiness': 0.0271, 'acousticness': 0.857, 'instrumentalness': 0.0122, 'liveness': 0.111, 'valence': 0.161, 'tempo': 150.011}, '4DuC9BznEnlwTwHQhWLzNt': {'name': 'David', 'artist_id': '34482S5nfxR441wcnVfrHi', 'artist_name': 'Noah Gundersen', 'album_name': 'Family', 'track_number': 1, 'duration_ms': 219026, 'popularity': 44, 'danceability': 0.3, 'energy': 0.626, 'loudness': -8.742, 'speechiness': 0.0418, 'acousticness': 0.595, 'instrumentalness': 0.000606, 'liveness': 0.286, 'valence': 0.501, 'tempo': 79.232}, '25eV7YkYtIohk3vAO9kseu': {'name': "Poor Man's Son", 'artist_id': '34482S5nfxR441wcnVfrHi', 'artist_name': 'Noah Gundersen', 'album_name': 'Ledges', 'track_number': 1, 'duration_ms': 314360, 'popularity': 43, 'danceability': 0.447, 'energy': 0.14, 'loudness': -11.596, 'speechiness': 0.0743, 'acousticness': 0.859, 'instrumentalness': 0, 'liveness': 0.35, 'valence': 0.245, 'tempo': 111.305}, '2Pqp8fhzDlRWevT5XchSUd': {'name': 'Cigarettes', 'artist_id': '34482S5nfxR441wcnVfrHi', 'artist_name': 'Noah Gundersen', 'album_name': 'Ledges', 'track_number': 8, 'duration_ms': 340773, 'popularity': 43, 'danceability': 0.521, 'energy': 0.241, 'loudness': -10.866, 'speechiness': 0.0424, 'acousticness': 0.533, 'instrumentalness': 0.000184, 'liveness': 0.129, 'valence': 0.101, 'tempo': 120.301}, '7J1AXo68jW9zCxUfPKYqyI': {'name': 'Nashville', 'artist_id': '34482S5nfxR441wcnVfrHi', 'artist_name': 'Noah Gundersen', 'album_name': 'Family', 'track_number': 3, 'duration_ms': 217013, 'popularity': 42, 'danceability': 0.365, 'energy': 0.339, 'loudness': -9.45, 'speechiness': 0.0277, 'acousticness': 0.681, 'instrumentalness': 0.000197, 'liveness': 0.0933, 'valence': 0.288, 'tempo': 85.411}, '2EC80pl6LRaWTpErarvN5C': {'name': 'Jealous Love', 'artist_id': '34482S5nfxR441wcnVfrHi', 'artist_name': 'Noah Gundersen', 'album_name': 'Carry The Ghost', 'track_number': 8, 'duration_ms': 206013, 'popularity': 41, 'danceability': 0.506, 'energy': 0.464, 'loudness': -7.365, 'speechiness': 0.0251, 'acousticness': 0.32, 'instrumentalness': 0, 'liveness': 0.125, 'valence': 0.349, 'tempo': 75.985}, '55FRkhs8VGcBiidGnUuyud': {'name': "Don't Lose Your Love", 'artist_id': '3D1IyJznpDnWnnFrzjuWnh', 'artist_name': 'Ivan & Alyosha', 'album_name': "It's All Just Pretend (Deluxe Edition)", 'track_number': 11, 'duration_ms': 205200, 'popularity': 16, 'danceability': 0.435, 'energy': 0.153, 'loudness': -11.536, 'speechiness': 0.0499, 'acousticness': 0.953, 'instrumentalness': 0.00155, 'liveness': 0.11, 'valence': 0.329, 'tempo': 182.647}, '6GZEEoTST2iZcU52LfVDHZ': {'name': 'Running for Cover', 'artist_id': '3D1IyJznpDnWnnFrzjuWnh', 'artist_name': 'Ivan & Alyosha', 'album_name': 'All The Times We Had', 'track_number': 4, 'duration_ms': 236280, 'popularity': 49, 'danceability': 0.295, 'energy': 0.717, 'loudness': -7.537, 'speechiness': 0.0386, 'acousticness': 0.00691, 'instrumentalness': 1.05e-06, 'liveness': 0.101, 'valence': 0.221, 'tempo': 116.95}, '0El2kYoxWlzQKx0BkWSfJC': {'name': 'Easy To Love', 'artist_id': '3D1IyJznpDnWnnFrzjuWnh', 'artist_name': 'Ivan & Alyosha', 'album_name': 'All The Times We Had', 'track_number': 3, 'duration_ms': 216560, 'popularity': 39, 'danceability': 0.545, 'energy': 0.65, 'loudness': -8.806, 'speechiness': 0.024, 'acousticness': 0.246, 'instrumentalness': 0.218, 'liveness': 0.111, 'valence': 0.512, 'tempo': 82.997}, '3z1aYA2vuSXq1wnkcO6DoA': {'name': 'Be Your Man', 'artist_id': '3D1IyJznpDnWnnFrzjuWnh', 'artist_name': 'Ivan & Alyosha', 'album_name': 'All The Times We Had', 'track_number': 1, 'duration_ms': 236480, 'popularity': 37, 'danceability': 0.485, 'energy': 0.824, 'loudness': -7.656, 'speechiness': 0.0542, 'acousticness': 0.00771, 'instrumentalness': 0.000388, 'liveness': 0.0674, 'valence': 0.325, 'tempo': 141.941}, '6MhtBW8JT9gAghWDpysJvu': {'name': 'Oh This Love', 'artist_id': '3D1IyJznpDnWnnFrzjuWnh', 'artist_name': 'Ivan & Alyosha', 'album_name': "It's All Just Pretend (Deluxe Edition)", 'track_number': 6, 'duration_ms': 230186, 'popularity': 17, 'danceability': 0.683, 'energy': 0.662, 'loudness': -4.653, 'speechiness': 0.0291, 'acousticness': 0.0131, 'instrumentalness': 0.00141, 'liveness': 0.21, 'valence': 0.451, 'tempo': 112.899}, '09H2Zbr1089h1ZDIyfZczq': {'name': 'Come Rain, Come Shine', 'artist_id': '3D1IyJznpDnWnnFrzjuWnh', 'artist_name': 'Ivan & Alyosha', 'album_name': "It's All Just Pretend (Deluxe Edition)", 'track_number': 7, 'duration_ms': 209293, 'popularity': 16, 'danceability': 0.503, 'energy': 0.589, 'loudness': -6.314, 'speechiness': 0.0249, 'acousticness': 0.171, 'instrumentalness': 1.08e-05, 'liveness': 0.47, 'valence': 0.348, 'tempo': 83.526}, '59LQFxDuey8k7A4IEtbyPB': {'name': 'All This Wandering Around', 'artist_id': '3D1IyJznpDnWnnFrzjuWnh', 'artist_name': 'Ivan & Alyosha', 'album_name': "It's All Just Pretend (Deluxe Edition)", 'track_number': 3, 'duration_ms': 172466, 'popularity': 17, 'danceability': 0.375, 'energy': 0.851, 'loudness': -5.656, 'speechiness': 0.0528, 'acousticness': 0.0494, 'instrumentalness': 0.104, 'liveness': 0.501, 'valence': 0.533, 'tempo': 166.024}, '6tI9ywNUbWSs9PTdVkPonr': {'name': "It's All Just Pretend", 'artist_id': '3D1IyJznpDnWnnFrzjuWnh', 'artist_name': 'Ivan & Alyosha', 'album_name': "It's All Just Pretend (Deluxe Edition)", 'track_number': 4, 'duration_ms': 267573, 'popularity': 17, 'danceability': 0.437, 'energy': 0.769, 'loudness': -6.327, 'speechiness': 0.033, 'acousticness': 0.0576, 'instrumentalness': 0.000308, 'liveness': 0.209, 'valence': 0.211, 'tempo': 98.892}, '1qhlfTipmALXorAyNHoEiH': {'name': 'Easy to Love - Live at Spotify House', 'artist_id': '3D1IyJznpDnWnnFrzjuWnh', 'artist_name': 'Ivan & Alyosha', 'album_name': 'Spotify Sessions', 'track_number': 6, 'duration_ms': 217630, 'popularity': 30, 'danceability': 0.613, 'energy': 0.53, 'loudness': -8.201, 'speechiness': 0.035, 'acousticness': 0.294, 'instrumentalness': 1.13e-05, 'liveness': 0.116, 'valence': 0.615, 'tempo': 171.814}, '08cXy6KUizaAelYXtcew3w': {'name': '1957', 'artist_id': '5euJsEvfrlfhYDorMR40OF', 'artist_name': 'Milo Greene', 'album_name': 'Milo Greene', 'track_number': 6, 'duration_ms': 204213, 'popularity': 64, 'danceability': 0.388, 'energy': 0.595, 'loudness': -9.799, 'speechiness': 0.0325, 'acousticness': 0.663, 'instrumentalness': 5.58e-05, 'liveness': 0.178, 'valence': 0.577, 'tempo': 190.043}, '2Uj2BjZXVv9WvYFEVl8TDi': {'name': 'Silent Way', 'artist_id': '5euJsEvfrlfhYDorMR40OF', 'artist_name': 'Milo Greene', 'album_name': 'Milo Greene', 'track_number': 5, 'duration_ms': 203826, 'popularity': 49, 'danceability': 0.47, 'energy': 0.296, 'loudness': -14.123, 'speechiness': 0.0328, 'acousticness': 0.853, 'instrumentalness': 0.368, 'liveness': 0.0957, 'valence': 0.0642, 'tempo': 78.999}, '2Rn0EeHNgRawztx5KCGpwK': {'name': 'Autumn Tree', 'artist_id': '5euJsEvfrlfhYDorMR40OF', 'artist_name': 'Milo Greene', 'album_name': 'Milo Greene', 'track_number': 13, 'duration_ms': 230920, 'popularity': 48, 'danceability': 0.232, 'energy': 0.222, 'loudness': -14.154, 'speechiness': 0.031, 'acousticness': 0.771, 'instrumentalness': 0, 'liveness': 0.081, 'valence': 0.048, 'tempo': 81.832}, '3yaFjAn6FwqgbuPMpV7Tix': {'name': "What's The Matter", 'artist_id': '5euJsEvfrlfhYDorMR40OF', 'artist_name': 'Milo Greene', 'album_name': 'Milo Greene', 'track_number': 1, 'duration_ms': 268226, 'popularity': 46, 'danceability': 0.543, 'energy': 0.596, 'loudness': -10.248, 'speechiness': 0.0293, 'acousticness': 0.723, 'instrumentalness': 0.595, 'liveness': 0.313, 'valence': 0.462, 'tempo': 126.0}, '70ST10v9DBXmKdVjMhSSUh': {'name': 'We Kept the Lights On', 'artist_id': '5euJsEvfrlfhYDorMR40OF', 'artist_name': 'Milo Greene', 'album_name': 'Never Ender EP', 'track_number': 2, 'duration_ms': 197173, 'popularity': 45, 'danceability': 0.495, 'energy': 0.834, 'loudness': -6.233, 'speechiness': 0.0861, 'acousticness': 0.258, 'instrumentalness': 0.00619, 'liveness': 0.264, 'valence': 0.386, 'tempo': 154.97}, '4gvAocL5C5UKJcJ2kEJlka': {'name': "Don't You Give Up On Me", 'artist_id': '5euJsEvfrlfhYDorMR40OF', 'artist_name': 'Milo Greene', 'album_name': 'Milo Greene', 'track_number': 3, 'duration_ms': 197873, 'popularity': 43, 'danceability': 0.56, 'energy': 0.613, 'loudness': -8.756, 'speechiness': 0.0275, 'acousticness': 0.118, 'instrumentalness': 0.00429, 'liveness': 0.226, 'valence': 0.491, 'tempo': 124.01}, '1GHozXj5A9Gttz3jI3bF8j': {'name': "I'll Wait", 'artist_id': '5euJsEvfrlfhYDorMR40OF', 'artist_name': 'Milo Greene', 'album_name': 'Never Ender EP', 'track_number': 5, 'duration_ms': 220053, 'popularity': 42, 'danceability': 0.465, 'energy': 0.361, 'loudness': -10.575, 'speechiness': 0.03, 'acousticness': 0.894, 'instrumentalness': 0.0011, 'liveness': 0.109, 'valence': 0.0816, 'tempo': 131.948}, '0RMH1oSrSU8VDBZHLNHASU': {'name': 'Afraid of Everything', 'artist_id': '5euJsEvfrlfhYDorMR40OF', 'artist_name': 'Milo Greene', 'album_name': 'Never Ender EP', 'track_number': 4, 'duration_ms': 198546, 'popularity': 42, 'danceability': 0.512, 'energy': 0.746, 'loudness': -5.872, 'speechiness': 0.0415, 'acousticness': 0.0186, 'instrumentalness': 0.000278, 'liveness': 0.0788, 'valence': 0.237, 'tempo': 137.993}, '480QORmTRo360UBGlx1YFc': {'name': "Parents' House", 'artist_id': '5euJsEvfrlfhYDorMR40OF', 'artist_name': 'Milo Greene', 'album_name': 'Control', 'track_number': 6, 'duration_ms': 250413, 'popularity': 31, 'danceability': 0.596, 'energy': 0.806, 'loudness': -7.471, 'speechiness': 0.0411, 'acousticness': 0.131, 'instrumentalness': 0.866, 'liveness': 0.355, 'valence': 0.203, 'tempo': 120.029}, '4W7s1XhCOGkzQYolfI4T2Z': {'name': 'Son My Son', 'artist_id': '5euJsEvfrlfhYDorMR40OF', 'artist_name': 'Milo Greene', 'album_name': 'Milo Greene', 'track_number': 11, 'duration_ms': 212160, 'popularity': 40, 'danceability': 0.486, 'energy': 0.558, 'loudness': -10.452, 'speechiness': 0.0273, 'acousticness': 0.413, 'instrumentalness': 4.52e-05, 'liveness': 0.109, 'valence': 0.291, 'tempo': 91.193}, '6PRr6dzkiaLTGbkLSdQCvL': {'name': 'Moving Mountains', 'artist_id': '6tK77FerjTNLS5EEhI0zGM', 'artist_name': 'The Brevet', 'album_name': 'American Novel: Ch. I', 'track_number': 3, 'duration_ms': 279500, 'popularity': 54, 'danceability': 0.506, 'energy': 0.789, 'loudness': -4.939, 'speechiness': 0.0404, 'acousticness': 0.0132, 'instrumentalness': 0.000749, 'liveness': 0.364, 'valence': 0.351, 'tempo': 119.946}, '5narWdetexXv1ucBDuZJfO': {'name': 'Embers', 'artist_id': '6tK77FerjTNLS5EEhI0zGM', 'artist_name': 'The Brevet', 'album_name': 'E M B E R S: Ch. 2', 'track_number': 2, 'duration_ms': 190000, 'popularity': 44, 'danceability': 0.513, 'energy': 0.926, 'loudness': -4.299, 'speechiness': 0.0682, 'acousticness': 0.000201, 'instrumentalness': 6.89e-05, 'liveness': 0.317, 'valence': 0.676, 'tempo': 157.977}, '20mKWH9u1dAVvHHX0ssZMq': {'name': 'Hold On', 'artist_id': '6tK77FerjTNLS5EEhI0zGM', 'artist_name': 'The Brevet', 'album_name': 'E M B E R S: Ch. 2', 'track_number': 5, 'duration_ms': 256500, 'popularity': 38, 'danceability': 0.252, 'energy': 0.763, 'loudness': -5.23, 'speechiness': 0.0393, 'acousticness': 0.137, 'instrumentalness': 3.65e-05, 'liveness': 0.341, 'valence': 0.138, 'tempo': 155.816}, '4XHSgX7Y1jsNfp2leylP5W': {'name': 'There With You', 'artist_id': '6tK77FerjTNLS5EEhI0zGM', 'artist_name': 'The Brevet', 'album_name': 'E M B E R S: Ch. 2', 'track_number': 4, 'duration_ms': 278000, 'popularity': 37, 'danceability': 0.444, 'energy': 0.806, 'loudness': -5.845, 'speechiness': 0.103, 'acousticness': 0.0811, 'instrumentalness': 2.27e-05, 'liveness': 0.136, 'valence': 0.219, 'tempo': 151.993}, '4QMYdLsnDax4hn6FBojILG': {'name': 'Hazy Eyes', 'artist_id': '6tK77FerjTNLS5EEhI0zGM', 'artist_name': 'The Brevet', 'album_name': 'American Novel: Ch. I', 'track_number': 2, 'duration_ms': 307500, 'popularity': 36, 'danceability': 0.412, 'energy': 0.824, 'loudness': -4.982, 'speechiness': 0.056, 'acousticness': 0.0171, 'instrumentalness': 0, 'liveness': 0.231, 'valence': 0.343, 'tempo': 151.87}, '3k6FJ3WdPib8KQ65wEra0F': {'name': 'Moving Mountains (Acoustic)', 'artist_id': '6tK77FerjTNLS5EEhI0zGM', 'artist_name': 'The Brevet', 'album_name': 'Into the Storm', 'track_number': 2, 'duration_ms': 282000, 'popularity': 33, 'danceability': 0.517, 'energy': 0.614, 'loudness': -7.577, 'speechiness': 0.0265, 'acousticness': 0.35, 'instrumentalness': 0.00065, 'liveness': 0.0855, 'valence': 0.121, 'tempo': 92.076}, '60WU0pqbwheu1iS90EZN6z': {'name': 'Meet Me in the Night', 'artist_id': '6tK77FerjTNLS5EEhI0zGM', 'artist_name': 'The Brevet', 'album_name': 'E M B E R S: Ch. 2', 'track_number': 1, 'duration_ms': 297000, 'popularity': 33, 'danceability': 0.43, 'energy': 0.829, 'loudness': -5.201, 'speechiness': 0.0538, 'acousticness': 0.0559, 'instrumentalness': 0.00035, 'liveness': 0.123, 'valence': 0.529, 'tempo': 168.135}, '1oyWYzwnbyvz36UXcc1msE': {'name': 'Ups and Downs', 'artist_id': '6tK77FerjTNLS5EEhI0zGM', 'artist_name': 'The Brevet', 'album_name': 'Battle of the Heart', 'track_number': 5, 'duration_ms': 251240, 'popularity': 30, 'danceability': 0.473, 'energy': 0.784, 'loudness': -6.814, 'speechiness': 0.0463, 'acousticness': 0.267, 'instrumentalness': 1.18e-05, 'liveness': 0.11, 'valence': 0.355, 'tempo': 155.188}, '6tJX7dQ0IEyKLVMDnedMNQ': {'name': 'Rocks Beneath the Water', 'artist_id': '6tK77FerjTNLS5EEhI0zGM', 'artist_name': 'The Brevet', 'album_name': 'Battle of the Heart', 'track_number': 4, 'duration_ms': 304000, 'popularity': 30, 'danceability': 0.459, 'energy': 0.617, 'loudness': -5.717, 'speechiness': 0.0275, 'acousticness': 0.0951, 'instrumentalness': 1.64e-06, 'liveness': 0.139, 'valence': 0.158, 'tempo': 158.129}, '4kbj5MwxO1bq9wjT5g9HaA': {'name': 'Shut Up and Dance', 'artist_id': '6DIS6PRrLS3wbnZsf7vYic', 'artist_name': 'WALK THE MOON', 'album_name': 'TALKING IS HARD', 'track_number': 3, 'duration_ms': 199080, 'popularity': 78, 'danceability': 0.578, 'energy': 0.866, 'loudness': -3.804, 'speechiness': 0.0619, 'acousticness': 0.00701, 'instrumentalness': 0, 'liveness': 0.257, 'valence': 0.619, 'tempo': 128.038}, '3e0yTP5trHBBVvV32jwXqF': {'name': 'Anna Sun', 'artist_id': '6DIS6PRrLS3wbnZsf7vYic', 'artist_name': 'WALK THE MOON', 'album_name': 'Walk The Moon', 'track_number': 4, 'duration_ms': 321280, 'popularity': 67, 'danceability': 0.472, 'energy': 0.844, 'loudness': -6.578, 'speechiness': 0.054, 'acousticness': 0.00173, 'instrumentalness': 0, 'liveness': 0.24, 'valence': 0.343, 'tempo': 140.034}, '76EeScTnI2sCjDY0SfEoSb': {'name': 'Work This Body', 'artist_id': '6DIS6PRrLS3wbnZsf7vYic', 'artist_name': 'WALK THE MOON', 'album_name': 'TALKING IS HARD', 'track_number': 8, 'duration_ms': 175906, 'popularity': 65, 'danceability': 0.421, 'energy': 0.831, 'loudness': -5.128, 'speechiness': 0.107, 'acousticness': 0.0283, 'instrumentalness': 0, 'liveness': 0.464, 'valence': 0.489, 'tempo': 134.027}, '44psOy0D0SP8rcIiUgKgBs': {'name': 'Tightrope', 'artist_id': '6DIS6PRrLS3wbnZsf7vYic', 'artist_name': 'WALK THE MOON', 'album_name': 'Walk The Moon', 'track_number': 5, 'duration_ms': 209186, 'popularity': 61, 'danceability': 0.467, 'energy': 0.794, 'loudness': -6.174, 'speechiness': 0.0349, 'acousticness': 8.39e-05, 'instrumentalness': 0.00204, 'liveness': 0.103, 'valence': 0.577, 'tempo': 162.435}, '3Xzog9enTvbsc0G7G9M58D': {'name': 'Shut Up and Dance - Live Accoustic', 'artist_id': '6DIS6PRrLS3wbnZsf7vYic', 'artist_name': 'WALK THE MOON', 'album_name': 'Shut Up And Dance (Acoustic)', 'track_number': 1, 'duration_ms': 193986, 'popularity': 60, 'danceability': 0.82, 'energy': 0.615, 'loudness': -4.548, 'speechiness': 0.0466, 'acousticness': 0.151, 'instrumentalness': 0, 'liveness': 0.204, 'valence': 0.783, 'tempo': 129.874}, '3RRRDZig4RNJhVGfwwOOFZ': {'name': 'Different Colors', 'artist_id': '6DIS6PRrLS3wbnZsf7vYic', 'artist_name': 'WALK THE MOON', 'album_name': 'TALKING IS HARD', 'track_number': 1, 'duration_ms': 222053, 'popularity': 60, 'danceability': 0.48, 'energy': 0.826, 'loudness': -4.602, 'speechiness': 0.0397, 'acousticness': 0.000797, 'instrumentalness': 1.01e-06, 'liveness': 0.125, 'valence': 0.701, 'tempo': 96.0}, '3JxaZPq4UjkOaxnpyMUtAC': {'name': 'Avalanche', 'artist_id': '6DIS6PRrLS3wbnZsf7vYic', 'artist_name': 'WALK THE MOON', 'album_name': 'TALKING IS HARD', 'track_number': 5, 'duration_ms': 218720, 'popularity': 58, 'danceability': 0.594, 'energy': 0.858, 'loudness': -4.339, 'speechiness': 0.0387, 'acousticness': 0.00059, 'instrumentalness': 3.11e-06, 'liveness': 0.0642, 'valence': 0.646, 'tempo': 138.021}, '7eMpW9I1ZpVs6VQ90naDBh': {'name': 'Jenny', 'artist_id': '6DIS6PRrLS3wbnZsf7vYic', 'artist_name': 'WALK THE MOON', 'album_name': 'Walk The Moon', 'track_number': 6, 'duration_ms': 245133, 'popularity': 56, 'danceability': 0.544, 'energy': 0.788, 'loudness': -5.593, 'speechiness': 0.0474, 'acousticness': 0.000366, 'instrumentalness': 0, 'liveness': 0.141, 'valence': 0.821, 'tempo': 148.121}, '4xTMKnLtz1PVfZRElleujx': {'name': 'Ghostbusters', 'artist_id': '6DIS6PRrLS3wbnZsf7vYic', 'artist_name': 'WALK THE MOON', 'album_name': 'Ghostbusters (Original Motion Picture Soundtrack)', 'track_number': 1, 'duration_ms': 224680, 'popularity': 55, 'danceability': 0.693, 'energy': 0.887, 'loudness': -3.572, 'speechiness': 0.0378, 'acousticness': 0.00905, 'instrumentalness': 0.000118, 'liveness': 0.777, 'valence': 0.64, 'tempo': 116.502}, '6XMYnm4OTEysN8blzqiCL9': {'name': "Ain't No Man", 'artist_id': '196lKsA13K3keVXMDFK66q', 'artist_name': 'The Avett Brothers', 'album_name': 'True Sadness', 'track_number': 1, 'duration_ms': 212346, 'popularity': 63, 'danceability': 0.766, 'energy': 0.695, 'loudness': -5.564, 'speechiness': 0.341, 'acousticness': 0.315, 'instrumentalness': 0, 'liveness': 0.112, 'valence': 0.731, 'tempo': 90.805}, '19n9s9SfnLtwPEODqk8KCT': {'name': 'Live And Die', 'artist_id': '196lKsA13K3keVXMDFK66q', 'artist_name': 'The Avett Brothers', 'album_name': 'The Carpenter', 'track_number': 2, 'duration_ms': 271186, 'popularity': 57, 'danceability': 0.591, 'energy': 0.746, 'loudness': -5.054, 'speechiness': 0.0285, 'acousticness': 0.113, 'instrumentalness': 0, 'liveness': 0.151, 'valence': 0.611, 'tempo': 117.807}, '7Kho44itYaCQZvZQVV2SLW': {'name': 'Head Full Of Doubt/Road Full Of Promise', 'artist_id': '196lKsA13K3keVXMDFK66q', 'artist_name': 'The Avett Brothers', 'album_name': 'I And Love And You', 'track_number': 3, 'duration_ms': 287986, 'popularity': 57, 'danceability': 0.304, 'energy': 0.483, 'loudness': -7.263, 'speechiness': 0.0383, 'acousticness': 0.437, 'instrumentalness': 2.94e-05, 'liveness': 0.0984, 'valence': 0.16, 'tempo': 176.283}, '711WfDztCZpnmJg7Uvwod3': {'name': 'No Hard Feelings', 'artist_id': '196lKsA13K3keVXMDFK66q', 'artist_name': 'The Avett Brothers', 'album_name': 'True Sadness', 'track_number': 3, 'duration_ms': 314680, 'popularity': 57, 'danceability': 0.485, 'energy': 0.324, 'loudness': -8.185, 'speechiness': 0.031, 'acousticness': 0.693, 'instrumentalness': 2.37e-05, 'liveness': 0.115, 'valence': 0.185, 'tempo': 142.011}, '0DcBU93zLXGRdPPbUnP1iS': {'name': 'Swept Away', 'artist_id': '196lKsA13K3keVXMDFK66q', 'artist_name': 'The Avett Brothers', 'album_name': 'Mignonette', 'track_number': 15, 'duration_ms': 233280, 'popularity': 56, 'danceability': 0.372, 'energy': 0.512, 'loudness': -8.135, 'speechiness': 0.028, 'acousticness': 0.119, 'instrumentalness': 0, 'liveness': 0.126, 'valence': 0.553, 'tempo': 160.859}, '3h5AZDf5z7D18plaLtHTfi': {'name': 'Murder in the City', 'artist_id': '196lKsA13K3keVXMDFK66q', 'artist_name': 'The Avett Brothers', 'album_name': 'The Second Gleam', 'track_number': 2, 'duration_ms': 192426, 'popularity': 53, 'danceability': 0.632, 'energy': 0.254, 'loudness': -10.898, 'speechiness': 0.0338, 'acousticness': 0.922, 'instrumentalness': 9.06e-05, 'liveness': 0.13, 'valence': 0.228, 'tempo': 106.026}, '4agZCOTdZDD4r33mPPDy8b': {'name': 'January Wedding', 'artist_id': '196lKsA13K3keVXMDFK66q', 'artist_name': 'The Avett Brothers', 'album_name': 'I And Love And You', 'track_number': 2, 'duration_ms': 228000, 'popularity': 53, 'danceability': 0.473, 'energy': 0.382, 'loudness': -9.268, 'speechiness': 0.0279, 'acousticness': 0.379, 'instrumentalness': 3.79e-06, 'liveness': 0.308, 'valence': 0.592, 'tempo': 134.798}, '1nMlHxWuPc5P9Y5nGvenlj': {'name': 'I Wish I Was', 'artist_id': '196lKsA13K3keVXMDFK66q', 'artist_name': 'The Avett Brothers', 'album_name': 'True Sadness', 'track_number': 8, 'duration_ms': 316440, 'popularity': 53, 'danceability': 0.555, 'energy': 0.306, 'loudness': -8.766, 'speechiness': 0.0311, 'acousticness': 0.814, 'instrumentalness': 0, 'liveness': 0.187, 'valence': 0.278, 'tempo': 110.511}, '7huuoVBXjskB8kLgdRU9zu': {'name': 'True Sadness', 'artist_id': '196lKsA13K3keVXMDFK66q', 'artist_name': 'The Avett Brothers', 'album_name': 'True Sadness', 'track_number': 7, 'duration_ms': 275360, 'popularity': 51, 'danceability': 0.509, 'energy': 0.677, 'loudness': -3.733, 'speechiness': 0.0355, 'acousticness': 0.157, 'instrumentalness': 2.07e-06, 'liveness': 0.108, 'valence': 0.721, 'tempo': 96.99}, '4Eq0F51L7foy3hFvz0zQNp': {'name': 'A Little Fire', 'artist_id': '0MASTEXfUt3bpiyGOoEaur', 'artist_name': 'Parker Millsap', 'album_name': 'The Very Last Day', 'track_number': 10, 'duration_ms': 265186, 'popularity': 57, 'danceability': 0.441, 'energy': 0.11, 'loudness': -12.508, 'speechiness': 0.039, 'acousticness': 0.824, 'instrumentalness': 0, 'liveness': 0.0981, 'valence': 0.265, 'tempo': 120.205}, '70wMwfp8wAqaxip65R8Hkf': {'name': 'Jealous Sun', 'artist_id': '0MASTEXfUt3bpiyGOoEaur', 'artist_name': 'Parker Millsap', 'album_name': 'The Very Last Day', 'track_number': 7, 'duration_ms': 158306, 'popularity': 57, 'danceability': 0.444, 'energy': 0.116, 'loudness': -14.447, 'speechiness': 0.0385, 'acousticness': 0.829, 'instrumentalness': 0, 'liveness': 0.0904, 'valence': 0.313, 'tempo': 102.745}, '2Yf3wwS48rkAoBRXNJ34kz': {'name': 'Hades Pleads', 'artist_id': '0MASTEXfUt3bpiyGOoEaur', 'artist_name': 'Parker Millsap', 'album_name': 'The Very Last Day', 'track_number': 1, 'duration_ms': 156106, 'popularity': 51, 'danceability': 0.568, 'energy': 0.632, 'loudness': -6.958, 'speechiness': 0.161, 'acousticness': 0.0245, 'instrumentalness': 0.000246, 'liveness': 0.401, 'valence': 0.707, 'tempo': 164.823}, '0CjojcaWJEq0HYyxpkXlzu': {'name': 'Your Water', 'artist_id': '0MASTEXfUt3bpiyGOoEaur', 'artist_name': 'Parker Millsap', 'album_name': 'Luck Mansion Sessions', 'track_number': 1, 'duration_ms': 162408, 'popularity': 47, 'danceability': 0.941, 'energy': 0.082, 'loudness': -19.666, 'speechiness': 0.0814, 'acousticness': 0.546, 'instrumentalness': 1.76e-05, 'liveness': 0.0564, 'valence': 0.622, 'tempo': 125.06}, '0FbKvqTBo2TsSzhT5ohFI2': {'name': 'Heaven Sent', 'artist_id': '0MASTEXfUt3bpiyGOoEaur', 'artist_name': 'Parker Millsap', 'album_name': 'The Very Last Day', 'track_number': 4, 'duration_ms': 232880, 'popularity': 46, 'danceability': 0.403, 'energy': 0.281, 'loudness': -10.365, 'speechiness': 0.0292, 'acousticness': 0.454, 'instrumentalness': 0, 'liveness': 0.106, 'valence': 0.193, 'tempo': 112.881}, '7Lhc9rgUp3cwfwEgo21kZi': {'name': 'Wherever You Are', 'artist_id': '0MASTEXfUt3bpiyGOoEaur', 'artist_name': 'Parker Millsap', 'album_name': 'The Very Last Day', 'track_number': 8, 'duration_ms': 182186, 'popularity': 44, 'danceability': 0.636, 'energy': 0.526, 'loudness': -7.372, 'speechiness': 0.0363, 'acousticness': 0.0162, 'instrumentalness': 2.3e-06, 'liveness': 0.089, 'valence': 0.34, 'tempo': 76.447}, '4zm37YNRt5XrbFOTPk0jBp': {'name': 'Old Time Religion', 'artist_id': '0MASTEXfUt3bpiyGOoEaur', 'artist_name': 'Parker Millsap', 'album_name': 'Parker Millsap', 'track_number': 1, 'duration_ms': 234000, 'popularity': 44, 'danceability': 0.682, 'energy': 0.336, 'loudness': -7.515, 'speechiness': 0.0957, 'acousticness': 0.721, 'instrumentalness': 0, 'liveness': 0.0896, 'valence': 0.593, 'tempo': 119.767}, '76Fc9ApTagfE0DFLFdnMj1': {'name': 'The Very Last Day', 'artist_id': '0MASTEXfUt3bpiyGOoEaur', 'artist_name': 'Parker Millsap', 'album_name': 'The Very Last Day', 'track_number': 5, 'duration_ms': 180013, 'popularity': 42, 'danceability': 0.595, 'energy': 0.331, 'loudness': -9.258, 'speechiness': 0.0546, 'acousticness': 0.143, 'instrumentalness': 0, 'liveness': 0.349, 'valence': 0.432, 'tempo': 90.07}, '2necAV33vY9L5x2SUXYZeY': {'name': 'Pining', 'artist_id': '0MASTEXfUt3bpiyGOoEaur', 'artist_name': 'Parker Millsap', 'album_name': 'The Very Last Day', 'track_number': 2, 'duration_ms': 164533, 'popularity': 42, 'danceability': 0.738, 'energy': 0.466, 'loudness': -7.096, 'speechiness': 0.101, 'acousticness': 0.0824, 'instrumentalness': 0, 'liveness': 0.071, 'valence': 0.787, 'tempo': 92.6}, '1mTrfm7XOVkmVBaTaUJIN9': {'name': 'The Glory of Love', 'artist_id': '0MASTEXfUt3bpiyGOoEaur', 'artist_name': 'Parker Millsap', 'album_name': 'Luck Mansion Sessions', 'track_number': 2, 'duration_ms': 194428, 'popularity': 41, 'danceability': 0.51, 'energy': 0.0225, 'loudness': -19.479, 'speechiness': 0.0517, 'acousticness': 0.869, 'instrumentalness': 0, 'liveness': 0.229, 'valence': 0.377, 'tempo': 76.364}, '0kzfqqvipRSBQchrB3xX8D': {'name': 'When My Time Comes', 'artist_id': '0CDUUM6KNRvgBFYIbWxJwV', 'artist_name': 'Dawes', 'album_name': 'North Hills', 'track_number': 5, 'duration_ms': 308373, 'popularity': 59, 'danceability': 0.327, 'energy': 0.501, 'loudness': -8.885, 'speechiness': 0.0434, 'acousticness': 0.722, 'instrumentalness': 0.00245, 'liveness': 0.113, 'valence': 0.374, 'tempo': 115.199}, '4zF51hAnzL84vE8unhEH5N': {'name': 'Right On Time', 'artist_id': '0CDUUM6KNRvgBFYIbWxJwV', 'artist_name': 'Dawes', 'album_name': 'All Your Favorite Bands', 'track_number': 8, 'duration_ms': 288666, 'popularity': 56, 'danceability': 0.554, 'energy': 0.648, 'loudness': -6.725, 'speechiness': 0.0299, 'acousticness': 0.0575, 'instrumentalness': 0.000214, 'liveness': 0.119, 'valence': 0.375, 'tempo': 101.678}, '0HOvoZ4m0aJp6vY4fVrI51': {'name': 'All Your Favorite Bands', 'artist_id': '0CDUUM6KNRvgBFYIbWxJwV', 'artist_name': 'Dawes', 'album_name': 'All Your Favorite Bands', 'track_number': 4, 'duration_ms': 215359, 'popularity': 53, 'danceability': 0.427, 'energy': 0.396, 'loudness': -7.725, 'speechiness': 0.0304, 'acousticness': 0.777, 'instrumentalness': 2e-06, 'liveness': 0.102, 'valence': 0.367, 'tempo': 133.131}, '23Q4sMxgEKRXDMi62xPP5R': {'name': 'When The Tequila Runs Out', 'artist_id': '0CDUUM6KNRvgBFYIbWxJwV', 'artist_name': 'Dawes', 'album_name': "We're All Gonna Die", 'track_number': 7, 'duration_ms': 284720, 'popularity': 50, 'danceability': 0.681, 'energy': 0.761, 'loudness': -6.225, 'speechiness': 0.0409, 'acousticness': 0.0451, 'instrumentalness': 0.00029, 'liveness': 0.367, 'valence': 0.866, 'tempo': 155.989}, '5UDEGEbvqFwrzT2P2PcJ27': {'name': 'A Little Bit Of Everything', 'artist_id': '0CDUUM6KNRvgBFYIbWxJwV', 'artist_name': 'Dawes', 'album_name': 'Nothing Is Wrong', 'track_number': 11, 'duration_ms': 339493, 'popularity': 48, 'danceability': 0.51, 'energy': 0.393, 'loudness': -9.526, 'speechiness': 0.0364, 'acousticness': 0.395, 'instrumentalness': 0, 'liveness': 0.138, 'valence': 0.276, 'tempo': 143.739}, '5czb6N8T50aNnJoKWQRgQo': {'name': 'That Western Skyline', 'artist_id': '0CDUUM6KNRvgBFYIbWxJwV', 'artist_name': 'Dawes', 'album_name': 'North Hills', 'track_number': 1, 'duration_ms': 358773, 'popularity': 48, 'danceability': 0.55, 'energy': 0.387, 'loudness': -7.923, 'speechiness': 0.0287, 'acousticness': 0.349, 'instrumentalness': 0.307, 'liveness': 0.206, 'valence': 0.212, 'tempo': 113.996}, '2V5tSSOgNs1L6hmVnNoaUZ': {'name': 'Roll With The Punches', 'artist_id': '0CDUUM6KNRvgBFYIbWxJwV', 'artist_name': 'Dawes', 'album_name': "We're All Gonna Die", 'track_number': 3, 'duration_ms': 265120, 'popularity': 46, 'danceability': 0.73, 'energy': 0.473, 'loudness': -6.38, 'speechiness': 0.0531, 'acousticness': 0.0196, 'instrumentalness': 3.81e-05, 'liveness': 0.0783, 'valence': 0.943, 'tempo': 172.032}, '08NjEcoCYhb72r26U3wh7X': {'name': 'Most People', 'artist_id': '0CDUUM6KNRvgBFYIbWxJwV', 'artist_name': 'Dawes', 'album_name': "Stories Don't End", 'track_number': 5, 'duration_ms': 271320, 'popularity': 45, 'danceability': 0.555, 'energy': 0.491, 'loudness': -7.82, 'speechiness': 0.0354, 'acousticness': 0.00506, 'instrumentalness': 0, 'liveness': 0.315, 'valence': 0.391, 'tempo': 78.208}, '1SwrPOu6BfuyzNTn7iA3j1': {'name': "We're All Gonna Die", 'artist_id': '0CDUUM6KNRvgBFYIbWxJwV', 'artist_name': 'Dawes', 'album_name': "We're All Gonna Die", 'track_number': 2, 'duration_ms': 304733, 'popularity': 45, 'danceability': 0.616, 'energy': 0.289, 'loudness': -6.739, 'speechiness': 0.0358, 'acousticness': 0.419, 'instrumentalness': 0.0206, 'liveness': 0.105, 'valence': 0.373, 'tempo': 133.806}, '1QesQ27kCWYTYuXJi8SApS': {'name': 'Wait so Long', 'artist_id': '3GjVVVcFmUgEJEAAsbGkf4', 'artist_name': 'Trampled By Turtles', 'album_name': 'Palomino', 'track_number': 1, 'duration_ms': 206400, 'popularity': 60, 'danceability': 0.254, 'energy': 0.928, 'loudness': -5.885, 'speechiness': 0.318, 'acousticness': 0.487, 'instrumentalness': 1.33e-05, 'liveness': 0.112, 'valence': 0.32, 'tempo': 189.451}, '5H06kjjKa1Oz8BZcGeplel': {'name': 'Alone', 'artist_id': '3GjVVVcFmUgEJEAAsbGkf4', 'artist_name': 'Trampled By Turtles', 'album_name': 'Stars and Satellites', 'track_number': 2, 'duration_ms': 268280, 'popularity': 54, 'danceability': 0.546, 'energy': 0.429, 'loudness': -10.636, 'speechiness': 0.0321, 'acousticness': 0.758, 'instrumentalness': 0.403, 'liveness': 0.0976, 'valence': 0.291, 'tempo': 141.091}, '2dJrn376fJPUCj1f4txnRQ': {'name': 'Where Is My Mind?', 'artist_id': '3GjVVVcFmUgEJEAAsbGkf4', 'artist_name': 'Trampled By Turtles', 'album_name': 'Where Is My Mind?', 'track_number': 1, 'duration_ms': 210628, 'popularity': 53, 'danceability': 0.523, 'energy': 0.482, 'loudness': -6.646, 'speechiness': 0.0245, 'acousticness': 0.612, 'instrumentalness': 0.0103, 'liveness': 0.264, 'valence': 0.297, 'tempo': 79.581}, '6AKYhRh9Oz1nzscR5kZS7T': {'name': 'Victory', 'artist_id': '3GjVVVcFmUgEJEAAsbGkf4', 'artist_name': 'Trampled By Turtles', 'album_name': 'Palomino', 'track_number': 2, 'duration_ms': 237000, 'popularity': 50, 'danceability': 0.454, 'energy': 0.719, 'loudness': -7.74, 'speechiness': 0.0326, 'acousticness': 0.28, 'instrumentalness': 0.00209, 'liveness': 0.089, 'valence': 0.589, 'tempo': 121.548}, '6pr0vBUsNzV3ayyTTDhn9m': {'name': 'Wild Animals', 'artist_id': '3GjVVVcFmUgEJEAAsbGkf4', 'artist_name': 'Trampled By Turtles', 'album_name': 'Wild Animals', 'track_number': 1, 'duration_ms': 353133, 'popularity': 48, 'danceability': 0.251, 'energy': 0.44, 'loudness': -5.181, 'speechiness': 0.0324, 'acousticness': 0.249, 'instrumentalness': 0.0361, 'liveness': 0.128, 'valence': 0.0757, 'tempo': 129.869}, '4SI6ia4b6L5J1n6k42WeHC': {'name': 'Midnight on the Interstate', 'artist_id': '3GjVVVcFmUgEJEAAsbGkf4', 'artist_name': 'Trampled By Turtles', 'album_name': 'Stars and Satellites', 'track_number': 1, 'duration_ms': 205560, 'popularity': 46, 'danceability': 0.433, 'energy': 0.317, 'loudness': -11.785, 'speechiness': 0.0302, 'acousticness': 0.755, 'instrumentalness': 0.167, 'liveness': 0.184, 'valence': 0.338, 'tempo': 160.731}, '5dyqyS9nuV9LmTHItuQO7l': {'name': 'Repetition', 'artist_id': '3GjVVVcFmUgEJEAAsbGkf4', 'artist_name': 'Trampled By Turtles', 'album_name': 'Wild Animals', 'track_number': 3, 'duration_ms': 187413, 'popularity': 46, 'danceability': 0.24, 'energy': 0.612, 'loudness': -2.813, 'speechiness': 0.0302, 'acousticness': 0.054, 'instrumentalness': 3.79e-06, 'liveness': 0.071, 'valence': 0.521, 'tempo': 145.534}, '6nQ5z2EDrltb8MZs3HhfgL': {'name': 'Walt Whitman', 'artist_id': '3GjVVVcFmUgEJEAAsbGkf4', 'artist_name': 'Trampled By Turtles', 'album_name': 'Stars and Satellites', 'track_number': 3, 'duration_ms': 158680, 'popularity': 44, 'danceability': 0.464, 'energy': 0.73, 'loudness': -5.379, 'speechiness': 0.0319, 'acousticness': 0.611, 'instrumentalness': 0.277, 'liveness': 0.185, 'valence': 0.729, 'tempo': 151.375}, '3lBzK00y8cKvFA1oDOcw0E': {'name': 'Where Is My Mind? (Live)', 'artist_id': '3GjVVVcFmUgEJEAAsbGkf4', 'artist_name': 'Trampled By Turtles', 'album_name': 'Live at First Avenue', 'track_number': 5, 'duration_ms': 211040, 'popularity': 41, 'danceability': 0.358, 'energy': 0.592, 'loudness': -7.699, 'speechiness': 0.03, 'acousticness': 0.36, 'instrumentalness': 0.0053, 'liveness': 0.939, 'valence': 0.251, 'tempo': 162.038}, '7mfn1O2YQifrW5nZhAhCGL': {'name': 'This Train is Bound for Glory', 'artist_id': '4DBi4EYXgiqbkxvWUXUzMi', 'artist_name': 'Old Crow Medicine Show', 'album_name': 'Woody Guthrie: At 100! (Live At The Kennedy Center)', 'track_number': 18, 'duration_ms': 221826, 'popularity': 49, 'danceability': 0.392, 'energy': 0.942, 'loudness': -8.62, 'speechiness': 0.559, 'acousticness': 0.158, 'instrumentalness': 4.48e-05, 'liveness': 0.802, 'valence': 0.56, 'tempo': 174.311}, '0EnoW6gDUgYowcfek2GnWR': {'name': 'Sweet Amarillo', 'artist_id': '4DBi4EYXgiqbkxvWUXUzMi', 'artist_name': 'Old Crow Medicine Show', 'album_name': 'Remedy', 'track_number': 3, 'duration_ms': 202730, 'popularity': 48, 'danceability': 0.476, 'energy': 0.709, 'loudness': -5.692, 'speechiness': 0.0274, 'acousticness': 0.155, 'instrumentalness': 0, 'liveness': 0.377, 'valence': 0.752, 'tempo': 167.951}, '1HJrJjCNgviyQYC6rYoBYS': {'name': 'Carry Me Back To Virginia', 'artist_id': '4DBi4EYXgiqbkxvWUXUzMi', 'artist_name': 'Old Crow Medicine Show', 'album_name': 'Carry Me Back', 'track_number': 1, 'duration_ms': 160693, 'popularity': 46, 'danceability': 0.681, 'energy': 0.922, 'loudness': -5.195, 'speechiness': 0.0413, 'acousticness': 0.465, 'instrumentalness': 6.52e-06, 'liveness': 0.0787, 'valence': 0.958, 'tempo': 136.068}, '3kp1DqoICwe4Vhf2zVzpUW': {'name': 'Methamphetamine', 'artist_id': '4DBi4EYXgiqbkxvWUXUzMi', 'artist_name': 'Old Crow Medicine Show', 'album_name': 'Tennessee Pusher', 'track_number': 4, 'duration_ms': 327760, 'popularity': 46, 'danceability': 0.604, 'energy': 0.589, 'loudness': -6.969, 'speechiness': 0.0269, 'acousticness': 0.0172, 'instrumentalness': 2.69e-06, 'liveness': 0.249, 'valence': 0.659, 'tempo': 123.935}, '5hF5VODEuBVFNTVu7j3NrL': {'name': 'This Land is Your Land', 'artist_id': '4DBi4EYXgiqbkxvWUXUzMi', 'artist_name': 'Old Crow Medicine Show', 'album_name': 'Woody Guthrie: At 100! (Live At The Kennedy Center)', 'track_number': 19, 'duration_ms': 295200, 'popularity': 44, 'danceability': 0.26, 'energy': 0.82, 'loudness': -8.387, 'speechiness': 0.216, 'acousticness': 0.309, 'instrumentalness': 1.65e-05, 'liveness': 0.975, 'valence': 0.63, 'tempo': 173.314}, '7m1TJgrWNy72WgKmK51QgJ': {'name': 'Down Home Girl', 'artist_id': '4DBi4EYXgiqbkxvWUXUzMi', 'artist_name': 'Old Crow Medicine Show', 'album_name': 'Big Iron World', 'track_number': 1, 'duration_ms': 226893, 'popularity': 42, 'danceability': 0.698, 'energy': 0.638, 'loudness': -5.968, 'speechiness': 0.0371, 'acousticness': 0.313, 'instrumentalness': 2.67e-06, 'liveness': 0.0937, 'valence': 0.817, 'tempo': 111.205}, '1KYQoFEiIqPYHLeuXWwUmX': {'name': 'Tell It To Me', 'artist_id': '4DBi4EYXgiqbkxvWUXUzMi', 'artist_name': 'Old Crow Medicine Show', 'album_name': 'O.C.M.S.', 'track_number': 1, 'duration_ms': 167893, 'popularity': 42, 'danceability': 0.592, 'energy': 0.518, 'loudness': -8.668, 'speechiness': 0.149, 'acousticness': 0.722, 'instrumentalness': 0, 'liveness': 0.326, 'valence': 0.807, 'tempo': 167.001}, '2mKMIVcKPczPULJF13Ztvo': {'name': 'Angel from Montgomery', 'artist_id': '4DBi4EYXgiqbkxvWUXUzMi', 'artist_name': 'Old Crow Medicine Show', 'album_name': 'Broken Hearts & Dirty Windows: Songs of John Prine', 'track_number': 8, 'duration_ms': 270080, 'popularity': 42, 'danceability': 0.574, 'energy': 0.36, 'loudness': -8.861, 'speechiness': 0.0602, 'acousticness': 0.511, 'instrumentalness': 0, 'liveness': 0.0711, 'valence': 0.505, 'tempo': 142.722}, '0xEaA9gekxEFwoDjX8dq6c': {'name': 'My Good Gal', 'artist_id': '4DBi4EYXgiqbkxvWUXUzMi', 'artist_name': 'Old Crow Medicine Show', 'album_name': 'Big Iron World', 'track_number': 4, 'duration_ms': 258653, 'popularity': 40, 'danceability': 0.529, 'energy': 0.401, 'loudness': -9.702, 'speechiness': 0.0299, 'acousticness': 0.585, 'instrumentalness': 0.000402, 'liveness': 0.0899, 'valence': 0.619, 'tempo': 154.986}, '4m9DSdV4XU49dDJ8yhaMMv': {'name': 'Land of the Living', 'artist_id': '0XHM5ZNJDU8e4CfbWMeSzC', 'artist_name': 'Roo Panes', 'album_name': 'Land of the Living EP', 'track_number': 4, 'duration_ms': 264986, 'popularity': 57, 'danceability': 0.512, 'energy': 0.384, 'loudness': -8.799, 'speechiness': 0.0331, 'acousticness': 0.512, 'instrumentalness': 0.000193, 'liveness': 0.128, 'valence': 0.271, 'tempo': 121.992}, '61X18xzfxAYZGouAXm4ISi': {'name': 'Silver Moon', 'artist_id': '0XHM5ZNJDU8e4CfbWMeSzC', 'artist_name': 'Roo Panes', 'album_name': 'Land of the Living EP', 'track_number': 5, 'duration_ms': 291360, 'popularity': 56, 'danceability': 0.397, 'energy': 0.269, 'loudness': -13.249, 'speechiness': 0.0366, 'acousticness': 0.89, 'instrumentalness': 0.34, 'liveness': 0.111, 'valence': 0.048, 'tempo': 116.938}, '5hPWh1uz7UGnbKgP5iTy5q': {'name': "I'll Move Mountains", 'artist_id': '0XHM5ZNJDU8e4CfbWMeSzC', 'artist_name': 'Roo Panes', 'album_name': 'Once EP', 'track_number': 1, 'duration_ms': 305437, 'popularity': 14, 'danceability': 0.34, 'energy': 0.34, 'loudness': -11.102, 'speechiness': 0.0359, 'acousticness': 0.713, 'instrumentalness': 0.286, 'liveness': 0.126, 'valence': 0.116, 'tempo': 115.127}, '1IycYHHYjKgxvB8AHCdu7O': {'name': 'Open Road', 'artist_id': '0XHM5ZNJDU8e4CfbWMeSzC', 'artist_name': 'Roo Panes', 'album_name': 'Weight of Your World EP', 'track_number': 2, 'duration_ms': 258730, 'popularity': 54, 'danceability': 0.564, 'energy': 0.455, 'loudness': -8.282, 'speechiness': 0.0369, 'acousticness': 0.807, 'instrumentalness': 0.000184, 'liveness': 0.0832, 'valence': 0.323, 'tempo': 132.196}, '1fOtFSwFOdv4vSInE3Ep2Y': {'name': 'Water Over Fire', 'artist_id': '0XHM5ZNJDU8e4CfbWMeSzC', 'artist_name': 'Roo Panes', 'album_name': 'Paperweights', 'track_number': 6, 'duration_ms': 268426, 'popularity': 37, 'danceability': 0.675, 'energy': 0.166, 'loudness': -13.383, 'speechiness': 0.0613, 'acousticness': 0.82, 'instrumentalness': 8.69e-05, 'liveness': 0.352, 'valence': 0.294, 'tempo': 138.997}, '3ZrxDW8SSPZkGPwDggS9zh': {'name': 'Home from Home', 'artist_id': '0XHM5ZNJDU8e4CfbWMeSzC', 'artist_name': 'Roo Panes', 'album_name': 'Land of the Living EP', 'track_number': 3, 'duration_ms': 180613, 'popularity': 49, 'danceability': 0.528, 'energy': 0.28, 'loudness': -10.181, 'speechiness': 0.0368, 'acousticness': 0.807, 'instrumentalness': 0.000377, 'liveness': 0.116, 'valence': 0.347, 'tempo': 102.061}, '3QOM7UY7jnHqutxr1ptZzJ': {'name': 'The Original', 'artist_id': '0XHM5ZNJDU8e4CfbWMeSzC', 'artist_name': 'Roo Panes', 'album_name': 'Paperweights', 'track_number': 3, 'duration_ms': 176080, 'popularity': 44, 'danceability': 0.581, 'energy': 0.252, 'loudness': -11.649, 'speechiness': 0.0313, 'acousticness': 0.807, 'instrumentalness': 4.24e-05, 'liveness': 0.106, 'valence': 0.44, 'tempo': 76.175}, '1wmMA2Uh2f74yCYgH6IqYh': {'name': 'Mistral', 'artist_id': '0XHM5ZNJDU8e4CfbWMeSzC', 'artist_name': 'Roo Panes', 'album_name': 'Once EP', 'track_number': 4, 'duration_ms': 309254, 'popularity': 13, 'danceability': 0.355, 'energy': 0.472, 'loudness': -9.019, 'speechiness': 0.029, 'acousticness': 0.571, 'instrumentalness': 0.299, 'liveness': 0.121, 'valence': 0.2, 'tempo': 114.22}, '2PYuLwC2eTncWexIYVoF2X': {'name': 'Paperweights', 'artist_id': '0XHM5ZNJDU8e4CfbWMeSzC', 'artist_name': 'Roo Panes', 'album_name': 'Paperweights', 'track_number': 5, 'duration_ms': 246000, 'popularity': 45, 'danceability': 0.408, 'energy': 0.154, 'loudness': -13.783, 'speechiness': 0.0428, 'acousticness': 0.708, 'instrumentalness': 0.0012, 'liveness': 0.116, 'valence': 0.325, 'tempo': 127.19}, '2dtcNplc1W8GFAo9LPzLri': {'name': 'Dear Wormwood', 'artist_id': '3Fe3pszR2t4TOBVz41B1WR', 'artist_name': 'The Oh Hellos', 'album_name': 'Dear Wormwood', 'track_number': 11, 'duration_ms': 316066, 'popularity': 61, 'danceability': 0.519, 'energy': 0.601, 'loudness': -10.409, 'speechiness': 0.033, 'acousticness': 0.227, 'instrumentalness': 0.007, 'liveness': 0.112, 'valence': 0.163, 'tempo': 158.055}, '1TKygFgEQtUaSTnNPnl6o9': {'name': 'Lay Me Down', 'artist_id': '3Fe3pszR2t4TOBVz41B1WR', 'artist_name': 'The Oh Hellos', 'album_name': 'The Oh Hellos EP', 'track_number': 2, 'duration_ms': 183437, 'popularity': 52, 'danceability': 0.544, 'energy': 0.422, 'loudness': -10.826, 'speechiness': 0.0345, 'acousticness': 0.0204, 'instrumentalness': 0, 'liveness': 0.332, 'valence': 0.359, 'tempo': 140.284}, '0TgaaBAEf84VqvdTshIdPw': {'name': 'Cold Is The Night', 'artist_id': '3Fe3pszR2t4TOBVz41B1WR', 'artist_name': 'The Oh Hellos', 'album_name': 'The Oh Hellos EP', 'track_number': 3, 'duration_ms': 195011, 'popularity': 50, 'danceability': 0.621, 'energy': 0.0795, 'loudness': -17.238, 'speechiness': 0.0324, 'acousticness': 0.364, 'instrumentalness': 0, 'liveness': 0.197, 'valence': 0.409, 'tempo': 79.986}, '3rhyMywAzKIALXc1uQYB1d': {'name': 'Like The Dawn', 'artist_id': '3Fe3pszR2t4TOBVz41B1WR', 'artist_name': 'The Oh Hellos', 'album_name': 'Through the Deep, Dark Valley', 'track_number': 2, 'duration_ms': 305000, 'popularity': 49, 'danceability': 0.571, 'energy': 0.491, 'loudness': -11.351, 'speechiness': 0.0281, 'acousticness': 0.503, 'instrumentalness': 0.00568, 'liveness': 0.098, 'valence': 0.392, 'tempo': 96.028}, '3CiPunzgvlLdvJj0bUErJd': {'name': 'I Have Made Mistakes', 'artist_id': '3Fe3pszR2t4TOBVz41B1WR', 'artist_name': 'The Oh Hellos', 'album_name': 'Through the Deep, Dark Valley', 'track_number': 9, 'duration_ms': 289500, 'popularity': 48, 'danceability': 0.334, 'energy': 0.235, 'loudness': -15.555, 'speechiness': 0.0372, 'acousticness': 0.845, 'instrumentalness': 4.4e-05, 'liveness': 0.342, 'valence': 0.0636, 'tempo': 79.58}, '7xwOCSKispEfJOlZHW08R2': {'name': 'Bitter Water', 'artist_id': '3Fe3pszR2t4TOBVz41B1WR', 'artist_name': 'The Oh Hellos', 'album_name': 'Dear Wormwood', 'track_number': 2, 'duration_ms': 196920, 'popularity': 48, 'danceability': 0.585, 'energy': 0.639, 'loudness': -9.757, 'speechiness': 0.0307, 'acousticness': 0.343, 'instrumentalness': 9.04e-06, 'liveness': 0.142, 'valence': 0.396, 'tempo': 95.021}, '6afpT3wW8NdIe7nimRNRd0': {'name': 'The Lament Of Eustace Scrubb', 'artist_id': '3Fe3pszR2t4TOBVz41B1WR', 'artist_name': 'The Oh Hellos', 'album_name': 'Through the Deep, Dark Valley', 'track_number': 7, 'duration_ms': 245777, 'popularity': 46, 'danceability': 0.422, 'energy': 0.331, 'loudness': -12.473, 'speechiness': 0.0333, 'acousticness': 0.493, 'instrumentalness': 0.00719, 'liveness': 0.35, 'valence': 0.0387, 'tempo': 135.1}, '5kqyZy0WrBpSoLPy7ojjzx': {'name': 'The Valley', 'artist_id': '3Fe3pszR2t4TOBVz41B1WR', 'artist_name': 'The Oh Hellos', 'album_name': 'Through the Deep, Dark Valley', 'track_number': 1, 'duration_ms': 174313, 'popularity': 46, 'danceability': 0.486, 'energy': 0.826, 'loudness': -7.349, 'speechiness': 0.0363, 'acousticness': 0.00768, 'instrumentalness': 0.0381, 'liveness': 0.35, 'valence': 0.509, 'tempo': 102.035}, '0sZfwxyHuEOsKJOiXcjHU7': {'name': 'Wishing Well', 'artist_id': '3Fe3pszR2t4TOBVz41B1WR', 'artist_name': 'The Oh Hellos', 'album_name': 'Through the Deep, Dark Valley', 'track_number': 5, 'duration_ms': 217894, 'popularity': 45, 'danceability': 0.568, 'energy': 0.193, 'loudness': -12.827, 'speechiness': 0.0273, 'acousticness': 0.661, 'instrumentalness': 1.98e-06, 'liveness': 0.11, 'valence': 0.183, 'tempo': 76.002}, '7agKHhiI7ubqzf6sgWkNjp': {'name': 'You Taste Like Wine', 'artist_id': '3sva1UjOJOx6cGISZOpItl', 'artist_name': 'The Collection', 'album_name': 'Listen to the River', 'track_number': 2, 'duration_ms': 226401, 'popularity': 40, 'danceability': 0.569, 'energy': 0.757, 'loudness': -6.629, 'speechiness': 0.0379, 'acousticness': 0.114, 'instrumentalness': 0.00442, 'liveness': 0.102, 'valence': 0.505, 'tempo': 167.958}, '1x9cEmDslp7wH52UuLGyj3': {'name': 'The Gown of Green', 'artist_id': '3sva1UjOJOx6cGISZOpItl', 'artist_name': 'The Collection', 'album_name': 'Ars Moriendi', 'track_number': 4, 'duration_ms': 199617, 'popularity': 39, 'danceability': 0.509, 'energy': 0.356, 'loudness': -6.54, 'speechiness': 0.0522, 'acousticness': 0.109, 'instrumentalness': 0, 'liveness': 0.152, 'valence': 0.595, 'tempo': 127.559}, '7I0vmekPKKMmWW14zDFhIF': {'name': 'Threshing Floor', 'artist_id': '3sva1UjOJOx6cGISZOpItl', 'artist_name': 'The Collection', 'album_name': 'Listen to the River', 'track_number': 1, 'duration_ms': 78733, 'popularity': 38, 'danceability': 0.431, 'energy': 0.206, 'loudness': -8.696, 'speechiness': 0.0332, 'acousticness': 0.699, 'instrumentalness': 0, 'liveness': 0.151, 'valence': 0.21, 'tempo': 105.117}, '6Qjb563OGlWPrVWIqowvpD': {'name': 'Mama', 'artist_id': '3sva1UjOJOx6cGISZOpItl', 'artist_name': 'The Collection', 'album_name': 'Listen to the River', 'track_number': 3, 'duration_ms': 251661, 'popularity': 35, 'danceability': 0.57, 'energy': 0.422, 'loudness': -7.689, 'speechiness': 0.0325, 'acousticness': 0.169, 'instrumentalness': 0.00682, 'liveness': 0.558, 'valence': 0.227, 'tempo': 133.991}, '5bfa4ucJ3vozYtrvtTtfQA': {'name': 'Birds', 'artist_id': '3sva1UjOJOx6cGISZOpItl', 'artist_name': 'The Collection', 'album_name': 'Listen to the River', 'track_number': 4, 'duration_ms': 265304, 'popularity': 35, 'danceability': 0.355, 'energy': 0.527, 'loudness': -7.935, 'speechiness': 0.0425, 'acousticness': 0.0398, 'instrumentalness': 0.0118, 'liveness': 0.0815, 'valence': 0.0853, 'tempo': 104.679}, '7pJqpTz3eTq0aJIyoLxamG': {'name': 'Dirt', 'artist_id': '3sva1UjOJOx6cGISZOpItl', 'artist_name': 'The Collection', 'album_name': 'The Collection EP', 'track_number': 1, 'duration_ms': 295226, 'popularity': 34, 'danceability': 0.654, 'energy': 0.344, 'loudness': -9.409, 'speechiness': 0.0291, 'acousticness': 0.865, 'instrumentalness': 1.27e-06, 'liveness': 0.0805, 'valence': 0.256, 'tempo': 125.978}, '18zzR5w624JxWnSZEKeoHA': {'name': 'Sing of the Moon', 'artist_id': '3sva1UjOJOx6cGISZOpItl', 'artist_name': 'The Collection', 'album_name': 'Listen to the River', 'track_number': 7, 'duration_ms': 246366, 'popularity': 33, 'danceability': 0.317, 'energy': 0.325, 'loudness': -8.752, 'speechiness': 0.0345, 'acousticness': 0.693, 'instrumentalness': 0.00478, 'liveness': 0.115, 'valence': 0.106, 'tempo': 81.456}, '0c4uFfnflVhAXSXLthHJXb': {'name': 'No Maps of the Past', 'artist_id': '3sva1UjOJOx6cGISZOpItl', 'artist_name': 'The Collection', 'album_name': 'Listen to the River', 'track_number': 5, 'duration_ms': 282286, 'popularity': 32, 'danceability': 0.452, 'energy': 0.17, 'loudness': -13.575, 'speechiness': 0.0286, 'acousticness': 0.863, 'instrumentalness': 0.000391, 'liveness': 0.094, 'valence': 0.227, 'tempo': 78.376}, '0fKeNF09yFaOguCSE9HrNa': {'name': 'Siddhartha (My Light Was a Ghost)', 'artist_id': '3sva1UjOJOx6cGISZOpItl', 'artist_name': 'The Collection', 'album_name': 'Listen to the River', 'track_number': 6, 'duration_ms': 245318, 'popularity': 30, 'danceability': 0.39, 'energy': 0.583, 'loudness': -8.087, 'speechiness': 0.0349, 'acousticness': 0.017, 'instrumentalness': 0.015, 'liveness': 0.138, 'valence': 0.191, 'tempo': 119.991}, '6IUVyMsCzAnHSSNFkLzmya': {'name': 'The Older One', 'artist_id': '3sva1UjOJOx6cGISZOpItl', 'artist_name': 'The Collection', 'album_name': 'Listen to the River', 'track_number': 9, 'duration_ms': 390155, 'popularity': 30, 'danceability': 0.405, 'energy': 0.301, 'loudness': -10.773, 'speechiness': 0.0334, 'acousticness': 0.709, 'instrumentalness': 0.0375, 'liveness': 0.167, 'valence': 0.125, 'tempo': 137.958}, '0TD0ydYJuFPEaqshquDEpw': {'name': 'Valentina', 'artist_id': '1fFdRZK1GDGXL7vRxxUWLH', 'artist_name': 'The Hunts', 'album_name': 'Those Younger Days', 'track_number': 1, 'duration_ms': 230212, 'popularity': 43, 'danceability': 0.629, 'energy': 0.831, 'loudness': -6.627, 'speechiness': 0.0328, 'acousticness': 0.385, 'instrumentalness': 0.0025, 'liveness': 0.239, 'valence': 0.585, 'tempo': 144.014}, '6q1iHfSRuT2rNbaeOtcUTT': {'name': 'Lifting The Sea', 'artist_id': '1fFdRZK1GDGXL7vRxxUWLH', 'artist_name': 'The Hunts', 'album_name': 'Those Younger Days', 'track_number': 6, 'duration_ms': 299119, 'popularity': 33, 'danceability': 0.7, 'energy': 0.414, 'loudness': -10.817, 'speechiness': 0.0375, 'acousticness': 0.934, 'instrumentalness': 0.0102, 'liveness': 0.0918, 'valence': 0.188, 'tempo': 145.965}, '0c4qRoM7FMFo6iguuIlVIJ': {'name': 'Remember Us', 'artist_id': '1fFdRZK1GDGXL7vRxxUWLH', 'artist_name': 'The Hunts', 'album_name': 'Those Younger Days', 'track_number': 4, 'duration_ms': 242812, 'popularity': 32, 'danceability': 0.612, 'energy': 0.369, 'loudness': -10.58, 'speechiness': 0.0279, 'acousticness': 0.758, 'instrumentalness': 0.0146, 'liveness': 0.0934, 'valence': 0.327, 'tempo': 138.929}, '0DSaUCe6GTuDYeevMJ5uBX': {'name': 'Illuminate', 'artist_id': '1fFdRZK1GDGXL7vRxxUWLH', 'artist_name': 'The Hunts', 'album_name': 'Those Younger Days', 'track_number': 2, 'duration_ms': 230746, 'popularity': 30, 'danceability': 0.516, 'energy': 0.783, 'loudness': -7.976, 'speechiness': 0.0304, 'acousticness': 0.0542, 'instrumentalness': 0.0251, 'liveness': 0.0872, 'valence': 0.268, 'tempo': 100.988}, '0du9w3e8Xkrbl2b7SyZ6Ma': {'name': 'This Is Love', 'artist_id': '1fFdRZK1GDGXL7vRxxUWLH', 'artist_name': 'The Hunts', 'album_name': 'Those Younger Days', 'track_number': 8, 'duration_ms': 223986, 'popularity': 30, 'danceability': 0.5, 'energy': 0.473, 'loudness': -7.073, 'speechiness': 0.0314, 'acousticness': 0.0439, 'instrumentalness': 7.19e-06, 'liveness': 0.0729, 'valence': 0.349, 'tempo': 177.854}, '3zQX4mlMtH5fUdJXcArLXt': {'name': 'Douse The Flame', 'artist_id': '1fFdRZK1GDGXL7vRxxUWLH', 'artist_name': 'The Hunts', 'album_name': 'Those Younger Days', 'track_number': 9, 'duration_ms': 292119, 'popularity': 29, 'danceability': 0.542, 'energy': 0.705, 'loudness': -9.128, 'speechiness': 0.0313, 'acousticness': 0.231, 'instrumentalness': 0.0341, 'liveness': 0.111, 'valence': 0.43, 'tempo': 132.031}, '1xnVivWRSk3ihIc9eskMEy': {'name': 'Ages', 'artist_id': '1fFdRZK1GDGXL7vRxxUWLH', 'artist_name': 'The Hunts', 'album_name': 'Those Younger Days', 'track_number': 7, 'duration_ms': 190066, 'popularity': 29, 'danceability': 0.645, 'energy': 0.702, 'loudness': -6.304, 'speechiness': 0.0302, 'acousticness': 0.0286, 'instrumentalness': 0.000101, 'liveness': 0.109, 'valence': 0.341, 'tempo': 121.096}, '6f223VXzVbvFAivhYptz9f': {'name': 'Just For A While', 'artist_id': '1fFdRZK1GDGXL7vRxxUWLH', 'artist_name': 'The Hunts', 'album_name': 'Those Younger Days', 'track_number': 3, 'duration_ms': 189666, 'popularity': 29, 'danceability': 0.636, 'energy': 0.65, 'loudness': -6.288, 'speechiness': 0.0315, 'acousticness': 0.319, 'instrumentalness': 1.02e-05, 'liveness': 0.0548, 'valence': 0.881, 'tempo': 199.974}, '43168z8wHwMiHtNUvE73cD': {'name': 'Please Let It Go', 'artist_id': '1fFdRZK1GDGXL7vRxxUWLH', 'artist_name': 'The Hunts', 'album_name': 'Those Younger Days', 'track_number': 10, 'duration_ms': 209012, 'popularity': 26, 'danceability': 0.561, 'energy': 0.217, 'loudness': -11.876, 'speechiness': 0.0279, 'acousticness': 0.641, 'instrumentalness': 0.000105, 'liveness': 0.126, 'valence': 0.277, 'tempo': 127.993}, '6JrhK1EuBS9EKpFmcuhrp1': {'name': 'West Coast', 'artist_id': '3PMXHMqW4MNj8usJ0fxAlj', 'artist_name': 'Hey Marseilles', 'album_name': 'Hey Marseilles', 'track_number': 2, 'duration_ms': 218133, 'popularity': 43, 'danceability': 0.575, 'energy': 0.651, 'loudness': -5.209, 'speechiness': 0.0258, 'acousticness': 0.00831, 'instrumentalness': 2.99e-06, 'liveness': 0.099, 'valence': 0.412, 'tempo': 138.804}, '3f8DQVBBB3nQVuOdDALRgX': {'name': 'Elegy', 'artist_id': '3PMXHMqW4MNj8usJ0fxAlj', 'artist_name': 'Hey Marseilles', 'album_name': 'Lines We Trace', 'track_number': 4, 'duration_ms': 254440, 'popularity': 28, 'danceability': 0.423, 'energy': 0.197, 'loudness': -14.562, 'speechiness': 0.0288, 'acousticness': 0.729, 'instrumentalness': 0.052, 'liveness': 0.129, 'valence': 0.217, 'tempo': 144.769}, '5RLSjCJB9pQ3yQk2YTJufZ': {'name': 'To Travels and Trunks', 'artist_id': '3PMXHMqW4MNj8usJ0fxAlj', 'artist_name': 'Hey Marseilles', 'album_name': 'To Travels and Trunks', 'track_number': 2, 'duration_ms': 187506, 'popularity': 39, 'danceability': 0.217, 'energy': 0.599, 'loudness': -6.308, 'speechiness': 0.0292, 'acousticness': 0.13, 'instrumentalness': 0, 'liveness': 0.0713, 'valence': 0.257, 'tempo': 109.908}, '6To2fU3EazmMNDR9hwNywO': {'name': 'Eyes On You', 'artist_id': '3PMXHMqW4MNj8usJ0fxAlj', 'artist_name': 'Hey Marseilles', 'album_name': 'Hey Marseilles', 'track_number': 1, 'duration_ms': 176413, 'popularity': 35, 'danceability': 0.515, 'energy': 0.724, 'loudness': -5.228, 'speechiness': 0.0517, 'acousticness': 0.00239, 'instrumentalness': 0.00376, 'liveness': 0.0862, 'valence': 0.28, 'tempo': 157.827}, '6OMgG0xTvMS2o4dXM4WZrE': {'name': 'North And South', 'artist_id': '3PMXHMqW4MNj8usJ0fxAlj', 'artist_name': 'Hey Marseilles', 'album_name': 'Hey Marseilles', 'track_number': 9, 'duration_ms': 189253, 'popularity': 32, 'danceability': 0.387, 'energy': 0.377, 'loudness': -6.466, 'speechiness': 0.044, 'acousticness': 0.591, 'instrumentalness': 2.33e-06, 'liveness': 0.092, 'valence': 0.0651, 'tempo': 120.045}, '6nzNsWi3vJRiTAY7oqqpbm': {'name': 'Heart Beats', 'artist_id': '3PMXHMqW4MNj8usJ0fxAlj', 'artist_name': 'Hey Marseilles', 'album_name': 'Lines We Trace', 'track_number': 2, 'duration_ms': 251120, 'popularity': 32, 'danceability': 0.536, 'energy': 0.411, 'loudness': -12.62, 'speechiness': 0.0333, 'acousticness': 0.154, 'instrumentalness': 0.0296, 'liveness': 0.12, 'valence': 0.203, 'tempo': 125.999}, '17CkR7hqDVTVIRopJAZ3Rf': {'name': 'Rio', 'artist_id': '3PMXHMqW4MNj8usJ0fxAlj', 'artist_name': 'Hey Marseilles', 'album_name': 'To Travels and Trunks', 'track_number': 4, 'duration_ms': 238200, 'popularity': 31, 'danceability': 0.636, 'energy': 0.784, 'loudness': -5.274, 'speechiness': 0.0476, 'acousticness': 0.396, 'instrumentalness': 0.000423, 'liveness': 0.0736, 'valence': 0.792, 'tempo': 97.427}, '5qPU3nfW5ajPlp9RBTD1rm': {'name': 'Rainfall', 'artist_id': '3PMXHMqW4MNj8usJ0fxAlj', 'artist_name': 'Hey Marseilles', 'album_name': 'Lines We Trace', 'track_number': 9, 'duration_ms': 252426, 'popularity': 11, 'danceability': 0.581, 'energy': 0.324, 'loudness': -13.012, 'speechiness': 0.0271, 'acousticness': 0.352, 'instrumentalness': 0.0258, 'liveness': 0.166, 'valence': 0.354, 'tempo': 103.015}, '141UQ2wXw3PswOHt4U5Kh7': {'name': 'Marseilles', 'artist_id': '3PMXHMqW4MNj8usJ0fxAlj', 'artist_name': 'Hey Marseilles', 'album_name': 'To Travels and Trunks', 'track_number': 1, 'duration_ms': 176213, 'popularity': 27, 'danceability': 0.415, 'energy': 0.154, 'loudness': -10.936, 'speechiness': 0.0362, 'acousticness': 0.945, 'instrumentalness': 0.916, 'liveness': 0.0789, 'valence': 0.0683, 'tempo': 119.941}, '5y6Nr0CiN1Uf1uIfdHtWuX': {'name': 'Tides', 'artist_id': '3PMXHMqW4MNj8usJ0fxAlj', 'artist_name': 'Hey Marseilles', 'album_name': 'Lines We Trace', 'track_number': 1, 'duration_ms': 262520, 'popularity': 26, 'danceability': 0.311, 'energy': 0.305, 'loudness': -13.2, 'speechiness': 0.0299, 'acousticness': 0.472, 'instrumentalness': 0.000541, 'liveness': 0.12, 'valence': 0.21, 'tempo': 179.813}, '3wsZYuHJrk3lssa7V7jvye': {'name': 'Poison & Wine', 'artist_id': '6J7rw7NELJUCThPbAfyLIE', 'artist_name': 'The Civil Wars', 'album_name': 'Barton Hollow', 'track_number': 5, 'duration_ms': 219466, 'popularity': 65, 'danceability': 0.285, 'energy': 0.186, 'loudness': -12.729, 'speechiness': 0.0288, 'acousticness': 0.76, 'instrumentalness': 7.3e-05, 'liveness': 0.104, 'valence': 0.226, 'tempo': 153.848}, '4zzi2eD2cEPpQ3a307mPPj': {'name': 'Billie Jean', 'artist_id': '6J7rw7NELJUCThPbAfyLIE', 'artist_name': 'The Civil Wars', 'album_name': 'Between The Bars (EP)', 'track_number': 3, 'duration_ms': 259920, 'popularity': 65, 'danceability': 0.532, 'energy': 0.203, 'loudness': -8.524, 'speechiness': 0.0668, 'acousticness': 0.829, 'instrumentalness': 0, 'liveness': 0.108, 'valence': 0.54, 'tempo': 89.646}, '5P6ZBMWS66FVo6deJaDdHy': {'name': 'Dust to Dust', 'artist_id': '6J7rw7NELJUCThPbAfyLIE', 'artist_name': 'The Civil Wars', 'album_name': 'The Civil Wars', 'track_number': 4, 'duration_ms': 229653, 'popularity': 62, 'danceability': 0.747, 'energy': 0.265, 'loudness': -14.141, 'speechiness': 0.0354, 'acousticness': 0.745, 'instrumentalness': 0.0169, 'liveness': 0.11, 'valence': 0.208, 'tempo': 138.017}, '6tZAbv5JEsfqjTpkBOrLje': {'name': 'Dance Me to the End of Love - Bonus Track', 'artist_id': '6J7rw7NELJUCThPbAfyLIE', 'artist_name': 'The Civil Wars', 'album_name': 'Barton Hollow', 'track_number': 14, 'duration_ms': 185053, 'popularity': 60, 'danceability': 0.473, 'energy': 0.184, 'loudness': -11.182, 'speechiness': 0.029, 'acousticness': 0.855, 'instrumentalness': 0, 'liveness': 0.145, 'valence': 0.288, 'tempo': 110.081}, '0iTqedrMdiwnUXKiUjtxAl': {'name': 'To Whom It May Concern', 'artist_id': '6J7rw7NELJUCThPbAfyLIE', 'artist_name': 'The Civil Wars', 'album_name': 'Barton Hollow', 'track_number': 4, 'duration_ms': 211360, 'popularity': 60, 'danceability': 0.309, 'energy': 0.159, 'loudness': -13.101, 'speechiness': 0.0315, 'acousticness': 0.912, 'instrumentalness': 0.000264, 'liveness': 0.1, 'valence': 0.14, 'tempo': 87.493}, '4qoD4IJbbir3hsAu4IowiG': {'name': "Devil's Backbone", 'artist_id': '6J7rw7NELJUCThPbAfyLIE', 'artist_name': 'The Civil Wars', 'album_name': 'The Civil Wars', 'track_number': 6, 'duration_ms': 149426, 'popularity': 59, 'danceability': 0.254, 'energy': 0.349, 'loudness': -10.02, 'speechiness': 0.0379, 'acousticness': 0.85, 'instrumentalness': 2.95e-05, 'liveness': 0.234, 'valence': 0.26, 'tempo': 170.214}, '2P84QNQFhSoexVt5jEsfmd': {'name': 'Dust to Dust - Acoustic', 'artist_id': '6J7rw7NELJUCThPbAfyLIE', 'artist_name': 'The Civil Wars', 'album_name': 'Bare Bones EP', 'track_number': 3, 'duration_ms': 223786, 'popularity': 57, 'danceability': 0.678, 'energy': 0.0921, 'loudness': -17.107, 'speechiness': 0.0437, 'acousticness': 0.967, 'instrumentalness': 0.00489, 'liveness': 0.111, 'valence': 0.158, 'tempo': 137.965}, '2ZheGCM31EbCwUfGs0WJB1': {'name': 'Barton Hollow', 'artist_id': '6J7rw7NELJUCThPbAfyLIE', 'artist_name': 'The Civil Wars', 'album_name': 'Barton Hollow', 'track_number': 7, 'duration_ms': 205773, 'popularity': 57, 'danceability': 0.403, 'energy': 0.659, 'loudness': -7.338, 'speechiness': 0.0303, 'acousticness': 0.123, 'instrumentalness': 0, 'liveness': 0.0857, 'valence': 0.443, 'tempo': 90.854}, '4mm4V9uS6AOuWBG0f65HH9': {'name': 'Between the Bars', 'artist_id': '6J7rw7NELJUCThPbAfyLIE', 'artist_name': 'The Civil Wars', 'album_name': 'Between The Bars (EP)', 'track_number': 2, 'duration_ms': 167386, 'popularity': 55, 'danceability': 0.421, 'energy': 0.21, 'loudness': -11.591, 'speechiness': 0.0371, 'acousticness': 0.893, 'instrumentalness': 8.67e-06, 'liveness': 0.0997, 'valence': 0.305, 'tempo': 117.671}, '4fwiUXTml7O24fL34JxFI7': {'name': 'Same Old Same Old', 'artist_id': '6J7rw7NELJUCThPbAfyLIE', 'artist_name': 'The Civil Wars', 'album_name': 'The Civil Wars', 'track_number': 3, 'duration_ms': 228333, 'popularity': 55, 'danceability': 0.401, 'energy': 0.161, 'loudness': -11.138, 'speechiness': 0.0372, 'acousticness': 0.781, 'instrumentalness': 3.56e-06, 'liveness': 0.118, 'valence': 0.103, 'tempo': 129.826}, '6lOsjTvgGL08uRf2nKrSed': {'name': 'Dreaming - The Chainsmokers Remix', 'artist_id': '4iiQabGKtS2RtTKpVkrVTw', 'artist_name': 'Smallpools', 'album_name': 'Dreaming Remix EP', 'track_number': 1, 'duration_ms': 297906, 'popularity': 63, 'danceability': 0.628, 'energy': 0.978, 'loudness': -3.739, 'speechiness': 0.0771, 'acousticness': 0.0132, 'instrumentalness': 0.0336, 'liveness': 0.0494, 'valence': 0.454, 'tempo': 127.04}, '6cMswWRv4lAU3mh5lclgCc': {'name': 'Dreaming', 'artist_id': '4iiQabGKtS2RtTKpVkrVTw', 'artist_name': 'Smallpools', 'album_name': 'LOVETAP!', 'track_number': 3, 'duration_ms': 216253, 'popularity': 56, 'danceability': 0.612, 'energy': 0.89, 'loudness': -2.827, 'speechiness': 0.047, 'acousticness': 0.000478, 'instrumentalness': 0, 'liveness': 0.0672, 'valence': 0.884, 'tempo': 118.989}, '0qnOjNW04qpcgXqD9dwru2': {'name': 'Killer Whales', 'artist_id': '4iiQabGKtS2RtTKpVkrVTw', 'artist_name': 'Smallpools', 'album_name': 'LOVETAP!', 'track_number': 2, 'duration_ms': 222760, 'popularity': 55, 'danceability': 0.416, 'energy': 0.849, 'loudness': -3.833, 'speechiness': 0.0503, 'acousticness': 0.000303, 'instrumentalness': 4.23e-05, 'liveness': 0.185, 'valence': 0.662, 'tempo': 144.844}, '0hxy93CbIX7Hd5WXaVjx5R': {'name': 'Street Fight', 'artist_id': '4iiQabGKtS2RtTKpVkrVTw', 'artist_name': 'Smallpools', 'album_name': 'LOVETAP!', 'track_number': 5, 'duration_ms': 203453, 'popularity': 53, 'danceability': 0.556, 'energy': 0.916, 'loudness': -5.143, 'speechiness': 0.0398, 'acousticness': 8.95e-05, 'instrumentalness': 0.00341, 'liveness': 0.347, 'valence': 0.461, 'tempo': 116.065}, '6WSJ5SmQubgYOXM66Eo9va': {'name': 'Over & Over', 'artist_id': '4iiQabGKtS2RtTKpVkrVTw', 'artist_name': 'Smallpools', 'album_name': 'LOVETAP!', 'track_number': 7, 'duration_ms': 167066, 'popularity': 51, 'danceability': 0.552, 'energy': 0.914, 'loudness': -4.112, 'speechiness': 0.0399, 'acousticness': 7.12e-05, 'instrumentalness': 1.68e-06, 'liveness': 0.187, 'valence': 0.291, 'tempo': 113.075}, '0m8z88MqUfbstTIUMK2wfZ': {'name': 'American Love', 'artist_id': '4iiQabGKtS2RtTKpVkrVTw', 'artist_name': 'Smallpools', 'album_name': 'LOVETAP!', 'track_number': 1, 'duration_ms': 179346, 'popularity': 48, 'danceability': 0.434, 'energy': 0.68, 'loudness': -4.84, 'speechiness': 0.0322, 'acousticness': 0.000525, 'instrumentalness': 0.0243, 'liveness': 0.211, 'valence': 0.396, 'tempo': 156.941}, '0UUl3PYC5aSdKrYBkNrN6C': {'name': "Dyin' to Live", 'artist_id': '4iiQabGKtS2RtTKpVkrVTw', 'artist_name': 'Smallpools', 'album_name': 'LOVETAP!', 'track_number': 10, 'duration_ms': 195400, 'popularity': 47, 'danceability': 0.594, 'energy': 0.824, 'loudness': -4.713, 'speechiness': 0.0494, 'acousticness': 0.0025, 'instrumentalness': 1.38e-05, 'liveness': 0.36, 'valence': 0.511, 'tempo': 129.968}, '2uV2tyFZ0Eex2Lsc8shIfN': {'name': 'Karaoke', 'artist_id': '4iiQabGKtS2RtTKpVkrVTw', 'artist_name': 'Smallpools', 'album_name': 'LOVETAP!', 'track_number': 4, 'duration_ms': 209933, 'popularity': 47, 'danceability': 0.585, 'energy': 0.906, 'loudness': -3.407, 'speechiness': 0.0515, 'acousticness': 0.0079, 'instrumentalness': 5.05e-06, 'liveness': 0.336, 'valence': 0.387, 'tempo': 126.957}, '23kzZbGbs51X03t9Vy5GMa': {'name': 'Run With the Bulls', 'artist_id': '4iiQabGKtS2RtTKpVkrVTw', 'artist_name': 'Smallpools', 'album_name': 'Run With the Bulls', 'track_number': 1, 'duration_ms': 88958, 'popularity': 46, 'danceability': 0.461, 'energy': 0.978, 'loudness': -4.226, 'speechiness': 0.113, 'acousticness': 0.000609, 'instrumentalness': 8.91e-05, 'liveness': 0.64, 'valence': 0.356, 'tempo': 170.142}, '6ZtlUSe5Vt1ev5767zg46s': {'name': 'Mason Jar', 'artist_id': '4iiQabGKtS2RtTKpVkrVTw', 'artist_name': 'Smallpools', 'album_name': 'LOVETAP!', 'track_number': 6, 'duration_ms': 219933, 'popularity': 43, 'danceability': 0.292, 'energy': 0.862, 'loudness': -3.81, 'speechiness': 0.0417, 'acousticness': 0.000267, 'instrumentalness': 0.13, 'liveness': 0.646, 'valence': 0.302, 'tempo': 134.602}, '1sPUneI4q4ZChaPXXNpfWa': {'name': 'March: Hills to Climb', 'artist_id': '44BkC9lJfLmhcRB4NV7Z38', 'artist_name': 'Tim Myers', 'album_name': 'The Year', 'track_number': 3, 'duration_ms': 239600, 'popularity': 42, 'danceability': 0.474, 'energy': 0.665, 'loudness': -6.886, 'speechiness': 0.0307, 'acousticness': 0.00285, 'instrumentalness': 0.0249, 'liveness': 0.106, 'valence': 0.222, 'tempo': 113.972}, '6BjPiZI6q7r4qXpOtYWOEe': {'name': 'June: Good Days Start Here', 'artist_id': '44BkC9lJfLmhcRB4NV7Z38', 'artist_name': 'Tim Myers', 'album_name': 'The Year', 'track_number': 6, 'duration_ms': 223560, 'popularity': 27, 'danceability': 0.592, 'energy': 0.704, 'loudness': -7.007, 'speechiness': 0.0265, 'acousticness': 4.89e-05, 'instrumentalness': 0.000243, 'liveness': 0.221, 'valence': 0.468, 'tempo': 110.039}, '19nbrRzEM0ldFwbqO0KsZI': {'name': 'A Beautiful World', 'artist_id': '44BkC9lJfLmhcRB4NV7Z38', 'artist_name': 'Tim Myers', 'album_name': 'Technicolor', 'track_number': 4, 'duration_ms': 205613, 'popularity': 26, 'danceability': 0.534, 'energy': 0.413, 'loudness': -9.701, 'speechiness': 0.0289, 'acousticness': 0.167, 'instrumentalness': 1.94e-06, 'liveness': 0.147, 'valence': 0.33, 'tempo': 138.135}, '0vmU1XjtNWBWJEpHG0GThM': {'name': "April: It's My Life", 'artist_id': '44BkC9lJfLmhcRB4NV7Z38', 'artist_name': 'Tim Myers', 'album_name': 'The Year', 'track_number': 4, 'duration_ms': 229986, 'popularity': 23, 'danceability': 0.37, 'energy': 0.582, 'loudness': -6.948, 'speechiness': 0.0315, 'acousticness': 0.213, 'instrumentalness': 0.000207, 'liveness': 0.0857, 'valence': 0.209, 'tempo': 180.166}, '344PGLp8wbKibf4zmnD4Gt': {'name': 'October: Written in the Stars', 'artist_id': '44BkC9lJfLmhcRB4NV7Z38', 'artist_name': 'Tim Myers', 'album_name': 'The Year', 'track_number': 10, 'duration_ms': 207146, 'popularity': 22, 'danceability': 0.306, 'energy': 0.319, 'loudness': -7.804, 'speechiness': 0.0299, 'acousticness': 0.649, 'instrumentalness': 0.00137, 'liveness': 0.0749, 'valence': 0.179, 'tempo': 68.853}, '6tuzzG8BsAI9SaIxyMPs3X': {'name': "Today's The Day", 'artist_id': '44BkC9lJfLmhcRB4NV7Z38', 'artist_name': 'Tim Myers', 'album_name': 'Technicolor', 'track_number': 11, 'duration_ms': 272986, 'popularity': 20, 'danceability': 0.624, 'energy': 0.878, 'loudness': -2.421, 'speechiness': 0.0281, 'acousticness': 0.0435, 'instrumentalness': 8.25e-05, 'liveness': 0.103, 'valence': 0.275, 'tempo': 126.055}, '0eaBGg1GCNiCtMTuFVM1rn': {'name': 'Young At Heart', 'artist_id': '44BkC9lJfLmhcRB4NV7Z38', 'artist_name': 'Tim Myers', 'album_name': 'The Way Way Back - Music From The Motion Picture', 'track_number': 10, 'duration_ms': 219320, 'popularity': 19, 'danceability': 0.513, 'energy': 0.965, 'loudness': -4.685, 'speechiness': 0.0531, 'acousticness': 0.0623, 'instrumentalness': 6.25e-06, 'liveness': 0.109, 'valence': 0.738, 'tempo': 177.967}, '2hdYsU1vooYiQmrgNJslrE': {'name': "July: Life's Adventures", 'artist_id': '44BkC9lJfLmhcRB4NV7Z38', 'artist_name': 'Tim Myers', 'album_name': 'The Year', 'track_number': 7, 'duration_ms': 193466, 'popularity': 18, 'danceability': 0.495, 'energy': 0.791, 'loudness': -7.522, 'speechiness': 0.0278, 'acousticness': 0.613, 'instrumentalness': 0.682, 'liveness': 0.0777, 'valence': 0.481, 'tempo': 152.013}, '5Oa6SAXiYPS4BffLcAdG46': {'name': 'August: Me & My Friends (feat. El May)', 'artist_id': '44BkC9lJfLmhcRB4NV7Z38', 'artist_name': 'Tim Myers', 'album_name': 'The Year', 'track_number': 8, 'duration_ms': 213240, 'popularity': 15, 'danceability': 0.655, 'energy': 0.707, 'loudness': -5.31, 'speechiness': 0.0313, 'acousticness': 0.0123, 'instrumentalness': 0.076, 'liveness': 0.15, 'valence': 0.716, 'tempo': 108.509}, '6xWGardFQzilB1HVxIsgrp': {'name': 'September: Wonderful Life', 'artist_id': '44BkC9lJfLmhcRB4NV7Z38', 'artist_name': 'Tim Myers', 'album_name': 'The Year', 'track_number': 9, 'duration_ms': 176760, 'popularity': 15, 'danceability': 0.398, 'energy': 0.784, 'loudness': -5.743, 'speechiness': 0.0293, 'acousticness': 0.842, 'instrumentalness': 0.925, 'liveness': 0.0589, 'valence': 0.207, 'tempo': 154.015}, '6C2XDnr9B6obGMVhHS1Nmo': {'name': 'Gonna Wanna Tonight', 'artist_id': '6pBNfggcZZDCmb0p92OnGn', 'artist_name': 'Chase Rice', 'album_name': 'Ignite the Night (Party Edition)', 'track_number': 8, 'duration_ms': 214949, 'popularity': 71, 'danceability': 0.584, 'energy': 0.79, 'loudness': -6.544, 'speechiness': 0.0412, 'acousticness': 0.0444, 'instrumentalness': 4.22e-05, 'liveness': 0.0734, 'valence': 0.702, 'tempo': 123.961}, '1CoOHJAHtKEDnUBrp3nKAB': {'name': 'Ride (feat. Macy Maloy)', 'artist_id': '6pBNfggcZZDCmb0p92OnGn', 'artist_name': 'Chase Rice', 'album_name': 'Ignite the Night (Party Edition)', 'track_number': 18, 'duration_ms': 241240, 'popularity': 67, 'danceability': 0.666, 'energy': 0.694, 'loudness': -7.184, 'speechiness': 0.0333, 'acousticness': 0.0374, 'instrumentalness': 0, 'liveness': 0.124, 'valence': 0.35, 'tempo': 115.07}, '3rh2f6nqswpfDN3Ef6Bi5J': {'name': 'Ready Set Roll', 'artist_id': '6pBNfggcZZDCmb0p92OnGn', 'artist_name': 'Chase Rice', 'album_name': 'Ignite the Night (Party Edition)', 'track_number': 1, 'duration_ms': 190587, 'popularity': 66, 'danceability': 0.513, 'energy': 0.803, 'loudness': -4.45, 'speechiness': 0.0777, 'acousticness': 0.0161, 'instrumentalness': 0, 'liveness': 0.667, 'valence': 0.737, 'tempo': 156.038}, '1MTEImRXVeL8VTDSDbgW6V': {'name': 'Carolina Can', 'artist_id': '6pBNfggcZZDCmb0p92OnGn', 'artist_name': 'Chase Rice', 'album_name': 'Ignite the Night (Party Edition)', 'track_number': 6, 'duration_ms': 220454, 'popularity': 66, 'danceability': 0.479, 'energy': 0.642, 'loudness': -5.727, 'speechiness': 0.0302, 'acousticness': 0.0269, 'instrumentalness': 0, 'liveness': 0.105, 'valence': 0.368, 'tempo': 157.981}, '6LcPSBPSYRTMG7brqZQ7aq': {'name': 'Everybody We Know Does', 'artist_id': '6pBNfggcZZDCmb0p92OnGn', 'artist_name': 'Chase Rice', 'album_name': 'Everybody We Know Does', 'track_number': 1, 'duration_ms': 221626, 'popularity': 62, 'danceability': 0.572, 'energy': 0.841, 'loudness': -2.988, 'speechiness': 0.0609, 'acousticness': 0.0115, 'instrumentalness': 0, 'liveness': 0.101, 'valence': 0.598, 'tempo': 136.978}, '6EdSZmWCQJfO8T66x9VCID': {'name': 'Whisper', 'artist_id': '6pBNfggcZZDCmb0p92OnGn', 'artist_name': 'Chase Rice', 'album_name': 'Whisper', 'track_number': 1, 'duration_ms': 191213, 'popularity': 57, 'danceability': 0.509, 'energy': 0.891, 'loudness': -4.89, 'speechiness': 0.0757, 'acousticness': 0.0138, 'instrumentalness': 0, 'liveness': 0.063, 'valence': 0.643, 'tempo': 128.108}, '4LGlMGHwJGY8tUXQfZWUzm': {'name': 'How She Rolls', 'artist_id': '6pBNfggcZZDCmb0p92OnGn', 'artist_name': 'Chase Rice', 'album_name': 'Ignite the Night (Party Edition)', 'track_number': 13, 'duration_ms': 179076, 'popularity': 54, 'danceability': 0.468, 'energy': 0.926, 'loudness': -4.404, 'speechiness': 0.0437, 'acousticness': 0.00019, 'instrumentalness': 0.00073, 'liveness': 0.139, 'valence': 0.669, 'tempo': 146.03}, '1ZT7y9KbzTwuyT51ch0jt0': {'name': '50 Shades of Crazy', 'artist_id': '6pBNfggcZZDCmb0p92OnGn', 'artist_name': 'Chase Rice', 'album_name': 'Ignite the Night (Party Edition)', 'track_number': 11, 'duration_ms': 190292, 'popularity': 53, 'danceability': 0.519, 'energy': 0.97, 'loudness': -4.469, 'speechiness': 0.0422, 'acousticness': 0.00031, 'instrumentalness': 0, 'liveness': 0.104, 'valence': 0.764, 'tempo': 151.984}, '3nd43CEbT11MUQVIh7GGiL': {'name': 'Look at My Truck', 'artist_id': '6pBNfggcZZDCmb0p92OnGn', 'artist_name': 'Chase Rice', 'album_name': 'Ignite the Night (Party Edition)', 'track_number': 9, 'duration_ms': 196130, 'popularity': 53, 'danceability': 0.455, 'energy': 0.842, 'loudness': -4.483, 'speechiness': 0.0386, 'acousticness': 0.00627, 'instrumentalness': 0, 'liveness': 0.34, 'valence': 0.569, 'tempo': 160.019}, '33ntke7makdcaGe5DsmcLi': {'name': "If I'm Bein' honest", 'artist_id': '6pBNfggcZZDCmb0p92OnGn', 'artist_name': 'Chase Rice', 'album_name': "If I'm Bein' honest", 'track_number': 1, 'duration_ms': 207407, 'popularity': 52, 'danceability': 0.571, 'energy': 0.514, 'loudness': -8.201, 'speechiness': 0.0303, 'acousticness': 0.855, 'instrumentalness': 5.42e-06, 'liveness': 0.278, 'valence': 0.472, 'tempo': 143.926}, '7xsjI11alpcfweV1y75dSs': {'name': 'Call The Captain', 'artist_id': '1a6tqLJPUs4DBAnNUZkr2O', 'artist_name': 'Steep Canyon Rangers', 'album_name': "Lovin' Pretty Women", 'track_number': 4, 'duration_ms': 254146, 'popularity': 36, 'danceability': 0.723, 'energy': 0.374, 'loudness': -11.298, 'speechiness': 0.0442, 'acousticness': 0.85, 'instrumentalness': 1.42e-06, 'liveness': 0.141, 'valence': 0.688, 'tempo': 122.079}, '26iGc8sFIpHUEpLkjtBIBF': {'name': 'Come Dance', 'artist_id': '1a6tqLJPUs4DBAnNUZkr2O', 'artist_name': 'Steep Canyon Rangers', 'album_name': 'Tell The Ones I Love', 'track_number': 4, 'duration_ms': 179653, 'popularity': 33, 'danceability': 0.621, 'energy': 0.69, 'loudness': -5.497, 'speechiness': 0.0301, 'acousticness': 0.655, 'instrumentalness': 0.00665, 'liveness': 0.331, 'valence': 0.895, 'tempo': 124.04}, '45or5lcxKF2pgrUKDqlYQY': {'name': 'Stand And Deliver', 'artist_id': '1a6tqLJPUs4DBAnNUZkr2O', 'artist_name': 'Steep Canyon Rangers', 'album_name': 'Tell The Ones I Love', 'track_number': 2, 'duration_ms': 210866, 'popularity': 32, 'danceability': 0.587, 'energy': 0.833, 'loudness': -7.22, 'speechiness': 0.0774, 'acousticness': 0.512, 'instrumentalness': 0.00813, 'liveness': 0.104, 'valence': 0.96, 'tempo': 169.764}, '3FJewohG3cojZjIwKhpuMQ': {'name': 'Tell The Ones I Love', 'artist_id': '1a6tqLJPUs4DBAnNUZkr2O', 'artist_name': 'Steep Canyon Rangers', 'album_name': 'Tell The Ones I Love', 'track_number': 1, 'duration_ms': 256973, 'popularity': 30, 'danceability': 0.435, 'energy': 0.645, 'loudness': -8.092, 'speechiness': 0.0339, 'acousticness': 0.767, 'instrumentalness': 0.0136, 'liveness': 0.122, 'valence': 0.769, 'tempo': 143.459}, '2AiTuukRNgoUeCyWxKo7wI': {'name': 'Radio', 'artist_id': '1a6tqLJPUs4DBAnNUZkr2O', 'artist_name': 'Steep Canyon Rangers', 'album_name': 'RADIO', 'track_number': 1, 'duration_ms': 205372, 'popularity': 29, 'danceability': 0.541, 'energy': 0.861, 'loudness': -5.883, 'speechiness': 0.0513, 'acousticness': 0.579, 'instrumentalness': 0.000508, 'liveness': 0.0665, 'valence': 0.864, 'tempo': 88.304}, '7JY0idqjJLLOCpEMNkzuKH': {'name': 'Looking Glass', 'artist_id': '1a6tqLJPUs4DBAnNUZkr2O', 'artist_name': 'Steep Canyon Rangers', 'album_name': 'RADIO', 'track_number': 6, 'duration_ms': 169546, 'popularity': 29, 'danceability': 0.566, 'energy': 0.793, 'loudness': -8.036, 'speechiness': 0.0314, 'acousticness': 0.459, 'instrumentalness': 0.746, 'liveness': 0.301, 'valence': 0.955, 'tempo': 138.95}, '2ATQkGLIx2ncMKG54jCM9M': {'name': 'Knob Creek', 'artist_id': '1a6tqLJPUs4DBAnNUZkr2O', 'artist_name': 'Steep Canyon Rangers', 'album_name': 'Nobody Knows You', 'track_number': 10, 'duration_ms': 317306, 'popularity': 27, 'danceability': 0.629, 'energy': 0.564, 'loudness': -7.774, 'speechiness': 0.0294, 'acousticness': 0.739, 'instrumentalness': 0.409, 'liveness': 0.201, 'valence': 0.747, 'tempo': 149.955}, '7rQZBa7ftCF9cNsLkl9ROk': {'name': 'The Great Remember (for Nancy)', 'artist_id': '1Bd4UVlqlaKEXYRG3wgrCK', 'artist_name': 'Steve Martin', 'album_name': 'Rare Bird Alert', 'track_number': 9, 'duration_ms': 190720, 'popularity': 26, 'danceability': 0.45, 'energy': 0.327, 'loudness': -13.601, 'speechiness': 0.0346, 'acousticness': 0.865, 'instrumentalness': 0.163, 'liveness': 0.0762, 'valence': 0.409, 'tempo': 106.009}, '5VUTiGp6CYP024gcbu4uE8': {'name': 'Rare Bird Alert', 'artist_id': '1Bd4UVlqlaKEXYRG3wgrCK', 'artist_name': 'Steve Martin', 'album_name': 'Rare Bird Alert', 'track_number': 1, 'duration_ms': 159826, 'popularity': 26, 'danceability': 0.525, 'energy': 0.795, 'loudness': -5.999, 'speechiness': 0.0378, 'acousticness': 0.775, 'instrumentalness': 0.126, 'liveness': 0.112, 'valence': 0.78, 'tempo': 135.66}, '5kxWGm7jRZwV5Ld0VpBCD8': {'name': 'Jubilation Day', 'artist_id': '1Bd4UVlqlaKEXYRG3wgrCK', 'artist_name': 'Steve Martin', 'album_name': 'Rare Bird Alert', 'track_number': 6, 'duration_ms': 192240, 'popularity': 26, 'danceability': 0.63, 'energy': 0.641, 'loudness': -9.027, 'speechiness': 0.0309, 'acousticness': 0.61, 'instrumentalness': 0.00491, 'liveness': 0.343, 'valence': 0.966, 'tempo': 130.164}, '0r7EiYTNNP0WCzcaefN6TZ': {'name': 'Wrapped In Piano Strings', 'artist_id': '5EM6xJN2QNk0cL7EEm9HR9', 'artist_name': 'Radical Face', 'album_name': 'Ghost', 'track_number': 6, 'duration_ms': 216613, 'popularity': 52, 'danceability': 0.398, 'energy': 0.489, 'loudness': -8.927, 'speechiness': 0.0303, 'acousticness': 0.454, 'instrumentalness': 0.145, 'liveness': 0.132, 'valence': 0.45, 'tempo': 140.952}, '1L4GiwqpSuuLKORJWHVNxc': {'name': 'Secrets (Cellar Door)', 'artist_id': '5EM6xJN2QNk0cL7EEm9HR9', 'artist_name': 'Radical Face', 'album_name': 'The Family Tree: The Leaves', 'track_number': 1, 'duration_ms': 265693, 'popularity': 51, 'danceability': 0.553, 'energy': 0.447, 'loudness': -11.243, 'speechiness': 0.0281, 'acousticness': 0.278, 'instrumentalness': 0.128, 'liveness': 0.115, 'valence': 0.316, 'tempo': 150.04}, '0ZRyqCgW7rM17pfINuIGW3': {'name': 'Sunn', 'artist_id': '5EM6xJN2QNk0cL7EEm9HR9', 'artist_name': 'Radical Face', 'album_name': 'Sunn', 'track_number': 1, 'duration_ms': 255486, 'popularity': 48, 'danceability': 0.599, 'energy': 0.449, 'loudness': -12.019, 'speechiness': 0.0288, 'acousticness': 0.0559, 'instrumentalness': 0.567, 'liveness': 0.387, 'valence': 0.292, 'tempo': 145.066}, '1gOTLXloeEsw7cbARwnEvs': {'name': 'Always Gold', 'artist_id': '5EM6xJN2QNk0cL7EEm9HR9', 'artist_name': 'Radical Face', 'album_name': 'The Family Tree: The Roots', 'track_number': 10, 'duration_ms': 355666, 'popularity': 34, 'danceability': 0.532, 'energy': 0.247, 'loudness': -13.072, 'speechiness': 0.0603, 'acousticness': 0.311, 'instrumentalness': 0.152, 'liveness': 0.11, 'valence': 0.276, 'tempo': 162.928}, '0qCqz7oecY7QqS8lhW62XI': {'name': 'Ghost Towns', 'artist_id': '5EM6xJN2QNk0cL7EEm9HR9', 'artist_name': 'Radical Face', 'album_name': 'The Family Tree: The Roots', 'track_number': 7, 'duration_ms': 233506, 'popularity': 44, 'danceability': 0.633, 'energy': 0.522, 'loudness': -11.84, 'speechiness': 0.0283, 'acousticness': 0.473, 'instrumentalness': 0.166, 'liveness': 0.107, 'valence': 0.406, 'tempo': 145.028}, '0nNFNjGK1xF5y1j5jlw4EK': {'name': 'Welcome Home - Reprise', 'artist_id': '5EM6xJN2QNk0cL7EEm9HR9', 'artist_name': 'Radical Face', 'album_name': 'Touch The Sky', 'track_number': 6, 'duration_ms': 148964, 'popularity': 46, 'danceability': 0.32, 'energy': 0.287, 'loudness': -11.62, 'speechiness': 0.0332, 'acousticness': 0.946, 'instrumentalness': 0.951, 'liveness': 0.0906, 'valence': 0.163, 'tempo': 141.413}, '28A1RDcLuedRL5VtOzM7ee': {'name': 'Sisters', 'artist_id': '5EM6xJN2QNk0cL7EEm9HR9', 'artist_name': 'Radical Face', 'album_name': 'The Bastards', 'track_number': 1, 'duration_ms': 228720, 'popularity': 45, 'danceability': 0.434, 'energy': 0.403, 'loudness': -15.006, 'speechiness': 0.0328, 'acousticness': 0.361, 'instrumentalness': 0.0992, 'liveness': 0.0547, 'valence': 0.249, 'tempo': 165.249}, '4KMZqHXHjBajYRVNX5aAJn': {'name': 'The Mute', 'artist_id': '5EM6xJN2QNk0cL7EEm9HR9', 'artist_name': 'Radical Face', 'album_name': 'The Family Tree: The Branches', 'track_number': 3, 'duration_ms': 236266, 'popularity': 45, 'danceability': 0.699, 'energy': 0.396, 'loudness': -11.122, 'speechiness': 0.0348, 'acousticness': 0.644, 'instrumentalness': 0.0744, 'liveness': 0.111, 'valence': 0.208, 'tempo': 111.229}, '4XoDdGtXBIkDLaGT0t8RbI': {'name': 'Glory', 'artist_id': '5EM6xJN2QNk0cL7EEm9HR9', 'artist_name': 'Radical Face', 'album_name': 'Ghost', 'track_number': 4, 'duration_ms': 374080, 'popularity': 44, 'danceability': 0.499, 'energy': 0.576, 'loudness': -11.019, 'speechiness': 0.0298, 'acousticness': 0.399, 'instrumentalness': 0.756, 'liveness': 0.235, 'valence': 0.355, 'tempo': 98.016}, '5hc71nKsUgtwQ3z52KEKQk': {'name': 'Somebody Else', 'artist_id': '3mIj9lX2MWuHmhNCA7LSCW', 'artist_name': 'The 1975', 'album_name': 'I like it when you sleep, for you are so beautiful yet so unaware of it', 'track_number': 10, 'duration_ms': 347520, 'popularity': 75, 'danceability': 0.611, 'energy': 0.799, 'loudness': -5.719, 'speechiness': 0.0641, 'acousticness': 0.202, 'instrumentalness': 0.0277, 'liveness': 0.123, 'valence': 0.51, 'tempo': 101.038}, '316r1KLN0bcmpr7TZcMCXT': {'name': 'The Sound', 'artist_id': '3mIj9lX2MWuHmhNCA7LSCW', 'artist_name': 'The 1975', 'album_name': 'I like it when you sleep, for you are so beautiful yet so unaware of it', 'track_number': 13, 'duration_ms': 248880, 'popularity': 70, 'danceability': 0.643, 'energy': 0.945, 'loudness': -4.66, 'speechiness': 0.0779, 'acousticness': 0.096, 'instrumentalness': 7.71e-06, 'liveness': 0.495, 'valence': 0.526, 'tempo': 120.723}, '44Ljlpy44mHvLJxcYUvTK0': {'name': 'Chocolate', 'artist_id': '3mIj9lX2MWuHmhNCA7LSCW', 'artist_name': 'The 1975', 'album_name': 'The 1975', 'track_number': 4, 'duration_ms': 224640, 'popularity': 68, 'danceability': 0.591, 'energy': 0.944, 'loudness': -4.325, 'speechiness': 0.0544, 'acousticness': 0.0041, 'instrumentalness': 0, 'liveness': 0.385, 'valence': 0.721, 'tempo': 100.124}, '5vgdeMt4uKUN2BeltZjoDh': {'name': 'UGH!', 'artist_id': '3mIj9lX2MWuHmhNCA7LSCW', 'artist_name': 'The 1975', 'album_name': 'I like it when you sleep, for you are so beautiful yet so unaware of it', 'track_number': 3, 'duration_ms': 180026, 'popularity': 65, 'danceability': 0.769, 'energy': 0.709, 'loudness': -4.027, 'speechiness': 0.183, 'acousticness': 0.213, 'instrumentalness': 0, 'liveness': 0.0833, 'valence': 0.864, 'tempo': 100.028}, '6VKX7rGnHoHJ4bECP12OOG': {'name': 'By Your Side', 'artist_id': '3mIj9lX2MWuHmhNCA7LSCW', 'artist_name': 'The 1975', 'album_name': 'By Your Side', 'track_number': 1, 'duration_ms': 295151, 'popularity': 63, 'danceability': 0.619, 'energy': 0.312, 'loudness': -9.705, 'speechiness': 0.0638, 'acousticness': 0.804, 'instrumentalness': 0.0333, 'liveness': 0.114, 'valence': 0.141, 'tempo': 137.985}, '5hRzAbY2AAO258hL6oqsqO': {'name': 'Love Me', 'artist_id': '3mIj9lX2MWuHmhNCA7LSCW', 'artist_name': 'The 1975', 'album_name': 'I like it when you sleep, for you are so beautiful yet so unaware of it', 'track_number': 2, 'duration_ms': 222040, 'popularity': 64, 'danceability': 0.624, 'energy': 0.803, 'loudness': -3.312, 'speechiness': 0.0382, 'acousticness': 0.00925, 'instrumentalness': 3.75e-05, 'liveness': 0.613, 'valence': 0.899, 'tempo': 97.027}, '2zyz614fJRrqQXW1q0sY1c': {'name': 'Girls', 'artist_id': '3mIj9lX2MWuHmhNCA7LSCW', 'artist_name': 'The 1975', 'album_name': 'The 1975 (Deluxe Version)', 'track_number': 11, 'duration_ms': 254620, 'popularity': 63, 'danceability': 0.663, 'energy': 0.913, 'loudness': -5.014, 'speechiness': 0.0544, 'acousticness': 0.00456, 'instrumentalness': 0.00123, 'liveness': 0.481, 'valence': 0.912, 'tempo': 108.01}, '4p1pxmqtPtPHqWbOd2RgXu': {'name': 'Loving Someone', 'artist_id': '3mIj9lX2MWuHmhNCA7LSCW', 'artist_name': 'The 1975', 'album_name': 'I like it when you sleep, for you are so beautiful yet so unaware of it', 'track_number': 11, 'duration_ms': 260426, 'popularity': 63, 'danceability': 0.576, 'energy': 0.648, 'loudness': -6.897, 'speechiness': 0.0611, 'acousticness': 0.0663, 'instrumentalness': 0.000833, 'liveness': 0.131, 'valence': 0.174, 'tempo': 90.016}, '51cd3bzVmLAjlnsSZn4ecW': {'name': "She's American", 'artist_id': '3mIj9lX2MWuHmhNCA7LSCW', 'artist_name': 'The 1975', 'album_name': 'I like it when you sleep, for you are so beautiful yet so unaware of it', 'track_number': 5, 'duration_ms': 270106, 'popularity': 63, 'danceability': 0.643, 'energy': 0.868, 'loudness': -3.953, 'speechiness': 0.0578, 'acousticness': 0.175, 'instrumentalness': 0.000463, 'liveness': 0.0794, 'valence': 0.518, 'tempo': 115.978}, '2J3ajGI1sVj9wnqThJHwPS': {'name': 'If I Believe You', 'artist_id': '3mIj9lX2MWuHmhNCA7LSCW', 'artist_name': 'The 1975', 'album_name': 'I like it when you sleep, for you are so beautiful yet so unaware of it', 'track_number': 6, 'duration_ms': 380320, 'popularity': 62, 'danceability': 0.698, 'energy': 0.311, 'loudness': -7.886, 'speechiness': 0.0356, 'acousticness': 0.73, 'instrumentalness': 0.00494, 'liveness': 0.103, 'valence': 0.345, 'tempo': 129.949}, '3TjbpRjtWYHFwigdLMr8Zl': {'name': 'Come Thou Fount', 'artist_id': '6P9fFbQ875B2bnmdiYwN9A', 'artist_name': 'Kings Kaleidoscope', 'album_name': "Asaph's Arrows", 'track_number': 2, 'duration_ms': 296800, 'popularity': 54, 'danceability': 0.504, 'energy': 0.563, 'loudness': -7.354, 'speechiness': 0.0323, 'acousticness': 0.0282, 'instrumentalness': 4.4e-05, 'liveness': 0.0961, 'valence': 0.334, 'tempo': 143.876}, '1g5b5gNTAh3dsSWZILzczm': {'name': 'In Christ Alone', 'artist_id': '6P9fFbQ875B2bnmdiYwN9A', 'artist_name': 'Kings Kaleidoscope', 'album_name': "Asaph's Arrows", 'track_number': 3, 'duration_ms': 284840, 'popularity': 50, 'danceability': 0.23, 'energy': 0.69, 'loudness': -5.495, 'speechiness': 0.037, 'acousticness': 0.00129, 'instrumentalness': 0.00878, 'liveness': 0.103, 'valence': 0.149, 'tempo': 138.371}, '0X6zo3gCOaS6ccC7IT9Emf': {'name': 'Jesus Paid It All', 'artist_id': '6P9fFbQ875B2bnmdiYwN9A', 'artist_name': 'Kings Kaleidoscope', 'album_name': "Asaph's Arrows", 'track_number': 4, 'duration_ms': 224720, 'popularity': 48, 'danceability': 0.35, 'energy': 0.226, 'loudness': -12.637, 'speechiness': 0.0292, 'acousticness': 0.746, 'instrumentalness': 4.87e-06, 'liveness': 0.0826, 'valence': 0.238, 'tempo': 76.821}, '1DdYWvSA2lJbYqzpm3moC6': {'name': "How Deep the Father's Love", 'artist_id': '6P9fFbQ875B2bnmdiYwN9A', 'artist_name': 'Kings Kaleidoscope', 'album_name': 'Sin', 'track_number': 7, 'duration_ms': 301400, 'popularity': 48, 'danceability': 0.314, 'energy': 0.552, 'loudness': -9.268, 'speechiness': 0.0489, 'acousticness': 0.00364, 'instrumentalness': 0.00449, 'liveness': 0.107, 'valence': 0.209, 'tempo': 123.952}, '2Nuh1lfaz61r49sXhD4Cpr': {'name': 'A Prayer', 'artist_id': '6P9fFbQ875B2bnmdiYwN9A', 'artist_name': 'Kings Kaleidoscope', 'album_name': 'Beyond Control', 'track_number': 12, 'duration_ms': 284466, 'popularity': 47, 'danceability': 0.25, 'energy': 0.415, 'loudness': -10.837, 'speechiness': 0.054, 'acousticness': 0.442, 'instrumentalness': 0.00143, 'liveness': 0.0892, 'valence': 0.0816, 'tempo': 118.278}, '6zSofKqVraFZt5Utpv83AE': {'name': 'Dust', 'artist_id': '6P9fFbQ875B2bnmdiYwN9A', 'artist_name': 'Kings Kaleidoscope', 'album_name': 'Beyond Control', 'track_number': 4, 'duration_ms': 231666, 'popularity': 45, 'danceability': 0.279, 'energy': 0.699, 'loudness': -7.205, 'speechiness': 0.0552, 'acousticness': 0.0406, 'instrumentalness': 0.000206, 'liveness': 0.666, 'valence': 0.396, 'tempo': 89.777}, '3JhCq2r9PbbWYdQ1qpoKEX': {'name': 'Grace Alone', 'artist_id': '6P9fFbQ875B2bnmdiYwN9A', 'artist_name': 'Kings Kaleidoscope', 'album_name': 'Becoming Who We Are', 'track_number': 8, 'duration_ms': 218973, 'popularity': 44, 'danceability': 0.376, 'energy': 0.366, 'loudness': -11.698, 'speechiness': 0.0385, 'acousticness': 0.479, 'instrumentalness': 0, 'liveness': 0.119, 'valence': 0.188, 'tempo': 139.534}, '3T1CKrdMfrXJC5VXC19LUm': {'name': 'Lost?', 'artist_id': '6P9fFbQ875B2bnmdiYwN9A', 'artist_name': 'Kings Kaleidoscope', 'album_name': 'Beyond Control', 'track_number': 9, 'duration_ms': 231400, 'popularity': 44, 'danceability': 0.203, 'energy': 0.229, 'loudness': -12.433, 'speechiness': 0.0325, 'acousticness': 0.633, 'instrumentalness': 0, 'liveness': 0.112, 'valence': 0.33, 'tempo': 76.146}, '4F1mJebZX8v8Oi1Zl0CRdl': {'name': 'Fix My Eyes (Live)', 'artist_id': '6P9fFbQ875B2bnmdiYwN9A', 'artist_name': 'Kings Kaleidoscope', 'album_name': 'Live in Color', 'track_number': 1, 'duration_ms': 192461, 'popularity': 44, 'danceability': 0.347, 'energy': 0.2, 'loudness': -14.11, 'speechiness': 0.0377, 'acousticness': 0.952, 'instrumentalness': 0.00058, 'liveness': 0.348, 'valence': 0.197, 'tempo': 123.982}, '3XBrhebJSAGEhrV5NNg9ia': {'name': 'Most of It', 'artist_id': '6P9fFbQ875B2bnmdiYwN9A', 'artist_name': 'Kings Kaleidoscope', 'album_name': 'Beyond Control', 'track_number': 3, 'duration_ms': 214773, 'popularity': 43, 'danceability': 0.727, 'energy': 0.514, 'loudness': -9.488, 'speechiness': 0.0503, 'acousticness': 0.222, 'instrumentalness': 4.83e-06, 'liveness': 0.0866, 'valence': 0.658, 'tempo': 108.96}, '2lFtnEmkIPm2ClN55e2chV': {'name': 'Black', 'artist_id': '7x8nK0m0cP2ksQf0mjWdPS', 'artist_name': 'Dierks Bentley', 'album_name': 'Black', 'track_number': 1, 'duration_ms': 211160, 'popularity': 77, 'danceability': 0.663, 'energy': 0.656, 'loudness': -6.548, 'speechiness': 0.0413, 'acousticness': 0.27, 'instrumentalness': 0.000279, 'liveness': 0.117, 'valence': 0.555, 'tempo': 120.037}, '5HJId22hZ2IvFnvNSy6ZbE': {'name': 'Different For Girls', 'artist_id': '7x8nK0m0cP2ksQf0mjWdPS', 'artist_name': 'Dierks Bentley', 'album_name': 'Black', 'track_number': 10, 'duration_ms': 180360, 'popularity': 74, 'danceability': 0.661, 'energy': 0.785, 'loudness': -5.623, 'speechiness': 0.0369, 'acousticness': 0.445, 'instrumentalness': 0.000266, 'liveness': 0.0854, 'valence': 0.365, 'tempo': 91.975}, '5CG9Ps5ynNjpKJHmwc95pa': {'name': 'Somewhere On A Beach', 'artist_id': '7x8nK0m0cP2ksQf0mjWdPS', 'artist_name': 'Dierks Bentley', 'album_name': 'Black', 'track_number': 5, 'duration_ms': 197120, 'popularity': 72, 'danceability': 0.573, 'energy': 0.635, 'loudness': -6.621, 'speechiness': 0.0275, 'acousticness': 0.000598, 'instrumentalness': 0, 'liveness': 0.0845, 'valence': 0.451, 'tempo': 144.031}, '1soxUgYIZb1qx1c7o1Lc7z': {'name': 'Drunk On A Plane', 'artist_id': '7x8nK0m0cP2ksQf0mjWdPS', 'artist_name': 'Dierks Bentley', 'album_name': 'RISER', 'track_number': 6, 'duration_ms': 254466, 'popularity': 71, 'danceability': 0.439, 'energy': 0.754, 'loudness': -5.566, 'speechiness': 0.0323, 'acousticness': 0.00512, 'instrumentalness': 7.45e-06, 'liveness': 0.186, 'valence': 0.666, 'tempo': 205.958}, '0HccAcPMNevr8ERJCWlFk3': {'name': 'Riser', 'artist_id': '7x8nK0m0cP2ksQf0mjWdPS', 'artist_name': 'Dierks Bentley', 'album_name': 'RISER', 'track_number': 8, 'duration_ms': 250000, 'popularity': 68, 'danceability': 0.516, 'energy': 0.658, 'loudness': -7.906, 'speechiness': 0.0345, 'acousticness': 0.128, 'instrumentalness': 0.00787, 'liveness': 0.0898, 'valence': 0.257, 'tempo': 164.104}, '2WKCH4ISejDV9ad7iPp5XU': {'name': '5-1-5-0', 'artist_id': '7x8nK0m0cP2ksQf0mjWdPS', 'artist_name': 'Dierks Bentley', 'album_name': 'Home', 'track_number': 10, 'duration_ms': 182893, 'popularity': 63, 'danceability': 0.554, 'energy': 0.849, 'loudness': -5.181, 'speechiness': 0.0357, 'acousticness': 0.0246, 'instrumentalness': 0.000233, 'liveness': 0.31, 'valence': 0.69, 'tempo': 116.992}, '0r8iDf65NHgFgZOGLwj5r8': {'name': "What Was I Thinkin'", 'artist_id': '7x8nK0m0cP2ksQf0mjWdPS', 'artist_name': 'Dierks Bentley', 'album_name': 'Dierks Bentley', 'track_number': 1, 'duration_ms': 260826, 'popularity': 63, 'danceability': 0.551, 'energy': 0.825, 'loudness': -6.24, 'speechiness': 0.044, 'acousticness': 0.152, 'instrumentalness': 6.2e-06, 'liveness': 0.0999, 'valence': 0.933, 'tempo': 164.857}, '4QJ58lQahpEtD7622moUxS': {'name': 'Pick Up', 'artist_id': '7x8nK0m0cP2ksQf0mjWdPS', 'artist_name': 'Dierks Bentley', 'album_name': 'Black', 'track_number': 2, 'duration_ms': 213386, 'popularity': 61, 'danceability': 0.587, 'energy': 0.797, 'loudness': -5.671, 'speechiness': 0.0429, 'acousticness': 0.0111, 'instrumentalness': 7.82e-05, 'liveness': 0.0851, 'valence': 0.463, 'tempo': 147.905}, '01e8dGbulrphX8j3fZDQYk': {'name': 'I Hold On', 'artist_id': '7x8nK0m0cP2ksQf0mjWdPS', 'artist_name': 'Dierks Bentley', 'album_name': 'RISER', 'track_number': 3, 'duration_ms': 279533, 'popularity': 57, 'danceability': 0.615, 'energy': 0.723, 'loudness': -6.506, 'speechiness': 0.0448, 'acousticness': 0.0917, 'instrumentalness': 0.000423, 'liveness': 0.101, 'valence': 0.214, 'tempo': 117.958}, '355DF4qq7l3Lc6EnPF0b5j': {'name': 'Bar at the End of the World', 'artist_id': '3grHWM9bx2E9vwJCdlRv9O', 'artist_name': 'Kenny Chesney', 'album_name': 'Cosmic Hallelujah', 'track_number': 6, 'duration_ms': 208813, 'popularity': 74, 'danceability': 0.345, 'energy': 0.798, 'loudness': -3.724, 'speechiness': 0.0404, 'acousticness': 0.00566, 'instrumentalness': 0, 'liveness': 0.0922, 'valence': 0.684, 'tempo': 200.061}, '3mtGoEJPXSFO2Lz5pw45ya': {'name': 'Setting the World On Fire', 'artist_id': '3grHWM9bx2E9vwJCdlRv9O', 'artist_name': 'Kenny Chesney', 'album_name': 'Cosmic Hallelujah', 'track_number': 3, 'duration_ms': 218733, 'popularity': 70, 'danceability': 0.609, 'energy': 0.819, 'loudness': -4.465, 'speechiness': 0.0363, 'acousticness': 0.0137, 'instrumentalness': 3.78e-06, 'liveness': 0.0911, 'valence': 0.403, 'tempo': 94.001}, '1dgWTMoHwTUnQhOQ8SR5fV': {'name': 'American Kids', 'artist_id': '3grHWM9bx2E9vwJCdlRv9O', 'artist_name': 'Kenny Chesney', 'album_name': 'The Big Revival', 'track_number': 4, 'duration_ms': 182960, 'popularity': 68, 'danceability': 0.733, 'energy': 0.589, 'loudness': -7.37, 'speechiness': 0.1, 'acousticness': 0.0476, 'instrumentalness': 5.85e-06, 'liveness': 0.0366, 'valence': 0.886, 'tempo': 170.097}, '3pkzJjJXfdDjhpXx639MIH': {'name': 'Somewhere With You', 'artist_id': '3grHWM9bx2E9vwJCdlRv9O', 'artist_name': 'Kenny Chesney', 'album_name': "Hemingway's Whiskey", 'track_number': 10, 'duration_ms': 243520, 'popularity': 66, 'danceability': 0.68, 'energy': 0.849, 'loudness': -6.475, 'speechiness': 0.0376, 'acousticness': 0.0862, 'instrumentalness': 0.00013, 'liveness': 0.174, 'valence': 0.549, 'tempo': 111.969}, '6BCrbWBpb8d6KWmEqZ41tr': {'name': 'Come Over', 'artist_id': '3grHWM9bx2E9vwJCdlRv9O', 'artist_name': 'Kenny Chesney', 'album_name': 'Welcome To The Fishbowl', 'track_number': 1, 'duration_ms': 248426, 'popularity': 65, 'danceability': 0.466, 'energy': 0.704, 'loudness': -7.169, 'speechiness': 0.0353, 'acousticness': 0.1, 'instrumentalness': 2.71e-05, 'liveness': 0.0744, 'valence': 0.484, 'tempo': 176.043}, '1t2hJFgJyUPD2crOafMUEk': {'name': 'You and Tequila', 'artist_id': '3grHWM9bx2E9vwJCdlRv9O', 'artist_name': 'Kenny Chesney', 'album_name': "Hemingway's Whiskey", 'track_number': 4, 'duration_ms': 242840, 'popularity': 64, 'danceability': 0.691, 'energy': 0.454, 'loudness': -9.13, 'speechiness': 0.0256, 'acousticness': 0.437, 'instrumentalness': 0.00227, 'liveness': 0.0783, 'valence': 0.342, 'tempo': 135.839}, '6wfTb2he5ANMQSFnlamnyi': {'name': 'Save It for a Rainy Day', 'artist_id': '3grHWM9bx2E9vwJCdlRv9O', 'artist_name': 'Kenny Chesney', 'album_name': 'The Big Revival', 'track_number': 9, 'duration_ms': 182213, 'popularity': 63, 'danceability': 0.538, 'energy': 0.775, 'loudness': -5.48, 'speechiness': 0.0291, 'acousticness': 0.0053, 'instrumentalness': 0, 'liveness': 0.0807, 'valence': 0.607, 'tempo': 154.889}, '5cj52tdE99xnvdZGKWmKIW': {'name': 'Noise', 'artist_id': '3grHWM9bx2E9vwJCdlRv9O', 'artist_name': 'Kenny Chesney', 'album_name': 'Cosmic Hallelujah', 'track_number': 4, 'duration_ms': 205533, 'popularity': 62, 'danceability': 0.579, 'energy': 0.799, 'loudness': -4.146, 'speechiness': 0.028, 'acousticness': 0.0095, 'instrumentalness': 0, 'liveness': 0.0789, 'valence': 0.57, 'tempo': 109.964}, '1Lh8n5owE0h0hgqWfqtvuD': {'name': "Til It's Gone", 'artist_id': '3grHWM9bx2E9vwJCdlRv9O', 'artist_name': 'Kenny Chesney', 'album_name': 'The Big Revival', 'track_number': 3, 'duration_ms': 250533, 'popularity': 60, 'danceability': 0.499, 'energy': 0.822, 'loudness': -7.122, 'speechiness': 0.049, 'acousticness': 0.00544, 'instrumentalness': 0.000197, 'liveness': 0.272, 'valence': 0.492, 'tempo': 86.481}, '3cE5ltZFHmBpiS77itKaOM': {'name': 'Summertime', 'artist_id': '3grHWM9bx2E9vwJCdlRv9O', 'artist_name': 'Kenny Chesney', 'album_name': 'The Road And The Radio', 'track_number': 5, 'duration_ms': 206586, 'popularity': 44, 'danceability': 0.48, 'energy': 0.928, 'loudness': -5.501, 'speechiness': 0.0899, 'acousticness': 0.169, 'instrumentalness': 0, 'liveness': 0.0479, 'valence': 0.725, 'tempo': 167.986}, '7FqrsV0vBwNiQNQI6jfzni': {'name': 'Old Number Seven', 'artist_id': '63knPlGzLHTNDf1J78Fvte', 'artist_name': 'The Devil Makes Three', 'album_name': 'The Devil Makes Three', 'track_number': 6, 'duration_ms': 200720, 'popularity': 58, 'danceability': 0.571, 'energy': 0.427, 'loudness': -7.574, 'speechiness': 0.0405, 'acousticness': 0.202, 'instrumentalness': 0, 'liveness': 0.1, 'valence': 0.892, 'tempo': 142.454}, '5fuON606j1hkPGJhFMwerY': {'name': 'Graveyard', 'artist_id': '63knPlGzLHTNDf1J78Fvte', 'artist_name': 'The Devil Makes Three', 'album_name': 'The Devil Makes Three', 'track_number': 2, 'duration_ms': 205053, 'popularity': 51, 'danceability': 0.69, 'energy': 0.494, 'loudness': -9.147, 'speechiness': 0.0275, 'acousticness': 0.407, 'instrumentalness': 3.79e-06, 'liveness': 0.114, 'valence': 0.836, 'tempo': 127.314}, '5oNyskwKyRceUQaYzmWobx': {'name': 'All Hail', 'artist_id': '63knPlGzLHTNDf1J78Fvte', 'artist_name': 'The Devil Makes Three', 'album_name': 'Do Wrong Right', 'track_number': 1, 'duration_ms': 241053, 'popularity': 50, 'danceability': 0.672, 'energy': 0.575, 'loudness': -8.514, 'speechiness': 0.0383, 'acousticness': 0.72, 'instrumentalness': 0, 'liveness': 0.0782, 'valence': 0.899, 'tempo': 117.805}, '191qPeOpllZfaApp35HXK3': {'name': 'The Plank', 'artist_id': '63knPlGzLHTNDf1J78Fvte', 'artist_name': 'The Devil Makes Three', 'album_name': 'The Devil Makes Three', 'track_number': 1, 'duration_ms': 146093, 'popularity': 49, 'danceability': 0.555, 'energy': 0.533, 'loudness': -9.162, 'speechiness': 0.0409, 'acousticness': 0.517, 'instrumentalness': 0, 'liveness': 0.116, 'valence': 0.808, 'tempo': 173.906}, '3ALem2cU9XKuWT4CLAeDMK': {'name': 'Ten Feet Tall', 'artist_id': '63knPlGzLHTNDf1J78Fvte', 'artist_name': 'The Devil Makes Three', 'album_name': 'The Devil Makes Three', 'track_number': 4, 'duration_ms': 166800, 'popularity': 48, 'danceability': 0.545, 'energy': 0.497, 'loudness': -10.768, 'speechiness': 0.036, 'acousticness': 0.329, 'instrumentalness': 0.00369, 'liveness': 0.186, 'valence': 0.828, 'tempo': 154.235}, '33GZ5QfNMeVVOmZABeb6Px': {'name': 'Do Wrong Right', 'artist_id': '63knPlGzLHTNDf1J78Fvte', 'artist_name': 'The Devil Makes Three', 'album_name': 'Do Wrong Right', 'track_number': 2, 'duration_ms': 261706, 'popularity': 45, 'danceability': 0.634, 'energy': 0.644, 'loudness': -7.213, 'speechiness': 0.0336, 'acousticness': 0.653, 'instrumentalness': 0, 'liveness': 0.122, 'valence': 0.87, 'tempo': 121.041}, '5pnjFG0695iwvR9qsnfTSk': {'name': 'The Bullet', 'artist_id': '63knPlGzLHTNDf1J78Fvte', 'artist_name': 'The Devil Makes Three', 'album_name': 'The Devil Makes Three', 'track_number': 9, 'duration_ms': 171280, 'popularity': 45, 'danceability': 0.552, 'energy': 0.633, 'loudness': -7.352, 'speechiness': 0.034, 'acousticness': 0.135, 'instrumentalness': 0, 'liveness': 0.302, 'valence': 0.772, 'tempo': 99.566}, '7jS3s8sv5ytlo7xgBGyCiL': {'name': 'Stranger', 'artist_id': '63knPlGzLHTNDf1J78Fvte', 'artist_name': 'The Devil Makes Three', 'album_name': "I'm a Stranger Here", 'track_number': 1, 'duration_ms': 208466, 'popularity': 28, 'danceability': 0.683, 'energy': 0.617, 'loudness': -9.239, 'speechiness': 0.0397, 'acousticness': 0.884, 'instrumentalness': 0.0328, 'liveness': 0.149, 'valence': 0.937, 'tempo': 112.119}, '0eAcBwrfgCjdTilx8oNQ8v': {'name': 'Champagne And Reefer', 'artist_id': '63knPlGzLHTNDf1J78Fvte', 'artist_name': 'The Devil Makes Three', 'album_name': 'Redemption & Ruin', 'track_number': 2, 'duration_ms': 174248, 'popularity': 42, 'danceability': 0.735, 'energy': 0.836, 'loudness': -7.467, 'speechiness': 0.0451, 'acousticness': 0.353, 'instrumentalness': 0.0143, 'liveness': 0.342, 'valence': 0.78, 'tempo': 121.251}, '5dZFvwgWR7Rww53oQAZlbS': {'name': 'Waiting Around To Die', 'artist_id': '63knPlGzLHTNDf1J78Fvte', 'artist_name': 'The Devil Makes Three', 'album_name': 'Redemption & Ruin', 'track_number': 6, 'duration_ms': 214543, 'popularity': 42, 'danceability': 0.4, 'energy': 0.16, 'loudness': -15.425, 'speechiness': 0.045, 'acousticness': 0.476, 'instrumentalness': 1.42e-05, 'liveness': 0.105, 'valence': 0.101, 'tempo': 143.939}, '498ZVInMGDkmmNVpSWqHiZ': {'name': 'May We All', 'artist_id': '3b8QkneNDz4JHKKKlLgYZg', 'artist_name': 'Florida Georgia Line', 'album_name': 'Dig Your Roots', 'track_number': 6, 'duration_ms': 226173, 'popularity': 79, 'danceability': 0.488, 'energy': 0.915, 'loudness': -4.255, 'speechiness': 0.0389, 'acousticness': 0.0406, 'instrumentalness': 0, 'liveness': 0.351, 'valence': 0.637, 'tempo': 75.019}, '0BCy325UZyR9z0t0uxwn2N': {'name': 'H.O.L.Y.', 'artist_id': '3b8QkneNDz4JHKKKlLgYZg', 'artist_name': 'Florida Georgia Line', 'album_name': 'Dig Your Roots', 'track_number': 4, 'duration_ms': 194186, 'popularity': 78, 'danceability': 0.525, 'energy': 0.685, 'loudness': -3.954, 'speechiness': 0.0351, 'acousticness': 0.385, 'instrumentalness': 0, 'liveness': 0.0731, 'valence': 0.522, 'tempo': 78.003}, '4VFE6ZNqa8jHAmbYICoAFg': {'name': 'God, Your Mama, And Me', 'artist_id': '3b8QkneNDz4JHKKKlLgYZg', 'artist_name': 'Florida Georgia Line', 'album_name': 'Dig Your Roots', 'track_number': 11, 'duration_ms': 183413, 'popularity': 78, 'danceability': 0.439, 'energy': 0.802, 'loudness': -3.644, 'speechiness': 0.054, 'acousticness': 0.333, 'instrumentalness': 0, 'liveness': 0.377, 'valence': 0.688, 'tempo': 168.032}, '2TR7A4ulH9R1PNwMyd8o8U': {'name': 'This Is How We Roll', 'artist_id': '3b8QkneNDz4JHKKKlLgYZg', 'artist_name': 'Florida Georgia Line', 'album_name': "Here's To The Good Times...This Is How We Roll", 'track_number': 12, 'duration_ms': 220906, 'popularity': 73, 'danceability': 0.56, 'energy': 0.933, 'loudness': -2.969, 'speechiness': 0.0384, 'acousticness': 0.0208, 'instrumentalness': 0, 'liveness': 0.404, 'valence': 0.709, 'tempo': 132.083}, '46ZfPS5VpSQVU5gb82hg3K': {'name': 'Anything Goes', 'artist_id': '3b8QkneNDz4JHKKKlLgYZg', 'artist_name': 'Florida Georgia Line', 'album_name': 'Anything Goes', 'track_number': 1, 'duration_ms': 218866, 'popularity': 72, 'danceability': 0.462, 'energy': 0.977, 'loudness': -3.805, 'speechiness': 0.045, 'acousticness': 0.00172, 'instrumentalness': 0, 'liveness': 0.352, 'valence': 0.757, 'tempo': 154.038}, '6IFPfV8PNSYOmufzQ95hmm': {'name': 'Confession', 'artist_id': '3b8QkneNDz4JHKKKlLgYZg', 'artist_name': 'Florida Georgia Line', 'album_name': 'Anything Goes', 'track_number': 10, 'duration_ms': 190640, 'popularity': 71, 'danceability': 0.556, 'energy': 0.873, 'loudness': -5.056, 'speechiness': 0.0348, 'acousticness': 0.101, 'instrumentalness': 0.000131, 'liveness': 0.176, 'valence': 0.457, 'tempo': 104.986}, '0i5el041vd6nxrGEU8QRxy': {'name': 'Cruise', 'artist_id': '3b8QkneNDz4JHKKKlLgYZg', 'artist_name': 'Florida Georgia Line', 'album_name': "Here's To The Good Times", 'track_number': 1, 'duration_ms': 208960, 'popularity': 70, 'danceability': 0.464, 'energy': 0.945, 'loudness': -3.342, 'speechiness': 0.0354, 'acousticness': 0.0189, 'instrumentalness': 0, 'liveness': 0.0575, 'valence': 0.869, 'tempo': 148.012}, '5T6DM9qjjngWnukcw0svkX': {'name': 'Round Here', 'artist_id': '3b8QkneNDz4JHKKKlLgYZg', 'artist_name': 'Florida Georgia Line', 'album_name': "Here's To The Good Times", 'track_number': 2, 'duration_ms': 215120, 'popularity': 69, 'danceability': 0.523, 'energy': 0.956, 'loudness': -3.053, 'speechiness': 0.0379, 'acousticness': 0.00407, 'instrumentalness': 0, 'liveness': 0.216, 'valence': 0.887, 'tempo': 141.977}, '6s9ICeczYOfbHHIaSMq9jd': {'name': 'Get Your Shine On', 'artist_id': '3b8QkneNDz4JHKKKlLgYZg', 'artist_name': 'Florida Georgia Line', 'album_name': "Here's To The Good Times", 'track_number': 3, 'duration_ms': 222013, 'popularity': 69, 'danceability': 0.508, 'energy': 0.93, 'loudness': -4.518, 'speechiness': 0.0372, 'acousticness': 0.00265, 'instrumentalness': 2.64e-06, 'liveness': 0.406, 'valence': 0.621, 'tempo': 96.993}, '5CXnIPD6rTjszYYQm6fY2P': {'name': 'Dirt', 'artist_id': '3b8QkneNDz4JHKKKlLgYZg', 'artist_name': 'Florida Georgia Line', 'album_name': 'Anything Goes', 'track_number': 4, 'duration_ms': 230586, 'popularity': 68, 'danceability': 0.554, 'energy': 0.875, 'loudness': -4.185, 'speechiness': 0.0487, 'acousticness': 0.0661, 'instrumentalness': 1.59e-05, 'liveness': 0.118, 'valence': 0.534, 'tempo': 121.976}, '3pLTOP0G0etiWUknFoRpsr': {'name': 'The Cave', 'artist_id': '3gd8FJtBJtkRxdfbTu19U2', 'artist_name': 'Mumford & Sons', 'album_name': 'Sigh No More', 'track_number': 2, 'duration_ms': 217986, 'popularity': 70, 'danceability': 0.576, 'energy': 0.486, 'loudness': -9.364, 'speechiness': 0.0406, 'acousticness': 0.0606, 'instrumentalness': 0.000143, 'liveness': 0.093, 'valence': 0.348, 'tempo': 141.951}, '2JHBMVs8E7bJJBLkXpKgHn': {'name': 'I Will Wait', 'artist_id': '3gd8FJtBJtkRxdfbTu19U2', 'artist_name': 'Mumford & Sons', 'album_name': 'Babel', 'track_number': 3, 'duration_ms': 276720, 'popularity': 69, 'danceability': 0.488, 'energy': 0.752, 'loudness': -5.131, 'speechiness': 0.0323, 'acousticness': 0.0165, 'instrumentalness': 0.00541, 'liveness': 0.301, 'valence': 0.432, 'tempo': 131.221}, '2BBkIgdXLv5vyp1DR0wpQl': {'name': 'Little Lion Man', 'artist_id': '3gd8FJtBJtkRxdfbTu19U2', 'artist_name': 'Mumford & Sons', 'album_name': 'Sigh No More', 'track_number': 7, 'duration_ms': 246973, 'popularity': 68, 'danceability': 0.519, 'energy': 0.512, 'loudness': -7.986, 'speechiness': 0.0282, 'acousticness': 0.0276, 'instrumentalness': 8.78e-05, 'liveness': 0.0976, 'valence': 0.438, 'tempo': 138.596}, '4A57CXs3jAmyNTMAwWaV53': {'name': 'Believe', 'artist_id': '3gd8FJtBJtkRxdfbTu19U2', 'artist_name': 'Mumford & Sons', 'album_name': 'Wilder Mind', 'track_number': 2, 'duration_ms': 220866, 'popularity': 66, 'danceability': 0.362, 'energy': 0.668, 'loudness': -5.975, 'speechiness': 0.0431, 'acousticness': 0.035, 'instrumentalness': 0.0212, 'liveness': 0.219, 'valence': 0.348, 'tempo': 113.996}, '5DVKKqwLGjvK9ojz3zLjB7': {'name': 'There Will Be Time', 'artist_id': '3gd8FJtBJtkRxdfbTu19U2', 'artist_name': 'Mumford & Sons', 'album_name': 'There Will Be Time', 'track_number': 1, 'duration_ms': 267946, 'popularity': 65, 'danceability': 0.513, 'energy': 0.709, 'loudness': -8.347, 'speechiness': 0.0523, 'acousticness': 0.0133, 'instrumentalness': 0, 'liveness': 0.0881, 'valence': 0.196, 'tempo': 74.983}, '3e6s8Z4MRSNgvNhVvpuUiw': {'name': 'Ditmas', 'artist_id': '3gd8FJtBJtkRxdfbTu19U2', 'artist_name': 'Mumford & Sons', 'album_name': 'Wilder Mind', 'track_number': 10, 'duration_ms': 218626, 'popularity': 61, 'danceability': 0.526, 'energy': 0.786, 'loudness': -5.77, 'speechiness': 0.043, 'acousticness': 0.00457, 'instrumentalness': 0.00256, 'liveness': 0.0862, 'valence': 0.591, 'tempo': 144.12}, '4PgJ0NUYaDDh659TW5mWBK': {'name': 'The Wolf', 'artist_id': '3gd8FJtBJtkRxdfbTu19U2', 'artist_name': 'Mumford & Sons', 'album_name': 'Wilder Mind', 'track_number': 3, 'duration_ms': 221240, 'popularity': 60, 'danceability': 0.422, 'energy': 0.827, 'loudness': -5.31, 'speechiness': 0.0445, 'acousticness': 0.000507, 'instrumentalness': 0.765, 'liveness': 0.198, 'valence': 0.322, 'tempo': 152.956}, '5VwKEmrYEN5eAPvWqrrKS2': {'name': 'Awake My Soul', 'artist_id': '3gd8FJtBJtkRxdfbTu19U2', 'artist_name': 'Mumford & Sons', 'album_name': 'Sigh No More', 'track_number': 10, 'duration_ms': 255826, 'popularity': 60, 'danceability': 0.262, 'energy': 0.466, 'loudness': -9.785, 'speechiness': 0.0341, 'acousticness': 0.0621, 'instrumentalness': 0.0273, 'liveness': 0.0913, 'valence': 0.248, 'tempo': 85.522}, '2QulT0LDnhH7011gzjFvLS': {'name': 'White Blank Page', 'artist_id': '3gd8FJtBJtkRxdfbTu19U2', 'artist_name': 'Mumford & Sons', 'album_name': 'Sigh No More', 'track_number': 5, 'duration_ms': 254160, 'popularity': 60, 'danceability': 0.334, 'energy': 0.402, 'loudness': -9.552, 'speechiness': 0.0355, 'acousticness': 0.234, 'instrumentalness': 1.88e-05, 'liveness': 0.576, 'valence': 0.307, 'tempo': 123.733}, '4aHzQbalMnDm04AAW5K4se': {'name': 'Timshel', 'artist_id': '3gd8FJtBJtkRxdfbTu19U2', 'artist_name': 'Mumford & Sons', 'album_name': 'Sigh No More', 'track_number': 8, 'duration_ms': 173400, 'popularity': 59, 'danceability': 0.463, 'energy': 0.279, 'loudness': -9.5, 'speechiness': 0.0344, 'acousticness': 0.863, 'instrumentalness': 6.94e-06, 'liveness': 0.114, 'valence': 0.0875, 'tempo': 82.509}, '05KfyCEE6otdlT1pp2VIjP': {'name': 'Believer', 'artist_id': '53XhwfbYqKCa1cC15pYq2q', 'artist_name': 'Imagine Dragons', 'album_name': 'Believer', 'track_number': 1, 'duration_ms': 203782, 'popularity': 88, 'danceability': 0.772, 'energy': 0.775, 'loudness': -4.388, 'speechiness': 0.112, 'acousticness': 0.0417, 'instrumentalness': 0, 'liveness': 0.226, 'valence': 0.742, 'tempo': 124.978}, '4dASQiO1Eoo3RJvt74FtXB': {'name': 'Sucker For Pain (with Wiz Khalifa, Imagine Dragons, Logic & Ty Dolla $ign feat. X Ambassadors)', 'artist_id': '55Aa2cqylxrFIXC767Z865', 'artist_name': 'Lil Wayne', 'album_name': 'Sucker For Pain (with Logic & Ty Dolla $ign feat. X Ambassadors)', 'track_number': 1, 'duration_ms': 243490, 'popularity': 84, 'danceability': 0.502, 'energy': 0.786, 'loudness': -4.378, 'speechiness': 0.317, 'acousticness': 0.255, 'instrumentalness': 0, 'liveness': 0.65, 'valence': 0.734, 'tempo': 169.021}, '4G8gkOterJn0Ywt6uhqbhp': {'name': 'Radioactive', 'artist_id': '53XhwfbYqKCa1cC15pYq2q', 'artist_name': 'Imagine Dragons', 'album_name': 'Night Visions', 'track_number': 1, 'duration_ms': 186813, 'popularity': 75, 'danceability': 0.478, 'energy': 0.799, 'loudness': -3.614, 'speechiness': 0.0638, 'acousticness': 0.126, 'instrumentalness': 0.000106, 'liveness': 0.76, 'valence': 0.201, 'tempo': 136.268}, '3LlAyCYU26dvFZBDUIMb7a': {'name': 'Demons', 'artist_id': '53XhwfbYqKCa1cC15pYq2q', 'artist_name': 'Imagine Dragons', 'album_name': 'Night Visions', 'track_number': 4, 'duration_ms': 175200, 'popularity': 75, 'danceability': 0.499, 'energy': 0.73, 'loudness': -2.831, 'speechiness': 0.0367, 'acousticness': 0.23, 'instrumentalness': 0.00018, 'liveness': 0.378, 'valence': 0.339, 'tempo': 90.058}, '4XLm8FNvaTlmTAZmSrrV82': {'name': 'Shots - Broiler Remix', 'artist_id': '53XhwfbYqKCa1cC15pYq2q', 'artist_name': 'Imagine Dragons', 'album_name': 'Shots EP', 'track_number': 1, 'duration_ms': 191266, 'popularity': 68, 'danceability': 0.738, 'energy': 0.768, 'loudness': -7.045, 'speechiness': 0.0348, 'acousticness': 0.381, 'instrumentalness': 0.145, 'liveness': 0.1, 'valence': 0.597, 'tempo': 120.013}, '6KuHjfXHkfnIjdmcIvt9r0': {'name': 'On Top Of The World', 'artist_id': '53XhwfbYqKCa1cC15pYq2q', 'artist_name': 'Imagine Dragons', 'album_name': 'Night Visions (Deluxe)', 'track_number': 5, 'duration_ms': 189840, 'popularity': 67, 'danceability': 0.64, 'energy': 0.924, 'loudness': -5.577, 'speechiness': 0.185, 'acousticness': 0.0894, 'instrumentalness': 3.92e-06, 'liveness': 0.0971, 'valence': 0.773, 'tempo': 99.959}, '1lgN0A2Vki2FTON5PYq42m': {'name': 'Warriors', 'artist_id': '53XhwfbYqKCa1cC15pYq2q', 'artist_name': 'Imagine Dragons', 'album_name': 'Smoke + Mirrors (Deluxe)', 'track_number': 18, 'duration_ms': 170066, 'popularity': 70, 'danceability': 0.361, 'energy': 0.855, 'loudness': -6.145, 'speechiness': 0.0708, 'acousticness': 0.072, 'instrumentalness': 0.00163, 'liveness': 0.243, 'valence': 0.322, 'tempo': 77.998}, '6BtmXhTJMM9sBTHeYYASGz': {'name': "It's Time", 'artist_id': '53XhwfbYqKCa1cC15pYq2q', 'artist_name': 'Imagine Dragons', 'album_name': 'Night Visions', 'track_number': 3, 'duration_ms': 237986, 'popularity': 66, 'danceability': 0.656, 'energy': 0.879, 'loudness': -4.614, 'speechiness': 0.0362, 'acousticness': 0.0178, 'instrumentalness': 0, 'liveness': 0.109, 'valence': 0.902, 'tempo': 104.997}, '4kDTvLhGF29gFsqceuxBSC': {'name': 'Not Today', 'artist_id': '53XhwfbYqKCa1cC15pYq2q', 'artist_name': 'Imagine Dragons', 'album_name': 'Me Before You (Original Motion Picture Soundtrack)', 'track_number': 9, 'duration_ms': 261079, 'popularity': 65, 'danceability': 0.463, 'energy': 0.386, 'loudness': -7.261, 'speechiness': 0.0286, 'acousticness': 0.565, 'instrumentalness': 0, 'liveness': 0.176, 'valence': 0.0538, 'tempo': 123.495}, '3Dbgo1HE3DErIBNDIO4Hyd': {'name': 'Blank Space/Stand By Me - Live From Spotify London', 'artist_id': '53XhwfbYqKCa1cC15pYq2q', 'artist_name': 'Imagine Dragons', 'album_name': 'Imagine Dragons (Spotify Sessions)', 'track_number': 2, 'duration_ms': 303433, 'popularity': 63, 'danceability': 0.764, 'energy': 0.575, 'loudness': -6.728, 'speechiness': 0.0966, 'acousticness': 0.407, 'instrumentalness': 0, 'liveness': 0.747, 'valence': 0.505, 'tempo': 101.759}, '0yqWOXyvDtC2ol1Idz8r8J': {'name': 'Build Your Kingdom Here', 'artist_id': '11Y54BxlxC3UIAUkU2eadQ', 'artist_name': 'Rend Collective', 'album_name': 'Homemade Worship by Handmade People', 'track_number': 6, 'duration_ms': 257959, 'popularity': 59, 'danceability': 0.456, 'energy': 0.508, 'loudness': -14.339, 'speechiness': 0.0402, 'acousticness': 0.0218, 'instrumentalness': 0, 'liveness': 0.237, 'valence': 0.56, 'tempo': 133.965}, '5AcdaSVQfLcUKMaqchfBie': {'name': 'My Lighthouse', 'artist_id': '11Y54BxlxC3UIAUkU2eadQ', 'artist_name': 'Rend Collective', 'album_name': 'The Art Of Celebration', 'track_number': 3, 'duration_ms': 224169, 'popularity': 58, 'danceability': 0.545, 'energy': 0.805, 'loudness': -5.792, 'speechiness': 0.0491, 'acousticness': 0.0326, 'instrumentalness': 0, 'liveness': 0.781, 'valence': 0.713, 'tempo': 110.008}, '18q8W11QNDEfhYIxwypTQK': {'name': 'Oceans (Where Feet May FaiI)', 'artist_id': '11Y54BxlxC3UIAUkU2eadQ', 'artist_name': 'Rend Collective', 'album_name': 'Campfire II: Simplicity', 'track_number': 4, 'duration_ms': 283066, 'popularity': 53, 'danceability': 0.538, 'energy': 0.776, 'loudness': -7.219, 'speechiness': 0.0556, 'acousticness': 0.142, 'instrumentalness': 0, 'liveness': 0.0921, 'valence': 0.375, 'tempo': 140.042}, '4upaAELySMLYyrMyaBl3Bb': {'name': 'More Than Conquerors', 'artist_id': '11Y54BxlxC3UIAUkU2eadQ', 'artist_name': 'Rend Collective', 'album_name': 'Campfire II: Simplicity', 'track_number': 11, 'duration_ms': 261106, 'popularity': 53, 'danceability': 0.583, 'energy': 0.787, 'loudness': -3.653, 'speechiness': 0.0318, 'acousticness': 0.085, 'instrumentalness': 0, 'liveness': 0.31, 'valence': 0.501, 'tempo': 104.987}, '5or2hHXDa6Y5gYYRWFUQCy': {'name': 'One And Only', 'artist_id': '11Y54BxlxC3UIAUkU2eadQ', 'artist_name': 'Rend Collective', 'album_name': 'As Family We Go', 'track_number': 5, 'duration_ms': 278252, 'popularity': 51, 'danceability': 0.485, 'energy': 0.534, 'loudness': -9.768, 'speechiness': 0.035, 'acousticness': 0.0229, 'instrumentalness': 0.000191, 'liveness': 0.116, 'valence': 0.36, 'tempo': 127.985}, '5Gfv5Mt5HiPTayAgGanuI2': {'name': 'You Are My Vision', 'artist_id': '11Y54BxlxC3UIAUkU2eadQ', 'artist_name': 'Rend Collective', 'album_name': 'Homemade Worship by Handmade People', 'track_number': 2, 'duration_ms': 233920, 'popularity': 49, 'danceability': 0.495, 'energy': 0.77, 'loudness': -14.424, 'speechiness': 0.0656, 'acousticness': 0.0196, 'instrumentalness': 0, 'liveness': 0.504, 'valence': 0.251, 'tempo': 123.013}, '3DgwAwHOyxfpQUuuMzvzUN': {'name': '10,000 Reasons', 'artist_id': '11Y54BxlxC3UIAUkU2eadQ', 'artist_name': 'Rend Collective', 'album_name': 'Campfire', 'track_number': 11, 'duration_ms': 300427, 'popularity': 48, 'danceability': 0.595, 'energy': 0.319, 'loudness': -10.656, 'speechiness': 0.0271, 'acousticness': 0.643, 'instrumentalness': 2.32e-06, 'liveness': 0.0898, 'valence': 0.244, 'tempo': 136.09}, '2EeCxglAQ4XK0IwuqjvRwj': {'name': 'Every Giant Will Fall', 'artist_id': '11Y54BxlxC3UIAUkU2eadQ', 'artist_name': 'Rend Collective', 'album_name': 'As Family We Go', 'track_number': 4, 'duration_ms': 225319, 'popularity': 48, 'danceability': 0.559, 'energy': 0.834, 'loudness': -6.894, 'speechiness': 0.0417, 'acousticness': 0.0194, 'instrumentalness': 0, 'liveness': 0.115, 'valence': 0.494, 'tempo': 112.003}, '7Dwb6OZi0EtRM8hBa10Uqz': {'name': 'Boldly I Approach (The Art of Celebration)', 'artist_id': '11Y54BxlxC3UIAUkU2eadQ', 'artist_name': 'Rend Collective', 'album_name': 'The Art Of Celebration', 'track_number': 11, 'duration_ms': 362449, 'popularity': 47, 'danceability': 0.39, 'energy': 0.505, 'loudness': -6.893, 'speechiness': 0.0307, 'acousticness': 0.00657, 'instrumentalness': 0, 'liveness': 0.111, 'valence': 0.215, 'tempo': 137.83}, '1uCVpUO24T2ukRcU0TCfFu': {'name': 'Whatever Comes', 'artist_id': '11Y54BxlxC3UIAUkU2eadQ', 'artist_name': 'Rend Collective', 'album_name': 'Campfire II: Simplicity', 'track_number': 7, 'duration_ms': 250906, 'popularity': 47, 'danceability': 0.526, 'energy': 0.392, 'loudness': -10.221, 'speechiness': 0.0363, 'acousticness': 0.86, 'instrumentalness': 0, 'liveness': 0.36, 'valence': 0.2, 'tempo': 128.932}, '644es5aYPJghtZLjM1rmSP': {'name': 'Concerning Hobbits', 'artist_id': '0OcclcP5o8VKH2TRqSY2A7', 'artist_name': 'Howard Shore', 'album_name': 'The Lord Of The Rings: The Fellowship Of The Ring (Original Motion Picture Soundtrack)', 'track_number': 2, 'duration_ms': 175040, 'popularity': 64, 'danceability': 0.488, 'energy': 0.0629, 'loudness': -21.524, 'speechiness': 0.0342, 'acousticness': 0.843, 'instrumentalness': 0.406, 'liveness': 0.133, 'valence': 0.181, 'tempo': 104.311}, '1ykbtFnlIjmIFnZ8j6wg6i': {'name': 'The Breaking Of The Fellowship - feat. "In Dreams"', 'artist_id': '0OcclcP5o8VKH2TRqSY2A7', 'artist_name': 'Howard Shore', 'album_name': 'The Lord Of The Rings: The Fellowship Of The Ring (Original Motion Picture Soundtrack)', 'track_number': 17, 'duration_ms': 440800, 'popularity': 63, 'danceability': 0.131, 'energy': 0.137, 'loudness': -20.553, 'speechiness': 0.0387, 'acousticness': 0.934, 'instrumentalness': 0.485, 'liveness': 0.087, 'valence': 0.0485, 'tempo': 78.577}, '3Knohqfb9jeYzL6wMZiWLM': {'name': 'The Council Of Elrond - feat. "Aniron Theme For Aragorn And Arwen "', 'artist_id': '0OcclcP5o8VKH2TRqSY2A7', 'artist_name': 'Howard Shore', 'album_name': 'The Lord Of The Rings: The Fellowship Of The Ring (Original Motion Picture Soundtrack)', 'track_number': 10, 'duration_ms': 229106, 'popularity': 63, 'danceability': 0.104, 'energy': 0.111, 'loudness': -20.031, 'speechiness': 0.0517, 'acousticness': 0.979, 'instrumentalness': 0.926, 'liveness': 0.11, 'valence': 0.0388, 'tempo': 83.933}, '1lIcdDpGlc2mO2LYA0f5KM': {'name': 'The Fellowship Reunited - feat. Sir James Galway, Viggo Mortensen And Rene Fleming', 'artist_id': '0OcclcP5o8VKH2TRqSY2A7', 'artist_name': 'Howard Shore', 'album_name': 'The Lord Of The Rings - The Return Of The King - The Complete Recordings (Limited Edition)', 'track_number': 49, 'duration_ms': 738080, 'popularity': 58, 'danceability': 0.137, 'energy': 0.0625, 'loudness': -22.77, 'speechiness': 0.04, 'acousticness': 0.941, 'instrumentalness': 0.926, 'liveness': 0.277, 'valence': 0.0365, 'tempo': 87.682}, '1TQKEwq4y9SkNciJuisE1m': {'name': 'Evenstar', 'artist_id': '0OcclcP5o8VKH2TRqSY2A7', 'artist_name': 'Howard Shore', 'album_name': 'The Lord Of The Rings: The Two Towers (Original Motion Picture Soundtrack)', 'track_number': 8, 'duration_ms': 195600, 'popularity': 56, 'danceability': 0.122, 'energy': 0.0407, 'loudness': -26.194, 'speechiness': 0.0457, 'acousticness': 0.96, 'instrumentalness': 0.847, 'liveness': 0.104, 'valence': 0.0345, 'tempo': 74.418}, '6HYCOHzY2xR4W2dOokH3ed': {'name': 'The Bridge Of Khazad Dum', 'artist_id': '0OcclcP5o8VKH2TRqSY2A7', 'artist_name': 'Howard Shore', 'album_name': 'The Lord Of The Rings: The Fellowship Of The Ring (Original Motion Picture Soundtrack)', 'track_number': 13, 'duration_ms': 357400, 'popularity': 55, 'danceability': 0.299, 'energy': 0.492, 'loudness': -13.19, 'speechiness': 0.0544, 'acousticness': 0.36, 'instrumentalness': 0.905, 'liveness': 0.202, 'valence': 0.0367, 'tempo': 84.204}, '0VfcYOujgf9JDAgwlgu1qm': {'name': 'Many Meetings', 'artist_id': '0OcclcP5o8VKH2TRqSY2A7', 'artist_name': 'Howard Shore', 'album_name': 'The Lord Of The Rings: The Fellowship Of The Ring (Original Motion Picture Soundtrack)', 'track_number': 9, 'duration_ms': 185426, 'popularity': 54, 'danceability': 0.0623, 'energy': 0.1, 'loudness': -20.607, 'speechiness': 0.0459, 'acousticness': 0.982, 'instrumentalness': 0.934, 'liveness': 0.116, 'valence': 0.0358, 'tempo': 64.791}, '63CXPpiEiW7JnXvZ1cUXcp': {'name': 'Lothlorien - feat. "Lament For Gandalf"', 'artist_id': '0OcclcP5o8VKH2TRqSY2A7', 'artist_name': 'Howard Shore', 'album_name': 'The Lord Of The Rings: The Fellowship Of The Ring (Original Motion Picture Soundtrack)', 'track_number': 14, 'duration_ms': 273933, 'popularity': 53, 'danceability': 0.167, 'energy': 0.117, 'loudness': -20.316, 'speechiness': 0.0374, 'acousticness': 0.869, 'instrumentalness': 0.928, 'liveness': 0.112, 'valence': 0.033, 'tempo': 86.378}, '6ANHfvTsKVUMQD1xD2VAMr': {'name': 'The Prophecy', 'artist_id': '0OcclcP5o8VKH2TRqSY2A7', 'artist_name': 'Howard Shore', 'album_name': 'The Lord Of The Rings: The Fellowship Of The Ring (Original Motion Picture Soundtrack)', 'track_number': 1, 'duration_ms': 235026, 'popularity': 52, 'danceability': 0.0735, 'energy': 0.0657, 'loudness': -21.943, 'speechiness': 0.0374, 'acousticness': 0.947, 'instrumentalness': 0.958, 'liveness': 0.258, 'valence': 0.0319, 'tempo': 177.549}, '54BDogj8DLMEAyMRz9gWnC': {'name': 'Delivering the News', 'artist_id': '0OcclcP5o8VKH2TRqSY2A7', 'artist_name': 'Howard Shore', 'album_name': 'Spotlight (Original Motion Picture Soundtrack)', 'track_number': 17, 'duration_ms': 220619, 'popularity': 52, 'danceability': 0.384, 'energy': 0.039, 'loudness': -23.58, 'speechiness': 0.0413, 'acousticness': 0.982, 'instrumentalness': 0.911, 'liveness': 0.111, 'valence': 0.0359, 'tempo': 116.914}, '18ycL9Q5zLDeY9M2Lr3Ozw': {'name': 'Mykonos', 'artist_id': '4EVpmkEwrLYEg6jIsiPMIb', 'artist_name': 'Fleet Foxes', 'album_name': 'Sun Giant', 'track_number': 4, 'duration_ms': 275306, 'popularity': 69, 'danceability': 0.3, 'energy': 0.452, 'loudness': -9.298, 'speechiness': 0.0305, 'acousticness': 0.395, 'instrumentalness': 0.000818, 'liveness': 0.137, 'valence': 0.338, 'tempo': 82.988}, '1Er5JMNcguoBMFXxwZ7BWH': {'name': 'White Winter Hymnal', 'artist_id': '4EVpmkEwrLYEg6jIsiPMIb', 'artist_name': 'Fleet Foxes', 'album_name': 'Fleet Foxes', 'track_number': 2, 'duration_ms': 147026, 'popularity': 66, 'danceability': 0.629, 'energy': 0.534, 'loudness': -9.054, 'speechiness': 0.0267, 'acousticness': 0.437, 'instrumentalness': 3.33e-06, 'liveness': 0.328, 'valence': 0.66, 'tempo': 124.964}, '3Q3LbqfjDhWjmyYeirHfDe': {'name': 'Third of May / daigahara - Edit', 'artist_id': '4EVpmkEwrLYEg6jIsiPMIb', 'artist_name': 'Fleet Foxes', 'album_name': 'Third of May / daigahara (Edit)', 'track_number': 1, 'duration_ms': 242989, 'popularity': 66, 'danceability': 0.256, 'energy': 0.513, 'loudness': -6.04, 'speechiness': 0.0338, 'acousticness': 0.0244, 'instrumentalness': 0.0028, 'liveness': 0.127, 'valence': 0.38, 'tempo': 142.293}, '3ol9IHaYnppYIK8IADJALx': {'name': 'Third of May / daigahara', 'artist_id': '4EVpmkEwrLYEg6jIsiPMIb', 'artist_name': 'Fleet Foxes', 'album_name': 'Third of May / daigahara', 'track_number': 1, 'duration_ms': 525426, 'popularity': 60, 'danceability': 0.266, 'energy': 0.464, 'loudness': -8.006, 'speechiness': 0.0322, 'acousticness': 0.117, 'instrumentalness': 0.0836, 'liveness': 0.0867, 'valence': 0.236, 'tempo': 142.777}, '1pbOvzdkL5iujppWgzBQdS': {'name': 'Helplessness Blues', 'artist_id': '4EVpmkEwrLYEg6jIsiPMIb', 'artist_name': 'Fleet Foxes', 'album_name': 'Helplessness Blues', 'track_number': 6, 'duration_ms': 303386, 'popularity': 59, 'danceability': 0.324, 'energy': 0.463, 'loudness': -7.247, 'speechiness': 0.0336, 'acousticness': 0.0781, 'instrumentalness': 5.63e-06, 'liveness': 0.103, 'valence': 0.194, 'tempo': 125.295}, '6T8qnBbc2rxlWLiweD1e5M': {'name': 'Blue Ridge Mountains', 'artist_id': '4EVpmkEwrLYEg6jIsiPMIb', 'artist_name': 'Fleet Foxes', 'album_name': 'Fleet Foxes', 'track_number': 10, 'duration_ms': 265773, 'popularity': 59, 'danceability': 0.524, 'energy': 0.446, 'loudness': -7.823, 'speechiness': 0.0275, 'acousticness': 0.688, 'instrumentalness': 0.000745, 'liveness': 0.101, 'valence': 0.22, 'tempo': 97.856}, '5gXF3XyUkM9BVA8QW7uYUg': {'name': 'Ragged Wood', 'artist_id': '4EVpmkEwrLYEg6jIsiPMIb', 'artist_name': 'Fleet Foxes', 'album_name': 'Fleet Foxes', 'track_number': 3, 'duration_ms': 307213, 'popularity': 57, 'danceability': 0.362, 'energy': 0.658, 'loudness': -5.929, 'speechiness': 0.0292, 'acousticness': 0.0995, 'instrumentalness': 0.0102, 'liveness': 0.0602, 'valence': 0.151, 'tempo': 104.21}, '6kzi5LTg5uECin8pC34nxV': {'name': 'Montezuma', 'artist_id': '4EVpmkEwrLYEg6jIsiPMIb', 'artist_name': 'Fleet Foxes', 'album_name': 'Helplessness Blues', 'track_number': 1, 'duration_ms': 217120, 'popularity': 56, 'danceability': 0.314, 'energy': 0.308, 'loudness': -9.117, 'speechiness': 0.0283, 'acousticness': 0.854, 'instrumentalness': 0.0117, 'liveness': 0.0993, 'valence': 0.0989, 'tempo': 99.214}, '5oYkuJL2VQ3Ss2oxNuRk3L': {'name': 'Tiger Mountain Peasant Song', 'artist_id': '4EVpmkEwrLYEg6jIsiPMIb', 'artist_name': 'Fleet Foxes', 'album_name': 'Fleet Foxes', 'track_number': 4, 'duration_ms': 208973, 'popularity': 54, 'danceability': 0.654, 'energy': 0.148, 'loudness': -11.963, 'speechiness': 0.0327, 'acousticness': 0.929, 'instrumentalness': 0.0016, 'liveness': 0.0895, 'valence': 0.268, 'tempo': 130.738}, '1gSWmUWt0Flr52cQoH0yDJ': {'name': 'Oliver James', 'artist_id': '4EVpmkEwrLYEg6jIsiPMIb', 'artist_name': 'Fleet Foxes', 'album_name': 'Fleet Foxes', 'track_number': 11, 'duration_ms': 203880, 'popularity': 54, 'danceability': 0.48, 'energy': 0.0631, 'loudness': -11.913, 'speechiness': 0.0413, 'acousticness': 0.946, 'instrumentalness': 0, 'liveness': 0.0801, 'valence': 0.155, 'tempo': 118.44}, '5C6uh95eAL0RBTSGXKQwvk': {'name': 'Hometown Girl', 'artist_id': '7vCtweS8UVAXTyau2j0rDT', 'artist_name': 'Josh Turner', 'album_name': 'Deep South', 'track_number': 3, 'duration_ms': 215080, 'popularity': 77, 'danceability': 0.505, 'energy': 0.79, 'loudness': -5.442, 'speechiness': 0.035, 'acousticness': 0.263, 'instrumentalness': 0.0884, 'liveness': 0.123, 'valence': 0.444, 'tempo': 155.934}, '1WzAeadSKJhqykZFbJNmQv': {'name': 'Your Man', 'artist_id': '7vCtweS8UVAXTyau2j0rDT', 'artist_name': 'Josh Turner', 'album_name': 'Your Man', 'track_number': 4, 'duration_ms': 211893, 'popularity': 66, 'danceability': 0.742, 'energy': 0.638, 'loudness': -4.332, 'speechiness': 0.0239, 'acousticness': 0.331, 'instrumentalness': 0.000221, 'liveness': 0.0584, 'valence': 0.744, 'tempo': 100.504}, '1KhrAWvLIjRlQIJtSTgvsi': {'name': 'Would You Go With Me', 'artist_id': '7vCtweS8UVAXTyau2j0rDT', 'artist_name': 'Josh Turner', 'album_name': 'Your Man', 'track_number': 1, 'duration_ms': 228186, 'popularity': 63, 'danceability': 0.604, 'energy': 0.846, 'loudness': -5.26, 'speechiness': 0.0288, 'acousticness': 0.131, 'instrumentalness': 0.00109, 'liveness': 0.11, 'valence': 0.787, 'tempo': 122.915}, '2p07VcUwRZ5sru3mJ0JogS': {'name': "Why Don't We Just Dance", 'artist_id': '7vCtweS8UVAXTyau2j0rDT', 'artist_name': 'Josh Turner', 'album_name': 'Haywire', 'track_number': 1, 'duration_ms': 192800, 'popularity': 62, 'danceability': 0.656, 'energy': 0.763, 'loudness': -5.636, 'speechiness': 0.0405, 'acousticness': 0.43, 'instrumentalness': 0.000175, 'liveness': 0.0985, 'valence': 0.69, 'tempo': 121.808}, '2rg3yLJKN5Yl4JCHHkMgeC': {'name': 'Time Is Love', 'artist_id': '7vCtweS8UVAXTyau2j0rDT', 'artist_name': 'Josh Turner', 'album_name': 'Punching Bag', 'track_number': 3, 'duration_ms': 200373, 'popularity': 59, 'danceability': 0.655, 'energy': 0.826, 'loudness': -4.828, 'speechiness': 0.0433, 'acousticness': 0.0869, 'instrumentalness': 0.000209, 'liveness': 0.0836, 'valence': 0.621, 'tempo': 111.986}, '2HqCaO7BV010qXS5FuiTED': {'name': 'Long Black Train', 'artist_id': '7vCtweS8UVAXTyau2j0rDT', 'artist_name': 'Josh Turner', 'album_name': 'Long Black Train', 'track_number': 1, 'duration_ms': 250626, 'popularity': 56, 'danceability': 0.472, 'energy': 0.709, 'loudness': -6.471, 'speechiness': 0.051, 'acousticness': 0.228, 'instrumentalness': 2.2e-05, 'liveness': 0.114, 'valence': 0.846, 'tempo': 169.867}, '5CdOqNxkQ7054Rp86f5OWi': {'name': 'Lay Low', 'artist_id': '7vCtweS8UVAXTyau2j0rDT', 'artist_name': 'Josh Turner', 'album_name': 'Deep South', 'track_number': 10, 'duration_ms': 260853, 'popularity': 55, 'danceability': 0.626, 'energy': 0.691, 'loudness': -5.873, 'speechiness': 0.0283, 'acousticness': 0.0887, 'instrumentalness': 9.63e-05, 'liveness': 0.115, 'valence': 0.394, 'tempo': 109.005}, '5z5RJbZqDRYOgaMU6RetVk': {'name': 'Never Had A Reason', 'artist_id': '7vCtweS8UVAXTyau2j0rDT', 'artist_name': 'Josh Turner', 'album_name': 'Deep South', 'track_number': 7, 'duration_ms': 241826, 'popularity': 52, 'danceability': 0.54, 'energy': 0.646, 'loudness': -6.953, 'speechiness': 0.0277, 'acousticness': 0.158, 'instrumentalness': 0.00204, 'liveness': 0.146, 'valence': 0.307, 'tempo': 77.031}, '5JtRN8PCpxoL03vnIpZXc7': {'name': 'Firecracker', 'artist_id': '7vCtweS8UVAXTyau2j0rDT', 'artist_name': 'Josh Turner', 'album_name': 'Everything Is Fine', 'track_number': 2, 'duration_ms': 208800, 'popularity': 39, 'danceability': 0.455, 'energy': 0.976, 'loudness': -5.303, 'speechiness': 0.108, 'acousticness': 0.0869, 'instrumentalness': 0.000348, 'liveness': 0.097, 'valence': 0.752, 'tempo': 174.719}, '0MVWxE7RIYMDt8JPC2vLNF': {'name': 'Deep South', 'artist_id': '7vCtweS8UVAXTyau2j0rDT', 'artist_name': 'Josh Turner', 'album_name': 'Deep South', 'track_number': 1, 'duration_ms': 235800, 'popularity': 50, 'danceability': 0.79, 'energy': 0.879, 'loudness': -5.698, 'speechiness': 0.0371, 'acousticness': 0.136, 'instrumentalness': 0.00118, 'liveness': 0.0845, 'valence': 0.962, 'tempo': 116.992}, '3OEgQVkIzrID6dSTNHz9FG': {'name': "Don't Call Me", 'artist_id': '1nf0nRF0W4ybnJdda00pKY', 'artist_name': 'The Swon Brothers', 'album_name': "Don't Call Me", 'track_number': 1, 'duration_ms': 220449, 'popularity': 57, 'danceability': 0.554, 'energy': 0.828, 'loudness': -5.112, 'speechiness': 0.044, 'acousticness': 0.144, 'instrumentalness': 0, 'liveness': 0.0643, 'valence': 0.672, 'tempo': 90.029}, '7lG4154Md1Kw7BMg56Pt4s': {'name': 'Later On', 'artist_id': '1nf0nRF0W4ybnJdda00pKY', 'artist_name': 'The Swon Brothers', 'album_name': 'The Swon Brothers', 'track_number': 2, 'duration_ms': 217160, 'popularity': 48, 'danceability': 0.411, 'energy': 0.903, 'loudness': -2.948, 'speechiness': 0.144, 'acousticness': 0.0544, 'instrumentalness': 0, 'liveness': 0.104, 'valence': 0.611, 'tempo': 180.078}, '3ScJqT6cpcaLQjMwu4yogi': {'name': 'Pretty Beautiful', 'artist_id': '1nf0nRF0W4ybnJdda00pKY', 'artist_name': 'The Swon Brothers', 'album_name': 'The Swon Brothers', 'track_number': 8, 'duration_ms': 195666, 'popularity': 46, 'danceability': 0.512, 'energy': 0.645, 'loudness': -5.511, 'speechiness': 0.0289, 'acousticness': 0.353, 'instrumentalness': 0, 'liveness': 0.118, 'valence': 0.242, 'tempo': 90.034}, '290cSxnINrpvrFzqOxFqft': {'name': 'Pray for You', 'artist_id': '1nf0nRF0W4ybnJdda00pKY', 'artist_name': 'The Swon Brothers', 'album_name': 'The Swon Brothers', 'track_number': 5, 'duration_ms': 234306, 'popularity': 45, 'danceability': 0.486, 'energy': 0.77, 'loudness': -4.545, 'speechiness': 0.0478, 'acousticness': 0.154, 'instrumentalness': 0, 'liveness': 0.0947, 'valence': 0.4, 'tempo': 83.945}, '3a8bHL5QtHvkoCIYWdYHui': {'name': 'Dwight Trashed', 'artist_id': '1nf0nRF0W4ybnJdda00pKY', 'artist_name': 'The Swon Brothers', 'album_name': 'Pretty Cool Scars', 'track_number': 1, 'duration_ms': 179457, 'popularity': 38, 'danceability': 0.515, 'energy': 0.918, 'loudness': -3.669, 'speechiness': 0.0699, 'acousticness': 0.00963, 'instrumentalness': 0, 'liveness': 0.315, 'valence': 0.68, 'tempo': 163.991}, '5fnGNW4axw52MaEaVvB77d': {'name': 'Timeless', 'artist_id': '1nf0nRF0W4ybnJdda00pKY', 'artist_name': 'The Swon Brothers', 'album_name': 'Timeless', 'track_number': 4, 'duration_ms': 189160, 'popularity': 36, 'danceability': 0.823, 'energy': 0.873, 'loudness': -4.49, 'speechiness': 0.0511, 'acousticness': 0.117, 'instrumentalness': 0, 'liveness': 0.0738, 'valence': 0.817, 'tempo': 110.023}, '6SSr6bidIF9m7QspjIhc5L': {'name': 'About Last Night', 'artist_id': '1nf0nRF0W4ybnJdda00pKY', 'artist_name': 'The Swon Brothers', 'album_name': 'Pretty Cool Scars', 'track_number': 5, 'duration_ms': 196764, 'popularity': 34, 'danceability': 0.581, 'energy': 0.858, 'loudness': -4.486, 'speechiness': 0.0604, 'acousticness': 0.0236, 'instrumentalness': 0, 'liveness': 0.0682, 'valence': 0.577, 'tempo': 109.943}, '03EwZBuDcnPrFAp15ThrYT': {'name': 'Pretty Cool Scars', 'artist_id': '1nf0nRF0W4ybnJdda00pKY', 'artist_name': 'The Swon Brothers', 'album_name': 'Pretty Cool Scars', 'track_number': 3, 'duration_ms': 200748, 'popularity': 33, 'danceability': 0.542, 'energy': 0.752, 'loudness': -4.604, 'speechiness': 0.0374, 'acousticness': 0.00416, 'instrumentalness': 0, 'liveness': 0.126, 'valence': 0.265, 'tempo': 107.921}, '7obPCswm0UiZfbl7Xj8VAy': {'name': 'Killing Me', 'artist_id': '1nf0nRF0W4ybnJdda00pKY', 'artist_name': 'The Swon Brothers', 'album_name': 'Timeless', 'track_number': 5, 'duration_ms': 177320, 'popularity': 33, 'danceability': 0.63, 'energy': 0.738, 'loudness': -6.304, 'speechiness': 0.0308, 'acousticness': 0.314, 'instrumentalness': 0, 'liveness': 0.0959, 'valence': 0.344, 'tempo': 96.995}, '4EkTUr57ihH1bjyJpExtGg': {'name': 'Just Another Girl', 'artist_id': '1nf0nRF0W4ybnJdda00pKY', 'artist_name': 'The Swon Brothers', 'album_name': 'Timeless', 'track_number': 1, 'duration_ms': 191120, 'popularity': 32, 'danceability': 0.527, 'energy': 0.85, 'loudness': -4.077, 'speechiness': 0.036, 'acousticness': 0.229, 'instrumentalness': 0, 'liveness': 0.0331, 'valence': 0.841, 'tempo': 170.029}, '4VNCVb4cgYUPPoHxIxtzJT': {'name': 'Skyrim (Main Theme)', 'artist_id': '7EIbKyiLnEJ1Y074UIUyZJ', 'artist_name': 'Peter Hollens', 'album_name': 'Peter Hollens', 'track_number': 2, 'duration_ms': 195386, 'popularity': 52, 'danceability': 0.579, 'energy': 0.799, 'loudness': -5.507, 'speechiness': 0.0415, 'acousticness': 0.537, 'instrumentalness': 0.325, 'liveness': 0.138, 'valence': 0.357, 'tempo': 100.414}, '04TaLOwlQA8wbXbsru1K8P': {'name': 'I See Fire', 'artist_id': '7EIbKyiLnEJ1Y074UIUyZJ', 'artist_name': 'Peter Hollens', 'album_name': 'Peter Hollens', 'track_number': 1, 'duration_ms': 291920, 'popularity': 47, 'danceability': 0.505, 'energy': 0.353, 'loudness': -6.857, 'speechiness': 0.0275, 'acousticness': 0.634, 'instrumentalness': 1.58e-06, 'liveness': 0.217, 'valence': 0.218, 'tempo': 76.06}, '5FUWnXhrCgEXM0b7GI2uvf': {'name': 'Baba Yetu', 'artist_id': '7EIbKyiLnEJ1Y074UIUyZJ', 'artist_name': 'Peter Hollens', 'album_name': 'Baba Yetu', 'track_number': 1, 'duration_ms': 218604, 'popularity': 47, 'danceability': 0.436, 'energy': 0.456, 'loudness': -10.396, 'speechiness': 0.0371, 'acousticness': 0.806, 'instrumentalness': 2.85e-06, 'liveness': 0.109, 'valence': 0.234, 'tempo': 92.054}, '5uBCfIO7v8KxMwu8MSCWuA': {'name': 'Misty Mountains', 'artist_id': '7EIbKyiLnEJ1Y074UIUyZJ', 'artist_name': 'Peter Hollens', 'album_name': 'Misty Mountains: Songs Inspired by The Hobbit and Lord of the Rings', 'track_number': 4, 'duration_ms': 258933, 'popularity': 47, 'danceability': 0.244, 'energy': 0.21, 'loudness': -8.793, 'speechiness': 0.0318, 'acousticness': 0.764, 'instrumentalness': 0.000488, 'liveness': 0.104, 'valence': 0.189, 'tempo': 137.543}, '36ZEUaeqwwKy7HOQGidW15': {'name': 'The Hanging Tree', 'artist_id': '7EIbKyiLnEJ1Y074UIUyZJ', 'artist_name': 'Peter Hollens', 'album_name': 'The Hanging Tree', 'track_number': 1, 'duration_ms': 203206, 'popularity': 47, 'danceability': 0.26, 'energy': 0.273, 'loudness': -11.196, 'speechiness': 0.0313, 'acousticness': 0.361, 'instrumentalness': 6.72e-05, 'liveness': 0.116, 'valence': 0.514, 'tempo': 68.969}, '7FKaz2DtsfSHYaUdg66WeX': {'name': 'Hobbit Drinking Medley', 'artist_id': '7EIbKyiLnEJ1Y074UIUyZJ', 'artist_name': 'Peter Hollens', 'album_name': 'Misty Mountains: Songs Inspired by The Hobbit and Lord of the Rings', 'track_number': 12, 'duration_ms': 151306, 'popularity': 46, 'danceability': 0.546, 'energy': 0.818, 'loudness': -4.63, 'speechiness': 0.359, 'acousticness': 0.566, 'instrumentalness': 0, 'liveness': 0.353, 'valence': 0.82, 'tempo': 107.416}, '5a5C2WzY2KTUaQDJynBuJx': {'name': 'Game of Thrones (Main Title)', 'artist_id': '7EIbKyiLnEJ1Y074UIUyZJ', 'artist_name': 'Peter Hollens', 'album_name': 'Game of Thrones (Main Title)', 'track_number': 1, 'duration_ms': 168824, 'popularity': 46, 'danceability': 0.337, 'energy': 0.791, 'loudness': -7.826, 'speechiness': 0.0642, 'acousticness': 0.147, 'instrumentalness': 0.952, 'liveness': 0.097, 'valence': 0.229, 'tempo': 173.899}, '7N2LelbPKDyWmFQZHhgvzw': {'name': 'Star Wars Medley', 'artist_id': '7EIbKyiLnEJ1Y074UIUyZJ', 'artist_name': 'Peter Hollens', 'album_name': 'Star Wars Medley', 'track_number': 1, 'duration_ms': 263087, 'popularity': 45, 'danceability': 0.375, 'energy': 0.602, 'loudness': -4.703, 'speechiness': 0.0374, 'acousticness': 0.856, 'instrumentalness': 0.873, 'liveness': 0.0672, 'valence': 0.608, 'tempo': 107.127}, '10kJzrXI48v0wzRBBPjo06': {'name': 'The Sound of Silence', 'artist_id': '7EIbKyiLnEJ1Y074UIUyZJ', 'artist_name': 'Peter Hollens', 'album_name': 'The Sound of Silence', 'track_number': 1, 'duration_ms': 196652, 'popularity': 45, 'danceability': 0.323, 'energy': 0.248, 'loudness': -9.187, 'speechiness': 0.0353, 'acousticness': 0.946, 'instrumentalness': 0, 'liveness': 0.251, 'valence': 0.197, 'tempo': 80.526}, '4yGO4h8Pn1E81Ev4Dl50vP': {'name': 'Into the West', 'artist_id': '7EIbKyiLnEJ1Y074UIUyZJ', 'artist_name': 'Peter Hollens', 'album_name': 'Misty Mountains: Songs Inspired by The Hobbit and Lord of the Rings', 'track_number': 10, 'duration_ms': 266133, 'popularity': 43, 'danceability': 0.378, 'energy': 0.359, 'loudness': -5.723, 'speechiness': 0.0298, 'acousticness': 0.342, 'instrumentalness': 0, 'liveness': 0.103, 'valence': 0.0822, 'tempo': 94.857}, '1ijrMIqQvZNsnoqGukPzFD': {'name': "I'm Forrest... Forrest Gump", 'artist_id': '0Xk15jHKly4c3AhPr5vjoA', 'artist_name': 'Alan Silvestri', 'album_name': 'Forrest Gump - Original Motion Picture Score', 'track_number': 1, 'duration_ms': 159666, 'popularity': 58, 'danceability': 0.402, 'energy': 0.046, 'loudness': -22.779, 'speechiness': 0.033, 'acousticness': 0.979, 'instrumentalness': 0.513, 'liveness': 0.0771, 'valence': 0.0889, 'tempo': 104.425}, '75uuO9osMuY3bgXgzTRagc': {'name': '"Best Day Ever"', 'artist_id': '0Xk15jHKly4c3AhPr5vjoA', 'artist_name': 'Alan Silvestri', 'album_name': 'Allied (Music from the Motion Picture)', 'track_number': 6, 'duration_ms': 111266, 'popularity': 53, 'danceability': 0.21, 'energy': 0.0356, 'loudness': -22.06, 'speechiness': 0.0391, 'acousticness': 0.985, 'instrumentalness': 0.964, 'liveness': 0.0894, 'valence': 0.0434, 'tempo': 91.488}, '5SXsXjVJCWeJuf7FHvgBYR': {'name': 'The Avengers', 'artist_id': '0Xk15jHKly4c3AhPr5vjoA', 'artist_name': 'Alan Silvestri', 'album_name': 'The Avengers', 'track_number': 18, 'duration_ms': 123360, 'popularity': 52, 'danceability': 0.436, 'energy': 0.56, 'loudness': -8.238, 'speechiness': 0.0387, 'acousticness': 0.55, 'instrumentalness': 0.906, 'liveness': 0.186, 'valence': 0.212, 'tempo': 119.071}, '2byBJ4bFeFPpSOgJnR6b8a': {'name': 'Where Heaven Ends', 'artist_id': '0Xk15jHKly4c3AhPr5vjoA', 'artist_name': 'Alan Silvestri', 'album_name': 'Forrest Gump - Original Motion Picture Score', 'track_number': 18, 'duration_ms': 92240, 'popularity': 51, 'danceability': 0.212, 'energy': 0.0107, 'loudness': -38.358, 'speechiness': 0.0416, 'acousticness': 0.592, 'instrumentalness': 0.72, 'liveness': 0.213, 'valence': 0.0407, 'tempo': 66.094}, '6eLLMXei71a3S1eBJANXaM': {'name': 'Jenny Returns', 'artist_id': '0Xk15jHKly4c3AhPr5vjoA', 'artist_name': 'Alan Silvestri', 'album_name': 'Forrest Gump - Original Motion Picture Score', 'track_number': 14, 'duration_ms': 160093, 'popularity': 51, 'danceability': 0.0846, 'energy': 0.0296, 'loudness': -27.324, 'speechiness': 0.0389, 'acousticness': 0.572, 'instrumentalness': 0.691, 'liveness': 0.125, 'valence': 0.0386, 'tempo': 70.873}, '0AE7HvW4tTLvajXI5R5UJf': {'name': 'Two Loves', 'artist_id': '0Xk15jHKly4c3AhPr5vjoA', 'artist_name': 'Alan Silvestri', 'album_name': 'The Walk (Original Motion Picture Soundtrack)', 'track_number': 3, 'duration_ms': 199546, 'popularity': 49, 'danceability': 0.215, 'energy': 0.0222, 'loudness': -28.845, 'speechiness': 0.0422, 'acousticness': 0.955, 'instrumentalness': 0.36, 'liveness': 0.216, 'valence': 0.105, 'tempo': 129.08}, '435vx38BVoUIqSG1VfoJOh': {'name': 'Suite From Forrest Gump', 'artist_id': '0Xk15jHKly4c3AhPr5vjoA', 'artist_name': 'Alan Silvestri', 'album_name': 'Forrest Gump - Original Motion Picture Score', 'track_number': 21, 'duration_ms': 394240, 'popularity': 48, 'danceability': 0.111, 'energy': 0.103, 'loudness': -18.36, 'speechiness': 0.0356, 'acousticness': 0.893, 'instrumentalness': 0.816, 'liveness': 0.164, 'valence': 0.0413, 'tempo': 84.52}, '1Ig5PYAhZaCiCVAdIEcdAC': {'name': '"All That Is or Ever Was or Ever Will Be"', 'artist_id': '0Xk15jHKly4c3AhPr5vjoA', 'artist_name': 'Alan Silvestri', 'album_name': 'Cosmos: A SpaceTime Odyssey (Music from the Original TV Series) Vol. 3', 'track_number': 1, 'duration_ms': 95720, 'popularity': 44, 'danceability': 0.292, 'energy': 0.139, 'loudness': -16.134, 'speechiness': 0.0354, 'acousticness': 0.981, 'instrumentalness': 0.00538, 'liveness': 0.32, 'valence': 0.0327, 'tempo': 73.37}, '68RXRtyaaccT2N0Kaq0Ko9': {'name': 'Forrest Gump Suite', 'artist_id': '0Xk15jHKly4c3AhPr5vjoA', 'artist_name': 'Alan Silvestri', 'album_name': 'Forrest Gump - The Soundtrack', 'track_number': 18, 'duration_ms': 529640, 'popularity': 28, 'danceability': 0.11, 'energy': 0.122, 'loudness': -15.631, 'speechiness': 0.038, 'acousticness': 0.958, 'instrumentalness': 0.871, 'liveness': 0.0759, 'valence': 0.039, 'tempo': 75.766}, '1FI5hblwy9ZwyPg4Jr5hni': {'name': 'Back To The Future: Back To The Future', 'artist_id': '0Xk15jHKly4c3AhPr5vjoA', 'artist_name': 'Alan Silvestri', 'album_name': 'The Back To The Future Trilogy', 'track_number': 1, 'duration_ms': 210960, 'popularity': 39, 'danceability': 0.163, 'energy': 0.386, 'loudness': -13.092, 'speechiness': 0.0373, 'acousticness': 0.774, 'instrumentalness': 0.882, 'liveness': 0.147, 'valence': 0.102, 'tempo': 71.468}, '2y5aJvzXhHPA94U5GFAcXe': {'name': 'I Dont Wanna Live Forever (Fifty Shades Darker)', 'artist_id': '5ZsFI1h6hIdQRw2ti0hz81', 'artist_name': 'ZAYN', 'album_name': 'Fifty Shades Darker (Original Motion Picture Soundtrack)', 'track_number': 1, 'duration_ms': 245653, 'popularity': 88, 'danceability': 0.737, 'energy': 0.452, 'loudness': -8.366, 'speechiness': 0.0534, 'acousticness': 0.0578, 'instrumentalness': 1.48e-05, 'liveness': 0.187, 'valence': 0.0971, 'tempo': 117.962}, '0z9UVN8VBHJ9HdfYsOuuNf': {'name': 'Safe & Sound - from The Hunger Games Soundtrack', 'artist_id': '06HL4z0CvFAxyc27GXpf02', 'artist_name': 'Taylor Swift', 'album_name': 'The Hunger Games: Songs From District 12 And Beyond', 'track_number': 4, 'duration_ms': 240066, 'popularity': 66, 'danceability': 0.476, 'energy': 0.3, 'loudness': -10.737, 'speechiness': 0.0277, 'acousticness': 0.893, 'instrumentalness': 1.53e-05, 'liveness': 0.0732, 'valence': 0.309, 'tempo': 144.163}, '5vyxXfD5gLlyPxGZMEjtmd': {'name': 'Crazier', 'artist_id': '06HL4z0CvFAxyc27GXpf02', 'artist_name': 'Taylor Swift', 'album_name': 'Hannah Montana The Movie', 'track_number': 12, 'duration_ms': 191946, 'popularity': 60, 'danceability': 0.441, 'energy': 0.546, 'loudness': -5.386, 'speechiness': 0.0283, 'acousticness': 0.0887, 'instrumentalness': 1.47e-05, 'liveness': 0.138, 'valence': 0.165, 'tempo': 133.049}, '7wjbSn8QHsxqKXU5M0jXGM': {'name': 'Eyes Open', 'artist_id': '06HL4z0CvFAxyc27GXpf02', 'artist_name': 'Taylor Swift', 'album_name': 'The Hunger Games: Songs From District 12 And Beyond', 'track_number': 14, 'duration_ms': 244586, 'popularity': 58, 'danceability': 0.601, 'energy': 0.723, 'loudness': -7.182, 'speechiness': 0.0361, 'acousticness': 0.00858, 'instrumentalness': 0.0012, 'liveness': 0.0756, 'valence': 0.319, 'tempo': 137.073}, '06FXaDDdg0BzXl15cthMS5': {'name': "Should've Said No - Live Show / Event", 'artist_id': '06HL4z0CvFAxyc27GXpf02', 'artist_name': 'Taylor Swift', 'album_name': 'Music from the 3D Concert Experience (International Version)', 'track_number': 8, 'duration_ms': 253800, 'popularity': 53, 'danceability': 0.355, 'energy': 0.981, 'loudness': -2.487, 'speechiness': 0.0684, 'acousticness': 0.022, 'instrumentalness': 1.75e-05, 'liveness': 0.828, 'valence': 0.415, 'tempo': 168.019}, '5DN6H6gepbZoVy9jSIV2ue': {'name': 'Save Me, Now', 'artist_id': '4IsX3za8eNto9exd3VlTTK', 'artist_name': 'Godwin', 'album_name': 'From Dust', 'track_number': 5, 'duration_ms': 263135, 'popularity': 1, 'danceability': 0.305, 'energy': 0.378, 'loudness': -12.228, 'speechiness': 0.0379, 'acousticness': 0.483, 'instrumentalness': 0.0108, 'liveness': 0.075, 'valence': 0.152, 'tempo': 67.767}, '1HigdORYp9eFlTsnnF4cRU': {'name': 'Curse of Adam', 'artist_id': '4IsX3za8eNto9exd3VlTTK', 'artist_name': 'Godwin', 'album_name': 'From Dust', 'track_number': 1, 'duration_ms': 288033, 'popularity': 1, 'danceability': 0.5, 'energy': 0.543, 'loudness': -9.164, 'speechiness': 0.0375, 'acousticness': 0.0209, 'instrumentalness': 0.0741, 'liveness': 0.367, 'valence': 0.16, 'tempo': 129.961}, '4dpRpHk4ohjALlZbyfa4by': {'name': 'Foolish Man', 'artist_id': '4IsX3za8eNto9exd3VlTTK', 'artist_name': 'Godwin', 'album_name': 'From Dust', 'track_number': 3, 'duration_ms': 242080, 'popularity': 0, 'danceability': 0.532, 'energy': 0.702, 'loudness': -7.151, 'speechiness': 0.0495, 'acousticness': 0.00595, 'instrumentalness': 0.00216, 'liveness': 0.096, 'valence': 0.378, 'tempo': 129.989}, '1xI4owym9GRbcyc35iGO8b': {'name': 'Tree', 'artist_id': '4IsX3za8eNto9exd3VlTTK', 'artist_name': 'Godwin', 'album_name': 'From Dust', 'track_number': 2, 'duration_ms': 322461, 'popularity': 0, 'danceability': 0.337, 'energy': 0.344, 'loudness': -11.545, 'speechiness': 0.0488, 'acousticness': 0.569, 'instrumentalness': 0.00498, 'liveness': 0.281, 'valence': 0.117, 'tempo': 85.981}, '1hAdl8eYz9ENrQKX95tRWt': {'name': 'The Veil', 'artist_id': '4IsX3za8eNto9exd3VlTTK', 'artist_name': 'Godwin', 'album_name': 'From Dust', 'track_number': 4, 'duration_ms': 173861, 'popularity': 0, 'danceability': 0.597, 'energy': 0.445, 'loudness': -9.444, 'speechiness': 0.0387, 'acousticness': 0.816, 'instrumentalness': 0.353, 'liveness': 0.0921, 'valence': 0.395, 'tempo': 84.941}, '2M1Qc1mGSI1IYtmJzQtfPq': {'name': 'This Year', 'artist_id': '3hyGGjxu73JuzBa757H6R5', 'artist_name': 'The Mountain Goats', 'album_name': 'The Sunset Tree', 'track_number': 3, 'duration_ms': 232893, 'popularity': 54, 'danceability': 0.699, 'energy': 0.719, 'loudness': -9.481, 'speechiness': 0.0312, 'acousticness': 0.118, 'instrumentalness': 0.00259, 'liveness': 0.0913, 'valence': 0.821, 'tempo': 138.958}, '4XpQ2F8NtzWMZ3g5t8qv2Y': {'name': 'No Children', 'artist_id': '3hyGGjxu73JuzBa757H6R5', 'artist_name': 'The Mountain Goats', 'album_name': 'Tallahassee', 'track_number': 7, 'duration_ms': 168306, 'popularity': 52, 'danceability': 0.606, 'energy': 0.411, 'loudness': -7.566, 'speechiness': 0.0413, 'acousticness': 0.6, 'instrumentalness': 0.000649, 'liveness': 0.103, 'valence': 0.411, 'tempo': 84.944}, '41LUI2mXScZDjIZWmvvWpR': {'name': 'Up The Wolves', 'artist_id': '3hyGGjxu73JuzBa757H6R5', 'artist_name': 'The Mountain Goats', 'album_name': 'The Sunset Tree', 'track_number': 7, 'duration_ms': 207400, 'popularity': 50, 'danceability': 0.489, 'energy': 0.366, 'loudness': -9.362, 'speechiness': 0.0269, 'acousticness': 0.494, 'instrumentalness': 7.25e-05, 'liveness': 0.0892, 'valence': 0.494, 'tempo': 157.547}, '098PgApK9llaanxaDvAeij': {'name': 'Andrew Eldritch Is Moving Back to Leeds', 'artist_id': '3hyGGjxu73JuzBa757H6R5', 'artist_name': 'The Mountain Goats', 'album_name': 'Andrew Eldritch Is Moving Back to Leeds', 'track_number': 1, 'duration_ms': 258279, 'popularity': 45, 'danceability': 0.766, 'energy': 0.475, 'loudness': -11.524, 'speechiness': 0.0287, 'acousticness': 0.51, 'instrumentalness': 0.384, 'liveness': 0.0996, 'valence': 0.836, 'tempo': 107.981}, '0SkIl3O2MVuY0bLiHQ72gi': {'name': 'Love Love Love', 'artist_id': '3hyGGjxu73JuzBa757H6R5', 'artist_name': 'The Mountain Goats', 'album_name': 'The Sunset Tree', 'track_number': 12, 'duration_ms': 168560, 'popularity': 45, 'danceability': 0.751, 'energy': 0.228, 'loudness': -17.085, 'speechiness': 0.0453, 'acousticness': 0.733, 'instrumentalness': 0.335, 'liveness': 0.0729, 'valence': 0.216, 'tempo': 110.42}, '38dYh2pToiZPEKGVErVISk': {'name': 'The Best Ever Death Metal Band in Denton', 'artist_id': '3hyGGjxu73JuzBa757H6R5', 'artist_name': 'The Mountain Goats', 'album_name': 'All Hail West Texas (Remastered)', 'track_number': 1, 'duration_ms': 156960, 'popularity': 44, 'danceability': 0.382, 'energy': 0.642, 'loudness': -7.659, 'speechiness': 0.0395, 'acousticness': 0.76, 'instrumentalness': 0.00947, 'liveness': 0.386, 'valence': 0.789, 'tempo': 63.009}, '07gqJjvwwuZ1assFLKbiNn': {'name': 'Dance Music', 'artist_id': '3hyGGjxu73JuzBa757H6R5', 'artist_name': 'The Mountain Goats', 'album_name': 'The Sunset Tree', 'track_number': 5, 'duration_ms': 117666, 'popularity': 43, 'danceability': 0.652, 'energy': 0.568, 'loudness': -8.205, 'speechiness': 0.0363, 'acousticness': 0.482, 'instrumentalness': 0, 'liveness': 0.0945, 'valence': 0.853, 'tempo': 168.182}, '1ey9ub4AISvEmjM7tkoBh0': {'name': 'Going to Georgia', 'artist_id': '3hyGGjxu73JuzBa757H6R5', 'artist_name': 'The Mountain Goats', 'album_name': 'Zopilote Machine', 'track_number': 18, 'duration_ms': 135693, 'popularity': 42, 'danceability': 0.569, 'energy': 0.44, 'loudness': -10.598, 'speechiness': 0.0341, 'acousticness': 0.579, 'instrumentalness': 0.725, 'liveness': 0.115, 'valence': 0.316, 'tempo': 118.382}, '7hyfYgXMS5BumjAjY98Xoe': {'name': 'The Legend of Chavo Guerrero', 'artist_id': '3hyGGjxu73JuzBa757H6R5', 'artist_name': 'The Mountain Goats', 'album_name': 'Beat the Champ', 'track_number': 2, 'duration_ms': 180133, 'popularity': 42, 'danceability': 0.688, 'energy': 0.858, 'loudness': -5.803, 'speechiness': 0.0449, 'acousticness': 0.00771, 'instrumentalness': 0.274, 'liveness': 0.368, 'valence': 0.92, 'tempo': 142.117}, '4rLLO47FTsKBwNILP9rMYI': {'name': 'Foreign Object', 'artist_id': '3hyGGjxu73JuzBa757H6R5', 'artist_name': 'The Mountain Goats', 'album_name': 'Beat the Champ', 'track_number': 3, 'duration_ms': 171480, 'popularity': 41, 'danceability': 0.778, 'energy': 0.736, 'loudness': -5.876, 'speechiness': 0.0276, 'acousticness': 0.0512, 'instrumentalness': 0.0266, 'liveness': 0.347, 'valence': 0.927, 'tempo': 137.739}, '4LT3jD9UcmFRKZiyuYlp7n': {'name': "If It Don't Work Out", 'artist_id': '1oplL2hHYq7CQykvSbd6gy', 'artist_name': "Anthony D'Amato", 'album_name': 'The Shipwreck from the Shore', 'track_number': 6, 'duration_ms': 183906, 'popularity': 43, 'danceability': 0.597, 'energy': 0.299, 'loudness': -8.711, 'speechiness': 0.0281, 'acousticness': 0.834, 'instrumentalness': 0, 'liveness': 0.119, 'valence': 0.266, 'tempo': 77.266}, '1zozfArqnkwK1wo9lMeW60': {'name': 'Was a Time', 'artist_id': '1oplL2hHYq7CQykvSbd6gy', 'artist_name': "Anthony D'Amato", 'album_name': 'The Shipwreck from the Shore', 'track_number': 1, 'duration_ms': 199800, 'popularity': 40, 'danceability': 0.411, 'energy': 0.826, 'loudness': -5.831, 'speechiness': 0.102, 'acousticness': 0.0393, 'instrumentalness': 0.00331, 'liveness': 0.221, 'valence': 0.335, 'tempo': 114.308}, '3zbM8xP6PwpY3mGxzvIdHS': {'name': 'Good and Ready', 'artist_id': '1oplL2hHYq7CQykvSbd6gy', 'artist_name': "Anthony D'Amato", 'album_name': 'The Shipwreck from the Shore', 'track_number': 3, 'duration_ms': 263480, 'popularity': 35, 'danceability': 0.679, 'energy': 0.434, 'loudness': -6.985, 'speechiness': 0.0284, 'acousticness': 0.346, 'instrumentalness': 0.000558, 'liveness': 0.167, 'valence': 0.677, 'tempo': 85.527}, '5B9PePNY0OkvGXuuw5Y8Xz': {'name': 'Back Back Back', 'artist_id': '1oplL2hHYq7CQykvSbd6gy', 'artist_name': "Anthony D'Amato", 'album_name': 'The Shipwreck from the Shore', 'track_number': 2, 'duration_ms': 229346, 'popularity': 34, 'danceability': 0.609, 'energy': 0.679, 'loudness': -6.334, 'speechiness': 0.0309, 'acousticness': 0.0633, 'instrumentalness': 0.00204, 'liveness': 0.162, 'valence': 0.726, 'tempo': 115.058}, '0M3vcAL55zGTn3oP2ih604': {'name': 'Oh My Goodness', 'artist_id': '1oplL2hHYq7CQykvSbd6gy', 'artist_name': "Anthony D'Amato", 'album_name': 'Cold Snap', 'track_number': 1, 'duration_ms': 250000, 'popularity': 32, 'danceability': 0.548, 'energy': 0.696, 'loudness': -7.064, 'speechiness': 0.0297, 'acousticness': 0.069, 'instrumentalness': 0.00129, 'liveness': 0.138, 'valence': 0.554, 'tempo': 88.941}, '1gUgiYnYktGcyPoF93lsnc': {'name': "Honey That's Not All", 'artist_id': '1oplL2hHYq7CQykvSbd6gy', 'artist_name': "Anthony D'Amato", 'album_name': 'Cold Snap', 'track_number': 11, 'duration_ms': 197000, 'popularity': 28, 'danceability': 0.56, 'energy': 0.263, 'loudness': -13.718, 'speechiness': 0.0333, 'acousticness': 0.797, 'instrumentalness': 6.42e-05, 'liveness': 0.111, 'valence': 0.486, 'tempo': 117.756}, '2l2PUbHGDbz6IGYaHpT1lz': {'name': 'Rain On A Strange Roof', 'artist_id': '1oplL2hHYq7CQykvSbd6gy', 'artist_name': "Anthony D'Amato", 'album_name': 'Cold Snap', 'track_number': 2, 'duration_ms': 201573, 'popularity': 25, 'danceability': 0.606, 'energy': 0.737, 'loudness': -5.819, 'speechiness': 0.0421, 'acousticness': 0.00347, 'instrumentalness': 0.000231, 'liveness': 0.0935, 'valence': 0.7, 'tempo': 140.095}, '3fiFIjj7Tpgx0DN8F6Kpgc': {'name': 'Cold Snap', 'artist_id': '1oplL2hHYq7CQykvSbd6gy', 'artist_name': "Anthony D'Amato", 'album_name': 'Cold Snap', 'track_number': 8, 'duration_ms': 300533, 'popularity': 19, 'danceability': 0.278, 'energy': 0.752, 'loudness': -5.791, 'speechiness': 0.0445, 'acousticness': 0.00328, 'instrumentalness': 0.116, 'liveness': 0.0951, 'valence': 0.285, 'tempo': 132.715}, '6iyC74ukfSSW8zkxyJ3tiY': {'name': 'Ballad Of The Undecided', 'artist_id': '1oplL2hHYq7CQykvSbd6gy', 'artist_name': "Anthony D'Amato", 'album_name': 'Cold Snap', 'track_number': 10, 'duration_ms': 294040, 'popularity': 18, 'danceability': 0.462, 'energy': 0.894, 'loudness': -4.814, 'speechiness': 0.0407, 'acousticness': 7.84e-05, 'instrumentalness': 0.512, 'liveness': 0.093, 'valence': 0.766, 'tempo': 115.843}, '5d8YytQAj4DzigDrDwUdY3': {'name': "If You're Gonna Build A Wall", 'artist_id': '1oplL2hHYq7CQykvSbd6gy', 'artist_name': "Anthony D'Amato", 'album_name': 'Cold Snap', 'track_number': 4, 'duration_ms': 184080, 'popularity': 17, 'danceability': 0.549, 'energy': 0.452, 'loudness': -11.468, 'speechiness': 0.033, 'acousticness': 0.671, 'instrumentalness': 0.0436, 'liveness': 0.15, 'valence': 0.262, 'tempo': 110.561}, '47fN6xeggnfG9NKPJUNC8H': {'name': 'Please Be My Strength', 'artist_id': '4J4o73Oun7v0XXRjN8DPif', 'artist_name': 'Gungor', 'album_name': 'Beautiful Things', 'track_number': 9, 'duration_ms': 212546, 'popularity': 46, 'danceability': 0.429, 'energy': 0.132, 'loudness': -16.858, 'speechiness': 0.037, 'acousticness': 0.915, 'instrumentalness': 0.000248, 'liveness': 0.113, 'valence': 0.166, 'tempo': 99.165}, '2ynZSIOI3DxnjuY2JTow05': {'name': 'Beautiful Things - Live', 'artist_id': '4J4o73Oun7v0XXRjN8DPif', 'artist_name': 'Gungor', 'album_name': 'A Creation Liturgy [Live]', 'track_number': 11, 'duration_ms': 376693, 'popularity': 46, 'danceability': 0.461, 'energy': 0.301, 'loudness': -10.286, 'speechiness': 0.0265, 'acousticness': 0.0452, 'instrumentalness': 0.502, 'liveness': 0.676, 'valence': 0.107, 'tempo': 82.02}, '60V6mN6EQttmhVsgPmPUJW': {'name': 'Who We Are', 'artist_id': '4J4o73Oun7v0XXRjN8DPif', 'artist_name': 'Gungor', 'album_name': 'Who We Are', 'track_number': 1, 'duration_ms': 245065, 'popularity': 45, 'danceability': 0.432, 'energy': 0.29, 'loudness': -10.658, 'speechiness': 0.0396, 'acousticness': 0.927, 'instrumentalness': 0.00189, 'liveness': 0.259, 'valence': 0.511, 'tempo': 139.958}, '5eEUZlp3CwFq0QoUBcgo0I': {'name': 'I Am Mountain', 'artist_id': '4J4o73Oun7v0XXRjN8DPif', 'artist_name': 'Gungor', 'album_name': 'I Am Mountain', 'track_number': 1, 'duration_ms': 248946, 'popularity': 44, 'danceability': 0.596, 'energy': 0.49, 'loudness': -8.983, 'speechiness': 0.0343, 'acousticness': 0.452, 'instrumentalness': 0.0167, 'liveness': 0.111, 'valence': 0.27, 'tempo': 86.884}, '6fPSbqWloDmdWf3nA1nE45': {'name': 'You Are The Beauty - Live', 'artist_id': '4J4o73Oun7v0XXRjN8DPif', 'artist_name': 'Gungor', 'album_name': 'A Creation Liturgy [Live]', 'track_number': 1, 'duration_ms': 376133, 'popularity': 42, 'danceability': 0.479, 'energy': 0.661, 'loudness': -9.492, 'speechiness': 0.036, 'acousticness': 0.106, 'instrumentalness': 0.0928, 'liveness': 0.96, 'valence': 0.304, 'tempo': 133.928}, '0Q6SwpdV7ZUpO3LG4ikAAv': {'name': 'Vapor', 'artist_id': '4J4o73Oun7v0XXRjN8DPif', 'artist_name': 'Gungor', 'album_name': 'One Wild Life: Soul', 'track_number': 12, 'duration_ms': 298040, 'popularity': 40, 'danceability': 0.396, 'energy': 0.375, 'loudness': -9.113, 'speechiness': 0.0327, 'acousticness': 0.0194, 'instrumentalness': 2.08e-05, 'liveness': 0.108, 'valence': 0.167, 'tempo': 147.944}, '4ywugrAa8pJtzVOFWaLnWz': {'name': 'Dry Bones', 'artist_id': '4J4o73Oun7v0XXRjN8DPif', 'artist_name': 'Gungor', 'album_name': 'Beautiful Things', 'track_number': 1, 'duration_ms': 316600, 'popularity': 39, 'danceability': 0.324, 'energy': 0.554, 'loudness': -7.161, 'speechiness': 0.0497, 'acousticness': 0.0371, 'instrumentalness': 0.000309, 'liveness': 0.274, 'valence': 0.171, 'tempo': 133.308}, '1BbvY4RSjqPykhVvYxWdsS': {'name': 'Long Way Off', 'artist_id': '4J4o73Oun7v0XXRjN8DPif', 'artist_name': 'Gungor', 'album_name': 'I Am Mountain', 'track_number': 3, 'duration_ms': 277040, 'popularity': 37, 'danceability': 0.743, 'energy': 0.395, 'loudness': -12.487, 'speechiness': 0.033, 'acousticness': 0.817, 'instrumentalness': 0.413, 'liveness': 0.104, 'valence': 0.179, 'tempo': 129.972}, '2RTkebdbPFyg4AMIzJZql1': {'name': 'Outrage', 'artist_id': '0xhIBddw7R69CWKsCt2gVt', 'artist_name': 'Capital Lights', 'album_name': 'This Is An Outrage!', 'track_number': 1, 'duration_ms': 229866, 'popularity': 44, 'danceability': 0.478, 'energy': 0.855, 'loudness': -4.881, 'speechiness': 0.0333, 'acousticness': 0.00665, 'instrumentalness': 0, 'liveness': 0.492, 'valence': 0.624, 'tempo': 164.916}, '4ZxgjHhnqz9TyAwBtTeGzN': {'name': 'Say Hey', 'artist_id': '0xhIBddw7R69CWKsCt2gVt', 'artist_name': 'Capital Lights', 'album_name': "Rhythm 'N' Moves", 'track_number': 7, 'duration_ms': 182453, 'popularity': 33, 'danceability': 0.808, 'energy': 0.485, 'loudness': -5.823, 'speechiness': 0.0333, 'acousticness': 0.0308, 'instrumentalness': 0, 'liveness': 0.0868, 'valence': 0.805, 'tempo': 98.018}, '0spVGAIkC7ntZL22jgdN5u': {'name': 'Mile Away', 'artist_id': '0xhIBddw7R69CWKsCt2gVt', 'artist_name': 'Capital Lights', 'album_name': 'This Is An Outrage!', 'track_number': 6, 'duration_ms': 223400, 'popularity': 33, 'danceability': 0.776, 'energy': 0.519, 'loudness': -7.098, 'speechiness': 0.0295, 'acousticness': 0.138, 'instrumentalness': 0, 'liveness': 0.107, 'valence': 0.61, 'tempo': 117.995}, '2BIH7pmQpDlWP6bCzv9SeA': {'name': 'Caroline', 'artist_id': '0xhIBddw7R69CWKsCt2gVt', 'artist_name': 'Capital Lights', 'album_name': "Rhythm 'N' Moves", 'track_number': 3, 'duration_ms': 205400, 'popularity': 30, 'danceability': 0.616, 'energy': 0.829, 'loudness': -4.786, 'speechiness': 0.0271, 'acousticness': 0.00317, 'instrumentalness': 0, 'liveness': 0.238, 'valence': 0.921, 'tempo': 142.997}, '0HjpouGnPswTLh3hSvWOMK': {'name': 'Let The Little Lady Talk', 'artist_id': '0xhIBddw7R69CWKsCt2gVt', 'artist_name': 'Capital Lights', 'album_name': 'This Is An Outrage!', 'track_number': 8, 'duration_ms': 249226, 'popularity': 29, 'danceability': 0.589, 'energy': 0.616, 'loudness': -6.164, 'speechiness': 0.0297, 'acousticness': 0.0302, 'instrumentalness': 0, 'liveness': 0.203, 'valence': 0.86, 'tempo': 81.463}, '5WH2cii4we48T6BMSlr162': {'name': 'Let Your Hair Down', 'artist_id': '0xhIBddw7R69CWKsCt2gVt', 'artist_name': 'Capital Lights', 'album_name': "Rhythm 'N' Moves", 'track_number': 2, 'duration_ms': 263720, 'popularity': 29, 'danceability': 0.51, 'energy': 0.926, 'loudness': -4.664, 'speechiness': 0.0274, 'acousticness': 0.00331, 'instrumentalness': 3.88e-05, 'liveness': 0.286, 'valence': 0.575, 'tempo': 144.995}, '0zrbISwByqUAWssIhgQwQr': {'name': 'His Favorite Christmas Story', 'artist_id': '0xhIBddw7R69CWKsCt2gVt', 'artist_name': 'Capital Lights', 'album_name': 'X Christmas', 'track_number': 15, 'duration_ms': 212680, 'popularity': 29, 'danceability': 0.675, 'energy': 0.63, 'loudness': -5.128, 'speechiness': 0.0311, 'acousticness': 0.0529, 'instrumentalness': 0, 'liveness': 0.146, 'valence': 0.674, 'tempo': 139.987}, '6UX5LsQp3rdWs8x73wXrtF': {'name': 'Coldfront Heatstroke', 'artist_id': '0xhIBddw7R69CWKsCt2gVt', 'artist_name': 'Capital Lights', 'album_name': "Rhythm 'N' Moves", 'track_number': 4, 'duration_ms': 207840, 'popularity': 28, 'danceability': 0.609, 'energy': 0.846, 'loudness': -4.155, 'speechiness': 0.0314, 'acousticness': 0.00407, 'instrumentalness': 0, 'liveness': 0.155, 'valence': 0.688, 'tempo': 146.071}, '0ZvAw2h9im8Yy1PE3CZcyQ': {'name': "Rhythm 'N' Moves", 'artist_id': '0xhIBddw7R69CWKsCt2gVt', 'artist_name': 'Capital Lights', 'album_name': "Rhythm 'N' Moves", 'track_number': 1, 'duration_ms': 225986, 'popularity': 28, 'danceability': 0.643, 'energy': 0.824, 'loudness': -4.153, 'speechiness': 0.0346, 'acousticness': 0.0231, 'instrumentalness': 1.77e-06, 'liveness': 0.33, 'valence': 0.739, 'tempo': 144.985}, '5S4iqbelathvMs6wlkXfmn': {'name': 'Worth As Much As A Counterfeit Dollar', 'artist_id': '0xhIBddw7R69CWKsCt2gVt', 'artist_name': 'Capital Lights', 'album_name': 'This Is An Outrage!', 'track_number': 2, 'duration_ms': 185293, 'popularity': 28, 'danceability': 0.494, 'energy': 0.923, 'loudness': -4.636, 'speechiness': 0.0406, 'acousticness': 0.00451, 'instrumentalness': 0, 'liveness': 0.124, 'valence': 0.869, 'tempo': 169.949}, '1n8NKQRg8LVHy7oUhUgbFF': {'name': "Hedwig's Theme", 'artist_id': '3dRfiJ2650SZu6GbydcHNb', 'artist_name': 'John Williams', 'album_name': "Harry Potter and The Sorcerer's Stone Original Motion Picture Soundtrack", 'track_number': 19, 'duration_ms': 309093, 'popularity': 61, 'danceability': 0.156, 'energy': 0.162, 'loudness': -17.101, 'speechiness': 0.036, 'acousticness': 0.897, 'instrumentalness': 0.691, 'liveness': 0.111, 'valence': 0.0689, 'tempo': 73.407}, '6CeCOC2zx1qS8mQNYHe6IM': {'name': 'Prologue', 'artist_id': '3dRfiJ2650SZu6GbydcHNb', 'artist_name': 'John Williams', 'album_name': "Harry Potter and The Sorcerer's Stone Original Motion Picture Soundtrack", 'track_number': 1, 'duration_ms': 130293, 'popularity': 60, 'danceability': 0.177, 'energy': 0.0188, 'loudness': -29.484, 'speechiness': 0.0367, 'acousticness': 0.957, 'instrumentalness': 0.446, 'liveness': 0.635, 'valence': 0.0813, 'tempo': 146.472}, '42gZM6AQ9BDMaTyTmMDVlN': {'name': "Theme From Schindler's List", 'artist_id': '3dRfiJ2650SZu6GbydcHNb', 'artist_name': 'John Williams', 'album_name': "Schindler's List (Soundtrack)", 'track_number': 1, 'duration_ms': 255160, 'popularity': 53, 'danceability': 0.161, 'energy': 0.143, 'loudness': -24.125, 'speechiness': 0.0431, 'acousticness': 0.868, 'instrumentalness': 0.768, 'liveness': 0.1, 'valence': 0.0757, 'tempo': 94.992}, '7di1zbwgfJkRLkTGV44icu': {'name': 'Duel of the Fates', 'artist_id': '3dRfiJ2650SZu6GbydcHNb', 'artist_name': 'John Williams', 'album_name': 'Star Wars: The Phantom Menace (Original Motion Picture Soundtrack)', 'track_number': 2, 'duration_ms': 254360, 'popularity': 57, 'danceability': 0.439, 'energy': 0.438, 'loudness': -17.341, 'speechiness': 0.0416, 'acousticness': 0.932, 'instrumentalness': 0.782, 'liveness': 0.266, 'valence': 0.219, 'tempo': 79.984}, '0RGZCtszeCpGRgbMyVigAG': {'name': "Sayuri's Theme", 'artist_id': '3dRfiJ2650SZu6GbydcHNb', 'artist_name': 'John Williams', 'album_name': 'Memoirs of a Geisha (Remastered)', 'track_number': 1, 'duration_ms': 91493, 'popularity': 32, 'danceability': 0.234, 'energy': 0.121, 'loudness': -20.542, 'speechiness': 0.0459, 'acousticness': 0.911, 'instrumentalness': 0.932, 'liveness': 0.111, 'valence': 0.069, 'tempo': 87.507}, '4lg0h4AJhPMxbO3VMpbUqS': {'name': "Harry's Wondrous World", 'artist_id': '3dRfiJ2650SZu6GbydcHNb', 'artist_name': 'John Williams', 'album_name': "Harry Potter and The Sorcerer's Stone Original Motion Picture Soundtrack", 'track_number': 2, 'duration_ms': 321066, 'popularity': 56, 'danceability': 0.227, 'energy': 0.264, 'loudness': -14.905, 'speechiness': 0.0325, 'acousticness': 0.881, 'instrumentalness': 0.9, 'liveness': 0.114, 'valence': 0.223, 'tempo': 84.986}, '2TZbQZXOuR8osP2AK8yYMN': {'name': 'Theme From Jurassic Park - From The "Jurassic Park" Soundtrack', 'artist_id': '3dRfiJ2650SZu6GbydcHNb', 'artist_name': 'John Williams', 'album_name': 'Jurassic Park (Soundtrack)', 'track_number': 2, 'duration_ms': 207426, 'popularity': 52, 'danceability': 0.163, 'energy': 0.17, 'loudness': -19.121, 'speechiness': 0.0368, 'acousticness': 0.942, 'instrumentalness': 0.753, 'liveness': 0.112, 'valence': 0.0684, 'tempo': 130.29}, '5wsHtmFHWntJzcN6n8ivjd': {'name': "Rey's Theme", 'artist_id': '3dRfiJ2650SZu6GbydcHNb', 'artist_name': 'John Williams', 'album_name': 'Star Wars: The Force Awakens (Original Motion Picture Soundtrack)', 'track_number': 6, 'duration_ms': 191066, 'popularity': 53, 'danceability': 0.229, 'energy': 0.158, 'loudness': -16.595, 'speechiness': 0.0338, 'acousticness': 0.977, 'instrumentalness': 0.851, 'liveness': 0.0814, 'valence': 0.135, 'tempo': 100.987}, '1PPTlPJqKuL0fdoTmzwXJy': {'name': 'A Window to the Past', 'artist_id': '3dRfiJ2650SZu6GbydcHNb', 'artist_name': 'John Williams', 'album_name': 'Harry Potter and the Prisoner of Azkaban / Original Motion Picture Soundtrack', 'track_number': 7, 'duration_ms': 234040, 'popularity': 53, 'danceability': 0.212, 'energy': 0.0443, 'loudness': -24.6, 'speechiness': 0.0434, 'acousticness': 0.954, 'instrumentalness': 0.537, 'liveness': 0.0998, 'valence': 0.133, 'tempo': 106.632}, '2Bsnj9KAmtYz8PW9RImef7': {'name': 'Across the Stars (Love Theme from "Star Wars: Attack of the Clones")', 'artist_id': '3dRfiJ2650SZu6GbydcHNb', 'artist_name': 'John Williams', 'album_name': 'Star Wars: Attack of the Clones (Original Motion Picture Soundtrack)', 'track_number': 2, 'duration_ms': 333306, 'popularity': 52, 'danceability': 0.0906, 'energy': 0.0975, 'loudness': -22.636, 'speechiness': 0.0389, 'acousticness': 0.857, 'instrumentalness': 0.915, 'liveness': 0.111, 'valence': 0.0687, 'tempo': 84.146}, '1kLeO0H9TdEewIZdr7Zi2i': {'name': 'Rooftop Kiss', 'artist_id': '3PhL2Vdao2v8SS8AptuhAr', 'artist_name': 'James Horner', 'album_name': 'The Amazing Spider-Man', 'track_number': 12, 'duration_ms': 154840, 'popularity': 64, 'danceability': 0.0833, 'energy': 0.00524, 'loudness': -36.281, 'speechiness': 0.0457, 'acousticness': 0.935, 'instrumentalness': 0.91, 'liveness': 0.0818, 'valence': 0.0366, 'tempo': 70.329}, '6vtY2LUeXJ7KISwgiTu0Ph': {'name': 'The Ludlows', 'artist_id': '3PhL2Vdao2v8SS8AptuhAr', 'artist_name': 'James Horner', 'album_name': 'Legends Of The Fall Original Motion Picture Soundtrack', 'track_number': 2, 'duration_ms': 340400, 'popularity': 62, 'danceability': 0.0767, 'energy': 0.0223, 'loudness': -27.684, 'speechiness': 0.0372, 'acousticness': 0.938, 'instrumentalness': 0.848, 'liveness': 0.0998, 'valence': 0.0497, 'tempo': 79.803}, '1UBd7aWHZCz8yirI9KCvAU': {'name': 'Becoming one of "The People" Becoming one with Neytiri', 'artist_id': '3PhL2Vdao2v8SS8AptuhAr', 'artist_name': 'James Horner', 'album_name': 'AVATAR Music From The Motion Picture Music Composed and Conducted by James Horner', 'track_number': 5, 'duration_ms': 463706, 'popularity': 59, 'danceability': 0.0993, 'energy': 0.0902, 'loudness': -26.307, 'speechiness': 0.0428, 'acousticness': 0.692, 'instrumentalness': 0.85, 'liveness': 0.0745, 'valence': 0.0377, 'tempo': 71.062}, '31loMj4ZFxOedEd2bHHQjg': {'name': 'Legends of the Fall', 'artist_id': '3PhL2Vdao2v8SS8AptuhAr', 'artist_name': 'James Horner', 'album_name': 'Legends Of The Fall Original Motion Picture Soundtrack', 'track_number': 1, 'duration_ms': 256733, 'popularity': 55, 'danceability': 0.164, 'energy': 0.0313, 'loudness': -28.301, 'speechiness': 0.0371, 'acousticness': 0.897, 'instrumentalness': 0.944, 'liveness': 0.0984, 'valence': 0.0356, 'tempo': 110.028}, '3q0Ks78ADSomVdDSap32mz': {'name': 'Emotions - Instrumental', 'artist_id': '3PhL2Vdao2v8SS8AptuhAr', 'artist_name': 'James Horner', 'album_name': 'Bicentennial Man - Original Motion Picture Soundtrack', 'track_number': 11, 'duration_ms': 236066, 'popularity': 54, 'danceability': 0.122, 'energy': 0.0161, 'loudness': -33.108, 'speechiness': 0.0476, 'acousticness': 0.952, 'instrumentalness': 0.934, 'liveness': 0.0958, 'valence': 0.0361, 'tempo': 148.561}, '3Yvi5NkUrSppVwrMHYkB6u': {'name': 'A Gift Of A Thistle', 'artist_id': '3PhL2Vdao2v8SS8AptuhAr', 'artist_name': 'James Horner', 'album_name': 'Braveheart - Original Motion Picture Soundtrack', 'track_number': 2, 'duration_ms': 97866, 'popularity': 49, 'danceability': 0.124, 'energy': 0.0116, 'loudness': -36.061, 'speechiness': 0.0408, 'acousticness': 0.92, 'instrumentalness': 0.871, 'liveness': 0.0938, 'valence': 0.0393, 'tempo': 80.655}, '55gn4hDvcrc8pmVWcBTVkR': {'name': 'Part 2 - Instrumental', 'artist_id': '3PhL2Vdao2v8SS8AptuhAr', 'artist_name': 'James Horner', 'album_name': 'IRIS - Original Motion Picture Soundtrack', 'track_number': 2, 'duration_ms': 204066, 'popularity': 53, 'danceability': 0.152, 'energy': 0.101, 'loudness': -25.083, 'speechiness': 0.0429, 'acousticness': 0.927, 'instrumentalness': 0.9, 'liveness': 0.201, 'valence': 0.0331, 'tempo': 71.049}, '2pl6chJQxGLXgpbAoiMGRf': {'name': 'For The Love Of A Princess', 'artist_id': '3PhL2Vdao2v8SS8AptuhAr', 'artist_name': 'James Horner', 'album_name': 'More Music from Braveheart', 'track_number': 17, 'duration_ms': 245000, 'popularity': 15, 'danceability': 0.165, 'energy': 0.0636, 'loudness': -26.014, 'speechiness': 0.048, 'acousticness': 0.508, 'instrumentalness': 0.939, 'liveness': 0.111, 'valence': 0.0359, 'tempo': 111.125}, '1TvpEAMfSY9c7WNTefmQWE': {'name': 'Tania (End Credits) - Voice', 'artist_id': '3PhL2Vdao2v8SS8AptuhAr', 'artist_name': 'James Horner', 'album_name': 'Enemy At The Gates - Original Motion Picture Soundtrack', 'track_number': 12, 'duration_ms': 413493, 'popularity': 53, 'danceability': 0.0603, 'energy': 0.0492, 'loudness': -27.52, 'speechiness': 0.0507, 'acousticness': 0.809, 'instrumentalness': 0.927, 'liveness': 0.102, 'valence': 0.0374, 'tempo': 60.601}, '4uQ8h0F0AShbx7MyaqMEBa': {'name': 'Rose', 'artist_id': '3PhL2Vdao2v8SS8AptuhAr', 'artist_name': 'James Horner', 'album_name': "Titanic: Original Motion Picture Soundtrack - Collector's Anniversary Edition", 'track_number': 4, 'duration_ms': 172520, 'popularity': 47, 'danceability': 0.147, 'energy': 0.0393, 'loudness': -24.563, 'speechiness': 0.0387, 'acousticness': 0.86, 'instrumentalness': 0.944, 'liveness': 0.131, 'valence': 0.0392, 'tempo': 138.478}, '4nMlau89VAjmV7agkl7OY3': {'name': 'Fresh Eyes', 'artist_id': '2oX42qP5ineK3hrhBECLmj', 'artist_name': 'Andy Grammer', 'album_name': 'Fresh Eyes', 'track_number': 1, 'duration_ms': 198001, 'popularity': 75, 'danceability': 0.822, 'energy': 0.544, 'loudness': -6.797, 'speechiness': 0.0332, 'acousticness': 0.562, 'instrumentalness': 2.4e-05, 'liveness': 0.144, 'valence': 0.865, 'tempo': 122.047}, '4orphgwPHHRsdEkfUmANSD': {'name': "Honey, I'm Good.", 'artist_id': '2oX42qP5ineK3hrhBECLmj', 'artist_name': 'Andy Grammer', 'album_name': 'Magazines Or Novels', 'track_number': 1, 'duration_ms': 199263, 'popularity': 67, 'danceability': 0.753, 'energy': 0.796, 'loudness': -6.406, 'speechiness': 0.0576, 'acousticness': 0.0378, 'instrumentalness': 0, 'liveness': 0.331, 'valence': 0.597, 'tempo': 122.025}, '7MapZTlRqFfUteNcghsTwf': {'name': 'Keep Your Head Up', 'artist_id': '2oX42qP5ineK3hrhBECLmj', 'artist_name': 'Andy Grammer', 'album_name': 'Andy Grammer', 'track_number': 1, 'duration_ms': 190480, 'popularity': 63, 'danceability': 0.666, 'energy': 0.78, 'loudness': -5.177, 'speechiness': 0.0404, 'acousticness': 0.044, 'instrumentalness': 0, 'liveness': 0.128, 'valence': 0.801, 'tempo': 90.004}, '7sjc0ColKnEt8D1WHwOdmS': {'name': 'Fresh Eyes - Ryan Riback Remix', 'artist_id': '2oX42qP5ineK3hrhBECLmj', 'artist_name': 'Andy Grammer', 'album_name': 'Fresh Eyes (Ryan Riback Remix)', 'track_number': 1, 'duration_ms': 232500, 'popularity': 55, 'danceability': 0.635, 'energy': 0.71, 'loudness': -6.151, 'speechiness': 0.0326, 'acousticness': 0.0184, 'instrumentalness': 1.83e-05, 'liveness': 0.144, 'valence': 0.623, 'tempo': 117.01}, '1fMEUGs5CvRv0VrcJlQITt': {'name': 'Good To Be Alive (Hallelujah)', 'artist_id': '2oX42qP5ineK3hrhBECLmj', 'artist_name': 'Andy Grammer', 'album_name': 'Magazines Or Novels (Deluxe Edition)', 'track_number': 13, 'duration_ms': 189869, 'popularity': 60, 'danceability': 0.784, 'energy': 0.882, 'loudness': -3.646, 'speechiness': 0.0451, 'acousticness': 0.0377, 'instrumentalness': 0, 'liveness': 0.65, 'valence': 0.702, 'tempo': 120.017}, '3uM14F9XYRMhx6MgDsS9iq': {'name': 'All Time Low - Recorded at Spotify Studios NYC', 'artist_id': '2oX42qP5ineK3hrhBECLmj', 'artist_name': 'Andy Grammer', 'album_name': 'Spotify Singles', 'track_number': 2, 'duration_ms': 185980, 'popularity': 59, 'danceability': 0.718, 'energy': 0.59, 'loudness': -5.67, 'speechiness': 0.0671, 'acousticness': 0.442, 'instrumentalness': 0, 'liveness': 0.198, 'valence': 0.536, 'tempo': 94.031}, '7tg0OrYieTMcQmxIczNMqE': {'name': 'Fine By Me', 'artist_id': '2oX42qP5ineK3hrhBECLmj', 'artist_name': 'Andy Grammer', 'album_name': 'Andy Grammer', 'track_number': 2, 'duration_ms': 172813, 'popularity': 59, 'danceability': 0.603, 'energy': 0.801, 'loudness': -4.095, 'speechiness': 0.0326, 'acousticness': 0.00975, 'instrumentalness': 0, 'liveness': 0.0443, 'valence': 0.854, 'tempo': 89.998}, '1TzHpSSy3oL0tTR3mXsQke': {'name': 'Fresh Eyes - Recorded at Spotify Studios NYC', 'artist_id': '2oX42qP5ineK3hrhBECLmj', 'artist_name': 'Andy Grammer', 'album_name': 'Spotify Singles', 'track_number': 1, 'duration_ms': 196127, 'popularity': 41, 'danceability': 0.792, 'energy': 0.508, 'loudness': -8.549, 'speechiness': 0.0402, 'acousticness': 0.424, 'instrumentalness': 0, 'liveness': 0.353, 'valence': 0.382, 'tempo': 122.085}, '4c78ZcuoiaNVBAm1HNoqNT': {'name': 'Fresh Eyes - Grey Remix', 'artist_id': '2oX42qP5ineK3hrhBECLmj', 'artist_name': 'Andy Grammer', 'album_name': 'Fresh Eyes (Grey Remix)', 'track_number': 1, 'duration_ms': 185095, 'popularity': 53, 'danceability': 0.774, 'energy': 0.643, 'loudness': -6.256, 'speechiness': 0.0449, 'acousticness': 0.288, 'instrumentalness': 0.000111, 'liveness': 0.227, 'valence': 0.573, 'tempo': 117.981}, '639nrBsmsfHMoP7wSeTPTm': {'name': 'Back Home', 'artist_id': '2oX42qP5ineK3hrhBECLmj', 'artist_name': 'Andy Grammer', 'album_name': 'Magazines Or Novels', 'track_number': 2, 'duration_ms': 199112, 'popularity': 53, 'danceability': 0.618, 'energy': 0.856, 'loudness': -6.482, 'speechiness': 0.047, 'acousticness': 0.034, 'instrumentalness': 0, 'liveness': 0.083, 'valence': 0.644, 'tempo': 99.968}, '3hfzKPRcP6uHRe6rv2sy6x': {'name': 'A New Life', 'artist_id': '7t8q7ikEtcPNtoaKAm9Vu6', 'artist_name': 'Jerry Goldsmith', 'album_name': 'First Knight Original Motion Picture Soundtrack', 'track_number': 5, 'duration_ms': 293306, 'popularity': 43, 'danceability': 0.135, 'energy': 0.0293, 'loudness': -22.418, 'speechiness': 0.0459, 'acousticness': 0.568, 'instrumentalness': 0.381, 'liveness': 0.0806, 'valence': 0.033, 'tempo': 83.702}, '1b6Spq4MiEzShOBQLtEhWe': {'name': 'Suite From Mulan', 'artist_id': '7t8q7ikEtcPNtoaKAm9Vu6', 'artist_name': 'Jerry Goldsmith', 'album_name': 'Mulan', 'track_number': 6, 'duration_ms': 426293, 'popularity': 41, 'danceability': 0.103, 'energy': 0.0972, 'loudness': -19.502, 'speechiness': 0.0385, 'acousticness': 0.8, 'instrumentalness': 0.922, 'liveness': 0.191, 'valence': 0.0836, 'tempo': 71.472}, '25AASoU47mZPdhzxeDp5gP': {'name': "Soarin' - From Soarin' Over California", 'artist_id': '7t8q7ikEtcPNtoaKAm9Vu6', 'artist_name': 'Jerry Goldsmith', 'album_name': 'Disney Classics', 'track_number': 11, 'duration_ms': 282720, 'popularity': 40, 'danceability': 0.105, 'energy': 0.423, 'loudness': -11.291, 'speechiness': 0.0337, 'acousticness': 0.586, 'instrumentalness': 0.752, 'liveness': 0.0992, 'valence': 0.0435, 'tempo': 77.237}, '5QLLhvfPdnls7G97VfJYiJ': {'name': "Mulan's Decision", 'artist_id': '7t8q7ikEtcPNtoaKAm9Vu6', 'artist_name': 'Jerry Goldsmith', 'album_name': 'Mulan', 'track_number': 8, 'duration_ms': 203080, 'popularity': 38, 'danceability': 0.179, 'energy': 0.253, 'loudness': -19.454, 'speechiness': 0.0548, 'acousticness': 0.607, 'instrumentalness': 0.882, 'liveness': 0.136, 'valence': 0.0574, 'tempo': 147.847}, '6mQlq4Fd8C1uBbnwdkkXYm': {'name': 'Blossoms', 'artist_id': '7t8q7ikEtcPNtoaKAm9Vu6', 'artist_name': 'Jerry Goldsmith', 'album_name': 'Mulan', 'track_number': 9, 'duration_ms': 387400, 'popularity': 36, 'danceability': 0.177, 'energy': 0.0812, 'loudness': -21.96, 'speechiness': 0.0385, 'acousticness': 0.743, 'instrumentalness': 0.455, 'liveness': 0.0422, 'valence': 0.0456, 'tempo': 99.512}, '6zqrAStxnMBLa0tvm3lXMP': {'name': 'Star Trek: Voyager - Main Title', 'artist_id': '7t8q7ikEtcPNtoaKAm9Vu6', 'artist_name': 'Jerry Goldsmith', 'album_name': 'Star Trek: Voyager (From the Premiere Episode Caretaker)', 'track_number': 1, 'duration_ms': 107226, 'popularity': 36, 'danceability': 0.264, 'energy': 0.227, 'loudness': -16.224, 'speechiness': 0.0313, 'acousticness': 0.714, 'instrumentalness': 0.452, 'liveness': 0.0692, 'valence': 0.138, 'tempo': 98.751}, '3wxy4wpLTdDktnlOcotayY': {'name': 'The Twilight Zone', 'artist_id': '7t8q7ikEtcPNtoaKAm9Vu6', 'artist_name': 'Jerry Goldsmith', 'album_name': 'Hawaii Five O: The 20 Greatest Tv Themes of All Time Including Batman, Mission Impossible, Star Trek, The Twilight Zone, The Flintstones, The Jetsons, And More!', 'track_number': 5, 'duration_ms': 58319, 'popularity': 36, 'danceability': 0.503, 'energy': 0.108, 'loudness': -20.553, 'speechiness': 0.0678, 'acousticness': 0.981, 'instrumentalness': 0.719, 'liveness': 0.072, 'valence': 0.0359, 'tempo': 126.967}, '3bR1GUNPSB1VVvh9atIMlO': {'name': 'Tryouts', 'artist_id': '7t8q7ikEtcPNtoaKAm9Vu6', 'artist_name': 'Jerry Goldsmith', 'album_name': 'Rudy (Original Motion Picture Soundtrack)', 'track_number': 6, 'duration_ms': 268293, 'popularity': 35, 'danceability': 0.334, 'energy': 0.224, 'loudness': -19.674, 'speechiness': 0.0317, 'acousticness': 0.768, 'instrumentalness': 0.552, 'liveness': 0.11, 'valence': 0.249, 'tempo': 60.532}, '62irSJnYNj3rKPFT6psxEV': {'name': 'Main Title', 'artist_id': '7t8q7ikEtcPNtoaKAm9Vu6', 'artist_name': 'Jerry Goldsmith', 'album_name': 'Rudy (Original Motion Picture Soundtrack)', 'track_number': 1, 'duration_ms': 216906, 'popularity': 35, 'danceability': 0.18, 'energy': 0.0975, 'loudness': -18.309, 'speechiness': 0.0407, 'acousticness': 0.88, 'instrumentalness': 0.857, 'liveness': 0.12, 'valence': 0.0568, 'tempo': 133.803}, '4D7qjCFBUSleoTGevgVZxn': {'name': 'The Burned-Out Village', 'artist_id': '7t8q7ikEtcPNtoaKAm9Vu6', 'artist_name': 'Jerry Goldsmith', 'album_name': 'Mulan', 'track_number': 11, 'duration_ms': 353320, 'popularity': 35, 'danceability': 0.129, 'energy': 0.0791, 'loudness': -25.191, 'speechiness': 0.0415, 'acousticness': 0.456, 'instrumentalness': 0.928, 'liveness': 0.144, 'valence': 0.0384, 'tempo': 93.719}}
    data.all_artists_features = {'16oZKvXb6WkQlVAjwo2Wbg': {'name': 'The Lumineers', 'top_songs': ['0W4Kpfp1w2xkY3PrV714B7', '3d8y0t70g7hw2FOWl9Z4Fm', '2ToW7zhGCrVrLU4fiKj9U1', '3ekNuTF3UpOvIZCfiejpnC', '5MMZJtHOiH1RmQSSe3DJdg', '3Hvg5tRKsQlX25wYwgMF9p', '66nJBHV6WtQI3IiU6n8fY5', '5bodDpPolC3xlame0SVcDY', '5kGBSOrKYmhRfdPBw4xD8D', '3CuscN8itbT86pQFKQMIk7']}, '6ltzsmQQbmdoHHbLZ4ZN25': {'name': 'Lord Huron', 'top_songs': ['0QZ5yyl6B6utIWkxeBDxQN', '4yyg2J2uXOjCtCyT64984C', '77x96TdWdkIia82QqU35SD', '0zCckv4tx3KzJ5GGTRbbLf', '1bqrRn1pJWowNLA5N9L6uW', '4UGoW08gaqIEWNTam1UNen', '5bE0gN3bXWh8rcWttcvMto', '3NNimGud58iHka1LHkda6D', '3SVSjlirwiGk5cepW66iBS', '5IleMdgH4wAm6MnWLLjEra']}, '4DX2G1URzfEiRg2wBfv4ub': {'name': 'Hudson Taylor', 'top_songs': ['3Htx5VpJjmftQjaC3O9Tre', '0eQBlLMUunP21spx6MeMts', '3UR1mTBpLALt8cQGzfTbRz', '1sKZ2ZXYlWmnEr8yJF1u21', '6KmnJh5FpFOJHPXAIJ6M2J', '5dSdEPRHR4c8v5fxS2F4Z6', '4cwivYcdU7K1cc8XmTvf82', '739iJdEQSZWC0IV12uoK4T', '2ATtrAE0jDv6QYJgL3CHQD', '2l0Q3cp5Ua1br9Sq1wCTRY']}, '3ZllGjNdP5pS8UFnT5Jj2x': {'name': 'Sea Wolf', 'top_songs': ['3pvTrpsqbBF3OduTOPOkii', '6xBv2Rlq9DiYeTBFno0uR5', '4cFMT3DwTYChrjBT71hqGy', '4BhEQsifqbzCdknLf52O1G', '2tJ5nxeNIFTNGSqyFvG8Ov', '26yoPdmJ5K44quYeTzxcsT', '73wwgXHDgUkF5foFy3oyuU', '5H7PvgENZHanmlrJyolIzK', '1aMiDQtbZlTAq93SsbG1wN', '2j9z9hejHzVbcRUyYM7PZ1']}, '7EQ0qTo7fWT7DPxmxtSYEc': {'name': 'Bastille', 'top_songs': ['3gbBpTdY8lnQwqxNCcf795', '1oxOiOjsi7plNOZEhoPLPj', '4Wg7VfvO7NVG57R8cSPDQG', '6ZeQp2XTOiPCePWRfCHSo5', '7BNDyzwDboNRR2wmd7GSew', '7yrx5A6zDOsd7Bn02WvbLH', '5dSFlPDHjAuYU1apyrRgqV', '2oTdiDj4AawNeeYFz8bipG', '6ezPXXacQCCz2wIzg4sEAj', '67wABU4SjBlnDHB0KiU3HL']}, '2Oboq4Pq88TcC9eUn2HSW9': {'name': 'Air Traffic Controller', 'top_songs': ['099TPpEaCSjEwysWZeTZv1', '0sF4M6WIH6yqzR8ijc8nON', '5uyRkr9cH64kAGh632Sj1T', '0iXuj965YYNsSAaRaWpBRI', '75DtJBMwCXqjLz1bXS1tVr', '0HsmznKa8h9AlqOrsBNkh4', '79uuGIdXuzA5yeSx6vNzij', '6bRu0aqwBqwoSRZpGaIL8C', '09qyIW5B7MuNUxQnDIZfVG', '0xHTTy2xujEwvjT3fqHN5t']}, '0n94vC3S9c3mb2HyNAOcjg': {'name': 'The Head and the Heart', 'top_songs': ['72zmwnbXjx9fMUjw3mbDSs', '3gvAGvbMCRvVDDp8ZaIPV5', '4Q6Kuze3wNMQRjamyBjHUR', '5Gtn8HgCAo0TUiaKKgP6us', '5bAJhDTVCWVScr5Ev4LnB2', '5m1L3o7fOfLFyw6VwumROL', '4HjEsfSpWo8gvZMr9SA3a1', '1JxNWpK9xTWKRPoYTIX4Qk', '0PHm9MrfZdEUasfd1XC0n2', '01NSrsQkOZ3PgRcGLGrOT5']}, '0YC192cP3KPCRWx8zr8MfZ': {'name': 'Hans Zimmer', 'top_songs': ['6ZFbXIJkuI1dVNWvzJzown', '18z7tK7u9DcDw85LYRR5Fe', '2H4zwjbv0D0ggDhf0E8j8j', '1elGwF4VwkwglV4nCBPJtv', '6WVRhBxRMW9fn6sRkt2gWn', '5xKVYMxOHB2XRLCUafFrz6', '1olO0IZxJUM6COX6i57RGe', '1uyB4BHbIicheenh3BgeQ3', '1PyEOnj3tdaHAcDcsqTYbv', '1TBJRUEWgRCKvcaVtojDad']}, '0OdUWJ0sBjDrqHygGUXeCF': {'name': 'Band of Horses', 'top_songs': ['4o0NjemqhmsYLIMwlcosvW', '5MYfpFJYm8WNFGssR6H2Oz', '3LeNQIGi0zwmQm8WShZB95', '1jKvrkkZxtQ7ZDiXdITOis', '5qWgGPylB0Al9IVq2HKTHE', '7sMcFdVYcwucGVtoV7r9lZ', '3MNTXYdBLLeBJjbihvTjOJ', '3wNti9PJJPrP9nF2ccsQvw', '1Z94DVkRor1ZzFPICesOUt', '6DVX4qug0tCQkdlcRT7nUf']}, '2ic4xySjQ39N7DJ0HZemeG': {'name': 'Bronze Radio Return', 'top_songs': ['5nQCeXUXtTFobB8LnOCslX', '4dI4oscajpdtjpg2dP1x28', '2GNFDAYqOl9uJEOTqYDISb', '60SV7HSk7dwgIDvVCi7Ru0', '0VrHcZMvnE3AslLG7lvmJX', '1exs6EE3ll55TUNkX3PZAA', '1nDjwLTeKD9f2jt22841U6', '5cJfRpdcXzoVEqYEaAseUZ', '1tnUlsPH9pTJKvBZ6TXI69', '0EjUR5qLuMMilc7bFbrzaa']}, '0e9H8oaYYRCKFXOVv848nt': {'name': 'Bad Books', 'top_songs': ['2kW59AS9OrpFsuXbi2939R', '61hvSzyzdXo4e2rAWmAoV0', '0YJBawdB7HwXmTg4wwWFpu', '0InFsFgdpCJuDSERgsM2hJ', '4cbHCYCabWrNz25xzH2p8w', '5pbXxljyrIYP4xIrRksjE6', '3rOcOcUJ2O9z5xEtse9d2F', '1DoxXO4w8FIu87Zztboz14', '0i1ypxjLSoirkgDTAWLAKa', '33d6D40n1ts4qmy5gBFbet']}, '4RwbDag6jWIYJnEGH6Wte9': {'name': 'Drew Holcomb & The Neighbors', 'top_songs': ['11TK5KLtLZUdKr1C549bAw', '7K36drJq6lInkW6Kkojucp', '1idjvenidUlcO6e7rsqo9P', '2f9h72MZuU0ZdEnGIfGf5H', '1M4AnTxC8qImcRSIooLd7x', '3sWSJmerUoVLaB1w8g07e5', '4yVdycF2kVA6ay8UvC1l4c', '19TXsT1N9vAoI4O2b92322', '0SkvSPb1uQH6OCQOFyA1Mz', '2qURbsi4Mds6xJ8DWanSfX']}, '6GwNGuDRNbx5XwoHQA3QiD': {'name': 'Twin Forks', 'top_songs': ['5gHR34g8eZzmDWKYmVw0Ye', '3T7KFsyl6n3UklWgfn0Lnp', '2wuFgUPBuzxYtNxsGxq5zj', '0e1COboAmkFQPNUlpo8Pya', '3tY4oBJYB44wTHQjUkP3OZ', '1JcGO7CIxm5X4pH2N56cEh', '46A0QpE6dz0LmwJPv4TekD', '5kcCAHnf84RmstfEidjtjW', '1UUfaWEtL31BDfwGat1ieE', '4B52oKoCXtye9H9LDW3wOI']}, '2gzH4rGNFJeNg13yv2uI4L': {'name': 'Jon Bryant', 'top_songs': ['1Pp7VoElB9xGZ4BeqUZ0ji', '3rQqqQef0tVevvbJwgtEM4', '6bMX6XfA8Bz47vvKxOLCRy', '23FJw5F8nipFrzkZviz5vQ', '5OeQ93epC1lutxGlmqR0AU', '431aJf5rb7MRvRK04Y1pZP', '6ZYdXHZFoumJyBH5kC2QhP', '4l6y5AjO3aFnvRr3YvqTvS', '59NpCm0lOMObumSe0soohI', '7bJUoMjysndU0HpyBM4AIi']}, '6Yuow6YoiBaVPFNjZ5BQi7': {'name': 'Green River Ordinance', 'top_songs': ['6uhkZFj3vzLY0FA9ONCM41', '2EaDYb12Pzd0fU8UmQBa4h', '4JkP8L0inEniMrIXSIj2SK', '663BdiOMzIQglSd7AaMUSN', '2BVGoBQCnuvOGdeESdvgP2', '72BNmHN1KzumgOt0nxEapE', '7KeSMKp6YTKg6sZqvH3FS8', '3td8BqcLSrW71Vi3LlhTsi', '6Xb7RS9idYr8jzuhyOCtDt', '2LaoI1GMcL2fBO4uZfmon7']}, '4BxCuXFJrSWGi1KHcVqaU4': {'name': 'Kodaline', 'top_songs': ['2PwXOevGUSkU8qaYZjgLq2', '5rZXBHUU2qz7huEckTwpqo', '0My8NPmENHrN5W7OfgZnZJ', '1VfJeju8B6qP4ZFsYuVW9U', '3weT2tgXC6sQ0AKZcj3vwH', '41Tfjvjuw8s61okfqPOV1Z', '1DIg9155AY65dpR5Lf5Vg4', '11IYMTXu5Uws1DjmUMLOcP', '16Lt4xHuWNaMX9JNzEpq9n', '3QFCL0dqEzXFIWlqWiVDJU']}, '5BvJzeQpmsdsFp4HGUYUEx': {'name': 'Vampire Weekend', 'top_songs': ['1595LW73XBxkRk2ciQOHfr', '7psPPGwhFzP3pyOcb3ivcT', '78J9MBkAoqfvyeEpQKJDzD', '104pmtTQOlmW8Zt2BipGKH', '2Ml0l8YWJLQhPrRDLpQaDM', '3t87C08isN6yw2DnWOorLm', '4eE6vZ2vOrceLq4xgz3VmG', '2gKZXeCTkQjblUQgnKF7Ow', '7q4MJZSiqPC16dbhQWxugv', '5y02IcERVgEUItFLeeZDz6']}, '0nJaMZM8paoA5HEUTUXPqi': {'name': "Bear's Den", 'top_songs': ['2v162mDpVPU2tUhKZtgjpV', '5V3c00YkpPZQSpGxi50kuu', '723paR6LrVISFCXFPf5z57', '0u3rkZ1Z5f1JIPHlLUX2Mi', '5hdyp3FQ2S1TdyFlO630CH', '6RmaaE3i8WpOzjjXwBPGLn', '2MaCvfadvDHyrttQen5kv2', '4wlTRoeZs9bMr65AmScn2L', '40YV3J6bAVimjb4yJf5ieJ', '7mLcjLqiY9rJUA3BQAywiH']}, '2JMtxA2S9SNUlqBlkDtXm6': {'name': 'The National Parks', 'top_songs': ['5ITmuvjtUUdxVQCCsaKBDx', '34fJIXIKjz8tbUwzRiD4lj', '7s8slcfStICYWbPUwf983B', '2AcN6OGdjrnvNNoLTLFSy6', '0rQDAm42zmL10iTmeQb1Hm', '5jR1sFQdmmb0wN0C8jq12F', '6Yx9yDESLdPcpytSmOmltM', '0I073R2LQQrkRNXXptWmdG', '1cYV9cRRD5GArn8jj5D6Od', '139OFhHYDAvIGbl1pxZEm3']}, '7IAFAOtc9kTYNTizhLSWM6': {'name': 'Hollow Coves', 'top_songs': ['2KCqAdd2ad0hpJc5ySoTE8', '4fPQ3n56NbnONBtlaPMa82', '08bo51XXjxoJRv3O9tuUaj', '5q3lFZYp9HLaXATffQSgcj', '6JcjrO7RInmcq8WNa0TrPn', '28sWYevC75ZrUMJ0tD4zWM', '6J2X5zPPmyDG80Nw5x7hQC']}, '5r2ltbRmBrS2c0J4oTwfGo': {'name': 'Matt Hires', 'top_songs': ['460VcG8aVLhv8KzTvULfLo', '1AZ3kCJfnyJt5O3broFxAD', '2jL97xZFlwpskNvmVIOQn0', '3mgpIfk3tDrfjyY0OoKiX2', '64uVjoozJhPeP4GVlBIFoR', '6k7HtqyhIYJMg6DgUwZc6M', '40sRbPxIlHNkDaaC4oFUIR', '5aHLzcx8t1KDMnHgU7LNRz', '1v83gmu2L9frOvrrT4UMZB', '4JUHCikVx6Fav0i9XOOegH']}, '0gadJ2b9A4SKsB1RFkBb66': {'name': 'Passenger', 'top_songs': ['6GmUVqe73u5YRfUUynZK6I', '3V2pTc1zYbZGzHlyd3YtlH', '1RNyz1P8eyL5BsCzooCguk', '3eeIdvZqXaffY0yVRgbGfQ', '4tzAf07GCR6DlycQkUKlgN', '6nd9ZMftN6tfm2YAoUvK7f', '1xUOevQqJdG7ERSLFByT7v', '0IknWdl7UzA71oKRQneQ41', '10D6VJLgBNPJLDCGJH8NKM', '17VHkJ5zeQBRHL3i0J0jT8']}, '5nCi3BB41mBaMH9gfr6Su0': {'name': 'fun.', 'top_songs': ['6t6oULCRS6hnI7rm0h5gwl', '7a86XRg84qjasly9f6bPSD', '7gpy7sfWPNuOKmUNs3XQYE', '53c9tTEHXWL5GkYNalbXZ3', '4orHVYvdG5v4G4bmp2Lwdg', '5tbz0VnVwfF3jubvjDGdHo', '1Y5wYXgX9dHwSKZdQNHEhV', '5QbQ5iAebksB5Wj5BPazNX', '1TQyRzRnGJflBhUHAwtk1x', '3xsMa7CA11iRjhmIdEy2N6']}, '0BvkDsjIUla7X0k6CSWh1I': {'name': 'Luke Bryan', 'top_songs': ['2gYiCTytrSRtuaHP1Nac6u', '03fT3OHB9KyMtGMt2zwqCT', '0dbzWSYpMcRtwjI1S7Pkql', '5XFu5S1vBY7sNHlheCapOz', '5HGibWoxnkYSkl6mHmAlOE', '0yD66650JxhqKbW76C2qCo', '3b7CDTKB0SRTmQ6ytYi5vZ', '6qoH2pKeEibNUG1pnJIjmZ', '5g15o2Sm55Hn9ShK5yEXgp', '0cV4xwUA4ue2deqq4CZFko']}, '3zt4I5TLIb0Z9RigaiHe5G': {'name': 'Cereus Bright', 'top_songs': ['32yiDCLJUdqYoaDR46z9gD', '0GqfyQKzlUvzfL6rF7LcVg', '38h1mljyMeayECUCx95GPh', '5pQ1e9moalBVW4IbUBZ1Rx', '06WH4YIbuVcRNEQdiYIj3U', '2UZG2fnQRvm7mLblQDwrTl', '240SHxowlaqE1jvVe6QEgA', '3IHGv6PVQ6qmLa6OML44Xa', '5cEACMcaVwmbFTaG8cjYki', '1hvuxAwZwZDCsB8HnJ06bu']}, '3cR4rhS2hBWqI7rJEBacvN': {'name': 'Leslie Odom Jr.', 'top_songs': ['4TTV7EcfroSLWzXRY6gLv6', '4cxvludVmQxryrnx1m9FqL', '71X7bPDljJHrmEGYCe7kQ8', '6dr7ekfhlbquvsVY8D7gyk', '7EqpEBPOohgk7NnKvBGFWo', '7m9XR7FquXLP1FewdAcNS9', '7qfoq1JFKBUEIvhqOHzuqX', '3nJYcY9yvKP8Oi2Ml8brXt', '2sEq2rC3ynYsT49x7utWnd', '2yBMVrq96wb9OHbMdBs0lF']}, '5schNIzWdI9gJ1QRK8SBnc': {'name': 'Ben Howard', 'top_songs': ['2uhEKg8kIzpdvz4gyy6x8W', '3CAX47TnPqTujLIQTw8nwI', '5fpEDGQX0Ah3utGnFYulQZ', '7gYwIAHB6VxzLJFSZMMv8i', '4qyfir5Yr7nfo05g6cyFMT', '2Viw81MZJPsOjODAz4A5nW', '5RySo0AAUR0reTHSCvb6HC', '6yPuQr6vjZ7tJ4oq1PEXle', '4dr5sJ1p6mdNpK3fIUz8vR', '2omeRL5Clxg3y8g2kv2enS']}, '0GklSybv01PPje5GlXFq2i': {'name': 'Jared & The Mill', 'top_songs': ['2hRBqxdkYuFySfyEkcsPOp', '1Gn1Yzgdk0RFq3H0lePlMB', '2qNIaXkc0wlR7IIN5l7KtL', '6ewlMqeK1LuFOmNG9x7tma', '2tux1s5FVabQQKpz7GEXbI', '5vqjiKUSu9Y9GmUkiUXrj7', '1T0uOwBt4KRVOC1cgbmlNa', '5dKKgYqiuLLC5xG8Sm9kVr', '5kYFOIJ1CUnYJhj9JAqQHF', '39EWzCLWBfkwkZKmJSakjX']}, '4dpARuHxo51G3z768sgnrY': {'name': 'Adele', 'top_songs': ['4vb4mFvYsr2h6enhjJsq9Y', '4kflIGfjdZJW4ot2ioixTB', '4BHzQ9C00ceJxfG16AlNWb', '7rPLZ8Krm6CZIbraFUlnWZ', '7IWkJwX9C0J7tHurTD7ViL', '4sPmO7WMQUAf45kwMOtONw', '2GblQ918RbkOs4Yo1Rpkcj', '3CKCZ9pfwAfoMZlMncA1Nc', '1wMALZpuqAy7amQsFBWQ8m', '7GgQi7JTG4b6J4iEF4RTjF']}, '7z5WFjZAIYejWy0NI5lv4T': {'name': 'Dan + Shay', 'top_songs': ['4n0xztUAbHPUV8G3NQvF30', '0lQJBl9YEsoMtE8D4yTE9g', '4W38RXuQNuoTSwVsQA1OGC', '16DRIwIBIgZdAgpp0vLh5q', '5xdFitc41cUXrRtR5dzwg5', '2IOvJJrN6RajoMOd9TyGra', '7ongSdLv28Z27WeCrzZXwB', '4w9LtJn74XQhsHD1zAHnzY', '4RBmXmZKf76IyNiPzebI55', '2pLw1tu9QEGeidJKBZRaZI']}, '3Lw97gGh8bp1MftsYmwJHG': {'name': 'Luke Sital-Singh', 'top_songs': ['6uFSls1Xd3U6Kt8yj3zVR0', '64qdx3vEpshNqch4EC5GMV', '6AmFUEceHzykYXeFAms8Ds', '67UAImj4r5ZfCwhpsTvn5l', '7cKQE2K6ggLByzlIMtCxzu', '2bzSwMHkc8XgTpSghMpYFB', '4vRuPvw2HQi1ukIaKu107k', '35D0xUf06Tu3yr1sqr4Vsv', '6KtizyqyvJ10bEbm1qNtPa', '4jMgRHnKEEHDEBBxU3PBMB']}, '6y8XlgIV8BLlIg1tT1R10i': {'name': 'Old Dominion', 'top_songs': ['7px4t7HGiuMUvFkEOpZEwp', '1JupdHkhDzE4XtrFFe9w6o', '5ZManJDV3CexO66nRCkdiV', '7I5fYc4qKJddht8Ozhqqdx', '6arLnfArtdWKOcCYzDd4rS', '74uXfGRDayyx7UIV1irrhK', '1E1LaXgZRkBOljpGXtlR7B', '3nC688MXGnFDAcL3lU1Ray', '5dTTvqEs42JMJv98b4SaoE', '6CCV2biTOmU2wRBTJzapxX']}, '6roFdX1y5BYSbp60OTJWMd': {'name': 'Tim McGraw', 'top_songs': ['6LIWwxXoHqm7AuOByjFyd2', '4wFUdSCer8bdQsrp1M90sa', '4Pn0JlCUusD2QHjADuOzuV', '7B1QliUMZv7gSTUGAfMRRD', '2op0kDNARK2VHWHntEeH4g', '2ZekuYUoEIBrUwHOY0gcgB', '3LbvNFkqDTrE1liGMmZBDL', '4pdoeoOQSu6DNznlfNc5FP', '503sFkc8Y2eyGnM6cu8kHm', '6leiB1fEsTnVCuPiielde5']}, '14r9dR01KeBLFfylVSKCZQ': {'name': 'Damien Rice', 'top_songs': ['08YEGpKt2LHJ0URCXKHEie', '4B2lJinAkeNLSJjcq3dg8Q', '3BFXgZr628FqwDP3pQCgvk', '5mb6SzBnxv1ywFSH9V3uxd', '7FCYixd46BlSiO2memrsPo', '6R0BVRF95vCERjhCabl17q', '4CVP2pvqUxH9tExsHJnzV9', '7r2az72yWEXzlrQEMJjcsz', '4bdjQvuoDBAsxdUPmEIltt', '3AkxSspcYOvhWTkaMvqyaD']}, '1UTPBmNbXNTittyMJrNkvw': {'name': 'Blake Shelton', 'top_songs': ['5sjIhQzNljMVrDklI91ezp', '0c4ICGb0jvszKj3KPR59JU', '0p1HtkrNYxv0iDfEKwXSTp', '1N7qGCKRRnvjoy8MGyHgpS', '0gY2iq0xJPRoIB1PScKSw4', '1zvQt99d5oTkEQLmSoO1yu', '6eJBihAzTWRxvvjJWuRQXM', '39FwE8edwuyiaa4PrGBkP7', '3JffB4CABj9lA0NC63kbCp', '5yIiXdLRE85OBiQmCaUenq']}, '4aXXDj9aZnlshx7mzj3W1N': {'name': 'Lin-Manuel Miranda', 'top_songs': ['6YH2r9NyEJTjlRmKOCvxgJ', '4TTV7EcfroSLWzXRY6gLv6', '4cxvludVmQxryrnx1m9FqL', '6dr7ekfhlbquvsVY8D7gyk', '7qfoq1JFKBUEIvhqOHzuqX', '3nJYcY9yvKP8Oi2Ml8brXt', '3HAh7a08YVxEyb8BM645bU', '0NJWhm3hUwIZSy5s0TGJ8q', '2G9lekfCh83S0lt2yfffBz', '2sEq2rC3ynYsT49x7utWnd']}, '5sQqZtsAbXAoAnvA8iN9kN': {'name': 'High Valley', 'top_songs': ['5o9LteJdhkA3ndUDz4JVfV', '2p2cCrOaNrIOLk5ArtlHy6', '1zMGZrrUG26o0pkfOPfHbo', '2dieIRxavIVIC0ZZYNZB5o', '6V647zWTLg2LcfzPzFljZA', '4JqSjvWYsFIHsnpwSZ0f8W', '3EV2ZdIDTcZ551RqIRspSw', '2uTzK6JPWHlsE8ekkwOFKF', '1zlFtrl1qpymPGtSQqMsJ9', '5misaMDzoPWVxvjBTVwx7v']}, '71jzN72g8qWMCMkWC5p1Z0': {'name': 'Alexandre Desplat', 'top_songs': ['0o9ivTBX7mjTnaUYF4Gk6t', '3GiE1hcocpQIEf1gC7fv2o', '2ISjP2XebyGSoKSM6Cnb0m', '0pyCqpKtJFbVvkZ2ATLT2C', '3eoeShZGzmkzqnIpHZfHPn', '5RKqgLYBUZC4IZrlGH9RuD', '3jXFtmb3OU9rhytuuT1VT6', '6WoCCsRd3ILkGcLm0C2XL8', '7wCacjnlvU9ZN3uBNTKycs', '3l1bpC1lrAZ911bplYydPb']}, '44LPOpECjnIlnwH91wo2ir': {'name': 'All Sons & Daughters', 'top_songs': ['1Hv54MWloXiAZDam1ez840', '13p3U002Sv8z722mFjTuWi', '23aRQxzv8AbUOAV4czlNmp', '23AX1TW2CCpmqXtktvYe42', '4PYOh644yKjYyvyVUHqcof', '19mFt7CznVnV5DH56ZoBTn', '5UgGtoBzu4mmslDkcbLduT', '51sy2ohrjo0E2O1lhJw64G', '7f6YUhXC4jknHbvhbqK4U4', '1YJ8qjJQpTZjQZVR2hgWfx']}, '5o206eFLx38glA2bb4zqIU': {'name': 'Bright Eyes', 'top_songs': ['5OiaAaIMYlCZONyDBxqk4G', '4PMvRfhHAx5j6Bb3XsFLoq', '6QSmeY9pNWnE0fAUrXmYC7', '558BHSecDFS85E2L2aKzP8', '7C4LTWRsikDhkxXrgc29q0', '6588w3GdDxmdtLMLuwf1tO', '1PW6GA54DjaQDwKU4ATCDE', '20Lo9M6nfdIAWrzPPV4yY0', '1fPLarHjgMC9QlsHfPijbr', '78aRLjDiQx6jo0GVW7aDA4']}, '7D5oTJSXSHf51auG0106CQ': {'name': 'Benjamin Francis Leftwich', 'top_songs': ['2im8Pxe6JuPf6dhpxhl2nX', '4gSYPXqENGdaJiwm6W0hkQ', '4sVnlrSGaRwnBaj35C2wXu', '2cEBG31c2Y7mfRlLY8g1ah', '2PLh0v3da9bVrRE6o8AWT8', '5FyxzFb5qOTtl9fCMFT20D', '3tF1VBq5c91U1aN2aWrjfP', '4bvtfm8XL26qmM2vliZfMP', '4E8Zv4wFRUsFJtpnsoT01V', '7IJK1KdKnLNl9fv21eh7h2']}, '0u2FHSq3ln94y5Q57xazwf': {'name': 'Keith Urban', 'top_songs': ['6wycnu8FWXsj68ig7BEot9', '5OUSPcqhYTOzpbXzoEvKim', '13wYXGimJ5fANFu0y2pqG1', '0b9djfiuDIMw1zKH6gV74g', '72f7jNxopSGvbx3M35i3Zl', '0lZxd99ZIjA0zUdQAY3FXr', '3MFV4DgrAOXz6KURPQxRj9', '61hmCqoIlTJjcVMMLhcH5n', '5vCgOg9VqRaAUbnflCO6P3', '7zHKBxCMAc9Qt6OrIaUmyi']}, '6yJCxee7QumYr820xdIsjo': {'name': 'Zac Brown Band', 'top_songs': ['4dGJf1SER1T6ooX46vwzRB', '31lhygAGEsvwcUvhakP6yY', '1yEwEiTpsaPhQi9lb5EVV4', '1qwnPVOIJjAFfCc40Etb1D', '5kjyiH6but1t2UDXq15aeS', '69XcvSymPaTke2Qb6f3W6P', '0vcfOQOvTCv8ckiRs8Xc1Z', '1M2l9ReoabUnvl6Y8jLUe7', '5PNcJn4oFNvlRfrZBHfqWh', '71zbcnCMLpQ8SPSv6sFlqF']}, '0YrtvWJMgSdVrk3SfNjTbx': {'name': 'Death Cab for Cutie', 'top_songs': ['3kZC0ZmFWrEHdUCmUqlvgZ', '59FC22eN2Syt9bbv2d6393', '5yc59J3MR3tVDPTOgwgRI5', '7DDRPKLKFIvDbNSQmnz19Y', '6wNCdMW82LwJgFrnGqLhpJ', '77vYwoC7e3pVoPq8BA9CuL', '7C1p70Zs3pBZEQGeWMF8sS', '1crbFuCkGL4kXnAGd63RXq', '4mCF3EBgGPSqmEm205KBAV', '7DkTneByAopqOjXFG6XlZK']}, '2eam0iDomRHGBypaDQLwWI': {'name': 'Bleachers', 'top_songs': ['0d3BJRrklQ6sTfbmrojuZI', '5L95vS64rG1YMIFm1hLjyZ', '1BwhFXqoIsePt21WyWIttb', '5li3FHS5s9V3l4xWsUcmQa', '7tY8crx0ZaIS4yScJcKaiU', '6YArGkJUr82ehzRFa2YaRK', '3Ao4MeZQu5BA3H3K2QeBl2', '7pK4jm4HiNaYVzL2zbQSoG', '06zKjN3gV8JDNQVz9HwQ3C', '0DdJoUPb3VXOZ9zl0vAwHn']}, '2txHhyCwHjUEpJjWrEyqyX': {'name': 'Tom Odell', 'top_songs': ['7otCGmgp9h4CsR2LhwB6gt', '5snyhxAh55A2wlNRH7VVZJ', '5baXzOMmD0sf26hayRqfqI', '1xVF9wZZ87uAz0bw6jT4sH', '1rGxG6Y5OgmSwGPRPJv9Q4', '4JBNKQg27FoumUSo96r2pk', '1DxjoJ2w0K9zQ8KgU9rXhr', '0rhJ30qQSus6Ckn3hKZ6Hr', '3B61es35RhmjeZgFuG6VV2', '23UCOmWmenFhxFQG71tTKL']}, '34482S5nfxR441wcnVfrHi': {'name': 'Noah Gundersen', 'top_songs': ['57FqmzNGTziRPCyuqaUrHo', '4EC81x7yH6ncvo3Fox53C8', '2CtHCWOxvOL33wm2OyHOtj', '0FvKy8AbNlEniYbmoykuBN', '1KkFmmhPyIwPDM3tzWgqT8', '4DuC9BznEnlwTwHQhWLzNt', '25eV7YkYtIohk3vAO9kseu', '2Pqp8fhzDlRWevT5XchSUd', '7J1AXo68jW9zCxUfPKYqyI', '2EC80pl6LRaWTpErarvN5C']}, '3D1IyJznpDnWnnFrzjuWnh': {'name': 'Ivan & Alyosha', 'top_songs': ['4ngv7whSPSAwD8ZP3zMHsd', '55FRkhs8VGcBiidGnUuyud', '6GZEEoTST2iZcU52LfVDHZ', '0El2kYoxWlzQKx0BkWSfJC', '3z1aYA2vuSXq1wnkcO6DoA', '6MhtBW8JT9gAghWDpysJvu', '09H2Zbr1089h1ZDIyfZczq', '59LQFxDuey8k7A4IEtbyPB', '6tI9ywNUbWSs9PTdVkPonr', '1qhlfTipmALXorAyNHoEiH']}, '5euJsEvfrlfhYDorMR40OF': {'name': 'Milo Greene', 'top_songs': ['08cXy6KUizaAelYXtcew3w', '2Uj2BjZXVv9WvYFEVl8TDi', '2Rn0EeHNgRawztx5KCGpwK', '3yaFjAn6FwqgbuPMpV7Tix', '70ST10v9DBXmKdVjMhSSUh', '4gvAocL5C5UKJcJ2kEJlka', '1GHozXj5A9Gttz3jI3bF8j', '0RMH1oSrSU8VDBZHLNHASU', '480QORmTRo360UBGlx1YFc', '4W7s1XhCOGkzQYolfI4T2Z']}, '6tK77FerjTNLS5EEhI0zGM': {'name': 'The Brevet', 'top_songs': ['6PRr6dzkiaLTGbkLSdQCvL', '5narWdetexXv1ucBDuZJfO', '20mKWH9u1dAVvHHX0ssZMq', '4XHSgX7Y1jsNfp2leylP5W', '4QMYdLsnDax4hn6FBojILG', '4YyhCfbXfeVrEjtj5LCO09', '3k6FJ3WdPib8KQ65wEra0F', '60WU0pqbwheu1iS90EZN6z', '1oyWYzwnbyvz36UXcc1msE', '6tJX7dQ0IEyKLVMDnedMNQ']}, '6DIS6PRrLS3wbnZsf7vYic': {'name': 'WALK THE MOON', 'top_songs': ['4kbj5MwxO1bq9wjT5g9HaA', '3e0yTP5trHBBVvV32jwXqF', '76EeScTnI2sCjDY0SfEoSb', '44psOy0D0SP8rcIiUgKgBs', '3Xzog9enTvbsc0G7G9M58D', '3RRRDZig4RNJhVGfwwOOFZ', '3JxaZPq4UjkOaxnpyMUtAC', '7eMpW9I1ZpVs6VQ90naDBh', '2CdNHP8DJ5tfbRoIRdcTeE', '4xTMKnLtz1PVfZRElleujx']}, '196lKsA13K3keVXMDFK66q': {'name': 'The Avett Brothers', 'top_songs': ['7CEV9VwA8XO9wwxTXgYKvY', '6XMYnm4OTEysN8blzqiCL9', '19n9s9SfnLtwPEODqk8KCT', '7Kho44itYaCQZvZQVV2SLW', '711WfDztCZpnmJg7Uvwod3', '0DcBU93zLXGRdPPbUnP1iS', '3h5AZDf5z7D18plaLtHTfi', '4agZCOTdZDD4r33mPPDy8b', '1nMlHxWuPc5P9Y5nGvenlj', '7huuoVBXjskB8kLgdRU9zu']}, '0MASTEXfUt3bpiyGOoEaur': {'name': 'Parker Millsap', 'top_songs': ['4Eq0F51L7foy3hFvz0zQNp', '70wMwfp8wAqaxip65R8Hkf', '2Yf3wwS48rkAoBRXNJ34kz', '0CjojcaWJEq0HYyxpkXlzu', '0FbKvqTBo2TsSzhT5ohFI2', '7Lhc9rgUp3cwfwEgo21kZi', '4zm37YNRt5XrbFOTPk0jBp', '76Fc9ApTagfE0DFLFdnMj1', '2necAV33vY9L5x2SUXYZeY', '1mTrfm7XOVkmVBaTaUJIN9']}, '0CDUUM6KNRvgBFYIbWxJwV': {'name': 'Dawes', 'top_songs': ['2SYvX2G6D5SD6BpijIOBpG', '0kzfqqvipRSBQchrB3xX8D', '4zF51hAnzL84vE8unhEH5N', '0HOvoZ4m0aJp6vY4fVrI51', '23Q4sMxgEKRXDMi62xPP5R', '5UDEGEbvqFwrzT2P2PcJ27', '5czb6N8T50aNnJoKWQRgQo', '2V5tSSOgNs1L6hmVnNoaUZ', '08NjEcoCYhb72r26U3wh7X', '1SwrPOu6BfuyzNTn7iA3j1']}, '3GjVVVcFmUgEJEAAsbGkf4': {'name': 'Trampled By Turtles', 'top_songs': ['1QesQ27kCWYTYuXJi8SApS', '5H06kjjKa1Oz8BZcGeplel', '2dJrn376fJPUCj1f4txnRQ', '6AKYhRh9Oz1nzscR5kZS7T', '7z6pDIQFv510mRKfyEjHR1', '6pr0vBUsNzV3ayyTTDhn9m', '4SI6ia4b6L5J1n6k42WeHC', '5dyqyS9nuV9LmTHItuQO7l', '6nQ5z2EDrltb8MZs3HhfgL', '3lBzK00y8cKvFA1oDOcw0E']}, '4DBi4EYXgiqbkxvWUXUzMi': {'name': 'Old Crow Medicine Show', 'top_songs': ['359krpyCKcFF8SFvqWES9L', '7mfn1O2YQifrW5nZhAhCGL', '0EnoW6gDUgYowcfek2GnWR', '1HJrJjCNgviyQYC6rYoBYS', '3kp1DqoICwe4Vhf2zVzpUW', '5hF5VODEuBVFNTVu7j3NrL', '7m1TJgrWNy72WgKmK51QgJ', '1KYQoFEiIqPYHLeuXWwUmX', '2mKMIVcKPczPULJF13Ztvo', '0xEaA9gekxEFwoDjX8dq6c']}, '0XHM5ZNJDU8e4CfbWMeSzC': {'name': 'Roo Panes', 'top_songs': ['2Cx61IzUXPJyhv3GzGtsZ3', '4m9DSdV4XU49dDJ8yhaMMv', '61X18xzfxAYZGouAXm4ISi', '5hPWh1uz7UGnbKgP5iTy5q', '1IycYHHYjKgxvB8AHCdu7O', '1fOtFSwFOdv4vSInE3Ep2Y', '3ZrxDW8SSPZkGPwDggS9zh', '3QOM7UY7jnHqutxr1ptZzJ', '1wmMA2Uh2f74yCYgH6IqYh', '2PYuLwC2eTncWexIYVoF2X']}, '3Fe3pszR2t4TOBVz41B1WR': {'name': 'The Oh Hellos', 'top_songs': ['2c62Xf5Po1YSa1N6LOjPHy', '2dtcNplc1W8GFAo9LPzLri', '1TKygFgEQtUaSTnNPnl6o9', '0TgaaBAEf84VqvdTshIdPw', '3rhyMywAzKIALXc1uQYB1d', '3CiPunzgvlLdvJj0bUErJd', '7xwOCSKispEfJOlZHW08R2', '6afpT3wW8NdIe7nimRNRd0', '5kqyZy0WrBpSoLPy7ojjzx', '0sZfwxyHuEOsKJOiXcjHU7']}, '3sva1UjOJOx6cGISZOpItl': {'name': 'The Collection', 'top_songs': ['7agKHhiI7ubqzf6sgWkNjp', '1x9cEmDslp7wH52UuLGyj3', '7I0vmekPKKMmWW14zDFhIF', '6Qjb563OGlWPrVWIqowvpD', '5bfa4ucJ3vozYtrvtTtfQA', '7pJqpTz3eTq0aJIyoLxamG', '18zzR5w624JxWnSZEKeoHA', '0c4uFfnflVhAXSXLthHJXb', '0fKeNF09yFaOguCSE9HrNa', '6IUVyMsCzAnHSSNFkLzmya']}, '1fFdRZK1GDGXL7vRxxUWLH': {'name': 'The Hunts', 'top_songs': ['0BGM5wPT4L0KNKrf3WsMkn', '0TD0ydYJuFPEaqshquDEpw', '6q1iHfSRuT2rNbaeOtcUTT', '0c4qRoM7FMFo6iguuIlVIJ', '0DSaUCe6GTuDYeevMJ5uBX', '0du9w3e8Xkrbl2b7SyZ6Ma', '3zQX4mlMtH5fUdJXcArLXt', '1xnVivWRSk3ihIc9eskMEy', '6f223VXzVbvFAivhYptz9f', '43168z8wHwMiHtNUvE73cD']}, '3PMXHMqW4MNj8usJ0fxAlj': {'name': 'Hey Marseilles', 'top_songs': ['6JrhK1EuBS9EKpFmcuhrp1', '3f8DQVBBB3nQVuOdDALRgX', '5RLSjCJB9pQ3yQk2YTJufZ', '6To2fU3EazmMNDR9hwNywO', '6OMgG0xTvMS2o4dXM4WZrE', '6nzNsWi3vJRiTAY7oqqpbm', '17CkR7hqDVTVIRopJAZ3Rf', '5qPU3nfW5ajPlp9RBTD1rm', '141UQ2wXw3PswOHt4U5Kh7', '5y6Nr0CiN1Uf1uIfdHtWuX']}, '6J7rw7NELJUCThPbAfyLIE': {'name': 'The Civil Wars', 'top_songs': ['3wsZYuHJrk3lssa7V7jvye', '4zzi2eD2cEPpQ3a307mPPj', '5P6ZBMWS66FVo6deJaDdHy', '6tZAbv5JEsfqjTpkBOrLje', '0iTqedrMdiwnUXKiUjtxAl', '4qoD4IJbbir3hsAu4IowiG', '2P84QNQFhSoexVt5jEsfmd', '2ZheGCM31EbCwUfGs0WJB1', '4mm4V9uS6AOuWBG0f65HH9', '4fwiUXTml7O24fL34JxFI7']}, '4iiQabGKtS2RtTKpVkrVTw': {'name': 'Smallpools', 'top_songs': ['6lOsjTvgGL08uRf2nKrSed', '6cMswWRv4lAU3mh5lclgCc', '0qnOjNW04qpcgXqD9dwru2', '0hxy93CbIX7Hd5WXaVjx5R', '6WSJ5SmQubgYOXM66Eo9va', '0m8z88MqUfbstTIUMK2wfZ', '0UUl3PYC5aSdKrYBkNrN6C', '2uV2tyFZ0Eex2Lsc8shIfN', '23kzZbGbs51X03t9Vy5GMa', '6ZtlUSe5Vt1ev5767zg46s']}, '44BkC9lJfLmhcRB4NV7Z38': {'name': 'Tim Myers', 'top_songs': ['1sPUneI4q4ZChaPXXNpfWa', '6BjPiZI6q7r4qXpOtYWOEe', '19nbrRzEM0ldFwbqO0KsZI', '0vmU1XjtNWBWJEpHG0GThM', '344PGLp8wbKibf4zmnD4Gt', '6tuzzG8BsAI9SaIxyMPs3X', '0eaBGg1GCNiCtMTuFVM1rn', '2hdYsU1vooYiQmrgNJslrE', '5Oa6SAXiYPS4BffLcAdG46', '6xWGardFQzilB1HVxIsgrp']}, '6pBNfggcZZDCmb0p92OnGn': {'name': 'Chase Rice', 'top_songs': ['6C2XDnr9B6obGMVhHS1Nmo', '1CoOHJAHtKEDnUBrp3nKAB', '3rh2f6nqswpfDN3Ef6Bi5J', '1MTEImRXVeL8VTDSDbgW6V', '6LcPSBPSYRTMG7brqZQ7aq', '6EdSZmWCQJfO8T66x9VCID', '4LGlMGHwJGY8tUXQfZWUzm', '1ZT7y9KbzTwuyT51ch0jt0', '3nd43CEbT11MUQVIh7GGiL', '33ntke7makdcaGe5DsmcLi']}, '1a6tqLJPUs4DBAnNUZkr2O': {'name': 'Steep Canyon Rangers', 'top_songs': ['7xsjI11alpcfweV1y75dSs', '26iGc8sFIpHUEpLkjtBIBF', '45or5lcxKF2pgrUKDqlYQY', '3FJewohG3cojZjIwKhpuMQ', '2AiTuukRNgoUeCyWxKo7wI', '7JY0idqjJLLOCpEMNkzuKH', '2ATQkGLIx2ncMKG54jCM9M', '7rQZBa7ftCF9cNsLkl9ROk', '5VUTiGp6CYP024gcbu4uE8', '5kxWGm7jRZwV5Ld0VpBCD8']}, '5EM6xJN2QNk0cL7EEm9HR9': {'name': 'Radical Face', 'top_songs': ['13PUJCvdTSCT1dn70tlGdm', '0r7EiYTNNP0WCzcaefN6TZ', '1L4GiwqpSuuLKORJWHVNxc', '0ZRyqCgW7rM17pfINuIGW3', '1gOTLXloeEsw7cbARwnEvs', '0qCqz7oecY7QqS8lhW62XI', '0nNFNjGK1xF5y1j5jlw4EK', '28A1RDcLuedRL5VtOzM7ee', '4KMZqHXHjBajYRVNX5aAJn', '4XoDdGtXBIkDLaGT0t8RbI']}, '3mIj9lX2MWuHmhNCA7LSCW': {'name': 'The 1975', 'top_songs': ['5hc71nKsUgtwQ3z52KEKQk', '316r1KLN0bcmpr7TZcMCXT', '44Ljlpy44mHvLJxcYUvTK0', '5vgdeMt4uKUN2BeltZjoDh', '6VKX7rGnHoHJ4bECP12OOG', '5hRzAbY2AAO258hL6oqsqO', '2zyz614fJRrqQXW1q0sY1c', '4p1pxmqtPtPHqWbOd2RgXu', '51cd3bzVmLAjlnsSZn4ecW', '2J3ajGI1sVj9wnqThJHwPS']}, '6P9fFbQ875B2bnmdiYwN9A': {'name': 'Kings Kaleidoscope', 'top_songs': ['3TjbpRjtWYHFwigdLMr8Zl', '1g5b5gNTAh3dsSWZILzczm', '0X6zo3gCOaS6ccC7IT9Emf', '1DdYWvSA2lJbYqzpm3moC6', '2Nuh1lfaz61r49sXhD4Cpr', '6zSofKqVraFZt5Utpv83AE', '3JhCq2r9PbbWYdQ1qpoKEX', '3T1CKrdMfrXJC5VXC19LUm', '4F1mJebZX8v8Oi1Zl0CRdl', '3XBrhebJSAGEhrV5NNg9ia']}, '7x8nK0m0cP2ksQf0mjWdPS': {'name': 'Dierks Bentley', 'top_songs': ['2lFtnEmkIPm2ClN55e2chV', '5HJId22hZ2IvFnvNSy6ZbE', '5CG9Ps5ynNjpKJHmwc95pa', '1soxUgYIZb1qx1c7o1Lc7z', '0HccAcPMNevr8ERJCWlFk3', '2WKCH4ISejDV9ad7iPp5XU', '0r8iDf65NHgFgZOGLwj5r8', '4QJ58lQahpEtD7622moUxS', '01e8dGbulrphX8j3fZDQYk', '2sE61ZmvYH8wiOx5jygkHH']}, '3grHWM9bx2E9vwJCdlRv9O': {'name': 'Kenny Chesney', 'top_songs': ['355DF4qq7l3Lc6EnPF0b5j', '3mtGoEJPXSFO2Lz5pw45ya', '1dgWTMoHwTUnQhOQ8SR5fV', '3pkzJjJXfdDjhpXx639MIH', '6BCrbWBpb8d6KWmEqZ41tr', '1t2hJFgJyUPD2crOafMUEk', '6wfTb2he5ANMQSFnlamnyi', '5cj52tdE99xnvdZGKWmKIW', '1Lh8n5owE0h0hgqWfqtvuD', '3cE5ltZFHmBpiS77itKaOM']}, '63knPlGzLHTNDf1J78Fvte': {'name': 'The Devil Makes Three', 'top_songs': ['7FqrsV0vBwNiQNQI6jfzni', '5fuON606j1hkPGJhFMwerY', '5oNyskwKyRceUQaYzmWobx', '191qPeOpllZfaApp35HXK3', '3ALem2cU9XKuWT4CLAeDMK', '33GZ5QfNMeVVOmZABeb6Px', '5pnjFG0695iwvR9qsnfTSk', '7jS3s8sv5ytlo7xgBGyCiL', '0eAcBwrfgCjdTilx8oNQ8v', '5dZFvwgWR7Rww53oQAZlbS']}, '3b8QkneNDz4JHKKKlLgYZg': {'name': 'Florida Georgia Line', 'top_songs': ['498ZVInMGDkmmNVpSWqHiZ', '0BCy325UZyR9z0t0uxwn2N', '4VFE6ZNqa8jHAmbYICoAFg', '2TR7A4ulH9R1PNwMyd8o8U', '46ZfPS5VpSQVU5gb82hg3K', '6IFPfV8PNSYOmufzQ95hmm', '0i5el041vd6nxrGEU8QRxy', '5T6DM9qjjngWnukcw0svkX', '6s9ICeczYOfbHHIaSMq9jd', '5CXnIPD6rTjszYYQm6fY2P']}, '3gd8FJtBJtkRxdfbTu19U2': {'name': 'Mumford & Sons', 'top_songs': ['3pLTOP0G0etiWUknFoRpsr', '2JHBMVs8E7bJJBLkXpKgHn', '2BBkIgdXLv5vyp1DR0wpQl', '4A57CXs3jAmyNTMAwWaV53', '5DVKKqwLGjvK9ojz3zLjB7', '3e6s8Z4MRSNgvNhVvpuUiw', '4PgJ0NUYaDDh659TW5mWBK', '5VwKEmrYEN5eAPvWqrrKS2', '2QulT0LDnhH7011gzjFvLS', '4aHzQbalMnDm04AAW5K4se']}, '53XhwfbYqKCa1cC15pYq2q': {'name': 'Imagine Dragons', 'top_songs': ['05KfyCEE6otdlT1pp2VIjP', '4dASQiO1Eoo3RJvt74FtXB', '4G8gkOterJn0Ywt6uhqbhp', '3LlAyCYU26dvFZBDUIMb7a', '4XLm8FNvaTlmTAZmSrrV82', '6KuHjfXHkfnIjdmcIvt9r0', '1lgN0A2Vki2FTON5PYq42m', '6BtmXhTJMM9sBTHeYYASGz', '4kDTvLhGF29gFsqceuxBSC', '3Dbgo1HE3DErIBNDIO4Hyd']}, '11Y54BxlxC3UIAUkU2eadQ': {'name': 'Rend Collective', 'top_songs': ['0yqWOXyvDtC2ol1Idz8r8J', '5AcdaSVQfLcUKMaqchfBie', '18q8W11QNDEfhYIxwypTQK', '4upaAELySMLYyrMyaBl3Bb', '5or2hHXDa6Y5gYYRWFUQCy', '5Gfv5Mt5HiPTayAgGanuI2', '3DgwAwHOyxfpQUuuMzvzUN', '2EeCxglAQ4XK0IwuqjvRwj', '7Dwb6OZi0EtRM8hBa10Uqz', '1uCVpUO24T2ukRcU0TCfFu']}, '0OcclcP5o8VKH2TRqSY2A7': {'name': 'Howard Shore', 'top_songs': ['644es5aYPJghtZLjM1rmSP', '1ykbtFnlIjmIFnZ8j6wg6i', '3Knohqfb9jeYzL6wMZiWLM', '1lIcdDpGlc2mO2LYA0f5KM', '1TQKEwq4y9SkNciJuisE1m', '6HYCOHzY2xR4W2dOokH3ed', '0VfcYOujgf9JDAgwlgu1qm', '63CXPpiEiW7JnXvZ1cUXcp', '6ANHfvTsKVUMQD1xD2VAMr', '54BDogj8DLMEAyMRz9gWnC']}, '4EVpmkEwrLYEg6jIsiPMIb': {'name': 'Fleet Foxes', 'top_songs': ['18ycL9Q5zLDeY9M2Lr3Ozw', '1Er5JMNcguoBMFXxwZ7BWH', '3Q3LbqfjDhWjmyYeirHfDe', '3ol9IHaYnppYIK8IADJALx', '1pbOvzdkL5iujppWgzBQdS', '6T8qnBbc2rxlWLiweD1e5M', '5gXF3XyUkM9BVA8QW7uYUg', '6kzi5LTg5uECin8pC34nxV', '5oYkuJL2VQ3Ss2oxNuRk3L', '1gSWmUWt0Flr52cQoH0yDJ']}, '7vCtweS8UVAXTyau2j0rDT': {'name': 'Josh Turner', 'top_songs': ['5C6uh95eAL0RBTSGXKQwvk', '1WzAeadSKJhqykZFbJNmQv', '1KhrAWvLIjRlQIJtSTgvsi', '2p07VcUwRZ5sru3mJ0JogS', '2rg3yLJKN5Yl4JCHHkMgeC', '2HqCaO7BV010qXS5FuiTED', '5CdOqNxkQ7054Rp86f5OWi', '5z5RJbZqDRYOgaMU6RetVk', '5JtRN8PCpxoL03vnIpZXc7', '0MVWxE7RIYMDt8JPC2vLNF']}, '1nf0nRF0W4ybnJdda00pKY': {'name': 'The Swon Brothers', 'top_songs': ['3OEgQVkIzrID6dSTNHz9FG', '7lG4154Md1Kw7BMg56Pt4s', '3ScJqT6cpcaLQjMwu4yogi', '290cSxnINrpvrFzqOxFqft', '3a8bHL5QtHvkoCIYWdYHui', '5fnGNW4axw52MaEaVvB77d', '6SSr6bidIF9m7QspjIhc5L', '03EwZBuDcnPrFAp15ThrYT', '7obPCswm0UiZfbl7Xj8VAy', '4EkTUr57ihH1bjyJpExtGg']}, '7ewhxhtYBkaKtWsilZIqPd': {'name': 'Kevin William', 'top_songs': ['0qcPs4kTUmCMCsGcj7E1Ze', '47zl5FL7ue5ez0zgXXg2gZ', '25pHcckhIot8apIQn6NN8F', '4XXkAMGVUz8Txq3m8MoIAR', '4bcUaD52IBY6VRYxfCiuYt', '4B6vZwJl0PJ42nD5bHUQeM', '0tcLy28fz77slArBF9e2k1']}, '7EIbKyiLnEJ1Y074UIUyZJ': {'name': 'Peter Hollens', 'top_songs': ['4VNCVb4cgYUPPoHxIxtzJT', '04TaLOwlQA8wbXbsru1K8P', '5FUWnXhrCgEXM0b7GI2uvf', '5uBCfIO7v8KxMwu8MSCWuA', '36ZEUaeqwwKy7HOQGidW15', '7FKaz2DtsfSHYaUdg66WeX', '5a5C2WzY2KTUaQDJynBuJx', '7N2LelbPKDyWmFQZHhgvzw', '10kJzrXI48v0wzRBBPjo06', '4yGO4h8Pn1E81Ev4Dl50vP']}, '0Xk15jHKly4c3AhPr5vjoA': {'name': 'Alan Silvestri', 'top_songs': ['1ijrMIqQvZNsnoqGukPzFD', '75uuO9osMuY3bgXgzTRagc', '5SXsXjVJCWeJuf7FHvgBYR', '2byBJ4bFeFPpSOgJnR6b8a', '6eLLMXei71a3S1eBJANXaM', '0AE7HvW4tTLvajXI5R5UJf', '435vx38BVoUIqSG1VfoJOh', '1Ig5PYAhZaCiCVAdIEcdAC', '68RXRtyaaccT2N0Kaq0Ko9', '1FI5hblwy9ZwyPg4Jr5hni']}, '06HL4z0CvFAxyc27GXpf02': {'name': 'Taylor Swift', 'top_songs': ['2y5aJvzXhHPA94U5GFAcXe', '0z9UVN8VBHJ9HdfYsOuuNf', '5vyxXfD5gLlyPxGZMEjtmd', '7wjbSn8QHsxqKXU5M0jXGM', '06FXaDDdg0BzXl15cthMS5']}, '4IsX3za8eNto9exd3VlTTK': {'name': 'Godwin', 'top_songs': ['5DN6H6gepbZoVy9jSIV2ue', '1HigdORYp9eFlTsnnF4cRU', '4dpRpHk4ohjALlZbyfa4by', '1xI4owym9GRbcyc35iGO8b', '1hAdl8eYz9ENrQKX95tRWt']}, '3hyGGjxu73JuzBa757H6R5': {'name': 'The Mountain Goats', 'top_songs': ['2M1Qc1mGSI1IYtmJzQtfPq', '4XpQ2F8NtzWMZ3g5t8qv2Y', '41LUI2mXScZDjIZWmvvWpR', '098PgApK9llaanxaDvAeij', '0SkIl3O2MVuY0bLiHQ72gi', '38dYh2pToiZPEKGVErVISk', '07gqJjvwwuZ1assFLKbiNn', '1ey9ub4AISvEmjM7tkoBh0', '7hyfYgXMS5BumjAjY98Xoe', '4rLLO47FTsKBwNILP9rMYI']}, '1oplL2hHYq7CQykvSbd6gy': {'name': "Anthony D'Amato", 'top_songs': ['4LT3jD9UcmFRKZiyuYlp7n', '1zozfArqnkwK1wo9lMeW60', '3zbM8xP6PwpY3mGxzvIdHS', '5B9PePNY0OkvGXuuw5Y8Xz', '0M3vcAL55zGTn3oP2ih604', '1gUgiYnYktGcyPoF93lsnc', '2l2PUbHGDbz6IGYaHpT1lz', '3fiFIjj7Tpgx0DN8F6Kpgc', '6iyC74ukfSSW8zkxyJ3tiY', '5d8YytQAj4DzigDrDwUdY3']}, '4J4o73Oun7v0XXRjN8DPif': {'name': 'Gungor', 'top_songs': ['06wxyCQFJOT0bjvSPMQj7x', '47fN6xeggnfG9NKPJUNC8H', '2ynZSIOI3DxnjuY2JTow05', '60V6mN6EQttmhVsgPmPUJW', '5eEUZlp3CwFq0QoUBcgo0I', '6fPSbqWloDmdWf3nA1nE45', '0Fu5Kgcj85v1n4pPs5CHUz', '0Q6SwpdV7ZUpO3LG4ikAAv', '4ywugrAa8pJtzVOFWaLnWz', '1BbvY4RSjqPykhVvYxWdsS']}, '0xhIBddw7R69CWKsCt2gVt': {'name': 'Capital Lights', 'top_songs': ['2RTkebdbPFyg4AMIzJZql1', '4ZxgjHhnqz9TyAwBtTeGzN', '0spVGAIkC7ntZL22jgdN5u', '2BIH7pmQpDlWP6bCzv9SeA', '0HjpouGnPswTLh3hSvWOMK', '5WH2cii4we48T6BMSlr162', '0zrbISwByqUAWssIhgQwQr', '6UX5LsQp3rdWs8x73wXrtF', '0ZvAw2h9im8Yy1PE3CZcyQ', '5S4iqbelathvMs6wlkXfmn']}, '3dRfiJ2650SZu6GbydcHNb': {'name': 'John Williams', 'top_songs': ['1n8NKQRg8LVHy7oUhUgbFF', '6CeCOC2zx1qS8mQNYHe6IM', '42gZM6AQ9BDMaTyTmMDVlN', '7di1zbwgfJkRLkTGV44icu', '0RGZCtszeCpGRgbMyVigAG', '4lg0h4AJhPMxbO3VMpbUqS', '2TZbQZXOuR8osP2AK8yYMN', '5wsHtmFHWntJzcN6n8ivjd', '1PPTlPJqKuL0fdoTmzwXJy', '2Bsnj9KAmtYz8PW9RImef7']}, '3PhL2Vdao2v8SS8AptuhAr': {'name': 'James Horner', 'top_songs': ['1kLeO0H9TdEewIZdr7Zi2i', '6vtY2LUeXJ7KISwgiTu0Ph', '1UBd7aWHZCz8yirI9KCvAU', '31loMj4ZFxOedEd2bHHQjg', '3q0Ks78ADSomVdDSap32mz', '3Yvi5NkUrSppVwrMHYkB6u', '55gn4hDvcrc8pmVWcBTVkR', '2pl6chJQxGLXgpbAoiMGRf', '1TvpEAMfSY9c7WNTefmQWE', '4uQ8h0F0AShbx7MyaqMEBa']}, '2oX42qP5ineK3hrhBECLmj': {'name': 'Andy Grammer', 'top_songs': ['4nMlau89VAjmV7agkl7OY3', '4orphgwPHHRsdEkfUmANSD', '7MapZTlRqFfUteNcghsTwf', '7sjc0ColKnEt8D1WHwOdmS', '1fMEUGs5CvRv0VrcJlQITt', '3uM14F9XYRMhx6MgDsS9iq', '7tg0OrYieTMcQmxIczNMqE', '1TzHpSSy3oL0tTR3mXsQke', '4c78ZcuoiaNVBAm1HNoqNT', '639nrBsmsfHMoP7wSeTPTm']}, '7t8q7ikEtcPNtoaKAm9Vu6': {'name': 'Jerry Goldsmith', 'top_songs': ['3hfzKPRcP6uHRe6rv2sy6x', '1b6Spq4MiEzShOBQLtEhWe', '25AASoU47mZPdhzxeDp5gP', '5QLLhvfPdnls7G97VfJYiJ', '6mQlq4Fd8C1uBbnwdkkXYm', '6zqrAStxnMBLa0tvm3lXMP', '3wxy4wpLTdDktnlOcotayY', '3bR1GUNPSB1VVvh9atIMlO', '62irSJnYNj3rKPFT6psxEV', '4D7qjCFBUSleoTGevgVZxn']}}
    data.top_songs = {'short_term': ['2BBb3UMJBNlofpC25pbSp4', '1Wdj4wRDYS7aT4CoPS0mAH', '5jQQSl7Uae4S8mlRkR4W8j', '6pOFkf24NgrPlf3YV1ESfq', '1WeF1b9XrQZpZ8IIEfYYJ5', '4vRuPvw2HQi1ukIaKu107k', '3bEmTTBl5I5cMkelx9foEK', '4YyhCfbXfeVrEjtj5LCO09', '5wTw73gergejPQEvWe5Lqv', '0rCcpuqlviUhA8TnBZGC9C', '06QdJtEtHOckzHhq5EbTfo', '0zf3DZPSvyOvGJ6PpsJKBE', '5bE0gN3bXWh8rcWttcvMto', '0wfbD5rAksdXUzRvMfM3x5', '4yRlTvPVfEyhXfp6GZurq9', '1dNIEtp7AY3oDAKCGg2XkH', '5f9Y4fa3y4mR6Lg1fifz86', '5OiaAaIMYlCZONyDBxqk4G', '2tux1s5FVabQQKpz7GEXbI', '77KyKfXIATnLVAougyvpBT', '0K90HGijiM6RpytZYyjbJB', '6k7HtqyhIYJMg6DgUwZc6M', '30qdwcNJ4n2iJqh75hmWak', '2j9z9hejHzVbcRUyYM7PZ1', '2ATtrAE0jDv6QYJgL3CHQD', '2eAv6wtp8l1GPJWUY4k7Ep', '3CuscN8itbT86pQFKQMIk7', '1KkFmmhPyIwPDM3tzWgqT8', '1DIg9155AY65dpR5Lf5Vg4', '3UR1mTBpLALt8cQGzfTbRz', '4hVJIlulH29qKVYGCT6cky', '67mjxSBrj9tMfz5aJdatcU', '3pvTrpsqbBF3OduTOPOkii', '75DtJBMwCXqjLz1bXS1tVr', '4yyg2J2uXOjCtCyT64984C', '78aRLjDiQx6jo0GVW7aDA4', '6cPyTS0Kk2sc4xQwC93kOg', '6fitB3zIBx8UybcuZg2ADv', '0dj1CtyRxZ4bnIT4Q20jNT', '1pJQAHpD51J7GYaFrrFO9S', '26AuyrZGzWWiYZPSd3XBIg', '4PMR2XYY8V8MVPRBxyeoxd', '5xhJmd0I15jFcEdqxfCzKk', '6KjbNLbRjuoa8rEq5yNA6H', '6V9kwssTrwkKT72imgowj9', '72jbDTw1piOOj770jWNeaG', '4gAgdhTIx6T76baPfbXHQX', '4ngv7whSPSAwD8ZP3zMHsd', '3Hvg5tRKsQlX25wYwgMF9p', '6ItGPha13j36IiQlvubGrT'], 'medium_term': ['4MgLY30kpo4vJTB29mhH1R', '4yRlTvPVfEyhXfp6GZurq9', '723paR6LrVISFCXFPf5z57', '2BBb3UMJBNlofpC25pbSp4', '7Hc1dKzCDzVqvlI8XaMZwH', '0ewrI06EIDMGXvgJxuyF3U', '6obkbpih6pYSgjPyoI75Xp', '1Wdj4wRDYS7aT4CoPS0mAH', '54CtOOuhXdUKGpG0KsEVDD', '13p3U002Sv8z722mFjTuWi', '2SYvX2G6D5SD6BpijIOBpG', '0FqK5zRZm46125vbLR7K6v', '3NXMZPpfTtiyteVW87c5EC', '2yEtO5IzwNttQ4SG38PDnF', '7H60aEC32oOX4Fy4Ug2l0r', '73Iyy1U5QR96t7YPPDrEKb', '1AtwsVXr1zaZf4YgIEOlDK', '06wxyCQFJOT0bjvSPMQj7x', '1RJFyMZOQhHCE26iixvM4Y', '1YhFtqwcN138S6ng3MT1nN', '4dI4oscajpdtjpg2dP1x28', '3E3I7DBGCIsIgT1a1UJEFK', '1irfge2G36vfmvs97KV6T0', '2wXbVH6oQtUPMcZrlUqnPs', '5jQQSl7Uae4S8mlRkR4W8j', '7f6YUhXC4jknHbvhbqK4U4', '5gTvQeSZbSFJdh7dxF71e0', '6pOFkf24NgrPlf3YV1ESfq', '1yLENA7X3q7xVEk57UjXY7', '2CdNHP8DJ5tfbRoIRdcTeE', '23AX1TW2CCpmqXtktvYe42', '5MMZJtHOiH1RmQSSe3DJdg', '0eLkNeny2GaXvu4VQiHtxG', '7LPNlKR6P8CYWEWJh1tg6K', '3Hvg5tRKsQlX25wYwgMF9p', '7HLTfpgbqC85BayqViMHmU', '7w5cxTEzp1rfV3KCy0Bd5N', '3Nby7PH0S2jJpwDMRkIfcb', '2F2zpDLZwxdGzT9soOfSZf', '0Fu5Kgcj85v1n4pPs5CHUz', '1tmYNUQaDTffVpBT9IASk0', '78aRLjDiQx6jo0GVW7aDA4', '32yiDCLJUdqYoaDR46z9gD', '4F9jpNQDKRFoyM4Ebpni6S', '7z6pDIQFv510mRKfyEjHR1', '2Cx61IzUXPJyhv3GzGtsZ3', '3Htx5VpJjmftQjaC3O9Tre', '5bE0gN3bXWh8rcWttcvMto', '2im8Pxe6JuPf6dhpxhl2nX', '6y468DyY1V67RBNCwzrMrC'], 'long_term': ['4yRlTvPVfEyhXfp6GZurq9', '5MMZJtHOiH1RmQSSe3DJdg', '13PUJCvdTSCT1dn70tlGdm', '3Hvg5tRKsQlX25wYwgMF9p', '44tlexN3Rxgake8xlZePPI', '72zmwnbXjx9fMUjw3mbDSs', '3HaiZ4gVk7BnYpayCvHIRO', '0ewrI06EIDMGXvgJxuyF3U', '4XXkAMGVUz8Txq3m8MoIAR', '2sE61ZmvYH8wiOx5jygkHH', '0BGM5wPT4L0KNKrf3WsMkn', '4KANJH1baadr3U7XsVbM17', '2SYvX2G6D5SD6BpijIOBpG', '25pHcckhIot8apIQn6NN8F', '47zl5FL7ue5ez0zgXXg2gZ', '6OtCIsQZ64Vs1EbzztvAv4', '5ITmuvjtUUdxVQCCsaKBDx', '2c62Xf5Po1YSa1N6LOjPHy', '7CEV9VwA8XO9wwxTXgYKvY', '3LbvNFkqDTrE1liGMmZBDL', '4y0Lt1KOuyhKGkGKFZjSlS', '0qcPs4kTUmCMCsGcj7E1Ze', '54CtOOuhXdUKGpG0KsEVDD', '0tcLy28fz77slArBF9e2k1', '0px0N4hIsQg1ITVi4Nee5c', '6ho8nmo2Z0y1tSCAdbjRE6', '4bcUaD52IBY6VRYxfCiuYt', '6fitB3zIBx8UybcuZg2ADv', '33y3ks1NgN9qCnKPLU3BTo', '3wx2kQWPn9p5UppQbNhPAk', '0gbpvYtk6nMyLa5nwUjPkJ', '4dI4oscajpdtjpg2dP1x28', '3T7KFsyl6n3UklWgfn0Lnp', '0ABHhxQTaluB94ohp2RLSr', '4B6vZwJl0PJ42nD5bHUQeM', '4q0SB41tm7eFqnAODPM8C6', '4yyg2J2uXOjCtCyT64984C', '6DEaND0SHv3sC11xobZLiy', '7hIRQZhDjab4YgqkkkehV9', '5misaMDzoPWVxvjBTVwx7v', '06wxyCQFJOT0bjvSPMQj7x', '1gRZZ2BQZ9XFu3t2lXvynZ', '4MgLY30kpo4vJTB29mhH1R', '5gTvQeSZbSFJdh7dxF71e0', '14s1A7gCghXIt7LXYYdYdp', '359krpyCKcFF8SFvqWES9L', '0IsjGDAqohBEdZWVoTaMjI', '1crbFuCkGL4kXnAGd63RXq', '1VklQ1e01s84jFTRD9np7n', '4F9jpNQDKRFoyM4Ebpni6S']}
    data.top_artists = {'short_term': ['16oZKvXb6WkQlVAjwo2Wbg', '6ltzsmQQbmdoHHbLZ4ZN25', '4DX2G1URzfEiRg2wBfv4ub', '3ZllGjNdP5pS8UFnT5Jj2x', '7EQ0qTo7fWT7DPxmxtSYEc', '2Oboq4Pq88TcC9eUn2HSW9', '0n94vC3S9c3mb2HyNAOcjg', '0YC192cP3KPCRWx8zr8MfZ', '0OdUWJ0sBjDrqHygGUXeCF', '2ic4xySjQ39N7DJ0HZemeG', '0e9H8oaYYRCKFXOVv848nt', '4RwbDag6jWIYJnEGH6Wte9', '6GwNGuDRNbx5XwoHQA3QiD', '2gzH4rGNFJeNg13yv2uI4L', '6Yuow6YoiBaVPFNjZ5BQi7', '4BxCuXFJrSWGi1KHcVqaU4', '5BvJzeQpmsdsFp4HGUYUEx', '0nJaMZM8paoA5HEUTUXPqi', '2JMtxA2S9SNUlqBlkDtXm6', '7IAFAOtc9kTYNTizhLSWM6', '5r2ltbRmBrS2c0J4oTwfGo', '0gadJ2b9A4SKsB1RFkBb66', '5nCi3BB41mBaMH9gfr6Su0', '0BvkDsjIUla7X0k6CSWh1I', '3zt4I5TLIb0Z9RigaiHe5G', '3cR4rhS2hBWqI7rJEBacvN', '5schNIzWdI9gJ1QRK8SBnc', '0GklSybv01PPje5GlXFq2i', '4dpARuHxo51G3z768sgnrY', '7z5WFjZAIYejWy0NI5lv4T', '3Lw97gGh8bp1MftsYmwJHG', '6y8XlgIV8BLlIg1tT1R10i', '6roFdX1y5BYSbp60OTJWMd', '14r9dR01KeBLFfylVSKCZQ', '1UTPBmNbXNTittyMJrNkvw', '4aXXDj9aZnlshx7mzj3W1N', '5sQqZtsAbXAoAnvA8iN9kN', '71jzN72g8qWMCMkWC5p1Z0', '44LPOpECjnIlnwH91wo2ir', '5o206eFLx38glA2bb4zqIU', '7D5oTJSXSHf51auG0106CQ', '0u2FHSq3ln94y5Q57xazwf', '6yJCxee7QumYr820xdIsjo', '0YrtvWJMgSdVrk3SfNjTbx', '2eam0iDomRHGBypaDQLwWI', '2txHhyCwHjUEpJjWrEyqyX', '34482S5nfxR441wcnVfrHi', '3D1IyJznpDnWnnFrzjuWnh', '5euJsEvfrlfhYDorMR40OF', '6tK77FerjTNLS5EEhI0zGM'], 'medium_term': ['44LPOpECjnIlnwH91wo2ir', '16oZKvXb6WkQlVAjwo2Wbg', '2Oboq4Pq88TcC9eUn2HSW9', '0YC192cP3KPCRWx8zr8MfZ', '6DIS6PRrLS3wbnZsf7vYic', '4DX2G1URzfEiRg2wBfv4ub', '6ltzsmQQbmdoHHbLZ4ZN25', '196lKsA13K3keVXMDFK66q', '0MASTEXfUt3bpiyGOoEaur', '3ZllGjNdP5pS8UFnT5Jj2x', '0CDUUM6KNRvgBFYIbWxJwV', '0n94vC3S9c3mb2HyNAOcjg', '3GjVVVcFmUgEJEAAsbGkf4', '71jzN72g8qWMCMkWC5p1Z0', '0nJaMZM8paoA5HEUTUXPqi', '4DBi4EYXgiqbkxvWUXUzMi', '0XHM5ZNJDU8e4CfbWMeSzC', '3Fe3pszR2t4TOBVz41B1WR', '2JMtxA2S9SNUlqBlkDtXm6', '4BxCuXFJrSWGi1KHcVqaU4', '0YrtvWJMgSdVrk3SfNjTbx', '5sQqZtsAbXAoAnvA8iN9kN', '6GwNGuDRNbx5XwoHQA3QiD', '5schNIzWdI9gJ1QRK8SBnc', '3sva1UjOJOx6cGISZOpItl', '1fFdRZK1GDGXL7vRxxUWLH', '3PMXHMqW4MNj8usJ0fxAlj', '6J7rw7NELJUCThPbAfyLIE', '1UTPBmNbXNTittyMJrNkvw', '5nCi3BB41mBaMH9gfr6Su0', '4iiQabGKtS2RtTKpVkrVTw', '6y8XlgIV8BLlIg1tT1R10i', '44BkC9lJfLmhcRB4NV7Z38', '6pBNfggcZZDCmb0p92OnGn', '0BvkDsjIUla7X0k6CSWh1I', '1a6tqLJPUs4DBAnNUZkr2O', '5EM6xJN2QNk0cL7EEm9HR9', '0gadJ2b9A4SKsB1RFkBb66', '0u2FHSq3ln94y5Q57xazwf', '2ic4xySjQ39N7DJ0HZemeG', '3mIj9lX2MWuHmhNCA7LSCW', '4RwbDag6jWIYJnEGH6Wte9', '5r2ltbRmBrS2c0J4oTwfGo', '0OdUWJ0sBjDrqHygGUXeCF', '6P9fFbQ875B2bnmdiYwN9A', '7x8nK0m0cP2ksQf0mjWdPS', '3grHWM9bx2E9vwJCdlRv9O', '63knPlGzLHTNDf1J78Fvte', '0e9H8oaYYRCKFXOVv848nt', '3b8QkneNDz4JHKKKlLgYZg'], 'long_term': ['0YC192cP3KPCRWx8zr8MfZ', '16oZKvXb6WkQlVAjwo2Wbg', '196lKsA13K3keVXMDFK66q', '3gd8FJtBJtkRxdfbTu19U2', '53XhwfbYqKCa1cC15pYq2q', '11Y54BxlxC3UIAUkU2eadQ', '0n94vC3S9c3mb2HyNAOcjg', '0CDUUM6KNRvgBFYIbWxJwV', '0OcclcP5o8VKH2TRqSY2A7', '4EVpmkEwrLYEg6jIsiPMIb', '2JMtxA2S9SNUlqBlkDtXm6', '6DIS6PRrLS3wbnZsf7vYic', '7vCtweS8UVAXTyau2j0rDT', '1nf0nRF0W4ybnJdda00pKY', '7ewhxhtYBkaKtWsilZIqPd', '0BvkDsjIUla7X0k6CSWh1I', '5schNIzWdI9gJ1QRK8SBnc', '2Oboq4Pq88TcC9eUn2HSW9', '44LPOpECjnIlnwH91wo2ir', '3PMXHMqW4MNj8usJ0fxAlj', '6pBNfggcZZDCmb0p92OnGn', '7EIbKyiLnEJ1Y074UIUyZJ', '0Xk15jHKly4c3AhPr5vjoA', '6ltzsmQQbmdoHHbLZ4ZN25', '06HL4z0CvFAxyc27GXpf02', '1UTPBmNbXNTittyMJrNkvw', '71jzN72g8qWMCMkWC5p1Z0', '7x8nK0m0cP2ksQf0mjWdPS', '4IsX3za8eNto9exd3VlTTK', '3sva1UjOJOx6cGISZOpItl', '3hyGGjxu73JuzBa757H6R5', '6J7rw7NELJUCThPbAfyLIE', '1oplL2hHYq7CQykvSbd6gy', '4J4o73Oun7v0XXRjN8DPif', '4DX2G1URzfEiRg2wBfv4ub', '0xhIBddw7R69CWKsCt2gVt', '4DBi4EYXgiqbkxvWUXUzMi', '6GwNGuDRNbx5XwoHQA3QiD', '3dRfiJ2650SZu6GbydcHNb', '3Fe3pszR2t4TOBVz41B1WR', '3PhL2Vdao2v8SS8AptuhAr', '0YrtvWJMgSdVrk3SfNjTbx', '6tK77FerjTNLS5EEhI0zGM', '0XHM5ZNJDU8e4CfbWMeSzC', '3ZllGjNdP5pS8UFnT5Jj2x', '2oX42qP5ineK3hrhBECLmj', '3GjVVVcFmUgEJEAAsbGkf4', '7t8q7ikEtcPNtoaKAm9Vu6', '1a6tqLJPUs4DBAnNUZkr2O', '7z5WFjZAIYejWy0NI5lv4T']}
    data.top_songs_all = ['06QdJtEtHOckzHhq5EbTfo', '06wxyCQFJOT0bjvSPMQj7x', '0ABHhxQTaluB94ohp2RLSr', '0BGM5wPT4L0KNKrf3WsMkn', '0FqK5zRZm46125vbLR7K6v', '0Fu5Kgcj85v1n4pPs5CHUz', '0IsjGDAqohBEdZWVoTaMjI', '0K90HGijiM6RpytZYyjbJB', '0dj1CtyRxZ4bnIT4Q20jNT', '0eLkNeny2GaXvu4VQiHtxG', '0ewrI06EIDMGXvgJxuyF3U', '0gbpvYtk6nMyLa5nwUjPkJ', '0px0N4hIsQg1ITVi4Nee5c', '0qcPs4kTUmCMCsGcj7E1Ze', '0rCcpuqlviUhA8TnBZGC9C', '0tcLy28fz77slArBF9e2k1', '0wfbD5rAksdXUzRvMfM3x5', '0zf3DZPSvyOvGJ6PpsJKBE', '13PUJCvdTSCT1dn70tlGdm', '13p3U002Sv8z722mFjTuWi', '14s1A7gCghXIt7LXYYdYdp', '1AtwsVXr1zaZf4YgIEOlDK', '1DIg9155AY65dpR5Lf5Vg4', '1KkFmmhPyIwPDM3tzWgqT8', '1RJFyMZOQhHCE26iixvM4Y', '1VklQ1e01s84jFTRD9np7n', '1Wdj4wRDYS7aT4CoPS0mAH', '1WeF1b9XrQZpZ8IIEfYYJ5', '1YhFtqwcN138S6ng3MT1nN', '1crbFuCkGL4kXnAGd63RXq', '1dNIEtp7AY3oDAKCGg2XkH', '1gRZZ2BQZ9XFu3t2lXvynZ', '1irfge2G36vfmvs97KV6T0', '1pJQAHpD51J7GYaFrrFO9S', '1tmYNUQaDTffVpBT9IASk0', '1yLENA7X3q7xVEk57UjXY7', '23AX1TW2CCpmqXtktvYe42', '25pHcckhIot8apIQn6NN8F', '26AuyrZGzWWiYZPSd3XBIg', '2ATtrAE0jDv6QYJgL3CHQD', '2BBb3UMJBNlofpC25pbSp4', '2CdNHP8DJ5tfbRoIRdcTeE', '2Cx61IzUXPJyhv3GzGtsZ3', '2F2zpDLZwxdGzT9soOfSZf', '2SYvX2G6D5SD6BpijIOBpG', '2c62Xf5Po1YSa1N6LOjPHy', '2eAv6wtp8l1GPJWUY4k7Ep', '2im8Pxe6JuPf6dhpxhl2nX', '2j9z9hejHzVbcRUyYM7PZ1', '2sE61ZmvYH8wiOx5jygkHH', '2tux1s5FVabQQKpz7GEXbI', '2wXbVH6oQtUPMcZrlUqnPs', '2yEtO5IzwNttQ4SG38PDnF', '30qdwcNJ4n2iJqh75hmWak', '32yiDCLJUdqYoaDR46z9gD', '33y3ks1NgN9qCnKPLU3BTo', '359krpyCKcFF8SFvqWES9L', '3CuscN8itbT86pQFKQMIk7', '3E3I7DBGCIsIgT1a1UJEFK', '3HaiZ4gVk7BnYpayCvHIRO', '3Htx5VpJjmftQjaC3O9Tre', '3Hvg5tRKsQlX25wYwgMF9p', '3LbvNFkqDTrE1liGMmZBDL', '3NXMZPpfTtiyteVW87c5EC', '3Nby7PH0S2jJpwDMRkIfcb', '3T7KFsyl6n3UklWgfn0Lnp', '3UR1mTBpLALt8cQGzfTbRz', '3bEmTTBl5I5cMkelx9foEK', '3pvTrpsqbBF3OduTOPOkii', '3wx2kQWPn9p5UppQbNhPAk', '44tlexN3Rxgake8xlZePPI', '47zl5FL7ue5ez0zgXXg2gZ', '4B6vZwJl0PJ42nD5bHUQeM', '4F9jpNQDKRFoyM4Ebpni6S', '4KANJH1baadr3U7XsVbM17', '4MgLY30kpo4vJTB29mhH1R', '4PMR2XYY8V8MVPRBxyeoxd', '4XXkAMGVUz8Txq3m8MoIAR', '4YyhCfbXfeVrEjtj5LCO09', '4bcUaD52IBY6VRYxfCiuYt', '4dI4oscajpdtjpg2dP1x28', '4gAgdhTIx6T76baPfbXHQX', '4hVJIlulH29qKVYGCT6cky', '4ngv7whSPSAwD8ZP3zMHsd', '4q0SB41tm7eFqnAODPM8C6', '4vRuPvw2HQi1ukIaKu107k', '4y0Lt1KOuyhKGkGKFZjSlS', '4yRlTvPVfEyhXfp6GZurq9', '4yyg2J2uXOjCtCyT64984C', '54CtOOuhXdUKGpG0KsEVDD', '5ITmuvjtUUdxVQCCsaKBDx', '5MMZJtHOiH1RmQSSe3DJdg', '5OiaAaIMYlCZONyDBxqk4G', '5bE0gN3bXWh8rcWttcvMto', '5f9Y4fa3y4mR6Lg1fifz86', '5gTvQeSZbSFJdh7dxF71e0', '5jQQSl7Uae4S8mlRkR4W8j', '5misaMDzoPWVxvjBTVwx7v', '5wTw73gergejPQEvWe5Lqv', '5xhJmd0I15jFcEdqxfCzKk', '67mjxSBrj9tMfz5aJdatcU', '6DEaND0SHv3sC11xobZLiy', '6ItGPha13j36IiQlvubGrT', '6KjbNLbRjuoa8rEq5yNA6H', '6OtCIsQZ64Vs1EbzztvAv4', '6V9kwssTrwkKT72imgowj9', '6cPyTS0Kk2sc4xQwC93kOg', '6fitB3zIBx8UybcuZg2ADv', '6ho8nmo2Z0y1tSCAdbjRE6', '6k7HtqyhIYJMg6DgUwZc6M', '6obkbpih6pYSgjPyoI75Xp', '6pOFkf24NgrPlf3YV1ESfq', '6y468DyY1V67RBNCwzrMrC', '723paR6LrVISFCXFPf5z57', '72jbDTw1piOOj770jWNeaG', '72zmwnbXjx9fMUjw3mbDSs', '73Iyy1U5QR96t7YPPDrEKb', '75DtJBMwCXqjLz1bXS1tVr', '77KyKfXIATnLVAougyvpBT', '78aRLjDiQx6jo0GVW7aDA4', '7CEV9VwA8XO9wwxTXgYKvY', '7H60aEC32oOX4Fy4Ug2l0r', '7HLTfpgbqC85BayqViMHmU', '7Hc1dKzCDzVqvlI8XaMZwH', '7LPNlKR6P8CYWEWJh1tg6K', '7f6YUhXC4jknHbvhbqK4U4', '7hIRQZhDjab4YgqkkkehV9', '7w5cxTEzp1rfV3KCy0Bd5N', '7z6pDIQFv510mRKfyEjHR1']
    data.top_artists_all = ['06HL4z0CvFAxyc27GXpf02', '0BvkDsjIUla7X0k6CSWh1I', '0CDUUM6KNRvgBFYIbWxJwV', '0GklSybv01PPje5GlXFq2i', '0MASTEXfUt3bpiyGOoEaur', '0OcclcP5o8VKH2TRqSY2A7', '0OdUWJ0sBjDrqHygGUXeCF', '0XHM5ZNJDU8e4CfbWMeSzC', '0Xk15jHKly4c3AhPr5vjoA', '0YC192cP3KPCRWx8zr8MfZ', '0YrtvWJMgSdVrk3SfNjTbx', '0e9H8oaYYRCKFXOVv848nt', '0gadJ2b9A4SKsB1RFkBb66', '0n94vC3S9c3mb2HyNAOcjg', '0nJaMZM8paoA5HEUTUXPqi', '0u2FHSq3ln94y5Q57xazwf', '0xhIBddw7R69CWKsCt2gVt', '11Y54BxlxC3UIAUkU2eadQ', '14r9dR01KeBLFfylVSKCZQ', '16oZKvXb6WkQlVAjwo2Wbg', '196lKsA13K3keVXMDFK66q', '1UTPBmNbXNTittyMJrNkvw', '1a6tqLJPUs4DBAnNUZkr2O', '1fFdRZK1GDGXL7vRxxUWLH', '1nf0nRF0W4ybnJdda00pKY', '1oplL2hHYq7CQykvSbd6gy', '2JMtxA2S9SNUlqBlkDtXm6', '2Oboq4Pq88TcC9eUn2HSW9', '2eam0iDomRHGBypaDQLwWI', '2gzH4rGNFJeNg13yv2uI4L', '2ic4xySjQ39N7DJ0HZemeG', '2oX42qP5ineK3hrhBECLmj', '2txHhyCwHjUEpJjWrEyqyX', '34482S5nfxR441wcnVfrHi', '3D1IyJznpDnWnnFrzjuWnh', '3Fe3pszR2t4TOBVz41B1WR', '3GjVVVcFmUgEJEAAsbGkf4', '3Lw97gGh8bp1MftsYmwJHG', '3PMXHMqW4MNj8usJ0fxAlj', '3PhL2Vdao2v8SS8AptuhAr', '3ZllGjNdP5pS8UFnT5Jj2x', '3b8QkneNDz4JHKKKlLgYZg', '3cR4rhS2hBWqI7rJEBacvN', '3dRfiJ2650SZu6GbydcHNb', '3gd8FJtBJtkRxdfbTu19U2', '3grHWM9bx2E9vwJCdlRv9O', '3hyGGjxu73JuzBa757H6R5', '3mIj9lX2MWuHmhNCA7LSCW', '3sva1UjOJOx6cGISZOpItl', '3zt4I5TLIb0Z9RigaiHe5G', '44BkC9lJfLmhcRB4NV7Z38', '44LPOpECjnIlnwH91wo2ir', '4BxCuXFJrSWGi1KHcVqaU4', '4DBi4EYXgiqbkxvWUXUzMi', '4DX2G1URzfEiRg2wBfv4ub', '4EVpmkEwrLYEg6jIsiPMIb', '4IsX3za8eNto9exd3VlTTK', '4J4o73Oun7v0XXRjN8DPif', '4RwbDag6jWIYJnEGH6Wte9', '4aXXDj9aZnlshx7mzj3W1N', '4dpARuHxo51G3z768sgnrY', '4iiQabGKtS2RtTKpVkrVTw', '53XhwfbYqKCa1cC15pYq2q', '5BvJzeQpmsdsFp4HGUYUEx', '5EM6xJN2QNk0cL7EEm9HR9', '5euJsEvfrlfhYDorMR40OF', '5nCi3BB41mBaMH9gfr6Su0', '5o206eFLx38glA2bb4zqIU', '5r2ltbRmBrS2c0J4oTwfGo', '5sQqZtsAbXAoAnvA8iN9kN', '5schNIzWdI9gJ1QRK8SBnc', '63knPlGzLHTNDf1J78Fvte', '6DIS6PRrLS3wbnZsf7vYic', '6GwNGuDRNbx5XwoHQA3QiD', '6J7rw7NELJUCThPbAfyLIE', '6P9fFbQ875B2bnmdiYwN9A', '6Yuow6YoiBaVPFNjZ5BQi7', '6ltzsmQQbmdoHHbLZ4ZN25', '6pBNfggcZZDCmb0p92OnGn', '6roFdX1y5BYSbp60OTJWMd', '6tK77FerjTNLS5EEhI0zGM', '6y8XlgIV8BLlIg1tT1R10i', '6yJCxee7QumYr820xdIsjo', '71jzN72g8qWMCMkWC5p1Z0', '7D5oTJSXSHf51auG0106CQ', '7EIbKyiLnEJ1Y074UIUyZJ', '7EQ0qTo7fWT7DPxmxtSYEc', '7IAFAOtc9kTYNTizhLSWM6', '7ewhxhtYBkaKtWsilZIqPd', '7t8q7ikEtcPNtoaKAm9Vu6', '7vCtweS8UVAXTyau2j0rDT', '7x8nK0m0cP2ksQf0mjWdPS', '7z5WFjZAIYejWy0NI5lv4T']
<<<<<<< HEAD
    # </REMOVE> #
=======
    # TEST #
>>>>>>> origin/master

    login_init(data)


################################################################################

# cs.cmu.edu/~112/notes/keyEventsDemo.py
# cs.cmu.edu/~112/notes/mouseEventsDemo.py

# The content of each function is original.

def set_event_info(event, data):
    data.ctrl = ((event.state & 0x0004) != 0)
    data.shift = ((event.state & 0x0001) != 0)


def ignore_key(event):
    ignore_sym = ['Shift_L', 'Shift_R', 'Control_L', 'Control_R', 'Caps_Lock']
    return (event.keysym in ignore_sym)


# Moving freely
def mouse_moved(event, data):
    data.mouse_moved_x, data.mouse_moved_y = event.x, event.y
    if (data.mode == 'login'):
        login_mouse_moved(data)
    elif (data.mode == 'organize'):
        organize_mouse_moved(data)
    elif (data.mode == 'analyze'):
        analyze_mouse_moved(data)


# Dragging
def left_moved(event, data):
    data.left_moved_x, data.left_moved_y = event.x, event.y
    if (data.mode == 'analyze'):
        analyze_left_moved(data)


def left_pressed(event, data):
    data.left_pressed_x, data.left_pressed_y = event.x, event.y
    if (data.mode == 'analyze'):
        analyze_left_pressed(data)


# Mouse-click
def left_released(event, data):
    data.left_released_x, data.left_released_y = (event.x, event.y)
    if (data.mode == 'login'):
        login_left_released(data)
    elif (data.mode == 'organize'):
        organize_left_released(data)
    elif (data.mode == 'analyze'):
        analyze_left_released(data)


def right_moved(event, data):
    data.right_moved_x, data.right_moved_y = event.x, event.y
    if (data.mode == 'analyze'):
        analyze_right_moved(data)


def right_pressed(event, data):
    data.right_pressed_x, data.right_pressed_y = event.x, event.y
    if (data.mode == 'analyze'):
        analyze_right_pressed(data)


# Right-click
def right_released(event, data):
    data.right_released_x, data.right_released_y = event.x, event.y
    if (data.mode == 'analyze'):
        analyze_right_released(data)


def key_pressed(event, data):
    if (not ignore_key(event)):
        data.keysym_pressed = event.keysym
        set_event_info(event, data)

    if (data.mode == 'organize'):
        organize_key_pressed(data)
    elif (data.mode == 'analyze'):
        analyze_key_pressed(data)


def key_released(event, data):
    if (not ignore_key(event)):
        data.keysym_released = event.keysym
        set_event_info(event, data)

    if (data.mode == 'analyze'):
        analyze_key_released(data)


def timer_fired(data):
    if (data.mode == 'analyze'):
        analyze_timer_fired(data)


def redraw_all(canvas, data):
    if (data.mode == 'login'):
        login_draw(canvas, data)
    elif (data.mode == 'organize'):
        organize_draw(canvas, data)
    elif (data.mode == 'analyze'):
        analyze_draw(canvas, data)


################################################################################

# All necessary colors
black = '#000000'
black_shadow = '#191919'
black_background = '#131313'
white = '#FFFFFF'
gray = '#8F8F8F'
gray_hover = '#1E1E1E'
gray_select = '#262626'
green = '#49A343'
green_hover = '#57C64C'
red = '#A34349'
red_hover = '#C64C57'
blue = '#4349A3'
blue_hover = '#4C57C6'


################################################################################

class Button(object):
    def __init__(self, data, cx_scale, cy_scale, color, hover_color, text,
                 text_color, text_hover_color, text_size, function):
        self.width = self.height = 0
        self.cx_scale, self.cy_scale = cx_scale, cy_scale
        self.cx = self.cy = self.x1 = self.y1 = self.x2 = self.y2 = 0
        self.fill = self.color = color
        self.hover_color = hover_color
        self.text_fill = self.text_color = text_color
        self.text_hover_color = text_hover_color
        self.text = text
        self.text_size = text_size
        self.function = function
        self.update_dimensions(data)

    def update_dimensions(self, data):
        self.width = data.width / data.scale
        self.height = data.width / data.scale ** 2
        self.cx = data.width * self.cx_scale
        self.cy = data.height * self.cy_scale
        self.x1 = self.cx - self.width / 2
        self.y1 = self.cy - self.height / 2
        self.x2 = self.cx + self.width / 2
        self.y2 = self.cy + self.height / 2

    def is_within_bounds(self, data, x, y):
        self.update_dimensions(data)
        return ((self.x1 <= x <= self.x2) and (self.y1 <= y <= self.y2))

    # Changes the color of the button when hovered/not hovered over
    def hover(self):
        self.fill = self.hover_color
        self.text_fill = self.text_hover_color

    def unhover(self):
        self.fill = self.color
        self.text_fill = self.text_color

    # Runs the correct function when pressed
    def select(self, data):
        self.function(data)

    # Draws each button with text inside it
    def draw(self, canvas, data):
        self.update_dimensions(data)
        canvas.create_rectangle(self.x1, self.y1, self.x2, self.y2,
                                fill=self.fill, width=0)
        canvas.create_text(data.width * self.cx_scale,
                           data.height * self.cy_scale, text=self.text,
                           fill=self.text_fill,
                           font='Proxima %d' % self.text_size)


################################################################################

class LeftSidebar(Button):
<<<<<<< HEAD
    def __init__(self, data, organize_ids, y_position, text):
=======
    def __init__(self, data, viewing_ids, y_position, text):
>>>>>>> origin/master
        self.y_position = y_position
        if (self.y_position < 5):
            self.is_songs = True
            self.is_artists = False
        else:
            self.is_songs = False
            self.is_artists = True

        if (self.is_songs):
<<<<<<< HEAD
            function = organize_songs
        elif (self.is_artists):
            function = organize_artists
        super().__init__(data, 0, 0, black_shadow, black_shadow, text, gray,
                         white, 10, function)
        self.is_selected = False
        self.organize_ids = organize_ids
=======
            function = view_songs
        elif (self.is_artists):
            function = view_artists
        super().__init__(data, 0, 0, black_shadow, black_shadow, text, gray,
                         white, 10, function)
        self.is_selected = False
        self.viewing_ids = viewing_ids
>>>>>>> origin/master
        self.width = self.height = 0
        self.x1 = self.y1 = self.x2 = self.y2 = self.cx = self.cy = 0
        self.update_dimensions(data)

    def update_dimensions(self, data):
        self.width = data.width * data.vertical1_scale
        self.height = 3 * data.height / data.scale ** 2
        self.x1 = 0
        self.y1 = self.y_position * self.height / 2
        self.x2 = self.width
        self.y2 = self.y1 + self.height / 2
        self.cx = self.x2 / 2
        self.cy = (self.y1 + self.y2) / 2

    def is_within_bounds(self, data, x, y):
        self.update_dimensions(data)
        return ((self.x1 <= x <= self.x2) and (self.y1 <= y <= self.y2))

<<<<<<< HEAD
=======
    def draw(self, canvas, data):
        self.update_dimensions(data)
        canvas.create_rectangle(self.x1, self.y1, self.x2, self.y2,
                                fill=self.fill, width=0)
        canvas.create_text(20, self.cy, text=self.text, fill=self.text_fill,
                           font='Proxima 11', anchor=W)
        if (self.is_selected):
            canvas.create_rectangle(0, self.y1, 6.5, self.y2, fill=green_hover,
                                    width=0)

>>>>>>> origin/master
    def unhover(self):
        if (not self.is_selected):
            super().unhover()

    def select(self, data):
<<<<<<< HEAD
        organize_clear(data)
        if (self.is_songs):
            data.is_songs = True
            data.is_artists = False
            data.is_artist_top_songs = False
            del data.songs_id[:]
            data.songs_id += self.organize_ids

        elif (self.is_artists):
            data.is_songs = False
            data.is_artists = True
            data.is_artist_top_songs = False
            del data.artists_id[:]
            data.artists_id += self.organize_ids

        if (self.text == 'TOP SONGS'):
            data.is_overall = True
            songs_by_title(data)
        elif (self.text == 'TOP ARTISTS'):
            data.is_overall = True
            artists_by_name(data)
=======
        clear_view(data)
        if (self.is_songs):
            data.is_viewing_songs = True
            data.is_viewing_artists = False
            data.is_viewing_artist_top_songs = False
            del data.viewing_songs_id[:]
            data.viewing_songs_id += self.viewing_ids

        elif (self.is_artists):
            data.is_viewing_songs = False
            data.is_viewing_artists = True
            data.is_viewing_artist_top_songs = False
            del data.viewing_artists_id[:]
            data.viewing_artists_id += self.viewing_ids

        if (self.text == 'TOP SONGS'):
            data.is_overall = True
            sort_songs_by_name(data)
        elif (self.text == 'TOP ARTISTS'):
            data.is_overall = True
            sort_artists_by_name(data)
>>>>>>> origin/master
        else:
            data.is_overall = False
            data.sort_mode = 0

        self.is_selected = True
        self.text_fill = white
<<<<<<< HEAD
        data.start = data.start = 0
        data.sort_mode_inner = 0
=======
        data.viewing_songs_start = data.viewing_artists_start = 0
        data.inner_sort_mode = 0
>>>>>>> origin/master
        self.function(data)

    def unselect(self, data):
        self.is_selected = False
        self.text_fill = gray

<<<<<<< HEAD
    def draw(self, canvas, data):
        self.update_dimensions(data)
        canvas.create_rectangle(self.x1, self.y1, self.x2, self.y2,
                                fill=self.fill, width=0)
        canvas.create_text(20, self.cy, text=self.text, fill=self.text_fill,
                           font='Proxima 11', anchor=W)
        if (self.is_selected):
            canvas.create_rectangle(0, self.y1, 6.5, self.y2, fill=green_hover,
                                    width=0)

################################################################################

class OrganizeSong(object):
=======

################################################################################

class ViewingSong(object):
>>>>>>> origin/master
    def __init__(self, data, y_position, song_id):
        self.y_position = y_position
        self.x1 = self.y1 = self.x2 = self.x2 = self.cy = 0
        self.fill = black_background
        self.text_fill = white
        self.song_id = song_id
        self.title = data.all_songs_features[self.song_id]['name']
        self.artist = data.all_songs_features[self.song_id]['artist_name']
        self.album = data.all_songs_features[self.song_id]['album_name']
        self.update_dimensions(data)
        self.is_selected_song = self.is_selected(data)
<<<<<<< HEAD
        data.is_songs = True
        data.is_artists = data.is_artist_top_songs = False
=======
        data.is_viewing_songs = True
        data.is_viewing_artists = data.is_viewing_artist_top_songs = False
>>>>>>> origin/master

    def get_id(self):
        return self.song_id

    def get_index(self):
        return y_position - 2

    def get_source(self):
<<<<<<< HEAD
        return data.songs_id
=======
        return data.viewing_songs_id
>>>>>>> origin/master

    def update_dimensions(self, data):
        height_scale = 1.5
        self.x1 = data.width * data.vertical1_scale
        self.y1 = self.y_position * height_scale * data.height / data.scale ** 2
        self.x2 = data.width * data.vertical2_scale
        self.y2 = self.y1 + height_scale * data.height / data.scale ** 2
        self.cy = (self.y1 + self.y2) / 2

    def is_within_bounds(self, data, x, y):
        self.update_dimensions(data)
        return ((self.x1 <= x <= self.x2) and (self.y1 <= y <= self.y2))

    def hover(self):
        self.fill = gray_hover

    def unhover(self):
        if (not self.is_selected_song):
            self.fill = black_background

    def is_selected(self, data):
<<<<<<< HEAD
        if (self.song_id in data.songs_id_selected):
=======
        if (self.song_id in data.selected_songs):
>>>>>>> origin/master
            self.is_selected_song = True
        else:
            self.is_selected_song = False
        return self.is_selected_song

    def select(self, data):
<<<<<<< HEAD
        if (self.song_id not in data.songs_id_selected):
            data.songs_id_selected += [self.song_id]
=======
        if (self.song_id not in data.selected_songs):
            data.selected_songs += [self.song_id]
>>>>>>> origin/master
        else:
            self.unselect(data)
        self.is_selected(data)
        if (self.is_selected_song):
            self.fill = gray_select

    def unselect(self, data):
<<<<<<< HEAD
        if (self.song_id in data.songs_id_selected):
            data.songs_id_selected.remove(self.song_id)
=======
        if (self.song_id in data.selected_songs):
            data.selected_songs.remove(self.song_id)
>>>>>>> origin/master
        self.is_selected(data)
        if (not self.is_selected_song):
            self.fill = black_background

    def staging_colors(self, data):
        if (self.song_id in data.stage_id):
            self.text_fill = green
        else:
            self.text_fill = white

    def draw(self, canvas, data):
        self.update_dimensions(data)
        self.staging_colors(data)
        start = self.x1 + data.width / 50
        end = self.x2 - data.width / 50
        canvas.create_rectangle(start, self.y1, end, self.y2, fill=self.fill,
                                width=0)
        canvas.create_line(start, self.y1, end, self.y1, fill=gray_hover)
        canvas.create_line(start, self.y2, end, self.y2, fill=gray_hover)
        canvas.create_text(start + 10, self.cy, text=self.title,
                           fill=self.text_fill, font='Proxima 10', anchor=W)
        canvas.create_text(start + (end - start) / 3, self.cy, text=self.artist,
                           fill=self.text_fill, font='Proxima 10', anchor=W)
        canvas.create_text(start + 1.83 * (end - start) / 3, self.cy,
                           text=self.album, fill=self.text_fill,
                           font='Proxima 10', anchor=W)


################################################################################

<<<<<<< HEAD
class OrganizeArtist(object):
=======
class ViewingArtist(object):
>>>>>>> origin/master
    def __init__(self, data, y_position, artist_id):
        self.y_position = y_position
        self.x1 = self.y1 = self.x2 = self.x2 = self.cy = 0
        self.fill = black_background
        self.artist_id = artist_id
        self.artist_name = data.all_artists_features[self.artist_id]['name']
        self.update_dimensions(data)
        self.is_selected_artist = self.is_selected(data)
<<<<<<< HEAD
        data.is_songs = False
        data.is_artists = True
        data.is_artist_top_songs = False
=======
        data.is_viewing_songs = False
        data.is_viewing_artists = True
        data.is_viewing_artist_top_songs = False
>>>>>>> origin/master

    def get_id(self):
        return self.artist_id

    def get_index(self):
        return y_position - 2

    def get_source(self):
<<<<<<< HEAD
        return data.artists_id
=======
        return data.viewing_artists_id
>>>>>>> origin/master

    def update_dimensions(self, data):
        height_scale = 1.5
        self.x1 = data.width * data.vertical1_scale
        self.y1 = self.y_position * height_scale * data.height / data.scale ** 2
        self.x2 = (self.x1 + (
                   self.x1 + data.width * data.vertical2_scale) * 2 / 9)
        self.y2 = self.y1 + height_scale * data.height / data.scale ** 2
        self.cy = (self.y1 + self.y2) / 2

    def is_within_bounds(self, data, x, y):
        self.update_dimensions(data)
        return ((self.x1 <= x <= self.x2) and (self.y1 <= y <= self.y2))

    def hover(self):
        self.fill = gray_hover

    def unhover(self):
        if (not self.is_selected_artist):
            self.fill = black_background

    def is_selected(self, data):
<<<<<<< HEAD
        if (self.artist_id in data.artists_id_selected):
=======
        if (self.artist_id in data.selected_artists):
>>>>>>> origin/master
            self.is_selected_artist = True
        else:
            self.is_selected_artist = False
        return self.is_selected_artist

    def select(self, data):
<<<<<<< HEAD
        if (self.artist_id not in data.artists_id_selected):
            data.artists_id_selected += [self.artist_id]
            data.artist_top_songs_id_selected += \
                data.all_artists_features[self.artist_id]['top_songs'][
                :data.artist_top_songs_end]
=======
        if (self.artist_id not in data.selected_artists):
            data.selected_artists += [self.artist_id]
            data.selected_artist_top_songs += \
                data.all_artists_features[self.artist_id]['top_songs'][
                :data.viewing_artist_top_songs_end]
>>>>>>> origin/master
        else:
            self.unselect(data)
        self.is_selected(data)
        if (self.is_selected_artist):
            self.fill = gray_select

<<<<<<< HEAD
        organize_clear(data, True, False, True)
        data.is_artist_top_songs = True
        del data.artist_top_songs_id[:]
        data.artist_top_songs_id += \
            data.all_artists_features[self.artist_id]['top_songs'][
            :data.artist_top_songs_end]
        data.sort_mode = data.sort_mode_inner = 0
        artist_top_songs(data)

    def unselect(self, data):
        if (self.artist_id in data.artists_id_selected):
            data.artists_id_selected.remove(self.artist_id)
=======
        clear_view(data, True, False, True)
        data.is_viewing_artist_top_songs = True
        del data.viewing_artist_top_songs_id[:]
        data.viewing_artist_top_songs_id += \
            data.all_artists_features[self.artist_id]['top_songs'][
            :data.viewing_artist_top_songs_end]
        data.sort_mode = data.inner_sort_mode = 0
        view_artist_top_songs(data)

    def unselect(self, data):
        if (self.artist_id in data.selected_artists):
            data.selected_artists.remove(self.artist_id)
>>>>>>> origin/master
        self.is_selected(data)
        if (not self.is_selected_artist):
            self.fill = black_background

    def draw(self, canvas, data):
        self.update_dimensions(data)
        start = self.x1 + data.width / 50
        end = self.x2 - data.width / 50
        canvas.create_rectangle(start, self.y1, end, self.y2, fill=self.fill,
                                width=0)
        canvas.create_line(start, self.y1, end, self.y1, fill=gray_hover)
        canvas.create_line(start, self.y2, end, self.y2, fill=gray_hover)
        canvas.create_text(start + 10, self.cy, text=self.artist_name,
                           fill=white, font='Proxima 10', anchor=W)


################################################################################

<<<<<<< HEAD
class OrganizeArtistTopSong(object):
=======
class ViewingArtistTopSong(object):
>>>>>>> origin/master
    def __init__(self, data, y_position, song_id):
        self.y_position = y_position
        self.x1 = self.y1 = self.x2 = self.x2 = self.cy = 0
        self.fill = black_background
        self.text_fill = white
        self.song_id = song_id
        self.title = data.all_songs_features[self.song_id]['name']
        self.album = data.all_songs_features[self.song_id]['album_name']
        self.update_dimensions(data)
        self.is_selected_artist_top_song = self.is_selected(data)
<<<<<<< HEAD
        data.is_songs = False
        data.is_artists = data.is_artist_top_songs = True
=======
        data.is_viewing_songs = False
        data.is_viewing_artists = data.is_viewing_artist_top_songs = True
>>>>>>> origin/master

    def get_id(self):
        return self.song_id

    def get_index(self):
        return y_position - 2

    def get_source(self):
<<<<<<< HEAD
        return data.artist_top_songs_id
=======
        return data.viewing_artist_top_songs_id
>>>>>>> origin/master

    def update_dimensions(self, data):
        height_scale = 1.5
        self.x1 = data.width * (data.vertical1_scale + (
            data.vertical1_scale + data.vertical2_scale) * 2 / 9)
        self.y1 = self.y_position * height_scale * data.height / data.scale ** 2
        self.x2 = data.width * data.vertical2_scale
        self.y2 = self.y1 + height_scale * data.height / data.scale ** 2
        self.cy = (self.y1 + self.y2) / 2

    def is_within_bounds(self, data, x, y):
        self.update_dimensions(data)
        return ((self.x1 <= x <= self.x2) and (self.y1 <= y <= self.y2))

    def hover(self):
        self.fill = gray_hover

    def unhover(self):
        if (not self.is_selected_artist_top_song):
            self.fill = black_background

    def is_selected(self, data):
<<<<<<< HEAD
        if (self.song_id in data.artist_top_songs_id_selected):
=======
        if (self.song_id in data.selected_artist_top_songs):
>>>>>>> origin/master
            self.is_selected_artist_top_song = True
        else:
            self.is_selected_artist_top_song = False
        return self.is_selected_artist_top_song

    def select(self, data):
<<<<<<< HEAD
        if (self.song_id not in data.artist_top_songs_id_selected):
            data.artist_top_songs_id_selected += [self.song_id]
=======
        if (self.song_id not in data.selected_artist_top_songs):
            data.selected_artist_top_songs += [self.song_id]
>>>>>>> origin/master
        else:
            self.unselect(data)
        self.is_selected(data)
        if (self.is_selected_artist_top_song):
            self.fill = gray_select

    def unselect(self, data):
<<<<<<< HEAD
        if (self.song_id in data.artist_top_songs_id_selected):
            data.artist_top_songs_id_selected.remove(self.song_id)
=======
        if (self.song_id in data.selected_artist_top_songs):
            data.selected_artist_top_songs.remove(self.song_id)
>>>>>>> origin/master
        self.is_selected(data)
        if (not self.is_selected_artist_top_song):
            self.fill = black_background

    def staging_colors(self, data):
        if (self.song_id in data.stage_id):
            self.text_fill = green
        else:
            self.text_fill = white

    def draw(self, canvas, data):
        self.update_dimensions(data)
        self.staging_colors(data)
        start = self.x1 + data.width / 50
        end = self.x2 - data.width / 50
        canvas.create_line(self.x1, 0, self.x1, data.height, fill=gray_select)
        canvas.create_rectangle(start, self.y1, end, self.y2, fill=self.fill,
                                width=0)
        canvas.create_line(start, self.y1, end, self.y1, fill=gray_hover)
        canvas.create_line(start, self.y2, end, self.y2, fill=gray_hover)
        canvas.create_text(start + 10, self.cy, text=self.title,
                           fill=self.text_fill, font='Proxima 10', anchor=W)
        canvas.create_text(start + 1.83 * (end - start) / 3, self.cy,
                           text=self.album, fill=self.text_fill,
                           font='Proxima 10', anchor=W)


################################################################################

class Header(object):
    def __init__(self, data, position, text, function):
        self.position = position
        self.y_scale = 1 / 20
        self.width = self.height = 0
        self.x1 = self.y1 = self.x2 = self.y2 = self.cy = 0
        self.symbol = ''
        self.text = text
        self.text_fill = gray
        self.function = function
        self.update_dimensions(data)

    def update_dimensions(self, data):
        start = data.width * (data.vertical1_scale + 1 / 50)
        end = data.width * (data.vertical2_scale - 1 / 50)
        if (self.position == 0):
            self.x1 = start + 10
<<<<<<< HEAD
        elif (data.is_songs):
=======
        elif (data.is_viewing_songs):
>>>>>>> origin/master
            if (self.position == 1):
                self.x1 = start + (end - start) / 3
            elif (self.position == 2):
                self.x1 = start + 1.83 * (end - start) / 3
<<<<<<< HEAD
        elif (data.is_artists):
=======
        elif (data.is_viewing_artists):
>>>>>>> origin/master
            if (self.position == 1):
                start1 = ((data.width * (data.vertical1_scale + (
                           data.vertical1_scale + data.vertical2_scale)
                           * 2 / 9)) + data.width / 50)
                self.x1 = start1 + 10
            elif (self.position == 2):
                start2 = ((data.width * (data.vertical1_scale + (
                           data.vertical1_scale + data.vertical2_scale)
                           * 2 / 9)) + data.width / 50)
                self.x1 = start2 + 1.83 * (end - start2) / 3
        self.width = data.width / data.scale ** 2 * 2
        self.height = data.width / data.scale ** 2
        self.y1 = data.height * self.y_scale - self.height / 2
        self.x2 = self.x1 + self.width
        self.y2 = self.y1 + self.height
        self.cy = (self.y1 + self.y2) / 2

    def is_within_bounds(self, data, x, y):
        self.update_dimensions(data)
        bleed = data.scale * 2
        return (((self.x1 - bleed) <= x <= (self.x2 + bleed)) and
                ((self.y1 - bleed) <= y <= (self.y2 + bleed)))

    def hover(self):
        self.text_fill = white

    def unhover(self):
        self.text_fill = gray

    def select(self, data):
        self.function(data)

    def get_symbol(self, data):
        if (self.position == 0):
            if (data.sort_mode == 1):
                self.symbol = '/\\'
            elif (data.sort_mode == 2):
                self.symbol = '\\/'
<<<<<<< HEAD
        elif (data.is_songs):
=======
        elif (data.is_viewing_songs):
>>>>>>> origin/master
            if (self.position == 1):
                if (data.sort_mode == 3):
                    self.symbol = '/\\'
                elif (data.sort_mode == 4):
                    self.symbol = '\\/'
            elif (self.position == 2):
                if (data.sort_mode == 5):
                    self.symbol = '/\\'
                elif (data.sort_mode == 6):
                    self.symbol = '\\/'
<<<<<<< HEAD
        elif (data.is_artists):
            if (self.position == 1):
                if (data.sort_mode_inner == 1):
                    self.symbol = '/\\'
                elif (data.sort_mode_inner == 2):
                    self.symbol = '\\/'
            elif (self.position == 2):
                if (data.sort_mode_inner == 3):
                    self.symbol = '/\\'
                elif (data.sort_mode_inner == 4):
                    self.symbol = '\\/'

    def draw(self, canvas, data):
        if (data.is_artists and (
                not data.is_artist_top_songs) and (self.position > 0)):
=======
        elif (data.is_viewing_artists):
            if (self.position == 1):
                if (data.inner_sort_mode == 1):
                    self.symbol = '/\\'
                elif (data.inner_sort_mode == 2):
                    self.symbol = '\\/'
            elif (self.position == 2):
                if (data.inner_sort_mode == 3):
                    self.symbol = '/\\'
                elif (data.inner_sort_mode == 4):
                    self.symbol = '\\/'

    def draw(self, canvas, data):
        if (data.is_viewing_artists and (
                not data.is_viewing_artist_top_songs) and (self.position > 0)):
>>>>>>> origin/master
            self.update_dimensions(data)
            self.get_symbol(data)
        else:
            self.update_dimensions(data)
            self.get_symbol(data)
            canvas.create_text(self.x1, self.cy, text=self.text,
                               fill=self.text_fill, font='Proxima 10', anchor=W)
            canvas.create_text(self.x1 - 10, self.cy, text=self.symbol,
                               fill=green)


################################################################################

class StageSong(object):
    def __init__(self, data, y_position, song_id):
        self.is_selected_song = False
        self.y_position = y_position
        self.x1 = self.y1 = self.x2 = self.x2 = self.cy = 0
        self.fill = None
        self.text_fill = green
        self.song_id = song_id
        self.title = data.all_songs_features[self.song_id]['name']
        self.artist = data.all_songs_features[self.song_id]['artist_name']
        self.update_dimensions(data)

    def update_dimensions(self, data):
        self.x1 = data.width * data.vertical2_scale + 5
        self.y1 = ((data.height * 2.75 / 24)
                   + 0.595 * self.y_position * data.height / data.scale ** 2)
        self.x2 = data.width - 5
        self.y2 = self.y1 + 0.595 * data.height / data.scale ** 2
        self.cy = (self.y1 + self.y2) / 2

    def is_within_bounds(self, data, x, y):
        self.update_dimensions(data)
        return ((self.x1 <= x <= self.x2) and (self.y1 <= y <= self.y2))

    def hover(self):
        self.fill = None
        self.text_fill = gray

    def unhover(self):
        if (self.is_selected_song):
            self.fill = gray_select
            self.text_fill = white
        else:
            self.fill = None
            self.text_fill = green

    def is_selected(self, data):
<<<<<<< HEAD
        if (self.song_id in data.songs_id_selected):
=======
        if (self.song_id in data.selected_songs):
>>>>>>> origin/master
            self.is_selected_song = True
        else:
            self.is_selected_song = False
        return self.is_selected_song

    def select(self, data):
<<<<<<< HEAD
        if (self.song_id not in data.songs_id_selected):
            data.songs_id_selected += [self.song_id]
=======
        if (self.song_id not in data.selected_songs):
            data.selected_songs += [self.song_id]
>>>>>>> origin/master
        self.fill = gray_select
        self.text_fill = white
        self.is_selected(data)

    def unselect(self, data):
<<<<<<< HEAD
        if (self.song_id in data.songs_id_selected):
            data.songs_id_selected.remove(self.song_id)
=======
        if (self.song_id in data.selected_songs):
            data.selected_songs.remove(self.song_id)
>>>>>>> origin/master
        self.fill = None
        self.text_fill = green
        self.is_selected(data)

    def draw(self, canvas, data):
        self.is_selected(data)
        self.update_dimensions(data)
        canvas.create_rectangle(self.x1, self.y1, self.x2, self.y2,
                                fill=self.fill, width=0)
        if (self.y_position <= 8):
            text_position = '  ' + str(self.y_position + 1)
        else:
            text_position = str(self.y_position + 1)
        text = text_position + '. ' + self.artist + ' | ' + self.title
        canvas.create_text(self.x1 + 5, self.cy, text=text, fill=self.text_fill,
                           font='Proxima 8', anchor=W)


################################################################################

def login_init(data):
    data.mode = 'login'
    data.scale = 6
    login_logo(data)
    login_buttons(data)


def login_logo(data):
    data.logo = PhotoImage(file='sortify_logo.gif')
    data.logo_scale = data.logo.width() // (data.width // data.scale)
    data.logo = data.logo.subsample(data.logo_scale, data.logo_scale)


def login_buttons(data):
    del data.buttons[:]
    data.buttons += [
        Button(data, 1 / 2, 3.3 / 9, black, black, 'USERNAME', green,
               green_hover, 20, input_username),
        Button(data, 1 / 2, 8 / 9, green, green_hover, 'AUTHORIZE', white,
               white, 14, authorize)]


def login_mouse_moved(data):
    for button in data.buttons:
        if (button.is_within_bounds(data, data.mouse_moved_x,
                                    data.mouse_moved_y)):
            button.hover()
        else:
            button.unhover()


def login_left_released(data):
    for button in data.buttons:
        if (button.is_within_bounds(data, data.left_released_x,
                data.left_released_y) and button.is_within_bounds(
            data, data.left_pressed_x, data.left_pressed_y)):
            button.select(data)


def login_draw(canvas, data):
    canvas.create_rectangle(0, 0, data.width, data.height, fill=black)
    for button in data.buttons:
        button.draw(canvas, data)
    canvas.create_image(data.width / 2, data.height * 1.75 / 9, image=data.logo)
    canvas.create_text(data.width / 2, data.height * 2.3 / 9,
                       text='Organize. Analyze. Simplify.   ', fill=gray,
                       font='Proxima 14')
    canvas.create_line(data.width / 4, data.height * 3.75 / 9,
                       data.width * 3 / 4, data.height * 3.75 / 9, fill=gray)
    canvas.create_line(data.width / 4, data.height * 7.25 / 9,
                       data.width * 3 / 4, data.height * 7.25 / 9, fill=gray)
    canvas.create_text(data.width / 2, data.height * 5.5 / 9, fill=gray,
                       font='Proxima 16', text=
'''
Please enter your username above.
Then click on the button below.
User authentication requires
interaction with your web browser.
Once you enter your credentials
and give authorization to Sortify,
you will be redirected to a URL.
Paste the URL you were directed to
to complete the authorization.
''')


################################################################################

# cs.cmu.edu/~112/notes/dialogs-demo1.py

def input_username(data):
    # <REMOVE> #
    msg = 'Please enter your Spotify username (steph.ananth).'
    # </REMOVE> #
    title = 'Username'
    data.username = simpledialog.askstring(title, msg)

def authorize(data):
    if (data.username == ''):
        msg = 'Please enter your username.'
        title = 'Username Required'
        messagebox.showwarning(title, msg)
    elif (data.mode == 'login'):
        # <REMOVE> #
        if (data.username != 'steph.ananth'):
        # </REMOVE> #
            # <UNINDENT> #
            prompt_for_user_token(data, 'user-top-read')
            get_top_songs(data)
            get_top_artists(data)
            # </UNINDENT> #
        organize_init(data)


################################################################################

# github.com/plamere/spotipy/blob/master/spotipy/util.py
# cs.cmu.edu/~112/notes/dialogs-demo1.py

# Checks if the user has already authorized an action
# If not, redirects them to an authorization page and opens a message box
# Adds the new token to data

def prompt_for_user_token(data, scope):
    client_id = os.getenv('SPOTIPY_CLIENT_ID')
    client_secret = os.getenv('SPOTIPY_CLIENT_SECRET')
    redirect_uri = os.getenv('SPOTIPY_REDIRECT_URI')
    sp_oauth = oauth2.SpotifyOAuth(client_id, client_secret, redirect_uri,
                                   scope=scope,
                                   cache_path='.cache-' + data.username)
    token_info = sp_oauth.get_cached_token()
    if not token_info:
        auth_url = sp_oauth.get_authorize_url()
        webbrowser.open(auth_url)
        msg = 'Enter the URL you were redirected to.'
        title = 'Authorize'
        response = simpledialog.askstring(title, msg)
        code = sp_oauth.parse_response_code(response)
        token_info = sp_oauth.get_access_token(code)
    data.tokens[scope] = token_info['access_token']


################################################################################

# gist.github.com/j4mie/557354

def normalize(s):
    if (isinstance(s, str)):
        return (unicodedata.normalize('NFKD', s).encode('ASCII',
                'ignore').decode('utf-8', 'ignore'))


################################################################################

<<<<<<< HEAD
# github.com/plamere/spotipy/tree/master/examples
=======

>>>>>>> origin/master

client_credentials_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)


def get_top_songs(data):
    sp = spotipy.Spotify(auth=data.tokens['user-top-read'])
    sp.trace = False
    for term in data.top_songs:
        results = sp.current_user_top_tracks(time_range=term, limit=50)
        for song in results['items']:
            data.top_songs[term] += [song['id']]
            data.top_songs_all_set.add(song['id'])
            if song['id'] not in data.all_songs_features:
                features = sp.audio_features([song['id']])[0]
                data.all_songs_features[song['id']] = {
                    'name': normalize(song['name']),
                    'artist_id': normalize(song['artists'][0]['id']),
                    'artist_name': normalize(song['artists'][0]['name']),
                    'album_name': normalize(song['album']['name']),
                    'track_number': normalize(song['track_number']),
                    'duration_ms': normalize(song['duration_ms']),
                    'popularity': normalize(song['popularity']),
                    'danceability': normalize(features['danceability']),
                    'energy': normalize(features['energy']),
                    'loudness': normalize(features['loudness']),
                    'speechiness': normalize(features['speechiness']),
                    'acousticness': normalize(features['acousticness']),
                    'instrumentalness': normalize(features['instrumentalness']),
                    'liveness': normalize(features['liveness']),
                    'valence': normalize(features['valence']),
                    'tempo': normalize(features['tempo'])}
    data.top_songs_all += sorted(list(data.top_songs_all_set))


def get_top_artists(data):
    sp = spotipy.Spotify(auth=data.tokens['user-top-read'])
    sp.trace = False
    for term in data.top_artists:
        results = sp.current_user_top_artists(time_range=term, limit=50)
        for artist in results['items']:
            data.top_artists[term] += [artist['id']]
            data.top_artists_all_set.add(artist['id'])
            if (artist['id'] not in data.all_artists_features):
                data.all_artists_features[artist['id']] = {
                    'name': artist['name'], 'top_songs': []}
                artist_top_songs = sp.artist_top_tracks(artist['id'])
                for song in artist_top_songs['tracks']:
                    data.all_artists_features[artist['id']]['top_songs'] += [
                        song['id']]
                    if song['id'] not in data.all_songs_features:
                        features = sp.audio_features([song['id']])[0]
                        data.all_songs_features[song['id']] = {
                            'name': normalize(song['name']),
                            'artist_id': normalize(song['artists'][0]['id']),
                            'artist_name': normalize(
                                song['artists'][0]['name']),
                            'album_name': normalize(song['album']['name']),
                            'track_number': normalize(song['track_number']),
                            'duration_ms': normalize(song['duration_ms']),
                            'popularity': normalize(song['popularity']),
                            'danceability': normalize(features['danceability']),
                            'energy': normalize(features['energy']),
                            'loudness': normalize(features['loudness']),
                            'speechiness': normalize(features['speechiness']),
                            'acousticness': normalize(features['acousticness']),
                            'instrumentalness': normalize(
                                features['instrumentalness']),
                            'liveness': normalize(features['liveness']),
                            'valence': normalize(features['valence']),
                            'tempo': normalize(features['tempo'])}
    data.top_artists_all += sorted(list(data.top_artists_all_set))


<<<<<<< HEAD
################################################################################

def organize_init(data):
    analyze_clean(data)
=======

################################################################################

def organize_init(data):
    organize_clean(data)
>>>>>>> origin/master
    data.mode = 'organize'
    data.scale = 6
    data.vertical1_scale = 1 / (data.scale + 3)
    data.vertical2_scale = (data.scale - 2) / (data.scale - 1)
    organize_left_sidebar_buttons(data)
    organize_buttons(data)
    organize_headers(data)


<<<<<<< HEAD
def analyze_clean(data):
    organize_clear(data)
    selected_clear(data)
    del data.songs_id[:]    
    del data.songs[:]    
    del data.artists_id[:]    
    del data.artists[:]  
    del data.artist_top_songs_id[:]    
    del data.artist_top_songs[:]
=======
def organize_clean(data):
    clear_view(data)
    clear_selected(data)
    del data.analyze_songs_id[:]    
    del data.analyze_songs[:]    
    del data.analyze_artists_id[:]    
    del data.analyze_artists[:]  
    del data.analyze_artist_top_songs_id[:]    
    del data.analyze_artist_top_songs[:]
>>>>>>> origin/master
    del data.sources[:]
    del data.parameters[:]
    del data.charts[:]
    del data.values[:]
<<<<<<< HEAD
=======
    del data.source[:]
>>>>>>> origin/master


def organize_left_sidebar_buttons(data):
    del data.left_sidebar_buttons[:]
    data.left_sidebar_buttons += [
        LeftSidebar(data, data.top_songs_all, 1, 'TOP SONGS'),
        LeftSidebar(data, data.top_songs['short_term'], 2, 'Short Term'),
        LeftSidebar(data, data.top_songs['medium_term'], 3, 'Medium Term'),
        LeftSidebar(data, data.top_songs['long_term'], 4, 'Long Term'),
        LeftSidebar(data, data.top_artists_all, 6, 'TOP ARTISTS'),
        LeftSidebar(data, data.top_artists['short_term'], 7, 'Short Term'),
        LeftSidebar(data, data.top_artists['medium_term'], 8, 'Medium Term'),
        LeftSidebar(data, data.top_artists['long_term'], 9, 'Long Term')]


def organize_buttons(data):
    del data.buttons[:]
    data.buttons += [
        Button(data, (data.vertical2_scale + 1) / 2, 1 / 30, green, green_hover,
<<<<<<< HEAD
               '+ ADD TO STAGING PLAYLIST +', white, white, 10, stage_add),
        Button(data, (data.vertical2_scale + 1) / 2, 1 / 11.5, red, red_hover,
               '- REMOVE FROM STAGING PLAYLIST -', white, white, 10,
               stage_remove),
=======
               '+ ADD TO STAGING PLAYLIST +', white, white, 10, add_to_stage),
        Button(data, (data.vertical2_scale + 1) / 2, 1 / 11.5, red, red_hover,
               '- REMOVE FROM STAGING PLAYLIST -', white, white, 10,
               remove_from_stage),
>>>>>>> origin/master
        Button(data, (data.vertical2_scale + 1) / 2, 29 / 30, blue, blue_hover,
               'ANALYZE PLAYLISTS', white, white, 10, analyze_init)]


def organize_headers(data):
    del data.headers[:]
<<<<<<< HEAD
    if (data.is_songs):
        data.headers += [Header(data, 0, 'TITLE', songs_by_title),
                         Header(data, 1, 'ARTIST', songs_by_artist),
                         Header(data, 2, 'ALBUM', songs_by_album)]
    
    elif (data.is_artists):
        data.headers += [
            Header(data, 0, 'ARTIST', artists_by_name),
            Header(data, 1, 'TITLE', artist_top_songs_by_title),
            Header(data, 2, 'ALBUM', artist_top_songs_by_album)]
=======
    if (data.is_viewing_songs):
        data.headers += [Header(data, 0, 'TITLE', sort_songs_by_name),
                         Header(data, 1, 'ARTIST', sort_songs_by_artist),
                         Header(data, 2, 'ALBUM', sort_songs_by_album)]
    elif (data.is_viewing_artists):
        data.headers += [
            Header(data, 0, 'ARTIST', sort_artists_by_name),
            Header(data, 1, 'TITLE', sort_artist_top_songs_by_title),
            Header(data, 2, 'ALBUM', sort_artist_top_songs_by_album)]
>>>>>>> origin/master


def organize_mouse_moved(data):
    for left_sidebar_button in data.left_sidebar_buttons:
        if (left_sidebar_button.is_within_bounds(data, data.mouse_moved_x,
                                                 data.mouse_moved_y)):
            left_sidebar_button.hover()
        else:
            left_sidebar_button.unhover()

    for header in data.headers:
        if (header.is_within_bounds(data, data.mouse_moved_x,
                                    data.mouse_moved_y)):
            header.hover()
        else:
            header.unhover()

    for button in data.buttons:
        if (button.is_within_bounds(data, data.mouse_moved_x,
                                    data.mouse_moved_y)):
            button.hover()
        else:
            button.unhover()

    for song in data.stage:
        if (song.is_within_bounds(data, data.mouse_moved_x,
                                  data.mouse_moved_y)):
            song.hover()
        else:
            song.unhover()

<<<<<<< HEAD
    if (data.is_songs):
        for organize_song in data.songs:
            if (organize_song.is_within_bounds(data, data.mouse_moved_x,
                                              data.mouse_moved_y)):
                organize_song.hover()
            else:
                organize_song.unhover()

    elif (data.is_artists):
        for organize_artist in data.artists:
            if (organize_artist.is_within_bounds(data, data.mouse_moved_x,
                                                data.mouse_moved_y)):
                organize_artist.hover()
            else:
                organize_artist.unhover()

        if (data.is_artist_top_songs):
            for artist_top_song in data.artist_top_songs:
                if (artist_top_song.is_within_bounds(data,
                        data.mouse_moved_x, data.mouse_moved_y)):
                    artist_top_song.hover()
                else:
                    artist_top_song.unhover()
=======
    if (data.is_viewing_songs):
        for viewing_song in data.viewing_songs:
            if (viewing_song.is_within_bounds(data, data.mouse_moved_x,
                                              data.mouse_moved_y)):
                viewing_song.hover()
            else:
                viewing_song.unhover()

    elif (data.is_viewing_artists):
        for viewing_artist in data.viewing_artists:
            if (viewing_artist.is_within_bounds(data, data.mouse_moved_x,
                                                data.mouse_moved_y)):
                viewing_artist.hover()
            else:
                viewing_artist.unhover()

        if (data.is_viewing_artist_top_songs):
            for viewing_artist_top_song in data.viewing_artist_top_songs:
                if (viewing_artist_top_song.is_within_bounds(data,
                        data.mouse_moved_x, data.mouse_moved_y)):
                    viewing_artist_top_song.hover()
                else:
                    viewing_artist_top_song.unhover()
>>>>>>> origin/master


def organize_left_released(data):
    for left_sidebar_button in data.left_sidebar_buttons:
        if (left_sidebar_button.is_within_bounds(data, data.left_released_x,
                                                 data.left_released_y) and
            left_sidebar_button.is_within_bounds(data, data.left_pressed_x,
                                                 data.left_pressed_y)):
            left_sidebar_button.select(data)
        elif (data.left_released_x <= data.width * data.vertical1_scale):
            left_sidebar_button.unselect(data)

    for header in data.headers:
        if (header.is_within_bounds(data, data.left_released_x,
                                    data.left_released_y) and
            header.is_within_bounds(data, data.left_pressed_x,
                                    data.left_pressed_y)):
            header.select(data)

    for button in data.buttons:
        if (button.is_within_bounds(data, data.left_released_x,
                                    data.left_released_y) and
            button.is_within_bounds(data, data.left_pressed_x,
                                    data.left_pressed_y)):
            button.select(data)

    for song in data.stage:
        if (song.is_within_bounds(data, data.left_released_x,
                                  data.left_released_y) and
            song.is_within_bounds(data, data.left_pressed_x,
                                  data.left_pressed_y)):
            song.select(data)
        elif (not (data.ctrl or data.shift)):
            song.unselect(data)

<<<<<<< HEAD
    if (data.is_songs):
        for organize_song in data.songs:
            if (organize_song.is_within_bounds(data, data.left_released_x,
                                              data.left_released_y) and
                organize_song.is_within_bounds(data, data.left_pressed_x,
                                              data.left_pressed_y)):
                organize_song.select(data)
            elif (not (data.ctrl or data.shift)):
                organize_song.unselect(data)

    elif (data.is_artists):
        for organize_artist in data.artists:
            if (organize_artist.is_within_bounds(data, data.left_released_x,
                                                data.left_released_y) and
                organize_artist.is_within_bounds(data, data.left_pressed_x,
                                                data.left_pressed_y)):
                organize_artist.select(data)
            elif (not (data.ctrl or data.shift)):
                organize_artist.unselect(data)

        if (data.is_artist_top_songs):
            for artist_top_song in data.artist_top_songs:
                if (artist_top_song.is_within_bounds(data,
                        data.left_released_x, data.left_released_y) and
                        artist_top_song.is_within_bounds(data,
                        data.left_pressed_x, data.left_pressed_y)):
                    artist_top_song.select(data)
                elif (not (data.ctrl or data.shift)):
                    artist_top_song.unselect(data)
=======
    if (data.is_viewing_songs):
        for viewing_song in data.viewing_songs:
            if (viewing_song.is_within_bounds(data, data.left_released_x,
                                              data.left_released_y) and
                viewing_song.is_within_bounds(data, data.left_pressed_x,
                                              data.left_pressed_y)):
                viewing_song.select(data)
            elif (not (data.ctrl or data.shift)):
                viewing_song.unselect(data)

    elif (data.is_viewing_artists):
        for viewing_artist in data.viewing_artists:
            if (viewing_artist.is_within_bounds(data, data.left_released_x,
                                                data.left_released_y) and
                viewing_artist.is_within_bounds(data, data.left_pressed_x,
                                                data.left_pressed_y)):
                viewing_artist.select(data)
            elif (not (data.ctrl or data.shift)):
                viewing_artist.unselect(data)

        if (data.is_viewing_artist_top_songs):
            for viewing_artist_top_song in data.viewing_artist_top_songs:
                if (viewing_artist_top_song.is_within_bounds(data,
                        data.left_released_x, data.left_released_y) and
                        viewing_artist_top_song.is_within_bounds(data,
                        data.left_pressed_x, data.left_pressed_y)):
                    viewing_artist_top_song.select(data)
                elif (not (data.ctrl or data.shift)):
                    viewing_artist_top_song.unselect(data)
>>>>>>> origin/master


def organize_key_pressed(data):
    if (data.keysym_pressed == 'Escape'):
<<<<<<< HEAD
        selected_clear(data)
    elif (data.is_songs):
        songs_key_pressed(data)
    elif (data.is_artists):
        artists_key_pressed(data)


def songs_key_pressed(data):
    if ((not data.ctrl) and (not data.shift)):
        if ((data.keysym_pressed == 'Up') and (data.start > 0)):
            data.start -= 1
        elif (data.keysym_pressed == 'Down'):
            data.start += 1
        organize_songs(data)


def artists_key_pressed(data):
    if ((not data.ctrl) and (not data.shift)):
        if ((data.keysym_pressed == 'Up') and (data.start > 0)):
            data.start -= 1
        elif (data.keysym_pressed == 'Down'):
            data.start += 1
        organize_artists(data)
=======
        clear_selected(data)
    elif (data.is_viewing_songs):
        viewing_songs_key_pressed(data)
    elif (data.is_viewing_artists):
        viewing_artists_key_pressed(data)


def viewing_songs_key_pressed(data):
    if ((not data.ctrl) and (not data.shift)):
        if ((data.keysym_pressed == 'Up') and (data.viewing_songs_start > 0)):
            data.viewing_songs_start -= 1
        elif (data.keysym_pressed == 'Down'):
            data.viewing_songs_start += 1
        view_songs(data)


def viewing_artists_key_pressed(data):
    if ((not data.ctrl) and (not data.shift)):
        if ((data.keysym_pressed == 'Up') and (data.viewing_artists_start > 0)):
            data.viewing_artists_start -= 1
        elif (data.keysym_pressed == 'Down'):
            data.viewing_artists_start += 1
        view_artists(data)
>>>>>>> origin/master


def organize_draw(canvas, data):
    x1 = data.width * data.vertical1_scale
    x2 = data.width * data.vertical2_scale
    background = black_background
    canvas.create_rectangle(0, 0, data.width, data.height, fill=black_shadow)
    canvas.create_rectangle(x1, 0, x2, data.height, fill=background, width=0)
    for left_sidebar_button in data.left_sidebar_buttons:
        left_sidebar_button.draw(canvas, data)
    for header in data.headers:
        header.draw(canvas, data)
    for button in data.buttons:
        button.draw(canvas, data)
<<<<<<< HEAD
    for organize_song in data.songs:
        organize_song.draw(canvas, data)
    for organize_artist in data.artists:
        organize_artist.draw(canvas, data)
    for artist_top_song in data.artist_top_songs:
        artist_top_song.draw(canvas, data)
=======
    for viewing_song in data.viewing_songs:
        viewing_song.draw(canvas, data)
    for viewing_artist in data.viewing_artists:
        viewing_artist.draw(canvas, data)
    for viewing_artist_top_song in data.viewing_artist_top_songs:
        viewing_artist_top_song.draw(canvas, data)
>>>>>>> origin/master
    for song in data.stage:
        song.draw(canvas, data)


################################################################################

<<<<<<< HEAD
def organize_clear(data, songs=True, artists=True, artist_top_songs=True):
    if (songs):
        del data.songs[:]
    if (artists):
        del data.artists[:]
    if (artist_top_songs):
        del data.artist_top_songs[:]


def organize_songs(data):
    organize_clear(data)
    for y_position, song_id in enumerate(
            data.songs_id[data.start:]):
        data.songs += [OrganizeSong(data, y_position + 2, song_id)]
    organize_headers(data)


def organize_artists(data):
    organize_clear(data)
    for y_position, artist_id in enumerate(
            data.artists_id[data.start:]):
        data.artists += [OrganizeArtist(data, y_position + 2, artist_id)]
    organize_headers(data)


def artist_top_songs(data):
    organize_clear(data, True, False, False)
    for y_position, song in enumerate(data.artist_top_songs_id[
                                      :data.artist_top_songs_end]):
        data.artist_top_songs += [
            OrganizeArtistTopSong(data, y_position + 2, song)]
=======
def clear_view(data, songs=True, artists=True, artist_top_songs=True):
    if (songs):
        del data.viewing_songs[:]
    if (artists):
        del data.viewing_artists[:]
    if (artist_top_songs):
        del data.viewing_artist_top_songs[:]


def view_songs(data):
    clear_view(data)
    for y_position, song_id in enumerate(
            data.viewing_songs_id[data.viewing_songs_start:]):
        data.viewing_songs += [ViewingSong(data, y_position + 2, song_id)]
    organize_headers(data)


def view_artists(data):
    clear_view(data)
    for y_position, artist_id in enumerate(
            data.viewing_artists_id[data.viewing_artists_start:]):
        data.viewing_artists += [ViewingArtist(data, y_position + 2, artist_id)]
    organize_headers(data)


def view_artist_top_songs(data):
    clear_view(data, True, False, False)
    for y_position, song in enumerate(data.viewing_artist_top_songs_id[
                                      :data.viewing_artist_top_songs_end]):
        data.viewing_artist_top_songs += [
            ViewingArtistTopSong(data, y_position + 2, song)]
>>>>>>> origin/master
    organize_headers(data)


################################################################################

<<<<<<< HEAD
def songs_by_title(data):
    organize_clear(data)
    if (data.sort_mode == 0):
        del data.songs_id_original[:]
        data.songs_id_original += data.songs_id
=======
def sort_songs_by_name(data):
    clear_view(data)
    if (data.sort_mode == 0):
        del data.original_viewing_songs[:]
        data.original_viewing_songs += data.viewing_songs_id
>>>>>>> origin/master
        data.sort_mode = 1
    elif (data.sort_mode == 1):
        data.sort_mode = 2
    elif (data.sort_mode == 2):
        if (data.is_overall):
            data.sort_mode = 1
        else:
            data.sort_mode = 0
    else:
        data.sort_mode = 1

    result = []
    if (data.sort_mode == 0):
<<<<<<< HEAD
        result += data.songs_id_original
    elif (data.sort_mode == 1):
        sorting_dictionary = {}
        for song_id in data.songs_id:
=======
        result += data.original_viewing_songs
    elif (data.sort_mode == 1):
        sorting_dictionary = {}
        for song_id in data.viewing_songs_id:
>>>>>>> origin/master
            name = data.all_songs_features[song_id]['name']
            if (name in sorting_dictionary):
                sorting_dictionary[name] += [song_id]
            else:
                sorting_dictionary[name] = [song_id]
        for name in sorted(sorting_dictionary.keys()):
            result += sorted(sorting_dictionary[name])
    elif (data.sort_mode == 2):
<<<<<<< HEAD
        result += data.songs_id[::-1]

    del data.songs_id[:]
    data.songs_id += result
    data.start = 0
    organize_songs(data)


def songs_by_artist(data):
    organize_clear(data)
    if (data.sort_mode == 0):
        del data.songs_id_original[:]
        data.songs_id_original += data.songs_id
=======
        result += data.viewing_songs_id[::-1]

    del data.viewing_songs_id[:]
    data.viewing_songs_id += result
    data.viewing_songs_start = 0
    view_songs(data)


def sort_songs_by_artist(data):
    clear_view(data)
    if (data.sort_mode == 0):
        del data.original_viewing_songs[:]
        data.original_viewing_songs += data.viewing_songs_id
>>>>>>> origin/master
        data.sort_mode = 3
    elif (data.sort_mode == 3):
        data.sort_mode = 4
    elif (data.sort_mode == 4):
        if (data.is_overall):
            data.sort_mode = 3
        else:
            data.sort_mode = 0
    else:
        data.sort_mode = 3

    result = []
    if (data.sort_mode == 0):
<<<<<<< HEAD
        result += data.songs_id_original
    elif (data.sort_mode == 3):
        sorting_dictionary = {}
        for song_id in data.songs_id:
=======
        result += data.original_viewing_songs
    elif (data.sort_mode == 3):
        sorting_dictionary = {}
        for song_id in data.viewing_songs_id:
>>>>>>> origin/master
            artist = data.all_songs_features[song_id]['artist_name']
            if (artist in sorting_dictionary):
                sorting_dictionary[artist] += [song_id]
            else:
                sorting_dictionary[artist] = [song_id]
        for artist in sorted(sorting_dictionary.keys()):
            result += sorted(sorting_dictionary[artist])
    elif (data.sort_mode == 4):
<<<<<<< HEAD
        result += data.songs_id[::-1]

    del data.songs_id[:]
    data.songs_id += result
    data.start = 0
    organize_songs(data)


def songs_by_album(data):
    organize_clear(data)
    if (data.sort_mode == 0):
        del data.songs_id_original[:]
        data.songs_id_original += data.songs_id
=======
        result += data.viewing_songs_id[::-1]

    del data.viewing_songs_id[:]
    data.viewing_songs_id += result
    data.viewing_songs_start = 0
    view_songs(data)


def sort_songs_by_album(data):
    clear_view(data)
    if (data.sort_mode == 0):
        del data.original_viewing_songs[:]
        data.original_viewing_songs += data.viewing_songs_id
>>>>>>> origin/master
        data.sort_mode = 5
    elif (data.sort_mode == 5):
        data.sort_mode = 6
    elif (data.sort_mode == 6):
        if (data.is_overall):
            data.sort_mode = 5
        else:
            data.sort_mode = 0
    else:
        data.sort_mode = 5

    result = []
    if (data.sort_mode == 0):
<<<<<<< HEAD
        result += data.songs_id_original
    elif (data.sort_mode == 5):
        sorting_dictionary = {}
        for song_id in data.songs_id:
=======
        result += data.original_viewing_songs
    elif (data.sort_mode == 5):
        sorting_dictionary = {}
        for song_id in data.viewing_songs_id:
>>>>>>> origin/master
            album = data.all_songs_features[song_id]['album_name']
            if (album in sorting_dictionary):
                sorting_dictionary[album] += [song_id]
            else:
                sorting_dictionary[album] = [song_id]
        for album in sorted(sorting_dictionary.keys()):
            result += sorted(sorting_dictionary[album])
    elif (data.sort_mode == 6):
<<<<<<< HEAD
        result += data.songs_id[::-1]

    del data.songs_id[:]
    data.songs_id += result
    data.start = 0
    organize_songs(data)


def artists_by_name(data):
    organize_clear(data)
    if (data.sort_mode == 0):
        del data.artists_id_original[:]
        data.artists_id_original += data.artists_id
=======
        result += data.viewing_songs_id[::-1]

    del data.viewing_songs_id[:]
    data.viewing_songs_id += result
    data.viewing_songs_start = 0
    view_songs(data)


def sort_artists_by_name(data):
    clear_view(data)
    if (data.sort_mode == 0):
        del data.original_viewing_artists[:]
        data.original_viewing_artists += data.viewing_artists_id
>>>>>>> origin/master
        data.sort_mode = 1
    elif (data.sort_mode == 1):
        data.sort_mode = 2
    elif (data.sort_mode == 2):
        if (data.is_overall):
            data.sort_mode = 1
        else:
            data.sort_mode = 0
    else:
        data.sort_mode = 1

    result = []
    if (data.sort_mode == 0):
<<<<<<< HEAD
        result += data.artists_id_original
    elif (data.sort_mode == 1):
        sorting_dictionary = {}
        for artist_id in data.artists_id:
=======
        result += data.original_viewing_artists
    elif (data.sort_mode == 1):
        sorting_dictionary = {}
        for artist_id in data.viewing_artists_id:
>>>>>>> origin/master
            artist = data.all_artists_features[artist_id]['name']
            if (artist in sorting_dictionary):
                sorting_dictionary[artist] += [artist_id]
            else:
                sorting_dictionary[artist] = [artist_id]
        for artist in sorted(sorting_dictionary.keys()):
            result += sorted(sorting_dictionary[artist])
    elif (data.sort_mode == 2):
<<<<<<< HEAD
        result += data.artists_id[::-1]

    del data.artists_id[:]
    data.artists_id += result
    data.start = 0
    organize_artists(data)


def artist_top_songs_by_title(data):
    if (data.sort_mode_inner == 0):
        del data.artist_top_songs_id_original[:]
        data.artist_top_songs_id_original += data.artist_top_songs_id
        data.sort_mode_inner = 1
    elif (data.sort_mode_inner == 1):
        data.sort_mode_inner = 2
    elif (data.sort_mode_inner == 2):
        data.sort_mode_inner = 0
    else:
        data.sort_mode_inner = 1

    result = []
    if (data.sort_mode_inner == 0):
        result += data.artist_top_songs_id_original
    elif (data.sort_mode_inner == 1):
        sorting_dictionary = {}
        for song_id in data.artist_top_songs_id:
=======
        result += data.viewing_artists_id[::-1]

    del data.viewing_artists_id[:]
    data.viewing_artists_id += result
    data.viewing_artists_start = 0
    view_artists(data)


def sort_artist_top_songs_by_title(data):
    if (data.inner_sort_mode == 0):
        del data.original_viewing_top_songs[:]
        data.original_viewing_top_songs += data.viewing_artist_top_songs_id
        data.inner_sort_mode = 1
    elif (data.inner_sort_mode == 1):
        data.inner_sort_mode = 2
    elif (data.inner_sort_mode == 2):
        data.inner_sort_mode = 0
    else:
        data.inner_sort_mode = 1

    result = []
    if (data.inner_sort_mode == 0):
        result += data.original_viewing_top_songs
    elif (data.inner_sort_mode == 1):
        sorting_dictionary = {}
        for song_id in data.viewing_artist_top_songs_id:
>>>>>>> origin/master
            name = data.all_songs_features[song_id]['name']
            if (name in sorting_dictionary):
                sorting_dictionary[name] += [song_id]
            else:
                sorting_dictionary[name] = [song_id]
        for name in sorted(sorting_dictionary.keys()):
            result += sorted(sorting_dictionary[name])
<<<<<<< HEAD
    elif (data.sort_mode_inner == 2):
        result += data.artist_top_songs_id[::-1]

    del data.artist_top_songs_id[:]
    data.artist_top_songs_id += result
    artist_top_songs(data)


def artist_top_songs_by_album(data):
    if (data.sort_mode_inner == 0):
        del data.artist_top_songs_id_original[:]
        data.artist_top_songs_id_original += data.artist_top_songs_id
        data.sort_mode_inner = 3
    elif (data.sort_mode_inner == 3):
        data.sort_mode_inner = 4
    elif (data.sort_mode_inner == 4):
        data.sort_mode_inner = 0
    else:
        data.sort_mode_inner = 3

    result = []
    if (data.sort_mode_inner == 0):
        result += data.artist_top_songs_id_original
    elif (data.sort_mode_inner == 3):
        sorting_dictionary = {}
        for song_id in data.artist_top_songs_id:
=======
    elif (data.inner_sort_mode == 2):
        result += data.viewing_artist_top_songs_id[::-1]

    del data.viewing_artist_top_songs_id[:]
    data.viewing_artist_top_songs_id += result
    view_artist_top_songs(data)


def sort_artist_top_songs_by_album(data):
    if (data.inner_sort_mode == 0):
        del data.original_viewing_top_songs[:]
        data.original_viewing_top_songs += data.viewing_artist_top_songs_id
        data.inner_sort_mode = 3
    elif (data.inner_sort_mode == 3):
        data.inner_sort_mode = 4
    elif (data.inner_sort_mode == 4):
        data.inner_sort_mode = 0
    else:
        data.inner_sort_mode = 3

    result = []
    if (data.inner_sort_mode == 0):
        result += data.original_viewing_top_songs
    elif (data.inner_sort_mode == 3):
        sorting_dictionary = {}
        for song_id in data.viewing_artist_top_songs_id:
>>>>>>> origin/master
            album = data.all_songs_features[song_id]['album_name']
            if (album in sorting_dictionary):
                sorting_dictionary[album] += [song_id]
            else:
                sorting_dictionary[album] = [song_id]
        for album in sorted(sorting_dictionary.keys()):
            result += sorted(sorting_dictionary[album])
<<<<<<< HEAD
    elif (data.sort_mode_inner == 4):
        result += data.artist_top_songs_id[::-1]

    del data.artist_top_songs_id[:]
    data.artist_top_songs_id += result
    artist_top_songs(data)
=======
    elif (data.inner_sort_mode == 4):
        result += data.viewing_artist_top_songs_id[::-1]

    del data.viewing_artist_top_songs_id[:]
    data.viewing_artist_top_songs_id += result
    view_artist_top_songs(data)
>>>>>>> origin/master


################################################################################

<<<<<<< HEAD
def selected_clear(data):
    del data.songs_id_selected[:]
    del data.artists_id_selected[:]
    del data.artist_top_songs_id_selected[:]


def stage_add(data):
    for song_id in (data.songs_id_selected + data.artist_top_songs_id_selected):
        if (song_id not in data.stage_id):
            data.stage_id += [song_id]
    for artist_id in data.artists_id_selected:
        for song_id in data.all_artists_features[artist_id]['top_songs'][
                       :data.artist_top_songs_end]:
            if (song_id not in data.stage_id):
                data.stage_id += [song_id]
    selected_clear(data)
    stage(data)


def stage_remove(data):
    for song_id in data.songs_id_selected:
        if (song_id in data.stage_id):
            data.stage_id.remove(song_id)
    for song_id in data.artist_top_songs_id_selected:
        if (song_id in data.stage_id):
            data.stage_id.remove(song_id)
    selected_clear(data)
    stage(data)


def stage_clear(data):
    del data.stage_id[:]
    stage(data)


def stage(data):
    del data.stage[:]
    for y_position, song_id in enumerate(data.stage_id):
=======
def clear_selected(data):
    del data.selected_songs[:]
    del data.selected_artists[:]
    del data.selected_artist_top_songs[:]


def add_to_stage(data):
    for song_id in (data.selected_songs + data.selected_artist_top_songs):
        if (song_id not in data.stage_id):
            data.stage_id += [song_id]
    for artist_id in data.selected_artists:
        for song_id in data.all_artists_features[artist_id]['top_songs'][
                       :data.viewing_artist_top_songs_end]:
            if (song_id not in data.stage_id):
                data.stage_id += [song_id]
    clear_selected(data)
    view_stage(data)


def remove_from_stage(data):
    for song_id in data.selected_songs:
        if (song_id in data.stage_id):
            data.stage_id.remove(song_id)
    for song_id in data.selected_artist_top_songs:
        if (song_id in data.stage_id):
            data.stage_id.remove(song_id)
    clear_selected(data)
    view_stage(data)


def clear_stage(data):
    del data.stage_id[:]
    view_stage(data)


def view_stage(data):
    del data.stage[:]
    for y_position, song_id in enumerate(data.stage_id[:data.stage_end]):
>>>>>>> origin/master
        data.stage += [StageSong(data, y_position, song_id)]


################################################################################

class Source(object):
    def __init__(self, data, y_position, text, source, function):
        self.is_selected_source = False
        self.y_position = y_position
        self.x1 = self.y1 = self.x2 = self.y2 = self.cy = 0
        self.width = self.height = 0
        self.text = text
        self.text_fill = gray
        self.source = copy.deepcopy(source)
        self.function = function
        self.update_dimensions(data)

    def update_dimensions(self, data):
        self.width = data.width / data.scale
        self.height = data.width / data.scale ** 2
        self.x1 = 0
        self.y1 = self.y_position * self.height
        self.x2 = self.x1 + self.width
        self.y2 = self.y1 + self.height
        self.cy = (self.y1 + self.y2) / 2

    def is_within_bounds(self, data, x, y):
        self.update_dimensions(data)
        return ((self.x1 <= x <= self.x2) and (self.y1 <= y <= self.y2))

    def is_selected(self):
        return self.is_selected_source

<<<<<<< HEAD
=======
    def get_source(self):
        return self.source

>>>>>>> origin/master
    def hover(self):
        self.text_fill = white

    def unhover(self):
        if (not self.is_selected_source):
            self.text_fill = gray

    def select(self, data):
        self.is_selected_source = not self.is_selected_source
        if (self.is_selected_source):
            self.text_fill = white
            del data.source[:]
            data.source += self.source
            self.function(data)
        else:
            self.text_fill = gray
            del data.values[:]

    def unselect(self, data):
        self.is_selected_source = False
        self.text_fill = gray

    def draw(self, canvas, data):
        self.update_dimensions(data)
        canvas.create_text(data.scale * 2, self.cy, text=self.text,
                           fill=self.text_fill, anchor=W,
                           font='Proxima %d' % (data.scale + data.scale // 2))
        if (self.is_selected_source):
            canvas.create_rectangle(0, self.y1, data.scale, self.y2, fill=green,
                                    width=0)


################################################################################

class Parameter(object):
    def __init__(self, data, y_position, text, parameter):
        self.is_selected_parameter = False
        self.y_position = y_position
        self.x1 = self.y1 = self.x2 = self.y2 = self.cy = 0
        self.width = self.height = 0
        self.text = text
        self.text_fill = gray
        self.parameter = parameter

    def update_dimensions(self, data):
        self.width = data.width / data.scale
        self.height = data.width / data.scale ** 2
        self.x1 = self.width
        self.y1 = self.y_position * self.height
        self.x2 = self.x1 + self.width
        self.y2 = self.y1 + self.height
        self.cy = (self.y1 + self.y2) / 2

    def is_within_bounds(self, data, x, y):
        self.update_dimensions(data)
        return ((self.x1 <= x <= self.x2) and (self.y1 <= y <= self.y2))

    def is_selected(self):
        return self.is_selected_parameter

    def get_parameter(self):
        return self.parameter

    def hover(self):
        self.text_fill = white

    def unhover(self):
        if (self.is_selected_parameter):
            self.text_fill = white
        else:
            self.text_fill = gray

    def select(self, data):
        self.is_selected_parameter = not self.is_selected_parameter
        if (self.is_selected_parameter):
            self.text_fill = white
            data.parameter = self.parameter
<<<<<<< HEAD
=======
            if (self.y_position < 5):
                analyze_songs(data)
            else:
                analyze_artist(data)
>>>>>>> origin/master
        else:
            self.text_fill = gray
            del data.values[:]

<<<<<<< HEAD
=======

>>>>>>> origin/master
    def unselect(self, data):
        self.is_selected_parameter = False
        self.text_fill = gray

    def draw(self, canvas, data):
        self.update_dimensions(data)
        canvas.create_text(self.x1 + data.scale * 2, self.cy, text=self.text,
                           fill=self.text_fill, anchor=W,
                           font='Proxima %d' % (data.scale + data.scale // 2))
        if (self.is_selected_parameter):
            canvas.create_rectangle(self.x1, self.y1, self.x1 + data.scale / 2,
                                    self.y2, fill=blue, width=0)


################################################################################

class Chart(object):
    def __init__(self, data, y_position, text, function):
        self.is_selected_chart = False
        self.y_position = y_position
        self.x1 = self.y1 = self.x2 = self.y2 = self.cy = 0
        self.width = self.height = 0
        self.text = text
        self.text_fill = gray
        self.function = function

    def update_dimensions(self, data):
        self.width = data.width / data.scale
        self.height = data.width / data.scale ** 2
        self.x1 = 2 * self.width
        self.y1 = self.y_position * self.height
        self.x2 = self.x1 + self.width
        self.y2 = self.y1 + self.height
        self.cy = (self.y1 + self.y2) / 2

    def is_within_bounds(self, data, x, y):
        self.update_dimensions(data)
        return ((self.x1 <= x <= self.x2) and (self.y1 <= y <= self.y2))

    def is_selected(self):
        return self.is_selected_chart

    def get_chart(self):
        return self.chart

    def hover(self):
        self.text_fill = white

    def unhover(self):
        if (not self.is_selected_chart):
            self.text_fill = gray

    def select(self, data):
        self.is_selected_chart = not self.is_selected_chart
        if (self.is_selected_chart):
            self.text_fill = white
        else:
            self.text_fill = gray
        if (len(data.values) > 0):
            self.function(data)


    def unselect(self, data):
        self.is_selected_chart = False
        self.text_fill = gray

    def draw(self, canvas, data):
        self.update_dimensions(data)
        canvas.create_text(self.x1 + data.scale * 2, self.cy, text=self.text,
                           fill=self.text_fill, anchor=W,
                           font='Proxima %d' % (data.scale + data.scale // 2))
        if (self.is_selected_chart):
            canvas.create_rectangle(self.x1, self.y1, self.x1 + data.scale / 2,
                                    self.y2, fill=red, width=0)


################################################################################

# github.com/mwaskom/seaborn/blob/master/examples/timeseries_of_barplots.py

def bar_plot(data):
    pass

# github.com/mwaskom/seaborn/blob/master/examples/grouped_boxplot.py

def box_plot(data):
    pass

# github.com/mwaskom/seaborn/blob/master/examples/distplot_options.py

def distribution_plot(data):
    sns.set(style="dark", palette="muted", color_codes=True)
    rs = np.random.RandomState(10)

    # Set up the matplotlib figure
    f, axes = plt.subplots(1, 1, figsize=(7, 7), sharex=True)
    sns.despine(left=True)

    # Plot a filled kernel density estimate
    sns.distplot(data.values, hist=False, color="g",
                 kde_kws={"shade": True})

    plt.setp(axes, yticks=[])
    plt.tight_layout()
    plt.show()

# github.com/mwaskom/seaborn/blob/master/examples/distplot_options.py

def histogram(data):
    sns.set(style="white", palette="muted", color_codes=True)
    rs = np.random.RandomState(10)

    # Set up the matplotlib figure
    f, axes = plt.subplots(1, 1, figsize=(7, 7), sharex=True)
    sns.despine(left=True)

    # Plot a histogram and kernel density estimate
    sns.distplot(data.values, color="g")

    plt.setp(axes, yticks=[])
    plt.tight_layout()
    plt.show()

# github.com/mwaskom/seaborn/blob/master/examples/paired_pointplots.py

def paired_pointplot(data):
    pass

# github.com/mwaskom/seaborn/blob/master/examples/scatterplot_categorical.py

def scatter_plot(data):
    pass

# github.com/mwaskom/seaborn/blob/master/examples/simple_violinplots.py

def violin_plot(data):
    pass


################################################################################

class AnalyzeSong(object):
    def __init__(self, data, y_position, song_id):
        self.y_position = y_position
        self.x1 = self.y1 = self.x2 = self.x2 = self.cy = 0
        self.width = self.height = 0
        self.song_id = song_id
        self.title = data.all_songs_features[self.song_id]['name']
        self.artist = data.all_songs_features[self.song_id]['artist_name']
        self.album = data.all_songs_features[self.song_id]['album_name']
        if (data.parameter != ''):
            self.value = data.all_songs_features[self.song_id][data.parameter]
        else:
            self.value = ''
        self.update_dimensions(data)

    def update_dimensions(self, data):
        self.width = data.width / data.scale
        self.height = data.width / data.scale ** 2 / 2
        self.x1 = 3 * self.width
        self.y1 = self.y_position * self.height
        self.x2 = self.x1 + self.width * 3
        self.y2 = self.y1 + self.height
        self.cy = (self.y1 + self.y2) / 2

    def draw(self, canvas, data):
        self.update_dimensions(data)
        canvas.create_text(self.x1 + 3 * data.scale, self.cy, text=self.title,
                           fill=white, font='Proxima 8', anchor=W)
        canvas.create_text(self.x1 + self.width + 3 * data.scale, self.cy,
                           text=self.artist, fill=white, font='Proxima 8',
                           anchor=W)
        canvas.create_text(self.x1 + self.width * 2 + 3 * data.scale, self.cy,
                           text=self.album, fill=white, font='Proxima 8',
                           anchor=W)
        canvas.create_text(self.x1 + self.width * 3 + 3 * data.scale, self.cy,
                           text=self.value, fill=white,font='Proxima 8',
                           anchor=W)


################################################################################

class AnalyzeHeader(Header):
    def __init__(self, data, position, text, function):
        super().__init__(data, position, text, function)

    def update_dimensions(self, data):
        self.width = data.width / data.scale
        self.height = 1.25 * data.width / data.scale ** 2
        self.x1 = 3 * self.width + self.position * self.width
        self.y1 = 0
        self.x2 = self.x1 + self.width
        self.y2 = self.height
        self.cy = (self.y1 + self.y2) / 2

    def is_within_bounds(self, data, x, y):
        self.update_dimensions(data)
        return ((self.x1 <= x <= self.x2) and (self.y1 <= y <= self.y2))

    def get_symbol(self, data):
        if (data.sort_mode == 0):
            self.symbol = ''
        elif (self.position == 0):
            if (data.sort_mode == 1):
                self.symbol = '/\\'
            elif (data.sort_mode == 2):
                self.symbol = '\\/'
<<<<<<< HEAD
        elif (data.is_songs):
=======
        elif (data.is_viewing_songs):
>>>>>>> origin/master
            if (self.position == 1):
                if (data.sort_mode == 3):
                    self.symbol = '/\\'
                elif (data.sort_mode == 4):
                    self.symbol = '\\/'
            elif (self.position == 2):
                if (data.sort_mode == 5):
                    self.symbol = '/\\'
                elif (data.sort_mode == 6):
                    self.symbol = '\\/'
            elif (self.position == 3):
                if (data.sort_mode == 7):
                    self.symbol = '/\\'
                elif (data.sort_mode == 8):
                    self.symbol = '\\/'
<<<<<<< HEAD
        elif (data.is_artists):
            if (self.position == 1):
                if (data.sort_mode_inner == 1):
                    self.symbol = '/\\'
                elif (data.sort_mode_inner == 2):
                    self.symbol = '\\/'
            elif (self.position == 2):
                if (data.sort_mode_inner == 3):
                    self.symbol = '/\\'
                elif (data.sort_mode_inner == 4):
                    self.symbol = '\\/'
            elif (self.position == 3):
                if (data.sort_mode_inner == 5):
                    self.symbol = '/\\'
                elif (data.sort_mode_inner == 6):
=======
        elif (data.is_viewing_artists):
            if (self.position == 1):
                if (data.inner_sort_mode == 1):
                    self.symbol = '/\\'
                elif (data.inner_sort_mode == 2):
                    self.symbol = '\\/'
            elif (self.position == 2):
                if (data.inner_sort_mode == 3):
                    self.symbol = '/\\'
                elif (data.inner_sort_mode == 4):
                    self.symbol = '\\/'
            elif (self.position == 3):
                if (data.inner_sort_mode == 5):
                    self.symbol = '/\\'
                elif (data.inner_sort_mode == 6):
>>>>>>> origin/master
                    self.symbol = '\\/'

    def draw(self, canvas, data):
        self.update_dimensions(data)
        self.get_symbol(data)
        canvas.create_text(self.x1 + 3 * data.scale, self.cy, text=self.text,
                           anchor=W, fill=self.text_fill, font='Proxima 10')
        canvas.create_text(self.x1 - data.scale, self.cy, text=self.symbol,
                           fill=green, anchor=W)

################################################################################

def analyze_init(data):
<<<<<<< HEAD
    organize_clean(data)
=======
    analyze_clean(data)
>>>>>>> origin/master
    data.mode = 'analyze'
    data.scale = 7
    analyze_buttons(data)
    analyze_headers(data)
    analyze_sources(data)
    analyze_parameters(data)
    analyze_charts(data)


<<<<<<< HEAD
def organize_clean(data):
    organize_clear(data)
    selected_clear(data)
    data.sort_mode = data.sort_mode_inner = 0
    del data.songs_id_original[:]
    del data.artists_id_original[:]
    del data.artist_top_songs_id_original[:]
    del data.songs_id[:]    
    del data.songs[:]    
    del data.artists_id[:]    
    del data.artists[:]  
    del data.artist_top_songs_id[:]    
    del data.artist_top_songs[:]
    del data.values[:]


=======
def analyze_clean(data):
    clear_view(data)
    clear_selected(data)
    data.sort_mode = data.inner_sort_mode = 0
    del data.original_viewing_songs[:]
    del data.original_viewing_artists[:]
    del data.original_viewing_top_songs[:]
    del data.viewing_songs_id[:]    
    del data.viewing_songs[:]    
    del data.viewing_artists_id[:]    
    del data.viewing_artists[:]  
    del data.viewing_artist_top_songs_id[:]    
    del data.viewing_artist_top_songs[:]
    del data.values[:]

>>>>>>> origin/master
def analyze_buttons(data):
    del data.buttons[:]
    data.buttons += [Button(data, 1 / data.scale / 2, 29 / 30, blue, blue_hover,
                     '<-- GO BACK', white, white, 10, organize_init)]

<<<<<<< HEAD

def analyze_headers(data):
    del data.headers[:]
    data.headers += [
        AnalyzeHeader(data, 0, 'TITLE', analyze_songs_by_title),
        AnalyzeHeader(data, 1, 'ARTIST', analyze_songs_by_artist),
        AnalyzeHeader(data, 2, 'ALBUM', analyze_songs_by_album),
        AnalyzeHeader(data, 3, 'PARAMETER', analyze_songs_by_parameter)]
=======
def analyze_headers(data):
    del data.headers[:]
    data.headers += [
        AnalyzeHeader(data, 0, 'TITLE', analyze_sort_songs_by_title),
        AnalyzeHeader(data, 1, 'ARTIST', analyze_sort_songs_by_artist),
        AnalyzeHeader(data, 2, 'ALBUM', analyze_sort_songs_by_album),
        AnalyzeHeader(data, 3, 'PARAMETER', analyze_sort_songs_by_parameter)]
>>>>>>> origin/master


def analyze_sources(data):
    del data.sources[:]
    data.sources += [
        Source(data, 1, 'TOP SONGS', data.top_songs_all, analyze_songs),
        Source(data, 2, 'Short Term', data.top_songs['short_term'], 
               analyze_songs),
        Source(data, 3, 'Medium Term', data.top_songs['medium_term'],
               analyze_songs),
        Source(data, 4, 'Long Term', data.top_songs['long_term'],
               analyze_songs),
<<<<<<< HEAD
        Source(data, 6, 'TOP ARTISTS', data.top_artists_all, analyze_artists),
        Source(data, 7, 'Short Term', data.top_artists['short_term'],
               analyze_artists),
        Source(data, 8, 'Medium Term', data.top_artists['medium_term'],
               analyze_artists),
        Source(data, 9, 'Long Term', data.top_artists['long_term'],
               analyze_artists),
=======
        Source(data, 6, 'TOP ARTISTS', data.top_artists_all, analyze_artist),
        Source(data, 7, 'Short Term', data.top_artists['short_term'],
               analyze_artist),
        Source(data, 8, 'Medium Term', data.top_artists['medium_term'],
               analyze_artist),
        Source(data, 9, 'Long Term', data.top_artists['long_term'],
               analyze_artist),
>>>>>>> origin/master
        Source(data, 11, 'Staging Playlist', data.stage_id, analyze_songs)]


def analyze_parameters(data):
    del data.parameters[:]
    data.parameters += [Parameter(data, 5, 'Length', 'duration_ms'),
                        Parameter(data, 7, 'Popularity', 'popularity'),
                        Parameter(data, 2, 'Danceability', 'danceability'),
                        Parameter(data, 3, 'Energy', 'energy'),
                        Parameter(data, 6, 'Loudness', 'loudness'),
                        Parameter(data, 8, 'Speechiness', 'speechiness'),
                        Parameter(data, 1, 'Acousticness', 'acousticness'),
                        Parameter(data, 4, 'Liveness', 'liveness'),
                        Parameter(data, 10, 'Valence', 'valence'),
                        Parameter(data, 9, 'Tempo', 'tempo')]


def analyze_charts(data):
    del data.charts[:]
    data.charts += [Chart(data, 3, 'Distribution Plot', distribution_plot),
                    Chart(data, 7, 'Violin Plot', violin_plot),
                    Chart(data, 4, 'Histogram', histogram),
                    Chart(data, 1, 'Bar Plot', bar_plot),
                    Chart(data, 2, 'Box Plot', box_plot),
                    Chart(data, 5, 'Paired Pointplot', paired_pointplot),
                    Chart(data, 6, 'Scatter Plot', scatter_plot)]


def analyze_songs(data):
<<<<<<< HEAD
    data.is_songs = True
    data.is_artists = data.is_artist_top_songs = False
    del data.values[:]
    del data.songs[:]
    for y_position, song_id in enumerate(data.source[data.source_start:]):
        if (data.parameter != ''):
                data.values += [data.all_songs_features[song_id][data.parameter]]
        data.songs += [AnalyzeSong(data, y_position + 2, song_id)]


def analyze_artists(data):
    data.is_songs = False
    data.is_artists = True
=======
    data.is_viewing_songs = True
    data.is_viewing_artists = data.is_viewing_artist_top_songs = False
    del data.values[:]
    del data.analyze_songs[:]
    for y_position, song_id in enumerate(data.source[data.source_start:]):
        if (data.parameter != ''):
            try:
                data.values += [data.all_songs_features[song_id][data.parameter]]
            except:
                continue
        data.analyze_songs += [AnalyzeSong(data, y_position + 2, song_id)]


def analyze_artist(data):
    data.is_viewing_songs = False
    data.is_viewing_artists = True
>>>>>>> origin/master


################################################################################

<<<<<<< HEAD

def analyze_clear(data, songs=True, artists=True, artist_top_songs=True):
    if (songs):
        del data.songs[:]
    if (artists):
        del data.artists[:]
    if (artist_top_songs):
        del data.artist_top_songs[:]


def analyze_songs_by_title(data):
    analyze_clear(data)
    if (data.sort_mode == 0):
        del data.songs_id_original[:]
        data.songs_id_original += data.songs_id
        data.sort_mode = 1
    elif (data.sort_mode == 1):
        data.sort_mode = 2
    elif (data.sort_mode == 2):
        if (data.is_overall):
            data.sort_mode = 1
        else:
            data.sort_mode = 0
    else:
        data.sort_mode = 1

    result = []
    if (data.sort_mode == 0):
        result += data.songs_id_original
    elif (data.sort_mode == 1):
        sorting_dictionary = {}
        for song_id in data.songs_id:
            name = data.all_songs_features[song_id]['name']
            if (name in sorting_dictionary):
                sorting_dictionary[name] += [song_id]
            else:
                sorting_dictionary[name] = [song_id]
        for name in sorted(sorting_dictionary.keys()):
            result += sorted(sorting_dictionary[name])
    elif (data.sort_mode == 2):
        result += data.songs_id[::-1]

    del data.songs_id[:]
    data.songs_id += result
    data.start = 0
    analyze_songs(data)


def analyze_songs_by_artist(data):
    analyze_clear(data)
    if (data.sort_mode == 0):
        del data.songs_id_original[:]
        data.songs_id_original += data.songs_id
        data.sort_mode = 3
    elif (data.sort_mode == 3):
        data.sort_mode = 4
    elif (data.sort_mode == 4):
        if (data.is_overall):
            data.sort_mode = 3
        else:
            data.sort_mode = 0
    else:
        data.sort_mode = 3

    result = []
    if (data.sort_mode == 0):
        result += data.songs_id_original
    elif (data.sort_mode == 3):
        sorting_dictionary = {}
        for song_id in data.songs_id:
            artist = data.all_songs_features[song_id]['artist_name']
            if (artist in sorting_dictionary):
                sorting_dictionary[artist] += [song_id]
            else:
                sorting_dictionary[artist] = [song_id]
        for artist in sorted(sorting_dictionary.keys()):
            result += sorted(sorting_dictionary[artist])
    elif (data.sort_mode == 4):
        result += data.songs_id[::-1]

    del data.songs_id[:]
    data.songs_id += result
    data.start = 0
    analyze_songs(data)


def analyze_songs_by_album(data):
    analyze_clear(data)
    if (data.sort_mode == 0):
        del data.songs_id_original[:]
        data.songs_id_original += data.songs_id
        data.sort_mode = 5
    elif (data.sort_mode == 5):
        data.sort_mode = 6
    elif (data.sort_mode == 6):
        if (data.is_overall):
            data.sort_mode = 5
        else:
            data.sort_mode = 0
    else:
        data.sort_mode = 5

    result = []
    if (data.sort_mode == 0):
        result += data.songs_id_original
    elif (data.sort_mode == 5):
        sorting_dictionary = {}
        for song_id in data.songs_id:
            album = data.all_songs_features[song_id]['album_name']
            if (album in sorting_dictionary):
                sorting_dictionary[album] += [song_id]
            else:
                sorting_dictionary[album] = [song_id]
        for album in sorted(sorting_dictionary.keys()):
            result += sorted(sorting_dictionary[album])
    elif (data.sort_mode == 6):
        result += data.songs_id[::-1]

    del data.songs_id[:]
    data.songs_id += result
    data.start = 0
    analyze_songs(data)


def analyze_songs_by_parameter(data):
    pass


def analyze_artists_by_name(data):
    analyze_clear(data)
    if (data.sort_mode == 0):
        del data.artists_id_original[:]
        data.artists_id_original += data.artists_id
        data.sort_mode = 1
    elif (data.sort_mode == 1):
        data.sort_mode = 2
    elif (data.sort_mode == 2):
        if (data.is_overall):
            data.sort_mode = 1
        else:
            data.sort_mode = 0
    else:
        data.sort_mode = 1

    result = []
    if (data.sort_mode == 0):
        result += data.artists_id_original
    elif (data.sort_mode == 1):
        sorting_dictionary = {}
        for artist_id in data.artists_id:
            artist = data.all_artists_features[artist_id]['name']
            if (artist in sorting_dictionary):
                sorting_dictionary[artist] += [artist_id]
            else:
                sorting_dictionary[artist] = [artist_id]
        for artist in sorted(sorting_dictionary.keys()):
            result += sorted(sorting_dictionary[artist])
    elif (data.sort_mode == 2):
        result += data.artists_id[::-1]

    del data.artists_id[:]
    data.artists_id += result
    data.start = 0
    analyze_artists(data)


def analyze_artist_top_songs_by_title(data):
    if (data.sort_mode_inner == 0):
        del data.artist_top_songs_id_original[:]
        data.artist_top_songs_id_original += data.artist_top_songs_id
        data.sort_mode_inner = 1
    elif (data.sort_mode_inner == 1):
        data.sort_mode_inner = 2
    elif (data.sort_mode_inner == 2):
        data.sort_mode_inner = 0
    else:
        data.sort_mode_inner = 1

    result = []
    if (data.sort_mode_inner == 0):
        result += data.artist_top_songs_id_original
    elif (data.sort_mode_inner == 1):
        sorting_dictionary = {}
        for song_id in data.artist_top_songs_id:
            name = data.all_songs_features[song_id]['name']
            if (name in sorting_dictionary):
                sorting_dictionary[name] += [song_id]
            else:
                sorting_dictionary[name] = [song_id]
        for name in sorted(sorting_dictionary.keys()):
            result += sorted(sorting_dictionary[name])
    elif (data.sort_mode_inner == 2):
        result += data.artist_top_songs_id[::-1]

    del data.artist_top_songs_id[:]
    data.artist_top_songs_id += result
    analyze_artist_top_songs(data)


def analyze_artist_top_songs_by_album(data):
    if (data.sort_mode_inner == 0):
        del data.artist_top_songs_id_original[:]
        data.artist_top_songs_id_original += data.artist_top_songs_id
        data.sort_mode_inner = 3
    elif (data.sort_mode_inner == 3):
        data.sort_mode_inner = 4
    elif (data.sort_mode_inner == 4):
        data.sort_mode_inner = 0
    else:
        data.sort_mode_inner = 3

    result = []
    if (data.sort_mode_inner == 0):
        result += data.artist_top_songs_id_original
    elif (data.sort_mode_inner == 3):
        sorting_dictionary = {}
        for song_id in data.artist_top_songs_id:
            album = data.all_songs_features[song_id]['album_name']
            if (album in sorting_dictionary):
                sorting_dictionary[album] += [song_id]
            else:
                sorting_dictionary[album] = [song_id]
        for album in sorted(sorting_dictionary.keys()):
            result += sorted(sorting_dictionary[album])
    elif (data.sort_mode_inner == 4):
        result += data.artist_top_songs_id[::-1]

    del data.artist_top_songs_id[:]
    data.artist_top_songs_id += result
    analyze_artist_top_songs(data)
=======
def analyze_sort_songs_by_title(data):
    pass


def analyze_sort_songs_by_artist(data):
    pass


def analyze_sort_songs_by_album(data):
    pass


def analyze_sort_songs_by_parameter(data):
    pass


def analyze_sort_artists_by_name(data):
    pass


def analyze_sort_artist_top_songs_by_name(data):
    pass


def analyze_sort_artist_top_songs_by_album(data):
    pass
>>>>>>> origin/master


################################################################################

def analyze_mouse_moved(data):
    for button in data.buttons:
        if (button.is_within_bounds(data, data.mouse_moved_x,
                                    data.mouse_moved_y)):
            button.hover()
        else:
            button.unhover()

    for header in data.headers:
        if (header.is_within_bounds(data, data.mouse_moved_x,
                                    data.mouse_moved_y)):
            header.hover()
        else:
            header.unhover()

    for source in data.sources:
        if (source.is_within_bounds(data, data.mouse_moved_x,
                                    data.mouse_moved_y)):
            source.hover()
        else:
            source.unhover()

    for parameter in data.parameters:
        if (parameter.is_within_bounds(data, data.mouse_moved_x,
                                       data.mouse_moved_y)):
            parameter.hover()
        else:
            parameter.unhover()

    for chart in data.charts:
        if (chart.is_within_bounds(data, data.mouse_moved_x,
                                   data.mouse_moved_y)):
            chart.hover()
        else:
            chart.unhover()


def analyze_left_moved(data):
    pass


def analyze_left_pressed(data):
    pass


def analyze_left_released(data):
    for button in data.buttons:
        if (button.is_within_bounds(data, data.left_released_x,
                                    data.left_released_y) and 
            button.is_within_bounds(data, data.left_pressed_x,
                                    data.left_pressed_y)):
            button.select(data)

    for header in data.headers:
        if (header.is_within_bounds(data, data.left_released_x,
                                    data.left_released_y) and 
            header.is_within_bounds(data, data.left_pressed_x,
                                    data.left_pressed_y)):
            header.select(data)

    if (data.left_released_x <= data.width / data.scale):
        for source in data.sources:
            if (source.is_within_bounds(data, data.left_released_x,
                                        data.left_released_y) and 
                source.is_within_bounds(data, data.left_pressed_x,
                                        data.left_pressed_y)):
                source.select(data)
            else:
                source.unselect(data)

    elif (data.left_released_x <= 2 * data.width / data.scale):
        for parameter in data.parameters:
            if (parameter.is_within_bounds(data, data.left_released_x,
                                           data.left_released_y) and 
                parameter.is_within_bounds(data, data.left_pressed_x,
                                           data.left_pressed_y)):
                parameter.select(data)
            else:
                parameter.unselect(data)

    elif (data.left_released_x <= 3 * data.width / data.scale):
        for chart in data.charts:
            if (chart.is_within_bounds(data, data.left_released_x,
                                       data.left_released_y) and 
                chart.is_within_bounds(data, data.left_pressed_x,
                                       data.left_pressed_y)):
                chart.select(data)
            else:
                chart.unselect(data)


def analyze_right_moved(data):
    pass


def analzye_right_pressed(data):
    pass


def analyze_right_released(data):
    pass


def analyze_key_pressed(data):
    pass


def analyze_key_released(data):
    pass


def analyze_timer_fired(data):
    pass


################################################################################

def analyze_draw(canvas, data):
    canvas.create_rectangle(0, 0, data.width, data.height, fill=black_shadow,
                            width=0)
    canvas.create_line(1 * data.width / data.scale, 0,
                       1 * data.width / data.scale, data.height,
                       fill=gray_hover)
    canvas.create_line(2 * data.width / data.scale, 0,
                       2 * data.width / data.scale, data.height,
                       fill=gray_hover)
    canvas.create_line(3 * data.width / data.scale, 0,
                       3 * data.width / data.scale, data.height,
                       fill=gray_hover)
    canvas.create_line(4 * data.width / data.scale, 0,
                       4 * data.width / data.scale, data.height,
                       fill=gray_hover)
    canvas.create_line(5 * data.width / data.scale, 0,
                       5 * data.width / data.scale, data.height,
                       fill=gray_hover)
    canvas.create_line(6 * data.width / data.scale, 0,
                       6 * data.width / data.scale, data.height,
                       fill=gray_hover)
<<<<<<< HEAD

=======
>>>>>>> origin/master
    for button in data.buttons:
        button.draw(canvas, data)
    for header in data.headers:
        header.draw(canvas, data)
    for source in data.sources:
        source.draw(canvas, data)
    for parameter in data.parameters:
        parameter.draw(canvas, data)
    for chart in data.charts:
        chart.draw(canvas, data)
<<<<<<< HEAD
    for song in data.songs:
=======
    for song in data.analyze_songs:
>>>>>>> origin/master
        song.draw(canvas, data)


################################################################################

run()
<<<<<<< HEAD
=======

################################################################################
>>>>>>> origin/master
