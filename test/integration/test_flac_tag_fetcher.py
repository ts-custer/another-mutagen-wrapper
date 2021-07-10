# test_flac_tag_fetcher.py
import os
import unittest

from flac.flac_tag_fetcher import FlacTagFetcher
from audio_tag_data import AudioTagData, AudioTagKey, AudioTagPicture

fixtures_directory_path = os.path.dirname(os.path.realpath(__file__)) + '/fixtures/'


class FlacTagFetcherTest(unittest.TestCase):

    def setUp(self) -> None:
        self.expected_tag_data = AudioTagData()
        self.expected_tag_data.set_key_value_pair(AudioTagKey.album, 'flac album')
        self.expected_tag_data.set_key_value_pair(AudioTagKey.artist, 'flac artist')
        self.expected_tag_data.set_key_value_pair(AudioTagKey.comment, 'flac comment')
        self.expected_tag_data.set_key_value_pair(AudioTagKey.composer, 'flac composer')
        self.expected_tag_data.set_key_value_pair(AudioTagKey.genre, 'flac genre')
        self.expected_tag_data.set_key_value_pair(AudioTagKey.title, 'flac title')
        self.expected_tag_data.set_key_value_pair(AudioTagKey.track_number, '10/13')
        self.expected_tag_data.set_key_value_pair(AudioTagKey.year, '2023')
        picture_name = 'flac.jpg'
        with open(fixtures_directory_path + picture_name, "rb") as f:
            picture_data = f.read()
        self.expected_tag_data.picture = AudioTagPicture(picture_name, picture_data)

    def test(self):
        flac_tag_fetcher = FlacTagFetcher(fixtures_directory_path + 'flac.flac')
        flac_tag_fetcher.fetch_tags()
        self.assertEqual(self.expected_tag_data, flac_tag_fetcher.tag_data)


if __name__ == '__main__':
    unittest.main()
