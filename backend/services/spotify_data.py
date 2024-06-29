import spotipy
from models.oauth2 import Oauth2
import time
import requests as rq
from typing import List, Dict, Any

class Spotify_API:
    def __init__(self):
        self.token = Oauth2().get_token()['access_token']
        self.headers = {"Authorization": "Bearer {}".format(self.token)}
        self.sp = spotipy.client.Spotify(self.headers)


    def extract_artist_info(self, artist_info: List[Dict[str, Any]]) -> (str, str):
        artist_name = artist_info[0]['name']
        artist_id = artist_info[0]['id']

        return artist_name, artist_id

    def extract_album_info(self, album: Dict[str, Any]) -> (str, str):
        album_name = album['name']
        album_image_url = album['images'][0]['url']
        return album_name, album_image_url

    def transform_item(self, item: Dict[str, Any]) -> List[Any]:
        current_track = item['track']
        time = item['played_at']
        album = current_track['album']
        album_name, album_image_url = self.extract_album_info(album)
        artist_name, artist_id = self.extract_artist_info(album['artists'])
        transformed_time = self._trans_time(time)
        return [current_track['name'], artist_name, album_image_url, transformed_time, artist_id]

    def extract_items_info(self, items: List[Dict[str, str]]) -> List[List[str]]:
        return [self.transform_item(item) for item in items]

    def fetch_recent_track(self) -> List[List[str]]:
        items = self.fetch_recent_items()
        recent_tracks = self.extract_items_info(items)

        for track in recent_tracks:
            artist_info = self.fetch_artist_info(track[-1])
            self.fetch_artist_genres(track, artist_info)
        return recent_tracks

    def fetch_artist_genres(self, track: List, artist_info: Dict[str, Any]):
        artist_image_url = artist_info['images'][0]['url']
        artist_genres = artist_info['genres']
        track[-1] = artist_image_url
        track.append(artist_genres)
        
    def fetch_artist_info(self, artist_id: str) -> Dict[str, Any]:
        URL = 'https://api.spotify.com/v1/artists/{}'.format(artist_id)
        artist_info = rq.get(URL, headers = self.headers).json()
        return artist_info

    def fetch_recent_items(self):
        data = self.sp.current_user_recently_played(50)
        if data is None:
            return None
        return data['items']

    def _trans_time(self, time: str) -> str:
        time = time.split('T')
        date = time[0]
        time = time[1].split('.')[0]
        return date + " " + time

    def fetch_user_info(self):
        user = self.sp.me()
        return [user['display_name'], user['images'][0]['url']]



    
