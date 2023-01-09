import spotipy
import spotipy.util as util

client_id = 'a5f4717d6cbe43fea2cc354da04490b6'
client_secret = '4eaba7b3f548455dae6a2ac83d8e39e1'
redirect_uri = 'http://localhost:8888/callback'
username = 'kevin880407'
scope = ['user-library-read','user-read-recently-played']


def get_token():
    username = 'kevin880407'
    scope = ['user-library-read','user-read-private','user-read-recently-played','user-read-currently-playing']
    # token = util.prompt_for_user_token(username,scope,
    #                         client_id='a5f4717d6cbe43fea2cc354da04490b6',
    #                         client_secret='4eaba7b3f548455dae6a2ac83d8e39e1',
    #                         redirect_uri='http://localhost:3000')
    Oauth = spotipy.oauth2.SpotifyPKCE(client_id,redirect_uri='http://localhost:8888/callback',scope=scope)
    token = Oauth.get_access_token()

    return token



# Oauth = spotipy.oauth2.SpotifyPKCE(client_id,redirect_uri='http://localhost:3000/callback/',scope=scope)
# token = Oauth.get_access_token()
# headers = {"Authorization": "Bearer {}".format(token)}
# print(headers)