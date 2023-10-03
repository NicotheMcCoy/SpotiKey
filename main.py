import spotipy
import os
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv

load_dotenv()

# Input Spotify API credentials
client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")

# Setup Spotify API client
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=client_id, client_secret=client_secret))


def get_track_id(artist_name, track_name):
    query = f"artist:{artist_name} track:{track_name}"
    results = sp.search(q=query, type="track", limit=1)
    items = results['tracks']['items']
    if items:
        return items[0]['id']
    else:
        return None


def get_track_features(track_id):
    features = sp.audio_features([track_id])[0]
    if features:
        return number_to_key(features['key']), mode_to_modality(features['mode']), features['tempo']
    else:
        return None, None, None


def number_to_key(note_number):
    keys = ["C", "C♯/D♭", "D", "D♯/E♭", "E", "F", "F♯/G♭", "G", "G♯/A♭", "A", "A♯/B♭", "B"]
    return keys[note_number]


def mode_to_modality(mode_number):
    return "Major" if mode_number == 1 else "Minor"


def main():
    # Input artist and song names
    artist_name = input("Enter the artist name: ")
    track_name = input("Enter the track name: ")

    # Get track ID
    track_id = get_track_id(artist_name, track_name)

    if track_id:
        # Get track features
        key, mode, bpm = get_track_features(track_id)
        if key is not None and mode is not None and bpm is not None:
            print(f"The song '{track_name}' by {artist_name} has a key of {key} {mode} and a BPM of {bpm}.")
        else:
            print(f"Could not retrieve the key and BPM for '{track_name}' by {artist_name}.")
    else:
        print(f"No track found for '{track_name}' by {artist_name}.")


if __name__ == "__main__":
    main()
