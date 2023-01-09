import spotipy,os
import spotipy.util as util


client_id = 'a5f4717d6cbe43fea2cc354da04490b6'
redirect_uri = 'http://localhost:8888/callback/'
scope = ['user-library-read','user-read-private','user-read-recently-played','user-read-currently-playing']


def get_token():
    Oauth = spotipy.oauth2.SpotifyPKCE(client_id,redirect_uri,scope=scope)
    token = Oauth.get_access_token()

    return token
