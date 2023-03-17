import spotipy,os
import spotipy.util as util
import json
  
client_id = 'a5f4717d6cbe43fea2cc354da04490b6'
redirect_uri = 'http://localhost:8888/callback/'
client_secret = '4eaba7b3f548455dae6a2ac83d8e39e1'
scope = ['user-library-read','user-read-private','user-read-recently-played','user-read-currently-playing']


def get_token():
    # Oauth = spotipy.oauth2.SpotifyPKCE(client_id,redirect_uri,scope=scope)
    Oauth = spotipy.oauth2.SpotifyOAuth(client_id=client_id,
                                    client_secret=client_secret,
                                    redirect_uri=redirect_uri,
                                    scope=scope)
    token = Oauth.get_access_token()
    # print(token)
    return token

def find_token():
    f = open('backend\.cache')
    token = json.load(f)
    return token
