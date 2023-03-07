import spotipy
import spotipy.util as util
import json
from models.get_token import get_token
from models.get_token import find_token

  
client_id = 'a5f4717d6cbe43fea2cc354da04490b6'
redirect_uri = 'http://localhost:8888/callback/'
scope = ['user-library-read','user-read-private','user-read-recently-played','user-read-currently-playing']

class Data_op():
    def get_token():
        Oauth = spotipy.oauth2.SpotifyPKCE(client_id,redirect_uri,scope=scope)
        token = Oauth.get_access_token()

        return token

    def find_token():
        f = open('backend\.cache')
        token = json.load(f)
        return token

    def find_songs_name(items):
        last50songs = []
        for i in range(len(items)):
            data = []
            current_track = items[i]['track']
            album = current_track['album']
            album_name = album['name']
            album_image_inf = album['images'][1]
            album_image_url = album_image_inf['url']
            artist_inf = album['artists']
            artist_name = artist_inf[0]['name']
            data.append(current_track['name'])
            data.append(album_image_url)
            last50songs.append(data)

        return last50songs
    
    def take_second(list):
        return list[2]

    def get_data():
        song_count = {}
        song_list = []
        token = get_token()
        headers = {"Authorization": "Bearer {}".format(token)}
        # print(headers)

        sp = spotipy.client.Spotify(headers)

        data = sp.current_user_recently_played(50)
        items =  data['items']


        last50songs = find_songs_name(items)

        for song in last50songs:
            # print(song)
            song_name = song[0]
            song_image_url = song[1]
            if song_name in song_count:
                continue
            else:
                song_count.setdefault(song_name,[])
                song_count[song_name].append(0)
                song_count[song_name].append(song_image_url)


        for song in last50songs:
            song_name = song[0]
            song_count[song_name][0] +=1

        for item in song_count:
            dic = {}
            dic['SongName'] = item
            dic['Cover'] = song_count[item][1]
            dic['Count'] = song_count[item][0]
            data = [item, song_count[item][1] ,song_count[item][0]]
            song_list.append(data)

        song_list.sort(key=take_second,reverse=True)

        return song_list

    def get_user_inf():
        token = find_token()
        headers = {"Authorization": "Bearer {}".format(token)}
        sp = spotipy.client.Spotify(headers)
        user = sp.me()
        print(user)
        print(user['display_name'])
        print(user['images'][0]['url'])

    def take_second(list):
        return list[2]

    def update_data(db_data,new_data):
        data_list = list(map(list,db_data))
        for i in new_data:
            if any(i[0] in (match := nested) for nested in data_list):
                match[2] = match[2]+i[2]
            else:
                data_list.append(i)

        data_list.sort(key=take_second,reverse=True)
        return data_list
