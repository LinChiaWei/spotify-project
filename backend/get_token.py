from secrets import *
import spotipy.util as util


def get_token():
    username = 'kevin880407'
    scope = ['user-library-read','user-read-private','user-read-recently-played','user-read-currently-playing']
    token = util.prompt_for_user_token(username,scope,
                                client_id='a5f4717d6cbe43fea2cc354da04490b6',
                                client_secret='4eaba7b3f548455dae6a2ac83d8e39e1',
                                redirect_uri='http://localhost:8888/callback')

    return token
