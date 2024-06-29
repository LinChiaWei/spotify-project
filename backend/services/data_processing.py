from typing import List, Dict, Any
from collections import defaultdict
from functools import reduce

class DataProcessing:
    def __init__(self):
        pass


    def mapper_song(self, song: List[str]) -> Dict[str, List[Any]]:
        song_name = song[0]
        artist_name = song[1]
        artist_img_url = song[2]
        song_image_url = song[3]
        return [[song_name, artist_name, artist_img_url, song_image_url, 1]]

    def reducer_song(self, acc: Dict[str, List[Any]], songs: List[List]) -> Dict[str, List[Any]]:
        for song in songs:
            if song[0] in acc:
                acc[song[0]][0] += song[4]
            else:
                acc[song[0]] = [1, song[1], song[2], song[3]]
        return acc 

    def mapper_artist(self, song: List[str]) -> Dict[str, List[Any]]:
        artist_name = song[1]
        artist_img_url = song[2]
        return [[artist_name, artist_img_url, 1]]

    def reducer_artist(self, acc: Dict[str, List[Any]], artists: List[List]) -> Dict[str, List[Any]]:
        for artist in artists:
            if artist[0] in acc:
                acc[artist[0]][0] += artist[2]
            else:
                acc[artist[0]] = [1, artist[1]]
        return acc

    def count_song(self, data: List[List[str]]) -> List[List[Any]]:
        mapped = map(self.mapper_song, data)
        reduced = reduce(self.reducer_song, mapped, defaultdict(list))
        
        song_list = [[name, details[1], details[2], details[3], details[0]] 
                    for name, details in reduced.items()]
        song_list.sort(key=lambda x: x[4], reverse=True)

        return song_list

    def count_artist(self, data: List[List[str]]) -> List[List[Any]]:
        mapped = map(self.mapper_artist, data)
        reduced = reduce(self.reducer_artist, mapped, defaultdict(list)) 

        artist_list = [[name, details[1], details[0]] 
                    for name, details in reduced.items()]
        artist_list.sort(key=lambda x: x[2], reverse=True)
        return artist_list

