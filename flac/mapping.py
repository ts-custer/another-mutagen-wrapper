from typing import Dict

import another_mutagen_wrapper as amw


key_to_field_name_mapping: Dict[amw.AudioTagKey, str] = {
    amw.AudioTagKey.album: 'ALBUM',
    amw.AudioTagKey.artist: 'ARTIST',
    amw.AudioTagKey.comment: 'DESCRIPTION',
    amw.AudioTagKey.composer: 'COMPOSER',
    amw.AudioTagKey.year: 'DATE',
    amw.AudioTagKey.genre: 'GENRE',
    amw.AudioTagKey.title: 'TITLE',
    amw.AudioTagKey.track_number: 'TRACKNUMBER',
    # field name 'PICTURE': AudioTagPicture is handled in another way!
}

field_name_to_key_mapping: Dict[str, amw.AudioTagKey] = {v: k for k, v in key_to_field_name_mapping.items()}
