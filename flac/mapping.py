from typing import Dict

from audio_tag_data import AudioTagKey

key_to_field_name_mapping: Dict[AudioTagKey, str] = {  # field name 'PICTURE': AudioTagPicture is handled in another way
    AudioTagKey.album: 'ALBUM',
    AudioTagKey.artist: 'ARTIST',
    AudioTagKey.comment: 'DESCRIPTION',
    AudioTagKey.composer: 'COMPOSER',
    AudioTagKey.year: 'DATE',
    AudioTagKey.genre: 'GENRE',
    AudioTagKey.title: 'TITLE',
    AudioTagKey.track_number: 'TRACKNUMBER',
}

field_name_to_key_mapping: Dict[str, AudioTagKey] = {v: k for k, v in key_to_field_name_mapping.items()}
