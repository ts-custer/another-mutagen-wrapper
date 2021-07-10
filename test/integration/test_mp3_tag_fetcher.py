import os
import unittest

from mp3 import Mp3TagFetcher
from audio_tag_data import AudioTagKey, AudioTagData, AudioTagPicture

fixtures_directory_path = os.path.dirname(os.path.realpath(__file__)) + '/fixtures/'


def initiate_tag_data(id3_subversion: int) -> AudioTagData:
    tag_data = AudioTagData()
    version = f'id3v2.{id3_subversion}'
    tag_data.set_key_value_pair(AudioTagKey.album, f'{version} album')
    tag_data.set_key_value_pair(AudioTagKey.artist, f'{version} artist')
    tag_data.set_key_value_pair(AudioTagKey.comment, f'{version} comment')
    tag_data.set_key_value_pair(AudioTagKey.composer, f'{version} composer')
    tag_data.set_key_value_pair(AudioTagKey.genre, f'{version} genre')
    tag_data.set_key_value_pair(AudioTagKey.title, f'{version} title')
    picture_name = f'{version}.jpg'
    with open(fixtures_directory_path + picture_name, "rb") as f:
        picture_data = f.read()
    tag_data.picture = AudioTagPicture(picture_name, picture_data)
    return tag_data


# class Id3v1FetcherTest(unittest.TestCase):
#
#     def setUp(self) -> None:
#         dir_path = os.path.dirname(os.path.realpath(__file__))
#         full_filename = dir_path + '/fixtures/id3v1.mp3'
#         mp3_file = mutagen.File(full_filename)
#         mp3_tag_fetcher.fetch_mp3_tag(mp3_file)
#
#
#     def test(self):
#         # mp3_tag_fetcher.tag_data.pprint()
#         self.assertEqual('id3v1 album', mp3_tag_fetcher.tag_data.get_value_by_key(key.album))
#         self.assertEqual('id3v1 artist', mp3_tag_fetcher.tag_data.get_value_by_key(key.artist))
#         self.assertEqual('2020', mp3_tag_fetcher.tag_data.get_value_by_key(key.date))
#         self.assertEqual('7', mp3_tag_fetcher.tag_data.get_value_by_key(key.track_number))
#         self.assertEqual('id3v1 title', mp3_tag_fetcher.tag_data.get_value_by_key(key.title))
#         self.assertEqual('Rock & Roll', mp3_tag_fetcher.tag_data.get_value_by_key(key.genre))
#         self.assertIsNone(mp3_tag_fetcher.tag_data.picture)


class Id3v23FetcherTest(unittest.TestCase):

    def setUp(self) -> None:
        self.expected_tag_data = initiate_tag_data(3)
        self.expected_tag_data.set_key_value_pair(AudioTagKey.track_number, '08/11')
        self.expected_tag_data.set_key_value_pair(AudioTagKey.year, '2021')

    def test(self):
        mp3_tag_fetcher = Mp3TagFetcher(fixtures_directory_path + 'id3v2.3.mp3')
        mp3_tag_fetcher.fetch_mp3_tag()
        self.assertEqual(self.expected_tag_data, mp3_tag_fetcher.tag_data)


class Id3v24FetcherTest(unittest.TestCase):

    def setUp(self) -> None:
        self.expected_tag_data = initiate_tag_data(4)
        self.expected_tag_data.set_key_value_pair(AudioTagKey.track_number, '09/12')
        self.expected_tag_data.set_key_value_pair(AudioTagKey.year, '2022')

    def test(self):
        mp3_tag_fetcher = Mp3TagFetcher(fixtures_directory_path + 'id3v2.4.mp3')
        mp3_tag_fetcher.fetch_mp3_tag()
        self.assertEqual(self.expected_tag_data, mp3_tag_fetcher.tag_data)


if __name__ == '__main__':
    unittest.main()
