# test_mp3_tag_writer.py
import os
import unittest

from mutagen.id3 import ID3

import mp3
import another_mutagen_wrapper as amw

fixtures_directory_path = os.path.dirname(os.path.realpath(__file__)) + '/fixtures/'
mp3_file_name = 'empty_mp3.mp3'


class Mp3TagWriterTest(unittest.TestCase):

    def setUp(self) -> None:
        mp3.delete_mp3_tags(fixtures_directory_path + mp3_file_name)
        self.expected_tag_data = amw.AudioTagData()
        self.expected_tag_data.set_key_value_pair(amw.AudioTagKey.album, 'test album 2')
        self.expected_tag_data.set_key_value_pair(amw.AudioTagKey.artist, 'test artist 2')
        self.expected_tag_data.set_key_value_pair(amw.AudioTagKey.comment, 'test comment ')
        self.expected_tag_data.set_key_value_pair(amw.AudioTagKey.composer, 'test composer 2')
        self.expected_tag_data.set_key_value_pair(amw.AudioTagKey.genre, 'test genre 2')
        self.expected_tag_data.set_key_value_pair(amw.AudioTagKey.title, 'test title 2')
        self.expected_tag_data.set_key_value_pair(amw.AudioTagKey.track_number, '22/22')
        self.expected_tag_data.set_key_value_pair(amw.AudioTagKey.year, '2022')

        picture_file_name = 'id3v2.3.jpg'
        self.picture_full_filename = fixtures_directory_path + picture_file_name
        with open(self.picture_full_filename, "rb") as f:
            picture_data = f.read()
        self.expected_tag_data.picture = amw.AudioTagPicture(picture_file_name, picture_data)
        mp3.Mp3TagWriter(fixtures_directory_path + mp3_file_name).write(self.expected_tag_data)

    def tearDown(self) -> None:
        mp3.delete_mp3_tags(fixtures_directory_path + mp3_file_name)

    def test(self):
        # Easy:
        mp3_tag_fetcher = mp3.Mp3TagFetcher(fixtures_directory_path + mp3_file_name)
        mp3_tag_fetcher.fetch_mp3_tag()
        self.assertEqual(self.expected_tag_data, mp3_tag_fetcher.tag_data)

        # Difficult:
        mp3_file = ID3(fixtures_directory_path + mp3_file_name)
        self.assertEqual(self.expected_tag_data.get_value_by_key(amw.AudioTagKey.album),
                         mp3_file['TALB'].text[0])
        self.assertEqual(self.expected_tag_data.get_value_by_key(amw.AudioTagKey.artist),
                         mp3_file['TPE1'].text[0])
        # unable to load comment in that way! :
        # self.assertEqual(self.expected_tag_data.get_value_by_key(amw.AudioTagKey.comment),
        #                  mp3_file['COMM'].text[0])
        self.assertEqual(self.expected_tag_data.get_value_by_key(amw.AudioTagKey.composer),
                         mp3_file['TCOM'].text[0])
        self.assertEqual(self.expected_tag_data.get_value_by_key(amw.AudioTagKey.genre),
                         mp3_file['TCON'].text[0])
        self.assertEqual(self.expected_tag_data.get_value_by_key(amw.AudioTagKey.title),
                         mp3_file['TIT2'].text[0])
        self.assertEqual(self.expected_tag_data.get_value_by_key(amw.AudioTagKey.track_number),
                         mp3_file['TRCK'].text[0])
        # error in loading year in that way! :
        # self.assertEqual(self.expected_tag_data.get_value_by_key(amw.AudioTagKey.year),
        #                  mp3_file['TDRC'].text[0])


if __name__ == '__main__':
    unittest.main()

