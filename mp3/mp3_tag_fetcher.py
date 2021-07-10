# mp3_tag_fetcher.py

import mutagen.flac

from .mapping import frame_id_to_key_mapping
from audio_tag_data import AudioTagData, AudioTagPicture, AudioTagKey


class Mp3TagFetcher:

    def __init__(self, mp3_file: str):
        self._tag_data = None
        self.mp3_file = mutagen.File(mp3_file)

    def fetch_mp3_tag(self):
        self._tag_data = AudioTagData()
        frame_id_to_mutagen_key = {mutagen_key[:4]: mutagen_key for mutagen_key in self.mp3_file.tags.keys()}
        for frame_id, mutagen_key in frame_id_to_mutagen_key.items():
            key: AudioTagKey = frame_id_to_key_mapping.get(frame_id)
            if key:
                content = self.mp3_file.tags.get(mutagen_key) and self.mp3_file.tags.get(mutagen_key).text[0]
                if content:
                    self._tag_data.set_key_value_pair(key, content)
        self.fetch_picture()

    def fetch_picture(self):
        apic_list = self.mp3_file.tags.getall('APIC')
        if apic_list:
            first_apic = apic_list[0]
            if first_apic:
                self._tag_data.picture = AudioTagPicture(first_apic.desc, first_apic.data)

    @property
    def tag_data(self):
        return self._tag_data
