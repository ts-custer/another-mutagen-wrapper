from typing import Dict

from mutagen.id3 import TALB, TPE1, COMM, TCOM, TYER, TDRC, TCON, TIT2, TRCK


import another_mutagen_wrapper as amw

_frame_class_to_key_mapping = {  # 'APIC': amw.AudioTagPicture is loaded, too, but in another way
    TALB: amw.AudioTagKey.album,
    TPE1: amw.AudioTagKey.artist,
    COMM: amw.AudioTagKey.comment,
    TCOM: amw.AudioTagKey.composer,
    # ID3v2.3:
    TYER: amw.AudioTagKey.year,
    # ID3v2.4:
    TDRC: amw.AudioTagKey.year,
    TCON: amw.AudioTagKey.genre,
    TIT2: amw.AudioTagKey.title,
    TRCK: amw.AudioTagKey.track_number,
}

key_to_frame_class_mapping = {v: k for k, v in _frame_class_to_key_mapping.items()}
# Mp3TagWriter writes ID3v2.4 tags, and frame id TDRC is right for ID3v2.4:
key_to_frame_class_mapping[amw.AudioTagKey.year] = TDRC

frame_id_to_key_mapping: Dict[str, amw.AudioTagKey] = {k.__name__: v for k, v in _frame_class_to_key_mapping.items()}
