# test_flag_tag_writer.py
import os
import unittest

import mutagen
from flac import FlacTagWriter, delete_flac_tags
from audio_tag_data import AudioTagKey, AudioTagData, AudioTagPicture

fixtures_directory_path = os.path.dirname(os.path.realpath(__file__)) + '/fixtures/'
flac_file_name = 'empty_flac.flac'


class FlacTagWriterTest(unittest.TestCase):

    def setUp(self) -> None:
        delete_flac_tags(fixtures_directory_path + flac_file_name)
        tag_data = AudioTagData()
        tag_data.set_key_value_pair(AudioTagKey.album, 'test album')
        tag_data.set_key_value_pair(AudioTagKey.artist, 'test artist')
        tag_data.set_key_value_pair(AudioTagKey.comment, 'test comment')
        tag_data.set_key_value_pair(AudioTagKey.composer, 'test composer')
        tag_data.set_key_value_pair(AudioTagKey.genre, 'test genre')
        tag_data.set_key_value_pair(AudioTagKey.title, 'test title')
        tag_data.set_key_value_pair(AudioTagKey.track_number, '01/17')
        tag_data.set_key_value_pair(AudioTagKey.year, '2021')

        picture_file_name = 'flac.jpg'
        self.picture_full_filename = fixtures_directory_path + picture_file_name
        with open(self.picture_full_filename, "rb") as f:
            picture_data = f.read()
        tag_data.picture = AudioTagPicture(picture_file_name, picture_data)
        FlacTagWriter(fixtures_directory_path + flac_file_name).write(tag_data)

    def tearDown(self) -> None:
        delete_flac_tags(fixtures_directory_path + flac_file_name)

    def test(self):
        flac_file = mutagen.File(fixtures_directory_path + flac_file_name)
        self.assertEqual('test album', flac_file.get('ALBUM')[0])
        self.assertEqual('test artist', flac_file.get('ARTIST')[0])
        self.assertEqual('test comment', flac_file.get('DESCRIPTION')[0])
        self.assertEqual('test composer', flac_file.get('COMPOSER')[0])
        self.assertEqual('2021', flac_file.get('DATE')[0])
        self.assertEqual('test genre', flac_file.get('GENRE')[0])
        self.assertEqual('test title', flac_file.get('TITLE')[0])
        self.assertEqual('01/17', flac_file.get('TRACKNUMBER')[0])

        embedded_picture = flac_file.pictures[0]
        with open(self.picture_full_filename, "rb") as f:
            picture_data = f.read()
        self.assertEqual(picture_data, embedded_picture.data)


if __name__ == '__main__':
    unittest.main()
