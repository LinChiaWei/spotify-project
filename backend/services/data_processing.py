def count_song(data):
    song_count = {}
    song_list = []
    for song in data:
        # print(song)
        song_name = song[0]
        artist_name =  song[1]
        artist_img_url =  song[2]
        song_image_url = song[3]
        if song_name in song_count:
            continue
        else:
            song_count.setdefault(song_name,[])
            song_count[song_name].append(0)
            song_count[song_name].append(artist_name)
            song_count[song_name].append(artist_img_url)
            song_count[song_name].append(song_image_url)

    for song in data:
        song_name = song[0]
        song_count[song_name][0] +=1

    for item in song_count:
        dic = {}
        dic['SongName'] = item
        dic['Artist'] = song_count[item][1]
        dic['ArtistImg'] = song_count[item][2]
        dic['Cover'] = song_count[item][3]
        dic['Count'] = song_count[item][0]
        data = [item, song_count[item][1],song_count[item][2],song_count[item][3],song_count[item][0]]
        song_list.append(data)

    song_list.sort(key=sort_song, reverse=True)
    
    return song_list

def count_artist(data):
    artist_count = {}
    artist_list = []
    for song in data:
        artist_name = song[1]
        artist_img_url =  song[2]
        if artist_name in artist_count:
            continue
        else:
            artist_count.setdefault(artist_name,[])
            artist_count[artist_name].append(0)
            artist_count[artist_name].append(artist_img_url)

    for song in data:
        artist_name = song[1]
        artist_count[artist_name][0] +=1

    for item in artist_count:
        dic = {}
        dic['Artist'] = item
        dic['ArtistImg'] = artist_count[item][1]
        dic['Count'] = artist_count[item][0]
        data = [item, artist_count[item][1],artist_count[item][0]]
        artist_list.append(data)

    artist_list.sort(key=sort_artist,reverse=True)
    
    return artist_list

    def _sort_song(list):
        return list[4]

    def _sort_artist(list):
        return list[2]