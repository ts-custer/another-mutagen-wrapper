from typing import Dict

from mutagen.id3 import TALB, TPE1, COMM, TCOM, TYER, TDRC, TCON, TIT2, TRCK


from audio_tag_data import AudioTagKey

frame_class_to_key_mapping = {  # 'APIC': AudioTagPicture is loaded, too, but in another way
    TALB: AudioTagKey.album,
    TPE1: AudioTagKey.artist,
    COMM: AudioTagKey.comment,
    TCOM: AudioTagKey.composer,
    # ID3v2.3:
    TYER: AudioTagKey.year,
    # ID3v2.4:
    TDRC: AudioTagKey.year,
    TCON: AudioTagKey.genre,
    TIT2: AudioTagKey.title,
    TRCK: AudioTagKey.track_number,
}

key_to_frame_class_mapping = {v: k for k, v in frame_class_to_key_mapping.items()}
# Mp3TagWriter writes ID3v2.4 tags, and frame id TDRC is right for ID3v2.4:
key_to_frame_class_mapping[AudioTagKey.year] = TDRC

frame_id_to_key_mapping: Dict[str, AudioTagKey] = {k.__name__: v for k, v in frame_class_to_key_mapping.items()}

key_to_frame_id_mapping: Dict[AudioTagKey, str] = {v: k for k, v in frame_id_to_key_mapping.items()}

