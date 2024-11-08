import pprint

import requests
from threading import Thread, Event
import queue

ACCESS_TOKEN = 'CXyFeSBw2lAdG41xkuU3LS6a_nwyxwwCz2dCkUohw-rw0C49x2HqP__6_4is5RPx'
RANDOM_GENRE_API_URL = 'https://binaryjazz.us/wp-json/genrenator/v1/genre/'
GENIUS_API_URL = 'https://api.genius.com/search'
GENIUS_URL = 'https://genius.com/'


class GetGenre(Thread):

    def __init__(self, queue, stop_event):
        self.queue = queue
        self.stop_event = stop_event
        super().__init__()

    def run(self):
        while not stop_event.is_set():
            genre = requests.get(RANDOM_GENRE_API_URL).json()
            self.queue.put(genre)

class Genius(Thread):
    all_songs = []

    def __init__(self, queue, stop_event, counter):
        self.queue = queue
        self.counter = counter
        self.stop_event = stop_event
        super().__init__()

    def run(self):
        while not self.stop_event.is_set():
            genre = self.queue.get()
            data = requests.get(GENIUS_API_URL, params={'access_token': ACCESS_TOKEN, 'q': genre})
            data = data.json()
            try:
                song_id = data['response']['hits'][0]['result']['api_path']
                self.all_songs.append({'genre': genre, 'song': f'{GENIUS_URL}{song_id}/apple_music_player'})
                if self._list_is_filed():
                    self.stop_event.set()
            except IndexError as e:
                self.run()

    def _list_is_filed(self):
        return len(self.all_songs) > self.counter



queue = queue.Queue()
stop_event = Event()
genre_list = []
genius_list = []
counter = 10

for _ in range(4):
    t = GetGenre(queue, stop_event)
    t.start()
    genre_list.append(t)

for _ in range(10):
    t = Genius(queue, stop_event, counter)
    t.start()
    genius_list.append(t)

for t in genius_list:
    t.join()
stop_event.set()

for t in genre_list:
    t.join()

print(queue.qsize())
pprint.pprint(Genius.all_songs)
print(len(Genius.all_songs))
