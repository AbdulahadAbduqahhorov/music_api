from django.test import TestCase,Client

from music.models import Artist, Album, Song


class TestArtistViewSet(TestCase):
    def setUp(self) -> None:
        self.artist = Artist.objects.create(name='Test Artist')
        self.client = Client()

    def test_get_all_albums(self):
        response = self.client.get('/artists/')
        data = response.data

        self.assertEqual(response.status_code,200)
        self.assertEqual(len(data),1)
        self.assertIsNotNone(data[0]['id'])
        self.assertEqual(data[0]['name'],'Test Artist')


class TestSongViewSet(TestCase):
    def setUp(self) -> None:
        self.artist = Artist.objects.create(name="Test artist")
        self.album = Album.objects.create(artist=self.artist,title="Test album")
        self.song = Song.objects.create(album=self.album,title="Test song")
        self.client = Client()

    def test_song_search(self):
        response = self.client.get('/songs/?search=Test')
        data = response.data


        self.assertEqual(response.status_code,200)
        self.assertEqual(len(data),1)
        self.assertEqual(data[0]['title'], "Test song")

