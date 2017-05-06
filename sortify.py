################################################################################

# Stephanie K. Ananth (sananth)

################################################################################

import copy
import json
import math
import os
import unicodedata
import webbrowser
from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog

import matplotlib

import spotipy
import spotipy.oauth2 as oauth2
import spotipy.util as util

matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

################################################################################

# Credentials from developer.spotify.com

os.environ['SPOTIPY_CLIENT_ID'] = '5c14698fcf8e41adb4f39b5518e55100'
os.environ['SPOTIPY_CLIENT_SECRET'] = '355d085eaf6049a1bda2e8dff93bdefd'
os.environ['SPOTIPY_REDIRECT_URI'] = 'https://www.spotify.com/us/'


################################################################################

# Adapted from:
# cs.cmu.edu/~112/notes/keyEventsDemo.py
# cs.cmu.edu/~112/notes/mouseEventsDemo.py
# cs.cmu.edu/~112/notes/resizableDemo.py


def run(width=825, height=510):
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
        # Pause, then call timer_fired again
        canvas.after(data.timer_delay, timer_fired_wrapper, canvas, data)

    # Create the root before data is initialized because data contains an image
    root = Tk()

    # Set up data and call init
    class Struct(object):
        pass

    data = Struct()
    data.width = width
    data.height = height
    data.timer_delay = 100  # milliseconds
    init(data)

    # Create the resizeable canvas
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.pack(fill=BOTH, expand=YES)

    # Set up events
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

    # 4 extra pixels for frame boundaries
    def size_changed(event):
        data.width = event.width - 4
        data.height = event.height - 4
        redraw_all_wrapper(canvas, data)

        # Resizes buttons with canvas after they have been initizlized
        if (data.mode == 'simplify'):
            simplify_buttons(data)

    root.bind('<Configure>', size_changed)
    root.minsize(785 + 4, 485 + 4)

    timer_fired_wrapper(canvas, data)
    # Launch the program
    root.mainloop()  # Blocks until window is closed
    print('Bye!')


################################################################################

# MODEL
# Store variables in data, a Struct, for easy access


def init(data):
    # MODEL
    data.songs = dict()
    data.songs_top = dict()
    data.top_songs = list()
    data.artists = dict()
    data.artists_top = dict()
    data.top_artists = list()
    data.playlists = dict()

    # VIEW --> LOGIN/HELP
    data.logo = PhotoImage(file='sortify_logo.gif')
    data.logo_scale = math.ceil(data.logo.width() / (data.width / scale ** 2))
    data.logo = data.logo.subsample(data.logo_scale, data.logo_scale)
    data.rows = 30
    data.columns = 20

    # CONTROLLER
    data.mode = 'login'
    data.username = ''
    data.tokens = dict()

    data.ctrl = False
    data.shift = False
    data.is_help = False
    data.is_songs = False
    data.is_artists = True

    # EVENT
    data.mouse_moved_x = 0
    data.mouse_moved_y = 0
    data.left_moved_x = 0
    data.left_moved_y = 0
    data.left_pressed_x = 0
    data.left_pressed_y = 0
    data.left_released_x = 0
    data.left_released_y = 0
    data.keysym_pressed = ''
    data.keysym_released = ''

    data.values = list()
    data.song_ids = list()
    data.stage_ids = list()
    data.artist_ids = list()
    data.artist_song_ids = list()
    data.selected_list = ''
    data.selected_ids = set()
    data.selected_artists = set()
    data.original_ids = list()
    data.analyze_ids = list()

    data.sort_mode = 0
    data.start_list = 0
    data.start_song = 0
    data.end_song = 10
    data.start_artist = 0
    data.end_artist = 50
    data.start_stage = 0
    data.start_values = 0

    # OOP
    data.buttons = login_buttons(data)
    data.sliders = list()
    data.stage_songs = list()
    data.analyze_songs = list()
    data.viewing_songs = list()
    data.viewing_artists = list()
    data.viewing_artist_songs = list()
    data.parameter = 'duration_ms'


################################################################################

# MODEL
# Everything that can/should be reset between modes


def clean(data):
    data.mode = ''
    data.is_songs = False
    data.is_artists = False
    del data.song_ids[:]
    del data.artist_ids[:]
    del data.artist_song_ids[:]
    data.selected_list = ''
    data.selected_ids.clear()
    data.selected_artists.clear()
    del data.original_ids[:]
    data.sort_mode = 0
    data.start_list = 0
    data.start_song = 0
    data.end_song = 10
    data.start_artist = 0
    data.end_artist = 50
    data.start_stage = 0
    del data.values[:]
    del data.song_ids[:]
    del data.artist_ids[:]
    del data.artist_song_ids[:]
    del data.original_ids[:]
    del data.analyze_ids[:]
    del data.buttons[:]
    del data.sliders[:]
    del data.stage_songs[:]
    del data.analyze_songs[:]
    del data.viewing_songs[:]
    del data.viewing_artists[:]
    del data.viewing_artist_songs[:]


################################################################################

# CONTROLLER
# EVENTS

# MOUSE


def mouse_moved(event, data):
    data.mouse_moved_x, data.mouse_moved_y = event.x, event.y
    if (not data.is_help):
        if (data.mode == 'login'):
            login_mouse_moved(data)
        elif (data.mode == 'simplify'):
            simplify_mouse_moved(data)
        elif (data.mode == 'analyze'):
            analyze_mouse_moved(data)


################################################################################

# CONTROLLER
# EVENTS

# LEFT


def left_moved(event, data):
    data.left_moved_x, data.left_moved_y = event.x, event.y
    if (not data.is_help):
        if (data.mode == 'analyze'):
            analyze_left_moved(data)


def left_pressed(event, data):
    data.left_pressed_x, data.left_pressed_y = event.x, event.y
    if (not data.is_help):
        if (data.mode == 'simplify'):
            simplify_left_pressed(data)
        elif (data.mode == 'analyze'):
            analyze_left_pressed(data)


def left_released(event, data):
    data.left_released_x, data.left_released_y = event.x, event.y
    if (not data.is_help):
        if (data.mode == 'login'):
            login_left_released(data)
        elif (data.mode == 'simplify'):
            simplify_left_released(data)


################################################################################

# CONTROLLER
# EVENTS

# RIGHT


def right_moved(event, data):
    pass


def right_pressed(event, data):
    pass


def right_released(event, data):
    pass


################################################################################

# CONTROLLER
# EVENTS

# KEY

# Adapted From:
# cs.cmu.edu/~112/notes/keyEventsDemo.py


# Returns boolean of whether to ignore keysym
def ignore_key(event):
    ignore_sym = ['Shift_L', 'Shift_R', 'Control_L', 'Control_R', 'Caps_Lock']
    return (event.keysym in ignore_sym)


# Stores shift and control as boolean values in data
def set_event_info(event, data):
    data.ctrl = ((event.state & 0x0004) != 0)
    data.shift = ((event.state & 0x0001) != 0)


def key_pressed(event, data):
    if (not ignore_key(event)):
        data.keysym_pressed = event.keysym
        set_event_info(event, data)
        if (data.keysym_pressed == 'space'):
            data.is_help = not data.is_help
        elif (not data.is_help):
            if (data.mode == 'simplify'):
                simplify_key_pressed(data)
            elif (data.mode == 'analyze'):
                analyze_key_pressed(data)


def key_released(event, data):
    if (not ignore_key(event)):
        data.keysym_released = event.keysym
        set_event_info(event, data)
        if (not data.is_help):
            if (data.mode == 'analyze'):
                analyze_key_released(data)


################################################################################

# CONTROLLER
# EVENTS

# TIMER


def timer_fired(data):
    pass


################################################################################

# VIEW


def redraw_all(canvas, data):
    if data.is_help:
        help_redraw_all(canvas, data)
    elif (data.mode == 'login'):
        login_redraw_all(canvas, data)
    elif (data.mode == 'simplify'):
        simplify_redraw_all(canvas, data)
    elif (data.mode == 'analyze'):
        analyze_redraw_all(canvas, data)


################################################################################

# VIEW


scale = (1 + 5 ** 0.5) / 2  # golden ratio
c_width = 6  # average pixels/character
black = '#000000'
black_background = '#131313'
black_shadow = '#191919'
gray_hover = '#1E1E1E'
gray_select = '#262626'
gray = '#8F8F8F'
red_hover = '#C64C57'
red = '#A34349'
green_hover = '#57C64C'
green = '#49A343'
blue_hover = '#4C57C6'
blue = '#4349A3'
white = '#FFFFFF'


################################################################################

# VIEW
# String/Text Functions


# Shortens strings to fit into given area
def truncate(s, width):
    length = math.floor(width / c_width)
    if (len(s) <= length):
        return s
    return s[:length] + '...'


# Ignore 'the' and capitalization when sorting
def sort_format(s):
    if (s.upper()[:4] == 'THE '):
        return s.upper()[4:]
    return s.upper()


# Slightly modified from:
# gist.github.com/j4mie/557354
# Normalizes a string (i.e. strips the accents) so it is viewable and printable
def strip(s):
    if isinstance(s, str):
        return (unicodedata.normalize('NFKD', s).encode('ASCII',
                                                        'ignore').decode(
            'utf-8', 'ignore'))
    return s


################################################################################

# OOP


class Button(object):
    def __init__(self, data, text, cx_scale, cy_scale, function, width_scale=0,
                 height_scale=0, color=None, color_hover=None, text_color=white,
                 text_color_hover=white, text_size=10):
        self.function = function
        self.text = text
        self.text_color = text_color
        self.text_color_hover = text_color_hover
        self.text_fill = self.text_color
        self.text_size = text_size
        self.color = color
        self.color_hover = color_hover
        self.fill = self.color
        self.cx_scale = cx_scale
        self.cy_scale = cy_scale
        if (width_scale == 0):
            self.width_scale = 1 / scale ** 3
        else:
            self.width_scale = width_scale
        if (height_scale == 0):
            self.height_scale = 1 / scale ** 6
        else:
            self.height_scale = height_scale
        self.cx = data.width * self.cx_scale
        self.cy = data.height * self.cy_scale
        self.width = data.width * self.width_scale
        self.height = data.height * self.height_scale
        self.x1 = self.cx - self.width / 2
        self.x2 = self.cx + self.width / 2
        self.y1 = self.cy - self.height / 2
        self.y2 = self.cy + self.height / 2

    # To maintain scalability
    def update_dimensions(self, data):
        self.cx = data.width * self.cx_scale
        self.cy = data.height * self.cy_scale
        self.width = data.width * self.width_scale
        self.height = data.height * self.height_scale
        self.x1 = self.cx - self.width / 2
        self.x2 = self.cx + self.width / 2
        self.y1 = self.cy - self.height / 2
        self.y2 = self.cy + self.height / 2

    # Useful for selecting and hovering
    def is_within_bounds(self, data, x, y):
        self.update_dimensions(data)
        return ((self.x1 <= x <= self.x2) and (self.y1 <= y <= self.y2))

    def hover(self):
        self.fill = self.color_hover
        self.text_fill = self.text_color_hover

    def unhover(self):
        self.fill = self.color
        self.text_fill = self.text_color

    # Buttons perform functions when pressed
    def press(self, data):
        self.function(data)

    def unpress(self, data):
        pass

    def draw(self, canvas, data):
        self.update_dimensions(data)
        canvas.create_rectangle(self.x1, self.y1, self.x2, self.y2,
                                fill=self.fill, width=0)
        canvas.create_text(self.cx, self.cy, fill=self.text_fill,
                           text=truncate(self.text, self.width),
                           font=('Proxima %d' % (self.text_size,)))


################################################################################

# HELP

# CONTROLLER
# VIEW


# Opens a splash screen with instructions
def help_init(data):
    data.is_help = True


def help_redraw_all(canvas, data):
    canvas.create_rectangle(0, 0, data.width, data.height,
                            fill=black_background)
    canvas.create_rectangle(data.width * (1 / 2 - scale / 5), 0,
                            data.width * (1 / 2 + scale / 5), data.height,
                            fill=black)
    canvas.create_line(data.width * (1 / 2 - scale / 5), 0,
                       data.width * (1 / 2 - scale / 5), data.height,
                       fill=black_shadow)
    canvas.create_line(data.width * (1 / 2 + scale / 5), 0,
                       data.width * (1 / 2 + scale / 5), data.height,
                       fill=black_shadow)
    canvas.create_image(data.width / 2, data.height / (3 * scale),
                        image=data.logo)
    canvas.create_text(data.width / 2, 5 * data.height / scale ** 6, fill=gray,
                       text='Simplify. Organize. Analyze. ', font='Proxima 14')
    canvas.create_line(data.width * (1 / 2 - 1 / scale ** 3),
                       data.height * scale / 5,
                       data.width * (1 / 2 + 1 / scale ** 3),
                       data.height * scale / 5,
                       fill=gray_select)
    canvas.create_text(data.width / 2, data.height * scale * 6 / 24,
                       text='Maximize the window for optimal viewing.',
                       fill=white, font='Proxima 14 bold')
    canvas.create_text(data.width / 2, data.height * scale * 7.25 / 24,
                    text='Use the up and down arrows on your keypad to scroll.',
                       fill=white, font='Proxima 14 bold')
    canvas.create_text(data.width / 2, data.height * scale * 7.75 / 24,
                    text='(Make sure your cursor is within the right section!)',
                       fill=white, font='Proxima 14 bold')
    canvas.create_text(data.width / 2, data.height * scale * 9 / 24,
                       text='Click on the headings to sort.',
                       fill=white, font='Proxima 14 bold')
    canvas.create_text(data.width / 2, data.height * scale * 10.25 / 24,
                text='Use control and shift to select multiple songs/artists.',
                       fill=white, font='Proxima 14 bold')
    canvas.create_text(data.width / 2, data.height * scale * 10.75 / 24,
                       text='(Use control + a to SELECT ALL.)',
                       fill=white, font='Proxima 14 bold')
    canvas.create_text(data.width / 2, data.height * scale * 12 / 24,
        text='Use the sliders to view and select more/less songs or artists.',
                       fill=white, font='Proxima 14 bold')
    canvas.create_text(data.width / 2, data.height * scale * 13 / 24, text=
    'Use buttons or hold control + drag to add to the playlist.',
                       fill=white, font='Proxima 14 bold')
    canvas.create_text(data.width / 2, data.height * (1 - 1 / scale ** 6),
                       text='PRESS THE SPACEBAR TO RETURN.',
                       fill=gray, font='Proxima 14')


################################################################################

# LOGIN

# MODEL
# Initializes the buttons for the login page


def login_buttons(data):
    return [
        Button(data, 'USERNAME', 1 / 2, 1 / scale ** 2, input_username,
               text_color=green, text_color_hover=green_hover, text_size=20),
        Button(data, 'LOG IN', 1 / 2, 1 - 1 / scale ** 4,
               authorize,
               color=green, color_hover=green_hover, text_size=14),
        Button(data, 'PRESS THE SPACEBAR FOR HELP AT ANY TIME', 1 / 2,
               1 - 1 / scale ** 6, help_init, width_scale=1 / 2,
               text_color=gray,
               text_color_hover=white, text_size=14)
    ]


################################################################################

# LOGIN
# CONTROLLER

# Adapted from:
# cs.cmu.edu/~112/notes/dialogs-demo1.py


# Simple message box asking for the user's Spotify username
def input_username(data):
    message = 'Please enter your Spotify username.'
    title = 'Username'
    data.username = simpledialog.askstring(title, message)


# Checks that there is a valid username and attempts to authenticate the user
# Raises a warning box if no username has been entered
def authorize(data):
    if (data.username == ''):
        message = 'Please enter your username to proceed.'
        title = 'Username Required'
        messagebox.showwarning(title, message)
    else:
        simplify_init(data)


################################################################################

# LOGIN
# CONTROLLER


# Very slightly modified from:
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

# LOGIN

# CONTROLLER
# EVENTS

# MOUSE


def login_mouse_moved(data):
    for button in data.buttons:
        if (button.is_within_bounds(data, data.mouse_moved_x,
                                    data.mouse_moved_y)):
            button.hover()
        else:
            button.unhover()


################################################################################

# LOGIN

# CONTROLLER
# EVENTS

# LEFT


def login_left_released(data):
    for button in data.buttons:
        if (button.is_within_bounds(data, data.left_released_x,
                                    data.left_released_y)):
            button.press(data)


################################################################################

# LOGIN
# VIEW


def login_redraw_all(canvas, data):
    canvas.create_rectangle(0, 0, data.width, data.height,
                            fill=black_background)
    canvas.create_rectangle(data.width * (1 / 2 - scale / 5), 0,
                            data.width * (1 / 2 + scale / 5), data.height,
                            fill=black)
    canvas.create_line(data.width * (1 / 2 - scale / 5), 0,
                       data.width * (1 / 2 - scale / 5), data.height,
                       fill=black_shadow)
    canvas.create_line(data.width * (1 / 2 + scale / 5), 0,
                       data.width * (1 / 2 + scale / 5), data.height,
                       fill=black_shadow)
    canvas.create_image(data.width / 2, data.height / (3 * scale),
                        image=data.logo)
    canvas.create_text(data.width / 2, 5 * data.height / scale ** 6, fill=gray,
                       text='Simplify. Analyze. Organize. ', font='Proxima 14')
    canvas.create_line(data.width * (1 / 2 - 1 / scale ** 3),
                       data.height * scale / 5,
                       data.width * (1 / 2 + 1 / scale ** 3),
                       data.height * scale / 5,
                       fill=gray_select)
    canvas.create_text(data.width / 2, data.height / scale, fill=white,
                       font='Proxima 15', text=
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
This may take some time.
''')
    for button in data.buttons:
        button.draw(canvas, data)


################################################################################

# LOGIN
# MODEL

# Initializes 'simplify' by pulling data
# Preference is to pull data from directory for speed an efficiency
# Directory is labeled with user's username and stored
# Creates buttons immediately afterward

def simplify_init(data):
    if (os.path.isdir(data.username)):
        import_user_data(data)
    else:
        prompt_for_user_token(data, 'user-library-modify')
        get_user_data(data)
        export_user_data(data)
    clean(data)
    data.mode = 'simplify'
    simplify_buttons(data)


################################################################################

# LOGIN 
# MODEL


# Gets user's top songs, artists, and their public playlists from Spotify
def get_user_data(data):
    for term in ['short_term', 'medium_term', 'long_term']:
        data.songs_top[term] = list()
        data.artists_top[term] = list()
    get_top_songs(data)
    get_top_artists(data)
    get_playlists(data)


# Saves user's top songs and their features on their computer using json
def export_user_data(data):
    os.makedirs(data.username)
    songs = open(data.username + os.sep + 'songs.txt', 'w')
    songs = json.dump(data.songs, songs)
    songs_top = open(data.username + os.sep + 'songs_top.txt', 'w')
    songs_top = json.dump(data.songs_top, songs_top)
    top_songs = open(data.username + os.sep + 'top_songs.txt', 'w')
    top_songs = json.dump(data.top_songs, top_songs)
    artists = open(data.username + os.sep + 'artists.txt', 'w')
    artists = json.dump(data.artists, artists)
    artists_top = open(data.username + os.sep + 'artists_top.txt', 'w')
    artists_top = json.dump(data.artists_top, artists_top)
    top_artists = open(data.username + os.sep + 'top_artists.txt', 'w')
    top_artists = json.dump(data.top_artists, top_artists)
    playlists = open(data.username + os.sep + 'playlists.txt', 'w')
    playlists = json.dump(data.playlists, playlists)


# Gets user's top songs and features that have been saved in a directory
def import_user_data(data):
    songs = open(data.username + os.sep + 'songs.txt', 'r')
    data.songs.update(json.load(songs))
    songs_top = open(data.username + os.sep + 'songs_top.txt', 'r')
    data.songs_top.update(json.load(songs_top))
    top_songs = open(data.username + os.sep + 'top_songs.txt', 'r')
    data.top_songs += json.load(top_songs)
    artists = open(data.username + os.sep + 'artists.txt', 'r')
    data.artists.update(json.load(artists))
    artists_top = open(data.username + os.sep + 'artists_top.txt', 'r')
    data.artists_top.update(json.load(artists_top))
    top_artists = open(data.username + os.sep + 'top_artists.txt', 'r')
    data.top_artists += json.load(top_artists)
    playlists = open(data.username + os.sep + 'playlists.txt', 'r')
    data.playlists.update(json.load(playlists))


################################################################################

# LOGIN
# MODEL

# Adapted from:
# github.com/plamere/spotipy/blob/master/examples/my_top_tracks.py
# github.com/plamere/spotipy/blob/master/examples/my_top_artists.py

# Pulls a user's top songs for each time range
# Puts the IDs into dictionaries by term and into meta dictionary for stats.


def get_top_songs(data):
    sp = spotipy.Spotify(auth=data.tokens['user-library-modify'])
    sp.trace = False
    for term in data.songs_top:
        songs = sp.current_user_top_tracks(time_range=term, limit=50)
        for song in songs['items']:
            data.songs_top[term] += [song['id']]
            if (song['id'] not in data.top_songs):
                data.top_songs += [song['id']]
            if (song['id'] not in data.songs):
                features = sp.audio_features([song['id']])[0]
                data.songs[song['id']] = {
                    'title': strip(song['name']),
                    'artist_id': song['artists'][0]['id'],
                    'artist_name': strip(song['artists'][0]['name']),
                    'album_name': strip(song['album']['name']),
                    'acousticness': strip(features['acousticness']),
                    'danceability': strip(features['danceability']),
                    'energy': strip(features['energy']),
                    'liveness': strip(features['liveness']),
                    'loudness': strip(features['loudness']),
                    'duration_ms': strip(song['duration_ms']),
                    'popularity': strip(song['popularity']),
                    'speechiness': strip(features['speechiness']),
                    'tempo': strip(features['tempo']),
                    'valence': strip(features['valence'])
                }


# Pulls a user's top artists for each time range
# Puts the IDs into dictionaries by term and into meta dictionary for stats.

def get_top_artists(data):
    sp = spotipy.Spotify(auth=data.tokens['user-library-modify'])
    sp.trace = False
    for term in data.artists_top:
        artists = sp.current_user_top_artists(time_range=term, limit=50)
        for artist in artists['items']:
            data.artists_top[term] += [artist['id']]
            if (artist['id'] not in data.top_artists):
                data.top_artists += [artist['id']]
            if (artist['id'] not in data.artists):
                data.artists[artist['id']] = {
                    'name': artist['name'],
                    'songs': list()
                }
                songs = sp.artist_top_tracks(artist['id'])
                for song in songs['tracks']:
                    data.artists[artist['id']]['songs'] += [song['id']]
                    if (song['id'] not in data.songs):
                        features = sp.audio_features([song['id']])[0]
                        data.songs[song['id']] = {
                            'title': strip(song['name']),
                            'artist_id': song['artists'][0]['id'],
                            'artist_name': strip(song['artists'][0]['name']),
                            'album_name': strip(song['album']['name']),
                            'acousticness': strip(features['acousticness']),
                            'danceability': strip(features['danceability']),
                            'energy': strip(features['energy']),
                            'liveness': strip(features['liveness']),
                            'loudness': strip(features['loudness']),
                            'duration_ms': strip(song['duration_ms']),
                            'popularity': strip(song['popularity']),
                            'speechiness': strip(features['speechiness']),
                            'tempo': strip(features['tempo']),
                            'valence': strip(features['valence'])
                        }


################################################################################

# LOGIN
# MODEL

# Gets a user's playlists and playlist contents from Spotify
# Puts data into a dictionary --> directory with json

def get_playlists(data):
    scope = 'user-library-modify'
    token = util.prompt_for_user_token(data.username, scope)
    sp = spotipy.Spotify(auth=token)
    playlists = sp.user_playlists(data.username)
    for playlist in playlists['items']:
        data.playlists[playlist['id']] = {
            'name': playlist['name'],
            'songs': list()
        }
        uri = playlist['uri']
        username = uri.split(':')[2]
        playlist_id = uri.split(':')[4]
        results = sp.user_playlist(username, playlist_id)
        for item in results['tracks']['items']:
            data.playlists[playlist['id']]['songs'] += [item['track']['id']]
    for playlist_id in data.playlists:
        for song_id in data.playlists[playlist_id]['songs']:
            if (song_id not in data.songs):
                song = sp.track(song_id)
                features = sp.audio_features([song_id])[0]
                data.songs[song_id] = {
                    'title': strip(song['name']),
                    'artist_id': song['artists'][0]['id'],
                    'artist_name': strip(song['artists'][0]['name']),
                    'album_name': strip(song['album']['name']),
                    'acousticness': strip(features['acousticness']),
                    'danceability': strip(features['danceability']),
                    'energy': strip(features['energy']),
                    'liveness': strip(features['liveness']),
                    'loudness': strip(features['loudness']),
                    'duration_ms': strip(song['duration_ms']),
                    'popularity': strip(song['popularity']),
                    'speechiness': strip(features['speechiness']),
                    'tempo': strip(features['tempo']),
                    'valence': strip(features['valence'])
                }


################################################################################

# OOP
# Sidebar selects input source


class Sidebar(Button):
    def __init__(self, data, text, row, list_of_ids):
        self.row = row
        super().__init__(data, text, 1.75 / data.columns,
                         (row + 1 / 2) / data.rows,
                         refresh_view, 3 / data.columns, 1 / data.rows,
                         text_color=gray)
        self.list_of_ids = copy.deepcopy(list_of_ids)

    def is_selected(self, data):
        return (data.selected_list == self.text)

    def values(self, data):
        del data.values[:]
        if (data.is_songs):
            for song_id in copy.deepcopy(self.list_of_ids):
                data.values += [data.songs[song_id][data.parameter]]

    def press(self, data):
        data.selected_list = self.text
        data.is_songs = True
        data.is_artists = False
        data.start_song = 0
        data.sort_mode = 0
        del data.song_ids[:]
        del data.artist_ids[:]
        del data.artist_song_ids[:]
        data.song_ids += self.list_of_ids
        self.values(data)
        refresh_view(data)
        analyze_view(data)
        if (data.mode == 'analyze'):
            analyze_buttons(data)
        else:
            simplify_buttons(data)

    def draw(self, canvas, data):
        if (self.is_selected(data)):
            self.text_fill = white
        self.update_dimensions(data)
        canvas.create_text(self.x1 + 1 / data.columns / 3, self.cy,
                           text=truncate(self.text, self.width),
                           font='Proxima 10',
                           fill=self.text_fill, anchor=W)
        if self.is_selected(data):
            canvas.create_rectangle(0, self.y1, data.width / data.columns / 9,
                                    self.y2, fill=green_hover)


################################################################################

# OOP
# Displays top artists for a user & their the artists' 10 top songs

class ArtistSidebar(Sidebar):
    def __init__(self, data, text, row, list_of_artist_ids):
        super().__init__(data, text, row, list_of_artist_ids)

    def press(self, data):
        data.selected_list = self.text
        data.is_songs = False
        data.is_artists = True
        data.start_song = 0
        data.start_artist = 0
        data.sort_mode = 0
        del data.song_ids[:]
        del data.artist_ids[:]
        del data.artist_song_ids[:]
        data.artist_ids += self.list_of_ids
        refresh_view(data)
        simplify_buttons(data)


################################################################################

# OOP


class SongHeader(Button):
    def __init__(self, data, text, position, function):
        self.position = position
        width_scale = 1 / data.columns
        height_scale = 1 / data.rows
        cy_scale = (1 / 2) * height_scale
        self.symbol = ''
        if (self.position == 0):
            cx_scale = 4.25 / data.columns
        elif (self.position == 1):
            cx_scale = 8.25 / data.columns
        elif (self.position == 2):
            cx_scale = 11.5 / data.columns
        elif (self.position == 3):
            cx_scale = 15.5 / data.columns
        super().__init__(data, text, cx_scale, cy_scale, function,
                         width_scale=width_scale, height_scale=height_scale,
                         color=None, color_hover=None, text_color=gray,
                         text_color_hover=white, text_size=10)

    def unpress(self, data):
        pass

    def get_symbol(self, data):
        if (self.position == 0):
            if (data.sort_mode == 1):
                self.symbol = '/\\'
            elif (data.sort_mode == 2):
                self.symbol = '\\/'
            else:
                self.symbol = ''
        elif (self.position == 1):
            if (data.sort_mode == 3):
                self.symbol = '/\\'
            elif (data.sort_mode == 4):
                self.symbol = '\\/'
            else:
                self.symbol = ''
        elif (self.position == 2):
            if (data.sort_mode == 5):
                self.symbol = '/\\'
            elif (data.sort_mode == 6):
                self.symbol = '\\/'
            else:
                self.symbol = ''
        elif (self.position == 3):
            if (data.sort_mode == 7):
                self.symbol = '/\\'
            elif (data.sort_mode == 8):
                self.symbol = '\\/'
            else:
                self.symbol = ''
        else:
            self.symbol = ''

    def draw(self, canvas, data):
        if (data.is_songs):
            self.update_dimensions(data)
            self.get_symbol(data)
            canvas.create_text(self.x1, self.cy, text=self.text,
                               fill=self.text_fill, font='Proxima 10', anchor=W)
            canvas.create_text(self.x1 - 10, self.cy, text=self.symbol,
                               fill=green, font='Proxima 10', anchor=E)


################################################################################

# OOP
# Slightly different from SongHeader for functions and postitions


class ArtistHeader(Button):
    def __init__(self, data, text, position, function):
        self.position = position
        width_scale = 1 / data.columns
        height_scale = 1 / data.rows
        cy_scale = (1 / 2) * height_scale
        self.symbol = ''
        if (self.position == 0):
            cx_scale = 4.25 / data.columns
        elif (self.position == 1):
            cx_scale = 7.75 / data.columns
        elif (self.position == 2):
            cx_scale = 11.5 / data.columns
        elif (self.position == 3):
            cx_scale = 15.5 / data.columns
        super().__init__(data, text, cx_scale, cy_scale, function,
                         width_scale=width_scale, height_scale=height_scale,
                         color=None, color_hover=None, text_color=gray,
                         text_color_hover=white, text_size=10)

    def unpress(self, data):
        pass

    def get_symbol(self, data):
        if (self.position == 0):
            if (data.sort_mode == 1):
                self.symbol = '/\\'
            elif (data.sort_mode == 2):
                self.symbol = '\\/'
            else:
                self.symbol = ''
        elif (self.position == 1):
            if (data.sort_mode == 3):
                self.symbol = '/\\'
            elif (data.sort_mode == 4):
                self.symbol = '\\/'
            else:
                self.symbol = ''
        elif (self.position == 2):
            if (data.sort_mode == 5):
                self.symbol = '/\\'
            elif (data.sort_mode == 6):
                self.symbol = '\\/'
            else:
                self.symbol = ''
        elif (self.position == 3):
            if (data.sort_mode == 7):
                self.symbol = '/\\'
            elif (data.sort_mode == 8):
                self.symbol = '\\/'
            else:
                self.symbol = ''
        else:
            self.symbol = ''

    def draw(self, canvas, data):
        if (data.is_artists):
            self.update_dimensions(data)
            self.get_symbol(data)
            canvas.create_text(self.x1, self.cy, text=self.text,
                               fill=self.text_fill, font='Proxima 10', anchor=W)
            canvas.create_text(self.x1 - 10, self.cy, text=self.symbol,
                               fill=green, font='Proxima 10', anchor=E)


################################################################################

# OOP
# Able to select, add to playlist, display artists' top songs, etc.


class Artist(Button):
    def __init__(self, data, row, artist_id):
        self.row = row
        self.artist_id = artist_id
        self.artist_name = data.artists[self.artist_id]['name']
        self.artist_songs = copy.deepcopy(data.artists[artist_id]['songs'])
        text = self.artist_name
        width_scale = 3.5 / data.columns
        height_scale = 1 / data.rows
        cx_scale = 4.75 / data.columns
        cy_scale = (self.row + 1 / 2) * height_scale
        super().__init__(data, text, cx_scale, cy_scale, function=None,
                         width_scale=width_scale, height_scale=height_scale,
                         color=black_shadow, color_hover=gray_hover,
                         text_color=white, text_color_hover=white,
                         text_size=10)
        self.update_dimensions(data)
        self.line_fill = gray_hover
        self.plus_color = green
        self.plus_color_hover = green_hover
        self.minus_color = red
        self.minus_color_hover = red_hover
        self.plus_fill = self.plus_color
        self.minus_fill = self.minus_color
        self.symbol_size = 10

    def is_selected(self, data):
        return (self.artist_id in data.selected_artists)

    def is_all_staged(self, data):
        for song_id in self.artist_songs:
            if (song_id not in data.stage_ids):
                return False
        return True

    def get_id(self):
        return self.artist_id

    def get_row(self):
        return self.row

    def hover(self):
        super().hover()
        self.plus_fill = self.plus_color_hover
        self.minus_fill = self.minus_color_hover
        self.symbol_size = self.text_size + 3

    def unhover(self):
        super().unhover()
        self.plus_fill = self.plus_color
        self.minus_fill = self.minus_color
        self.symbol_size = self.text_size + 1

    def press(self, data):
        if (data.left_pressed_x <=
                    self.x1 + data.width / data.columns * 0.75):
            data.selected_artists.add(self.artist_id)
            if (self.is_all_staged(data)):
                self.remove_from_stage(data)
            else:
                self.add_all_to_stage(data)
        elif (self.artist_id not in data.selected_artists):
            data.selected_artists.add(self.artist_id)
        elif (data.ctrl):
            data.selected_artists.remove(self.artist_id)
            data.selected_ids.clear()
        del data.artist_song_ids[:]
        data.artist_song_ids += self.artist_songs
        refresh_view(data)

    def unpress(self, data):
        if (self.artist_id in data.selected_artists):
            data.selected_artists.remove(self.artist_id)
        refresh_view(data)

    def add_all_to_stage(self, data):
        for song_id in self.artist_songs:
            if (song_id not in data.stage_ids):
                data.stage_ids += [song_id]
        refresh_view(data)

    def remove_from_stage(self, data):
        for song_id in self.artist_songs:
            if (song_id in data.stage_ids):
                data.stage_ids.remove(song_id)
        refresh_view(data)

    def draw(self, canvas, data):
        self.update_dimensions(data)
        if (self.is_selected(data)):
            self.fill = gray_select
            self.line_fill = black_shadow
        canvas.create_rectangle(self.x1 + data.width / data.columns / 3,
                                self.y1,
                                self.x2 - data.width / data.columns / 3,
                                self.y2,
                                fill=self.fill, width=0)
        canvas.create_line(self.x1 + data.width / data.columns / 3, self.y1,
                           self.x2 - data.width / data.columns / 3, self.y1,
                           fill=self.line_fill)
        canvas.create_line(self.x1 + data.width / data.columns / 3, self.y2,
                           self.x2 - data.width / data.columns / 3, self.y2,
                           fill=self.line_fill)
        canvas.create_text(self.x1 + data.width / data.columns * 0.75,
                           self.cy,
                           text=truncate(self.artist_name,
                                         data.width / data.columns * 4),
                           fill=self.text_fill, anchor=W, font='Proxima 10')
        if (not self.is_all_staged(data)):
            canvas.create_text(self.x1 + data.width / data.columns / 2,
                               self.cy,
                               text='+', fill=self.plus_fill,
                               font=(
                                   'Proxima %d bold' % (self.symbol_size,)))
        else:
            canvas.create_text(self.x1 + data.width / data.columns / 2,
                               self.cy,
                               text='-', fill=self.minus_fill,
                               font=(
                                   'Proxima %d bold' % (self.symbol_size,)))


################################################################################

# OOP
# Stores and displays all songs in playlists, etc. 


class Song(Button):
    def __init__(self, data, row, song_id):
        text = ''
        width_scale = (16 - 3) / data.columns
        height_scale = 1 / data.rows
        cx_scale = (3 + 16) / 2 / data.columns
        cy_scale = (row + 1 / 2) * height_scale
        self.line_fill = gray_hover
        self.plus_color = green
        self.plus_color_hover = green_hover
        self.minus_color = red
        self.minus_color_hover = red_hover
        self.plus_fill = self.plus_color
        self.minus_fill = self.minus_color
        self.symbol_size = 10
        self.row = row
        self.song_id = song_id
        self.title = data.songs[self.song_id]['title']
        self.artist_name = data.songs[self.song_id]['artist_name']
        self.album_name = data.songs[self.song_id]['album_name']
        duration_ms = data.songs[self.song_id]['duration_ms']
        self.duration = '%d:%02d' % (duration_ms // 60000,
                                     duration_ms % 60000 // 1000)
        super().__init__(data, text, cx_scale, cy_scale, function=None,
                         width_scale=width_scale, height_scale=height_scale,
                         color=black_shadow, color_hover=gray_hover,
                         text_color=white, text_color_hover=white, text_size=10)

    def is_selected(self, data):
        return (self.song_id in data.selected_ids)

    def get_id(self):
        return (self.song_id)

    def get_row(self):
        return (self.row)

    def hover(self):
        super().hover()
        self.plus_fill = self.plus_color_hover
        self.minus_fill = self.minus_color_hover
        self.symbol_size = self.text_size + 3

    def unhover(self):
        super().unhover()
        self.plus_fill = self.plus_color
        self.minus_fill = self.minus_color
        self.symbol_size = self.text_size + 1

    def press(self, data):
        if (data.left_pressed_x <= self.x1 + data.width / data.columns * 0.75):
            data.selected_ids.add(self.song_id)
            if (self.song_id in data.stage_ids):
                remove_selected_songs_from_stage(data)
            else:
                add_selected_songs_to_stage(data)
        elif (self.song_id not in data.selected_ids):
            data.selected_ids.add(self.song_id)
        elif (data.ctrl):
            data.selected_ids.remove(self.song_id)
        if (data.mode == 'simplify'):
            refresh_view(data)
        elif (data.mode == 'analyze'):
            analyze_view(data)

    def unpress(self, data):
        if (self.song_id in data.selected_ids):
            data.selected_ids.remove(self.song_id)
        if (data.mode == 'simplify'):
            refresh_view(data)
        elif (data.mode == 'analyze'):
            analyze_view(data)

    def draw(self, canvas, data):
        self.update_dimensions(data)
        if (self.is_selected(data)):
            self.fill = gray_select
            self.line_fill = black_shadow
        canvas.create_rectangle(self.x1 + data.width / data.columns / 3,
                                self.y1,
                                self.x2 - data.width / data.columns / 3,
                                self.y2,
                                fill=self.fill, width=0)
        canvas.create_line(self.x1 + data.width / data.columns / 3, self.y1,
                           self.x2 - data.width / data.columns / 3, self.y1,
                           fill=self.line_fill)
        canvas.create_line(self.x1 + data.width / data.columns / 3, self.y2,
                           self.x2 - data.width / data.columns / 3, self.y2,
                           fill=self.line_fill)
        canvas.create_text(self.x1 + data.width / data.columns * 0.75, self.cy,
                           text=truncate(self.title,
                                         data.width / data.columns * 4),
                           fill=self.text_fill, anchor=W, font='Proxima 10')
        canvas.create_text(data.width * 7.75 / data.columns, self.cy,
                           text=truncate(self.artist_name,
                                         data.width / data.columns * (3.25)),
                           fill=self.text_fill, anchor=W, font='Proxima 10')
        canvas.create_text(data.width * 11 / data.columns, self.cy,
                           text=truncate(self.album_name,
                                         data.width / data.columns * (4)),
                           fill=self.text_fill, anchor=W, font='Proxima 10')
        canvas.create_text(data.width * 15 / data.columns, self.cy,
                           text=self.duration, fill=gray, anchor=W,
                           font='Proxima 10')
        if (self.song_id not in data.stage_ids):
            canvas.create_text(self.x1 + data.width / data.columns / 2, self.cy,
                               text='+', fill=self.plus_fill,
                               font=('Proxima %d bold' % (self.symbol_size,)))
        else:
            canvas.create_text(self.x1 + data.width / data.columns / 2, self.cy,
                               text='-', fill=self.minus_fill,
                               font=('Proxima %d bold' % (self.symbol_size,)))


################################################################################

# OOP
# Stores/displays each user's top artists' top songs (up to 10)


class ArtistSong(Song):
    def __init__(self, data, rows, song_id):
        super().__init__(data, rows, song_id)
        self.cx_scale = 1 / data.columns * (6.5 + 16) / 2
        self.width_scale = (16 - 6.5) / data.columns
        self.update_dimensions(data)

    def press(self, data):
        self.update_dimensions(data)
        if (data.left_pressed_x <= self.x1 + data.width / data.columns * 0.75):
            data.selected_ids.add(self.song_id)
            if (self.song_id in data.stage_ids):
                remove_selected_songs_from_stage(data)
            else:
                add_selected_songs_to_stage(data)
        elif (self.song_id not in data.selected_ids):
            data.selected_ids.add(self.song_id)
        else:
            data.selected_ids.remove(self.song_id)

    def unpress(self, data):
        if (self.song_id in data.selected_ids):
            data.selected_ids.remove(self.song_id)

    def draw(self, canvas, data):
        if (self.song_id in data.selected_ids):
            self.fill = gray_select
        canvas.create_rectangle(self.x1 + data.width / data.columns / 3,
                                self.y1,
                                self.x2 - data.width / data.columns / 3,
                                self.y2,
                                fill=self.fill, width=0)
        canvas.create_line(self.x1 + data.width / data.columns / 3, self.y1,
                           self.x2 - data.width / data.columns / 3, self.y1,
                           fill=self.line_fill)
        canvas.create_line(self.x1 + data.width / data.columns / 3, self.y2,
                           self.x2 - data.width / data.columns / 3, self.y2,
                           fill=self.line_fill)
        canvas.create_text(self.x1 + data.width / data.columns * 0.75, self.cy,
                           text=truncate(self.title,
                                         data.width / data.columns * 4),
                           fill=self.text_fill, anchor=W, font='Proxima 10')
        canvas.create_text(data.width * 11 / data.columns, self.cy,
                           text=truncate(self.album_name,
                                         data.width / data.columns * (4)),
                           fill=self.text_fill, anchor=W, font='Proxima 10')
        canvas.create_text(data.width * 15 / data.columns, self.cy,
                           text=self.duration, fill=gray, anchor=W,
                           font='Proxima 10')
        if (self.song_id not in data.stage_ids):
            canvas.create_text(self.x1 + data.width / data.columns / 2, self.cy,
                               text='+', fill=self.plus_fill,
                               font=('Proxima %d bold' % (self.symbol_size,)))
        else:
            canvas.create_text(self.x1 + data.width / data.columns / 2, self.cy,
                               text='-', fill=self.minus_fill,
                               font=('Proxima %d bold' % (self.symbol_size,)))


################################################################################

# OOP
# Stores and displays the staging playlist


class StageSong(Song):
    def __init__(self, data, row, song_id):
        super().__init__(data, row, song_id)
        self.width_scale = 1 / data.columns * 3
        self.height_scale = 1 / data.rows * 2 / 3
        self.cx_scale = 1 / data.columns * 18
        self.cy_scale = self.height_scale * (row + 6.5 / 2)
        self.fill = black_background
        self.color = black_background
        self.color_hover = gray_hover
        self.text_color = white
        self.text_color_hover = white
        self.row = row
        self.song_id = song_id
        self.title = data.songs[self.song_id]['title']
        self.artist_name = data.songs[self.song_id]['artist_name']
        self.update_dimensions(data)

    def is_selected(self, data):
        return (self.song_id in data.selected_ids)

    def press(self, data):
        if (data.left_pressed_x <= self.x1 + 20):
            remove_selected_songs_from_stage(data)
        elif (self.song_id not in data.selected_ids):
            data.selected_ids.add(self.song_id)
        elif (data.ctrl):
            data.selected_ids.remove(self.song_id)
        refresh_view(data)

    def unpress(self, data):
        if (self.song_id in data.selected_ids):
            data.selected_ids.remove(self.song_id)
        refresh_view(data)

    def draw(self, canvas, data):
        if (self.row < 40):
            self.update_dimensions(data)
            if (self.is_selected(data)):
                self.fill = gray_select
            canvas.create_rectangle(self.x1, self.y1, self.x2, self.y2,
                                    fill=self.fill, width=0)
            canvas.create_text(self.x1 + 15, self.cy, text=truncate(
                ('%d. %s | %s') % (self.row + data.start_stage, self.title,
                                   self.artist_name), self.width),
                               fill=self.text_fill,
                               font='Proxima 9', anchor=W)
            canvas.create_text(self.x1 + 5, self.cy, text='-',
                               fill=self.minus_fill,
                               font=('Proxima %d bold' % (self.symbol_size,)))


################################################################################

# SIMPLIFY
# MODEL

# Creates Buttons/Sidebars/Headers for 'simplify'
# OOP to easily loop through many similar data types/values


def simplify_buttons(data):
    del data.buttons[:]
    data.buttons += [
        Button(data, '+ ADD TO PLAYLIST +', 18 / data.columns, 1 / data.rows,
               add_selected_songs_to_stage, 3 / data.columns, .95 / data.rows,
               green, green_hover),
        Button(data, '- REMOVE FROM PLAYLIST -', 18 / data.columns,
               2 / data.rows,
               remove_selected_songs_from_stage, 3 / data.columns,
               .95 / data.rows,
               red, red_hover),
        Button(data, 'CREATE & ANALYZE PLAYLISTS >>', 18 / data.columns,
               29 / data.rows, analyze_init, 3 / data.columns, .95 / data.rows,
               blue,
               blue_hover),
        Sidebar(data, 'YOUR TOP SONGS', 0 - data.start_list, data.top_songs),
        Sidebar(data, 'Short Term Top Songs', 1 - data.start_list,
                data.songs_top['short_term']),
        Sidebar(data, 'Medium Term Top Songs', 2 - data.start_list,
                data.songs_top['medium_term']),
        Sidebar(data, 'Long Term Top Songs', 3 - data.start_list,
                data.songs_top['long_term']),
        ArtistSidebar(data, 'YOUR TOP ARTISTS', 5 - data.start_list,
                      data.top_artists),
        ArtistSidebar(data, 'Short Term Top Artists', 6 - data.start_list,
                      data.artists_top['short_term']),
        ArtistSidebar(data, 'Medium Term Top Artists', 7 - data.start_list,
                      data.artists_top['medium_term']),
        ArtistSidebar(data, 'Long Term Top Artists', 8 - data.start_list,
                      data.artists_top['long_term']),
        Sidebar(data, 'YOUR PLAYLISTS', 10 - data.start_list, data.stage_ids)
    ]
    for offset, playlist_id in enumerate(data.playlists):
        data.buttons += [
            Sidebar(data, truncate(data.playlists[playlist_id]['name'],
                                   data.width / data.columns * 3),
                    11 + offset - data.start_list,
                    data.playlists[playlist_id]['songs'])
        ]
    if (data.is_songs):
        data.buttons += [
            SongHeader(data, truncate('TITLE', data.width / data.columns * 3),
                       0,
                       order_songs_by_title),
            SongHeader(data, truncate('ARTIST', data.width / data.columns * 3),
                       1,
                       order_songs_by_artist),
            SongHeader(data, truncate('ALBUM', data.width / data.columns * 3),
                       2,
                       order_songs_by_album),
            SongHeader(data, truncate('TIME', data.width / data.columns * 3), 3,
                       order_songs_by_time)
        ]
    elif (data.is_artists):
        data.buttons += [
            ArtistHeader(data,
                         truncate('ARTIST', data.width / data.columns * 3),
                         0, order_artists_by_name),
            ArtistHeader(data, truncate('TITLE', data.width / data.columns * 3),
                         1, order_artists_by_title),
            ArtistHeader(data, truncate('ALBUM', data.width / data.columns * 3),
                         2, order_artists_by_album),
            ArtistHeader(data, truncate('TIME', data.width / data.columns * 3),
                         3, order_artists_by_time)
        ]
    if (len(data.stage_ids) > 39):
        data.buttons += [
            Button(data, '/\\', 19.75 / data.columns, 3 / data.rows,
                   stage_to_top,
                   text_color=gray, text_color_hover=white),
            Button(data, '\\/', 19.75 / data.columns, 4 / data.rows,
                   stage_to_bottom, text_color=gray, text_color_hover=white),
        ]


################################################################################

# SIMPLIFY
# MODEL

# Every time the view is changed (scrolling, new playlist, etc.)
# This function updates the view without desctructively modifying the source


def refresh_view(data):
    if (data.mode == 'analyze'):
        analyze_view(data)
        return
    del data.stage_songs[:]
    del data.viewing_songs[:]
    del data.viewing_artists[:]
    del data.viewing_artist_songs[:]
    for row, song_id in enumerate(data.stage_ids[data.start_stage:]):
        data.stage_songs += [StageSong(data, row + 1, song_id)]
    if (data.is_songs):
        for row, song_id in enumerate(data.song_ids[data.start_song:]):
            data.viewing_songs += [Song(data, row + 1, song_id)]
    elif (data.is_artists):
        for row, artist_id in enumerate(data.artist_ids[data.start_artist:]):
            data.viewing_artists += [Artist(data, row + 1, artist_id)]
        for row, song_id in enumerate(data.artist_song_ids):
            data.viewing_artist_songs += [ArtistSong(data, row + 1, song_id)]


################################################################################

# SIMPLIFY

# CONTROLLER
# SORTING

# Following functions sort songs/artists by given parameters
# Takes case accents/not normal lettering into account


def order_songs_by_title(data):
    if (data.sort_mode == 0):
        del data.original_ids[:]
        data.original_ids += data.song_ids
        data.sort_mode = 1
    elif (data.sort_mode == 1):
        data.sort_mode = 2
    elif (data.sort_mode == 2):
        data.sort_mode = 0
    else:
        data.sort_mode = 1
    result = list()
    if (data.sort_mode == 0):
        result += data.original_ids
    elif (data.sort_mode == 1):
        sorting_dictionary = dict()
        for song_id in data.song_ids:
            name = sort_format(data.songs[song_id]['title'])
            if (name in sorting_dictionary):
                sorting_dictionary[name] += [song_id]
            else:
                sorting_dictionary[name] = [song_id]
        for name in sorted(sorting_dictionary.keys()):
            result += sorted(sorting_dictionary[name])
    elif (data.sort_mode == 2):
        result += data.song_ids[::-1]
    del data.song_ids[:]
    data.song_ids += result
    data.start_song = 0
    refresh_view(data)


def order_songs_by_artist(data):
    if (data.sort_mode == 0):
        del data.original_ids[:]
        data.original_ids += data.song_ids
        data.sort_mode = 3
    elif (data.sort_mode == 3):
        data.sort_mode = 4
    elif (data.sort_mode == 4):
        data.sort_mode = 0
    else:
        data.sort_mode = 3
    result = list()
    if (data.sort_mode == 0):
        result += data.original_ids
    elif (data.sort_mode == 3):
        sorting_dictionary = dict()
        for song_id in data.song_ids:
            artist_name = sort_format(data.songs[song_id]['artist_name'])
            if (artist_name in sorting_dictionary):
                sorting_dictionary[artist_name] += [song_id]
            else:
                sorting_dictionary[artist_name] = [song_id]
        for artist_name in sorted(sorting_dictionary.keys()):
            result += sorted(sorting_dictionary[artist_name])
    elif (data.sort_mode == 4):
        result += data.song_ids[::-1]
    del data.song_ids[:]
    data.song_ids += result
    data.start_song = 0
    refresh_view(data)


def order_songs_by_album(data):
    if (data.sort_mode == 0):
        del data.original_ids[:]
        data.original_ids += data.song_ids
        data.sort_mode = 5
    elif (data.sort_mode == 5):
        data.sort_mode = 6
    elif (data.sort_mode == 6):
        data.sort_mode = 0
    else:
        data.sort_mode = 5
    result = list()
    if (data.sort_mode == 0):
        result += data.original_ids
    elif (data.sort_mode == 5):
        sorting_dictionary = dict()
        for song_id in data.song_ids:
            album_name = sort_format(data.songs[song_id]['album_name'])
            if (album_name in sorting_dictionary):
                sorting_dictionary[album_name] += [song_id]
            else:
                sorting_dictionary[album_name] = [song_id]
        for album_name in sorted(sorting_dictionary.keys()):
            result += sorted(sorting_dictionary[album_name])
    elif (data.sort_mode == 6):
        result += data.song_ids[::-1]
    del data.song_ids[:]
    data.song_ids += result
    data.start_song = 0
    refresh_view(data)


def order_songs_by_time(data):
    if (data.sort_mode == 0):
        del data.original_ids[:]
        data.original_ids += data.song_ids
        data.sort_mode = 7
    elif (data.sort_mode == 7):
        data.sort_mode = 8
    elif (data.sort_mode == 8):
        data.sort_mode = 0
    else:
        data.sort_mode = 7
    result = list()
    if (data.sort_mode == 0):
        result += data.original_ids
    elif (data.sort_mode == 7):
        sorting_dictionary = dict()
        for song_id in data.song_ids:
            duration_ms = data.songs[song_id]['duration_ms']
            if (duration_ms in sorting_dictionary):
                sorting_dictionary[duration_ms] += [song_id]
            else:
                sorting_dictionary[duration_ms] = [song_id]
        for duration_ms in sorted(sorting_dictionary.keys()):
            result += sorted(sorting_dictionary[duration_ms])
    elif (data.sort_mode == 8):
        result += data.song_ids[::-1]
    del data.song_ids[:]
    data.song_ids += result
    data.start_song = 0
    refresh_view(data)


def order_artists_by_name(data):
    if (data.sort_mode == 0):
        del data.original_ids[:]
        data.original_ids += data.artist_ids
        data.sort_mode = 1
    elif (data.sort_mode == 1):
        data.sort_mode = 2
    elif (data.sort_mode == 2):
        data.sort_mode = 0
    else:
        data.sort_mode = 1
    result = list()
    if (data.sort_mode == 0):
        result += data.original_ids
    elif (data.sort_mode == 1):
        sorting_dictionary = dict()
        for artist_id in data.artist_ids:
            artist_name = sort_format(data.artists[artist_id]['name'])
            if (artist_name in sorting_dictionary):
                sorting_dictionary[artist_name] += [artist_id]
            else:
                sorting_dictionary[artist_name] = [artist_id]
        for artist_name in sorted(sorting_dictionary.keys()):
            result += sorted(sorting_dictionary[artist_name])
    elif (data.sort_mode == 2):
        result += data.artist_ids[::-1]
    del data.artist_ids[:]
    data.artist_ids += result
    data.start_artist = 0
    refresh_view(data)


def order_artists_by_title(data):
    if (data.sort_mode == 0):
        del data.original_ids[:]
        data.original_ids += data.artist_song_ids
        data.sort_mode = 3
    elif (data.sort_mode == 3):
        data.sort_mode = 4
    elif (data.sort_mode == 4):
        data.sort_mode = 0
    else:
        data.sort_mode = 3
    result = list()
    if (data.sort_mode == 0):
        result += data.original_ids
    elif (data.sort_mode == 3):
        sorting_dictionary = dict()
        for song_id in data.artist_song_ids:
            name = sort_format(data.songs[song_id]['title'])
            if (name in sorting_dictionary):
                sorting_dictionary[name] += [song_id]
            else:
                sorting_dictionary[name] = [song_id]
        for name in sorted(sorting_dictionary.keys()):
            result += sorted(sorting_dictionary[name])
    elif (data.sort_mode == 4):
        result += data.artist_song_ids[::-1]
    del data.artist_song_ids[:]
    data.artist_song_ids += result
    data.start_artist = 0
    refresh_view(data)


def order_artists_by_album(data):
    if (data.sort_mode == 0):
        del data.original_ids[:]
        data.original_ids += data.artist_song_ids
        data.sort_mode = 5
    elif (data.sort_mode == 5):
        data.sort_mode = 6
    elif (data.sort_mode == 6):
        data.sort_mode = 0
    else:
        data.sort_mode = 5
    result = list()
    if (data.sort_mode == 0):
        result += data.original_ids
    elif (data.sort_mode == 5):
        sorting_dictionary = dict()
        for song_id in data.artist_song_ids:
            album_name = sort_format(data.songs[song_id]['album_name'])
            if (album_name in sorting_dictionary):
                sorting_dictionary[album_name] += [song_id]
            else:
                sorting_dictionary[album_name] = [song_id]
        for album_name in sorted(sorting_dictionary.keys()):
            result += sorted(sorting_dictionary[album_name])
    elif (data.sort_mode == 6):
        result += data.artist_song_ids[::-1]
    del data.artist_song_ids[:]
    data.artist_song_ids += result
    data.start_artist = 0
    refresh_view(data)


def order_artists_by_time(data):
    if (data.sort_mode == 0):
        del data.original_ids[:]
        data.original_ids += data.artist_song_ids
        data.sort_mode = 7
    elif (data.sort_mode == 7):
        data.sort_mode = 8
    elif (data.sort_mode == 8):
        data.sort_mode = 0
    else:
        data.sort_mode = 7
    result = list()
    if (data.sort_mode == 0):
        result += data.original_ids
    elif (data.sort_mode == 7):
        sorting_dictionary = dict()
        for song_id in data.artist_song_ids:
            duration_ms = data.songs[song_id]['duration_ms']
            if (duration_ms in sorting_dictionary):
                sorting_dictionary[duration_ms] += [song_id]
            else:
                sorting_dictionary[duration_ms] = [song_id]
        for duration_ms in sorted(sorting_dictionary.keys()):
            result += sorted(sorting_dictionary[duration_ms])
    elif (data.sort_mode == 8):
        result += data.artist_song_ids[::-1]
    del data.artist_song_ids[:]
    data.artist_song_ids += result
    data.start_artist = 0
    refresh_view(data)


################################################################################

# SIMPLIFY

# CONTROLLER
# Playlist/staging functions for buttons and stage


def add_selected_songs_to_stage(data):
    for song_id in copy.deepcopy(list(data.selected_ids)):
        if (song_id not in data.stage_ids):
            data.stage_ids += [song_id]
    refresh_view(data)
    simplify_buttons(data)


def remove_selected_songs_from_stage(data):
    data.start_stage = 0
    for song_id in copy.deepcopy(list(data.selected_ids)):
        if (song_id in data.stage_ids):
            data.stage_ids.remove(song_id)
    refresh_view(data)
    simplify_buttons(data)


def stage_to_top(data):
    data.start_stage = 0
    refresh_view(data)


def stage_to_bottom(data):
    if (len(data.stage_ids) > 39):
        data.start_stage = len(data.stage_ids) - 39
    refresh_view(data)


################################################################################

# SIMPLIFY

# CONTROLLER
# EVENTS

# MOUSE


def simplify_mouse_moved(data):
    for song in data.viewing_songs:
        if (song.is_within_bounds(data, data.mouse_moved_x,
                                  data.mouse_moved_y)):
            song.hover()
        else:
            song.unhover()

    for button in data.buttons:
        if (button.is_within_bounds(data, data.mouse_moved_x,
                                    data.mouse_moved_y)):
            button.hover()
        else:
            button.unhover()

    for song in data.stage_songs:
        if (song.is_within_bounds(data, data.mouse_moved_x,
                                  data.mouse_moved_y)):
            song.hover()
        else:
            song.unhover()

    for artist in data.viewing_artists:
        if (artist.is_within_bounds(data, data.mouse_moved_x,
                                    data.mouse_moved_y)):
            artist.hover()
        else:
            artist.unhover()

    for song in data.viewing_artist_songs:
        if (song.is_within_bounds(data, data.mouse_moved_x,
                                  data.mouse_moved_y)):
            song.hover()
        else:
            song.unhover()


################################################################################

# SIMPLIFY
# CONTROLLER
# EVENTS 

# LEFT
# PRESSED 


def simplify_left_pressed(data):
    for button in data.buttons:
        if (button.is_within_bounds(data, data.left_pressed_x,
                                    data.left_pressed_y)):
            button.press(data)
        else:
            button.unpress(data)

    for i, song in enumerate(data.viewing_songs):
        if (song.is_within_bounds(data, data.left_pressed_x,
                                  data.left_pressed_y)):
            if (data.shift):
                data.selected_ids.add(song.get_id())
                for j, song_j in enumerate(data.viewing_songs):
                    if (i == j):
                        continue
                    elif (song_j.is_selected(data)):
                        data.selected_ids.clear()
                        if (j < i):
                            for k in range(j, i + 1):
                                data.selected_ids.add(
                                    data.viewing_songs[k].get_id()
                                )
                        elif (j > i):
                            for k in range(i, j + 1):
                                data.selected_ids.add(
                                    data.viewing_songs[k].get_id()
                                )
                        break
            else:
                song.press(data)
        elif (not (data.ctrl or data.shift)):
            song.unpress(data)

    for i, song in enumerate(data.stage_songs):
        if (song.is_within_bounds(data, data.left_pressed_x,
                                  data.left_pressed_y)):
            if (data.shift):
                data.selected_ids.add(song.get_id())
                for j, song_j in enumerate(data.stage_songs):
                    if (i == j):
                        continue
                    elif (song_j.is_selected(data)):
                        data.selected_ids.clear()
                        if (j < i):
                            for k in range(j, i + 1):
                                data.selected_ids.add(
                                    data.stage_songs[k].get_id()
                                )
                        elif (j > i):
                            for k in range(i, j + 1):
                                data.selected_ids.add(
                                    data.stage_songs[k].get_id()
                                )
                        break
            else:
                song.press(data)
        elif (not (data.ctrl or data.shift)):
            song.unpress(data)

    for i, artist in enumerate(data.viewing_artists):
        if (artist.is_within_bounds(data, data.left_pressed_x,
                                    data.left_pressed_y)):
            if (data.shift):
                artist.press(data)
                for j, artist_j in enumerate(data.viewing_artists):
                    if (i == j):
                        continue
                    elif (artist_j.is_selected(data)):
                        data.selected_artists.clear()
                        if (j < i):
                            for k in range(j, i + 1):
                                data.viewing_artists[k].press(data)
                        elif (j > i):
                            for k in range(i, j + 1):
                                data.viewing_artists[k].press(data)
                        break
            else:
                artist.press(data)
        elif ((data.width / data.columns * 3 < data.left_pressed_x
                   < data.width / data.columns * 6) and (
        not (data.ctrl or data.shift))):
            artist.unpress(data)

    for i, song in enumerate(data.viewing_artist_songs):
        if (song.is_within_bounds(data, data.left_pressed_x,
                                  data.left_pressed_y)):
            if (data.shift):
                data.selected_ids.add(song.get_id())
                for j, song_j in enumerate(data.viewing_artist_songs):
                    if (i == j):
                        continue
                    elif (song_j.is_selected(data)):
                        data.selected_ids.clear()
                        if (j < i):
                            for k in range(j, i + 1):
                                data.selected_ids.add(
                                    data.viewing_artist_songs[k].get_id()
                                )
                        elif (j > i):
                            for k in range(i, j + 1):
                                data.selected_ids.add(
                                    data.viewing_artist_songs[k].get_id()
                                )
                        break
            else:
                song.press(data)
        elif (not (data.ctrl or data.shift)):
            song.unpress(data)


################################################################################

# SIMPLIFY
# CONTROLLER
# EVENTS 

# LEFT
# RELEASED


def simplify_left_released(data):
    if (data.left_released_x >= data.width / data.columns * 16):
        add_selected_songs_to_stage(data)
        refresh_view(data)


################################################################################

# SIMPLIFY
# CONTROLLER
# EVENTS 

# KEY


def simplify_key_pressed(data):
    if (data.mouse_moved_x < (data.width / data.columns * 3)):
        lists_key_pressed(data)
    elif (data.mouse_moved_x > (data.width / data.columns * 16)):
        stage_key_pressed(data)
    elif (data.is_songs):
        songs_key_pressed(data)
    elif (data.is_artists):
        if (data.mouse_moved_x < (data.width / data.columns * 7)):
            artists_key_pressed(data)
        elif (data.mouse_moved_x > (data.width / data.columns * 7)):
            artist_songs_key_pressed(data)


def lists_key_pressed(data):
    if (data.keysym_pressed == 'Escape'):
        lists_escape(data)
    elif (data.keysym_pressed == 'Up'):
        lists_move_up(data)
    elif (data.keysym_pressed == 'Down'):
        lists_move_down(data)


def stage_key_pressed(data):
    if (data.keysym_pressed == 'Escape'):
        stage_escape(data)
    elif ((data.keysym_pressed == 'a') and data.ctrl):
        stage_select_all(data)
    elif (data.keysym_pressed == 'Up'):
        if (data.shift):
            stage_shift_up(data)
        else:
            stage_move_up(data)
    elif (data.keysym_pressed == 'Down'):
        if (data.shift):
            stage_shift_down(data)
        else:
            stage_move_down(data)


def songs_key_pressed(data):
    if (data.keysym_pressed == 'Escape'):
        songs_escape(data)
    elif ((data.keysym_pressed == 'a') and data.ctrl):
        songs_select_all(data)
    elif (data.keysym_pressed == 'Up'):
        if (data.shift):
            songs_shift_up(data)
        else:
            songs_move_up(data)
    elif (data.keysym_pressed == 'Down'):
        if (data.shift):
            songs_shift_down(data)
        else:
            songs_move_down(data)


def artists_key_pressed(data):
    if (data.keysym_pressed == 'Escape'):
        artists_escape(data)
    elif ((data.keysym_pressed == 'a') and data.ctrl):
        artists_select_all(data)
    elif (data.keysym_pressed == 'Up'):
        if (data.shift):
            artists_shift_up(data)
        else:
            artists_move_up(data)
    elif (data.keysym_pressed == 'Down'):
        if (data.shift):
            artists_shift_down(data)
        else:
            artists_move_down(data)


def artist_songs_key_pressed(data):
    if (data.keysym_pressed == 'Escape'):
        artist_songs_escape(data)
    elif ((data.keysym_pressed == 'a') and data.ctrl):
        artist_songs_select_all(data)
    elif (data.keysym_pressed == 'Up'):
        if (data.shift):
            artist_songs_shift_up(data)
        else:
            artist_songs_move_up(data)
    elif (data.keysym_pressed == 'Down'):
        if (data.shift):
            artist_songs_shift_down(data)
        else:
            artist_songs_move_down(data)


def lists_escape(data):
    data.selected_list = ''
    data.is_songs = False
    data.is_artists = False
    del data.song_ids[:]
    del data.artist_ids[:]
    del data.artist_song_ids[:]
    refresh_view(data)
    simplify_buttons(data)


def lists_move_up(data):
    sidebar_buttons = list()
    for button in data.buttons:
        if (isinstance(button, Sidebar)):
            sidebar_buttons += [button]
    for i, sidebar_button in enumerate(sidebar_buttons):
        if (data.ctrl):
            data.start_list = 0
            sidebar_button[0].press(data)
            return
        elif ((i > 0) and sidebar_button.is_selected(data)):
            if ((sidebar_button.get_row() == 0) and (data.start_list > 0)):
                data.start_list -= 1
            sidebar_buttons[i - 1].press(data)
            break


def lists_move_down(data):
    sidebar_buttons = list()
    for button in data.buttons:
        if (isinstance(button, Sidebar)):
            sidebar_buttons += [button]
    for i, sidebar_button in enumerate(sidebar_buttons):
        if (data.ctrl):
            sidebar_button[-1].press(data)
            return
        if ((i < (len(sidebar_buttons) - 1)) and sidebar_button.is_selected(
                data)):
            if (sidebar_button.get_row() == (data.rows - 1)):
                data.start_list += 1
            sidebar_buttons[i + 1].press(data)
            break


def stage_escape(data):
    data.selected_ids.clear()
    refresh_view(data)


def stage_select_all(data):
    data.selected_ids.update(set(copy.deepcopy(data.stage_ids)))
    refresh_view(data)


def stage_shift_up(data):
    for i, song in enumerate(data.stage_songs):
        if song.is_selected(data):
            if ((i == 0) and (data.start_stage == 0)):
                continue
            elif ((i == 0) and (data.start_stage > 0)):
                data.start_stage -= 1
                refresh_view(data)
                data.selected_ids.add(data.stage_songs[i].get_id())
                refresh_view(data)
                break
            else:
                data.selected_ids.add(data.stage_songs[i - 1].get_id())
                refresh_view(data)
                break


def stage_move_up(data):
    if (data.ctrl):
        data.start_stage = 0
        data.selected_ids.clear()
        data.selected_ids.add(data.stage_ids[0])
        refresh_view(data)
        return
    for i, song in enumerate(data.stage_songs):
        if ((i == 0) and (data.start_stage == 0)):
            continue
        elif song.is_selected(data):
            if ((i == 0) and (data.start_stage > 0)):
                data.selected_ids.clear()
                data.start_stage -= 1
                refresh_view(data)
                data.selected_ids.add(data.stage_songs[i].get_id())
                refresh_view(data)
                return
            elif (i > 0):
                data.selected_ids.clear()
                data.selected_ids.add(data.stage_songs[i - 1].get_id())
                refresh_view(data)
                return
    if (data.start_stage > 0):
        data.start_stage -= 1
        refresh_view(data)
    return


def stage_shift_down(data):
    for i, song in enumerate(data.stage_songs[::-1]):
        index = len(data.stage_songs) - i - 1
        if ((0 < song.get_row() < 40) and song.is_selected(data)):
            if (index == len(data.stage_songs) - 1):
                return
            elif (song.get_row() == 39):
                if (index < len(data.stage_songs) - 1):
                    data.start_stage += 1
                    refresh_view(data)
                    data.selected_ids.add(data.stage_songs[index].get_id())
                    refresh_view(data)
                return
            else:
                data.selected_ids.add(data.stage_songs[index + 1].get_id())
                refresh_view(data)
                return


def stage_move_down(data):
    if (data.ctrl):
        data.start_stage = len(data.stage_ids) - 39
        data.selected_ids.clear()
        data.selected_ids.add(data.stage_ids[-1])
        refresh_view(data)
        return
    for i, song in enumerate(data.stage_songs[::-1]):
        index = len(data.stage_songs) - i - 1
        if ((0 < song.get_row() < 40) and song.is_selected(data)):
            if ((song.get_row() == 39) and (index < len(data.stage_songs) - 1)):
                data.selected_ids.clear()
                data.start_stage += 1
                refresh_view(data)
                data.selected_ids.add(data.stage_songs[index].get_id())
                refresh_view(data)
                return
            elif (
                        (song.get_row() < 39) and (
                        index < len(data.stage_songs) - 1)):
                data.selected_ids.clear()
                data.selected_ids.add(data.stage_songs[index + 1].get_id())
                refresh_view(data)
                return
    if (data.start_stage + 39 == len(data.stage_ids)):
        return
    else:
        data.start_stage += 1
        refresh_view(data)
        return


def songs_escape(data):
    data.selected_ids.clear()
    refresh_view(data)


def songs_select_all(data):
    data.selected_ids.update(set(data.song_ids))
    refresh_view(data)


def songs_shift_up(data):
    for i, song in enumerate(data.viewing_songs):
        if song.is_selected(data):
            if ((i == 0) and (data.start_song == 0)):
                continue
            elif ((i == 0) and (data.start_song > 0)):
                data.start_song -= 1
                refresh_view(data)
                data.selected_ids.add(data.viewing_songs[i].get_id())
                refresh_view(data)
                break
            else:
                data.selected_ids.add(data.viewing_songs[i - 1].get_id())
                refresh_view(data)
                break


def songs_move_up(data):
    if (data.ctrl):
        data.start_song = 0
        data.selected_ids.clear()
        data.selected_ids.add(data.song_ids[0])
        refresh_view(data)
        return
    for i, song in enumerate(data.viewing_songs):
        if ((i == 0) and (data.start_song == 0)):
            continue
        elif song.is_selected(data):
            if ((i == 0) and (data.start_song > 0)):
                data.selected_ids.clear()
                data.start_song -= 1
                refresh_view(data)
                data.selected_ids.add(data.viewing_songs[i].get_id())
                refresh_view(data)
                return
            elif (i > 0):
                data.selected_ids.clear()
                data.selected_ids.add(data.viewing_songs[i - 1].get_id())
                refresh_view(data)
                return
    if (data.start_song > 0):
        data.start_song -= 1
        refresh_view(data)
    return


def songs_shift_down(data):
    for i, song in enumerate(data.viewing_songs[::-1]):
        index = len(data.viewing_songs) - i - 1
        if ((0 < song.get_row() < 30) and song.is_selected(data)):
            if (index == len(data.viewing_songs) - 1):
                return
            elif (song.get_row() == 29):
                if (index < len(data.viewing_songs) - 1):
                    data.start_song += 1
                    refresh_view(data)
                    data.selected_ids.add(data.viewing_songs[index].get_id())
                    refresh_view(data)
                return
            else:
                data.selected_ids.add(data.viewing_songs[index + 1].get_id())
                refresh_view(data)
                return


def songs_move_down(data):
    if (data.ctrl):
        data.start_song = len(data.song_ids) - 29
        data.selected_ids.clear()
        data.selected_ids.add(data.song_ids[-1])
        refresh_view(data)
        return
    for i, song in enumerate(data.viewing_songs[::-1]):
        index = len(data.viewing_songs) - i - 1
        if ((0 < song.get_row() < 30) and song.is_selected(data)):
            if ((song.get_row() == 29) and (
                        index < len(data.viewing_songs) - 1)):
                data.selected_ids.clear()
                data.start_song += 1
                refresh_view(data)
                data.selected_ids.add(data.viewing_songs[index].get_id())
                refresh_view(data)
                return
            elif ((song.get_row() < 29) and (
                        index < len(data.viewing_songs) - 1)):
                data.selected_ids.clear()
                data.selected_ids.add(data.viewing_songs[index + 1].get_id())
                refresh_view(data)
                return
    if (data.start_song + 29 == len(data.song_ids)):
        return
    else:
        data.start_song += 1
        refresh_view(data)
        return


def artists_escape(data):
    data.selected_ids.clear()
    data.selected_artists.clear()
    refresh_view(data)


def artists_select_all(data):
    data.selected_artists.update(set(data.artist_ids))
    for artist_id in data.artist_ids:
        data.selected_ids.updat(set(data.artists[artist_id]['songs']))
        refresh_view(data)


def artists_shift_up(data):
    for i, artist in enumerate(data.viewing_artists):
        if artist.is_selected(data):
            if ((i == 0) and (data.start_artist == 0)):
                continue
            elif ((i == 0) and (data.start_artist > 0)):
                data.start_artist -= 1
                refresh_view(data)
                data.selected_artists.add(data.viewing_artists[i].get_id())
                refresh_view(data)
                break
            else:
                data.selected_artists.add(data.viewing_artists[i - 1].get_id())
                refresh_view(data)
                break


def artists_move_up(data):
    if (data.ctrl):
        data.start_artist = 0
        data.selected_artists.clear()
        data.viewing_artists[0].press(data)
        refresh_view(data)
        return
    for i, artist in enumerate(data.viewing_artists):
        if ((i == 0) and (data.start_artist == 0)):
            continue
        elif artist.is_selected(data):
            if ((i == 0) and (data.start_artist > 0)):
                data.selected_artists.clear()
                data.start_artist -= 1
                refresh_view(data)
                data.viewing_artists[i].press(data)
                refresh_view(data)
                return
            elif (i > 0):
                data.selected_artists.clear()
                data.viewing_artists[i - 1].press(data)
                refresh_view(data)
                return
    if (data.start_artist > 0):
        data.start_artist -= 1
        refresh_view(data)
    return


def artists_shift_down(data):
    for i, song in enumerate(data.viewing_artists[::-1]):
        index = len(data.viewing_artists) - i - 1
        if ((0 < song.get_row() < 30) and song.is_selected(data)):
            if (index == len(data.viewing_artists) - 1):
                return
            elif (song.get_row() == 29):
                if (index < len(data.viewing_artists) - 1):
                    data.start_artist += 1
                    refresh_view(data)
                    data.viewing_artists[index].press(data)
                    refresh_view(data)
                return
            else:
                data.viewing_artists[index + 1].press(data)
                refresh_view(data)
                return


def artists_move_down(data):
    if (data.ctrl):
        data.start_artist = len(data.artist_ids) - 29
        data.selected_artists.clear()
        data.viewing_artists[-1].press(data)
        refresh_view(data)
        return
    for i, artist in enumerate(data.viewing_artists[::-1]):
        index = len(data.viewing_artists) - i - 1
        if ((0 < artist.get_row() < 30) and artist.is_selected(data)):
            if ((artist.get_row() == 29) and (
                        index < len(data.viewing_artists) - 1)):
                data.selected_artists.clear()
                data.start_artist += 1
                refresh_view(data)
                data.viewing_artists[index].press(data)
                refresh_view(data)
                return
            elif ((artist.get_row() < 29) and (
                        index < len(data.viewing_artists) - 1)):
                data.selected_artists.clear()
                data.viewing_artists[index + 1].press(data)
                refresh_view(data)
                return
    if (data.start_artist + 29 == len(data.artist_ids)):
        return
    else:
        data.start_artist += 1
        refresh_view(data)
        return


def artist_songs_escape(data):
    data.selected_ids.clear()
    refresh_view(data)


def artist_songs_select_all(data):
    data.selected_ids.update(set(data.viewing_artist_songs))
    refresh_view(data)


def artist_songs_shift_up(data):
    for i, song in enumerate(data.viewing_artist_songs):
        if song.is_selected(data):
            if ((i == 0) and (data.start_song == 0)):
                continue
            elif ((i == 0) and (data.start_song > 0)):
                data.start_song -= 1
                refresh_view(data)
                data.viewing_artist_songs[i].press(data)
                refresh_view(data)
                break
            else:
                data.viewing_artist_songs[i - 1].press(data)
                refresh_view(data)
                break


def artist_songs_move_up(data):
    if (data.ctrl):
        data.start_song = 0
        data.selected_ids.clear()
        data.selected_ids.add(data.song_ids[0])
        refresh_view(data)
        return
    for i, song in enumerate(data.viewing_artist_songs):
        if ((i == 0) and (data.start_song == 0)):
            continue
        elif song.is_selected(data):
            if ((i == 0) and (data.start_song > 0)):
                data.selected_ids.clear()
                data.start_song -= 1
                refresh_view(data)
                data.viewing_artist_songs[i].press(data)
                refresh_view(data)
                return
            elif (i > 0):
                data.selected_ids.clear()
                data.viewing_artist_songs[i - 1].press(data)
                refresh_view(data)
                return
    if (data.start_song > 0):
        data.start_song -= 1
        refresh_view(data)
    return


def artist_songs_shift_down(data):
    for i, song in enumerate(data.viewing_artist_songs[::-1]):
        index = len(data.viewing_artist_songs) - i - 1
        if ((0 < song.get_row() < 30) and song.is_selected(data)):
            if (index == len(data.viewing_artist_songs) - 1):
                return
            elif (song.get_row() == 29):
                if (index < len(data.viewing_artist_songs) - 1):
                    data.start_song += 1
                    refresh_view(data)
                    data.viewing_artist_songs[index].press(data)
                    refresh_view(data)
                return
            else:
                data.viewing_artist_songs[index + 1].press(data)
                refresh_view(data)
                return


def artist_songs_move_down(data):
    if (data.ctrl):
        data.start_song = len(data.song_ids) - 29
        data.selected_ids.clear()
        data.selected_ids.add(data.song_ids[-1])
        refresh_view(data)
        return
    for i, song in enumerate(data.viewing_artist_songs[::-1]):
        index = len(data.viewing_artist_songs) - i - 1
        if ((0 < song.get_row() < 30) and song.is_selected(data)):
            if ((song.get_row() == 29) and (
                        index < len(data.viewing_artist_songs) - 1)):
                data.selected_ids.clear()
                data.start_song += 1
                refresh_view(data)
                data.viewing_artist_songs[index].press()
                refresh_view(data)
                return
            elif ((song.get_row() < 29) and (
                        index < len(data.viewing_artist_songs) - 1)):
                data.selected_ids.clear()
                data.viewing_artist_songs[index + 1].press()
                refresh_view(data)
                return
    if (data.start_song + 29 == len(data.song_ids)):
        return
    else:
        data.start_song += 1
        refresh_view(data)
        return


################################################################################

# SIMPLIFY
# VIEW


def simplify_redraw_all(canvas, data):
    canvas.create_rectangle(0, 0, data.width, data.height,
                            fill=black_background, width=0)
    canvas.create_rectangle(data.width / data.columns * 3, 0,
                            data.width / data.columns * 16, data.height,
                            fill=black_shadow)
    for song in data.viewing_songs:
        song.draw(canvas, data)
    for artist in data.viewing_artists:
        artist.draw(canvas, data)
    for song in data.viewing_artist_songs:
        song.draw(canvas, data)
    for song in data.stage_songs:
        song.draw(canvas, data)
    for button in data.buttons:
        button.draw(canvas, data)


################################################################################

class AnalyzeSong(Song):
    def __init__(self, data, row, song_id):
        super().__init__(data, row, song_id)
        self.parameter = data.parameter
        self.time = self.duration

    def draw(self, canvas, data):
        self.update_dimensions(data)
        if (self.is_selected(data)):
            self.fill = gray_select
            self.line_fill = black_shadow
        canvas.create_rectangle(self.x1 + data.width / data.columns / 3,
                                self.y1,
                                self.x2 - data.width / data.columns / 3,
                                self.y2,
                                fill=self.fill, width=0)
        canvas.create_line(self.x1 + data.width / data.columns / 3, self.y1,
                           self.x2 - data.width / data.columns / 3, self.y1,
                           fill=self.line_fill)
        canvas.create_line(self.x1 + data.width / data.columns / 3, self.y2,
                           self.x2 - data.width / data.columns / 3, self.y2,
                           fill=self.line_fill)
        canvas.create_text(self.x1 + data.width / data.columns * 0.75, self.cy,
                           text=truncate(self.title,
                                         data.width / data.columns * 4),
                           fill=self.text_fill, anchor=W, font='Proxima 10')
        canvas.create_text(data.width * 7.75 / data.columns, self.cy,
                           text=truncate(self.artist_name,
                                         data.width / data.columns * (3.25)),
                           fill=self.text_fill, anchor=W, font='Proxima 10')
        canvas.create_text(data.width * 11 / data.columns, self.cy,
                           text=truncate(self.album_name,
                                         data.width / data.columns * (4)),
                           fill=self.text_fill, anchor=W, font='Proxima 10')
        canvas.create_text(data.width * 15 / data.columns, self.cy,
                           text=self.duration, fill=gray, anchor=W,
                           font='Proxima 10')
        if (self.song_id not in data.stage_ids):
            canvas.create_text(self.x1 + data.width / data.columns / 2, self.cy,
                               text='+', fill=self.plus_fill,
                               font=('Proxima %d bold' % (self.symbol_size,)))
        else:
            canvas.create_text(self.x1 + data.width / data.columns / 2, self.cy,
                               text='-', fill=self.minus_fill,
                               font=('Proxima %d bold' % (self.symbol_size,)))


################################################################################

# ANALYZE
# MODEL

def analyze_init(data):
    clean(data)
    data.mode = 'analyze'
    analyze_buttons(data)


def analyze_buttons(data):
    del data.buttons[:]
    data.buttons += [
        Button(data, 'DISPLAY HISTOGRAM', 18 / data.columns, 1 / data.rows,
               histogram, 3 / data.columns, .95 / data.rows,
               green, green_hover),
        Button(data, 'DISPLAY DISTRIBUTION PLOT', 18 / data.columns,
               2 / data.rows,
               distribution_plot, 3 / data.columns,
               .95 / data.rows,
               red, red_hover),
        Button(data, ' << STAGE CUSTOM PLAYLIST', 18 / data.columns,
               29 / data.rows,
               simplify_init, 3 / data.columns, .95 / data.rows, blue,
               blue_hover),
        Sidebar(data, 'YOUR TOP SONGS', 0 - data.start_list, data.top_songs),
        Sidebar(data, 'Short Term Top Songs', 1 - data.start_list,
                data.songs_top['short_term']),
        Sidebar(data, 'Medium Term Top Songs', 2 - data.start_list,
                data.songs_top['medium_term']),
        Sidebar(data, 'Long Term Top Songs', 3 - data.start_list,
                data.songs_top['long_term']),
        Sidebar(data, 'YOUR CUSTOM PLAYLIST', 5 - data.start_list,
                data.stage_ids)
    ]
    for offset, playlist_id in enumerate(data.playlists):
        data.buttons += [
            Sidebar(data, truncate(data.playlists[playlist_id]['name'],
                                   data.width / data.columns * 3),
                    6 + offset - data.start_list,
                    data.playlists[playlist_id]['songs'])
        ]
    if (data.is_songs):
        data.buttons += [
            SongHeader(data, truncate('TITLE', data.width / data.columns * 3),
                       0,
                       order_songs_by_title),
            SongHeader(data, truncate('ARTIST', data.width / data.columns * 3),
                       1,
                       order_songs_by_artist),
            SongHeader(data, truncate('ALBUM', data.width / data.columns * 3),
                       2,
                       order_songs_by_album),
            SongHeader(data, truncate('TIME', data.width / data.columns * 3), 3,
                       order_songs_by_time)
        ]

        data.buttons += [
            Button(data, 'acousticness', 18 / data.columns, 4 / data.rows,
                   acousticness, 3 / data.columns, .9 / data.rows,
                   blue, blue_hover),
            Button(data, 'danceability', 18 / data.columns, 5 / data.rows,
                   danceability, 3 / data.columns,
                   .9 / data.rows,
                   blue, blue_hover),
            Button(data, 'energy', 18 / data.columns, 6 / data.rows,
                   energy, 3 / data.columns, .9 / data.rows,
                   blue, blue_hover),
            Button(data, 'liveness', 18 / data.columns, 7 / data.rows,
                   liveness, 3 / data.columns,
                   .9 / data.rows,
                   blue, blue_hover),
            Button(data, 'time', 18 / data.columns, 8 / data.rows,
                   duration_ms, 3 / data.columns, .9 / data.rows,
                   blue, blue_hover),
            Button(data, 'loudness', 18 / data.columns, 9 / data.rows,
                   loudness, 3 / data.columns,
                   .9 / data.rows,
                   blue, blue_hover),
            Button(data, 'popularity', 18 / data.columns, 10 / data.rows,
                   popularity, 3 / data.columns, .9 / data.rows,
                   blue, blue_hover),
            Button(data, 'speechiness', 18 / data.columns, 11 / data.rows,
                   speechiness, 3 / data.columns,
                   .9 / data.rows,
                   blue, blue_hover),
            Button(data, 'tempo', 18 / data.columns, 12 / data.rows,
                   tempo, 3 / data.columns, .9 / data.rows,
                   blue, blue_hover),
            Button(data, 'valence', 18 / data.columns, 13 / data.rows,
                   valence, 3 / data.columns,
                   .9 / data.rows,
                   blue, blue_hover),
            Button(data, 'CREATE IN SPOTIFY', 18 / data.columns, 15 / data.rows,
                   create_playlist, 3 / data.columns, 1 / data.rows,
                   green, green_hover)
        ]


def acousticness(data):
    data.parameter = 'acousticness'
    analyze_view(data)


def danceability(data):
    data.parameter = 'danceability'
    analyze_view(data)


def energy(data):
    data.parameter = 'energy'
    analyze_view(data)


def liveness(data):
    data.parameter = 'liveness'
    analyze_view(data)


def duration_ms(data):
    data.parameter = 'duration_ms'
    analyze_view(data)


def loudness(data):
    data.parameter = 'loudness'
    analyze_view(data)


def popularity(data):
    data.parameter = 'popularity'
    analyze_view(data)


def speechiness(data):
    data.parameter = 'speechiness'
    analyze_view(data)


def tempo(data):
    data.parameter = 'tempo'
    analyze_view(data)


def valence(data):
    data.parameter = 'valence'
    analyze_view(data)


def create_playlist(data):
    try:
        token = util.prompt_for_user_token(data.username, 'user-library-modify')
        sp = spotipy.Spotify(auth=token)
    except:
        prompt_for_user_token(data.username, 'user-library-modify')
        sp = spotipy.Spotify(auth=token)
    sp.trace = False
    playlist = sp.user_playlist_create(data.username, data.selected_list)
    playlist_uri = playlist['uri']
    results = sp.user_playlist_add_tracks(data.username, playlist_uri,
                                          data.song_ids)


################################################################################


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

    f.suptitle('%s of %s' % (data.parameter, data.selected_list), fontsize=14,
               fontweight='bold')

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

    f.suptitle('%s of %s' % (data.parameter, data.selected_list), fontsize=14,
               fontweight='bold')

    plt.setp(axes, yticks=[])
    plt.tight_layout()
    plt.show()


################################################################################


def analyze_view(data):
    del data.values[:]
    del data.stage_songs[:]
    del data.viewing_songs[:]
    del data.viewing_artists[:]
    del data.viewing_artist_songs[:]
    for row, song_id in enumerate(data.song_ids[data.start_song:]):
        data.viewing_songs += [AnalyzeSong(data, row + 1, song_id)]
    for song_id in data.song_ids:
        data.values += [data.songs[song_id][data.parameter]]


################################################################################

# ANALYZE
# CONTROLLER
# EVENTS

# MOUSE


def analyze_mouse_moved(data):
    for song in data.viewing_songs:
        if (song.is_within_bounds(data, data.mouse_moved_x,
                                  data.mouse_moved_y)):
            song.hover()
        else:
            song.unhover()

    for button in data.buttons:
        if (button.is_within_bounds(data, data.mouse_moved_x,
                                    data.mouse_moved_y)):
            button.hover()
        else:
            button.unhover()


################################################################################

# ANALYZE
# CONTROLLER
# EVENTS

# LEFT
# PRESSED


def analyze_left_pressed(data):
    for button in data.buttons:
        if (button.is_within_bounds(data, data.left_pressed_x,
                                    data.left_pressed_y)):
            button.press(data)
        else:
            button.unpress(data)

    for i, song in enumerate(data.viewing_songs):
        if (song.is_within_bounds(data, data.left_pressed_x,
                                  data.left_pressed_y)):
            if (data.shift):
                data.selected_ids.add(song.get_id())
                for j, song_j in enumerate(data.viewing_songs):
                    if (i == j):
                        continue
                    elif (song_j.is_selected(data)):
                        data.selected_ids.clear()
                        if (j < i):
                            for k in range(j, i + 1):
                                data.selected_ids.add(
                                    data.viewing_songs[k].get_id()
                                )
                        elif (j > i):
                            for k in range(i, j + 1):
                                data.selected_ids.add(
                                    data.viewing_songs[k].get_id()
                                )
                        break
            else:
                song.press(data)
        elif (not (data.ctrl or data.shift)):
            song.unpress(data)


################################################################################

# ANALYZE
# CONTROLLER
# EVENTS

# KEY


def analyze_key_pressed(data):
    if (data.mouse_moved_x < (data.width / data.columns * 3)):
        lists_key_pressed(data)
    elif (data.mouse_moved_x > (data.width / data.columns * 16)):
        stage_key_pressed(data)
    elif (data.is_songs):
        songs_key_pressed(data)


def lists_key_pressed(data):
    if (data.keysym_pressed == 'Escape'):
        lists_escape(data)
    elif (data.keysym_pressed == 'Up'):
        lists_move_up(data)
    elif (data.keysym_pressed == 'Down'):
        lists_move_down(data)


def stage_key_pressed(data):
    if (data.keysym_pressed == 'Escape'):
        stage_escape(data)
    elif ((data.keysym_pressed == 'a') and data.ctrl):
        stage_select_all(data)
    elif (data.keysym_pressed == 'Up'):
        if (data.shift):
            stage_shift_up(data)
        else:
            stage_move_up(data)
    elif (data.keysym_pressed == 'Down'):
        if (data.shift):
            stage_shift_down(data)
        else:
            stage_move_down(data)


def songs_key_pressed(data):
    if (data.keysym_pressed == 'Escape'):
        songs_escape(data)
    elif ((data.keysym_pressed == 'a') and data.ctrl):
        songs_select_all(data)
    elif (data.keysym_pressed == 'Up'):
        if (data.shift):
            songs_shift_up(data)
        else:
            songs_move_up(data)
    elif (data.keysym_pressed == 'Down'):
        if (data.shift):
            songs_shift_down(data)
        else:
            songs_move_down(data)


def lists_escape(data):
    data.selected_list = ''
    data.is_songs = False
    data.is_artists = False
    del data.song_ids[:]
    del data.artist_ids[:]
    del data.artist_song_ids[:]
    analyze_view(data)
    analyze_buttons(data)


def lists_move_up(data):
    sidebar_buttons = list()
    for button in data.buttons:
        if (isinstance(button, Sidebar)):
            sidebar_buttons += [button]
    for i, sidebar_button in enumerate(sidebar_buttons):
        if (data.ctrl):
            data.start_list = 0
            sidebar_button[0].press(data)
            return
        elif ((i > 0) and sidebar_button.is_selected(data)):
            if ((sidebar_button.get_row() == 0) and (data.start_list > 0)):
                data.start_list -= 1
            sidebar_buttons[i - 1].press(data)
            break


def lists_move_down(data):
    sidebar_buttons = list()
    for button in data.buttons:
        if (isinstance(button, Sidebar)):
            sidebar_buttons += [button]
    for i, sidebar_button in enumerate(sidebar_buttons):
        if (data.ctrl):
            sidebar_button[-1].press(data)
            return
        if ((i < (len(sidebar_buttons) - 1)) and sidebar_button.is_selected(
                data)):
            if (sidebar_button.get_row() == (data.rows - 1)):
                data.start_list += 1
            sidebar_buttons[i + 1].press(data)
            break


def songs_escape(data):
    data.selected_ids.clear()
    analyze_view(data)


def songs_select_all(data):
    data.selected_ids.update(set(data.song_ids))
    analyze_view(data)


def songs_shift_up(data):
    for i, song in enumerate(data.viewing_songs):
        if song.is_selected(data):
            if ((i == 0) and (data.start_song == 0)):
                continue
            elif ((i == 0) and (data.start_song > 0)):
                data.start_song -= 1
                analyze_view(data)
                data.selected_ids.add(data.viewing_songs[i].get_id())
                analyze_view(data)
                break
            else:
                data.selected_ids.add(data.viewing_songs[i - 1].get_id())
                analyze_view(data)
                break


def songs_move_up(data):
    if (data.ctrl):
        data.start_song = 0
        data.selected_ids.clear()
        data.selected_ids.add(data.song_ids[0])
        analyze_view(data)
        return
    for i, song in enumerate(data.viewing_songs):
        if ((i == 0) and (data.start_song == 0)):
            continue
        elif song.is_selected(data):
            if ((i == 0) and (data.start_song > 0)):
                data.selected_ids.clear()
                data.start_song -= 1
                analyze_view(data)
                data.selected_ids.add(data.viewing_songs[i].get_id())
                analyze_view(data)
                return
            elif (i > 0):
                data.selected_ids.clear()
                data.selected_ids.add(data.viewing_songs[i - 1].get_id())
                analyze_view(data)
                return
    if (data.start_song > 0):
        data.start_song -= 1
        analyze_view(data)
    return


def songs_shift_down(data):
    for i, song in enumerate(data.viewing_songs[::-1]):
        index = len(data.viewing_songs) - i - 1
        if ((0 < song.get_row() < 30) and song.is_selected(data)):
            if (index == len(data.viewing_songs) - 1):
                return
            elif (song.get_row() == 29):
                if (index < len(data.viewing_songs) - 1):
                    data.start_song += 1
                    analyze_view(data)
                    data.selected_ids.add(data.viewing_songs[index].get_id())
                    analyze_view(data)
                return
            else:
                data.selected_ids.add(data.viewing_songs[index + 1].get_id())
                analyze_view(data)
                return


def songs_move_down(data):
    if (data.ctrl):
        data.start_song = len(data.song_ids) - 29
        data.selected_ids.clear()
        data.selected_ids.add(data.song_ids[-1])
        analyze_view(data)
        return
    for i, song in enumerate(data.viewing_songs[::-1]):
        index = len(data.viewing_songs) - i - 1
        if ((0 < song.get_row() < 30) and song.is_selected(data)):
            if ((song.get_row() == 29) and (
                        index < len(data.viewing_songs) - 1)):
                data.selected_ids.clear()
                data.start_song += 1
                analyze_view(data)
                data.selected_ids.add(data.viewing_songs[index].get_id())
                analyze_view(data)
                return
            elif ((song.get_row() < 29) and (
                        index < len(data.viewing_songs) - 1)):
                data.selected_ids.clear()
                data.selected_ids.add(data.viewing_songs[index + 1].get_id())
                analyze_view(data)
                return
    if (data.start_song + 29 == len(data.song_ids)):
        return
    else:
        data.start_song += 1
        analyze_view(data)
        return


################################################################################

# ANALYZE
# VIEW


def analyze_redraw_all(canvas, data):
    canvas.create_rectangle(0, 0, data.width, data.height,
                            fill=black_background, width=0)
    canvas.create_rectangle(data.width / data.columns * 3, 0,
                            data.width / data.columns * 16, data.height,
                            fill=black_shadow)
    for song in data.viewing_songs:
        song.draw(canvas, data)
    for button in data.buttons:
        button.draw(canvas, data)


################################################################################

run()

################################################################################
