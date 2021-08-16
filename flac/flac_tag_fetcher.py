# flac_tag_fetcher.py
import mutagen

import flac
import another_mutagen_wrapper as amw
from mutagen.flac import FLAC
from mutagen import id3


class FlacTagFetcher:

    def __init__(self, flac_file: str):
        self._tag_data = None
        self.flac_file = mutagen.File(flac_file)

    def fetch_tags(self):
        self._tag_data = amw.AudioTagData()
        for key, field_name in flac.key_to_field_name_mapping.items():
            content = self.flac_file.get(field_name)
            content = content and content[0]
            if content:
                self._tag_data.set_key_value_pair(key, content)
                if key == amw.AudioTagKey.track_number:
                    self.fix_track_number_if_necessary(content, key)
        self.fetch_picture()

    def fix_track_number_if_necessary(self, track_number, key):
        track_total_field_name = 'TRACKTOTAL'
        track_total = self.flac_file.get(track_total_field_name) and self.flac_file.get(track_total_field_name)[0]
        if track_total:
            self._tag_data.set_key_value_pair(key, track_number + '/' + track_total)

    def fetch_picture(self):
        flac = FLAC(self.flac_file.filename)
        pics = flac.pictures
        for p in pics:
            # if p.type == 3:  # front cover
            if p.type == id3.PictureType.COVER_FRONT:
                self._tag_data.picture = amw.AudioTagPicture(p.desc, p.data)

    @property
    def tag_data(self):
        return self._tag_data


