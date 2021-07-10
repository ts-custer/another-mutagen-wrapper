# audio_tag_writer.py
from flac import delete_flac_tags, FlacTagWriter
from mp3.mp3_tag_writer import delete_mp3_tags, Mp3TagWriter
from audio_tag_data import check_and_fetch_file_suffix, AudioTagData


def write_tag_data_to_file(tag_data: AudioTagData, audio_file: str):
    file_suffix = check_and_fetch_file_suffix(audio_file)
    if file_suffix == '.mp3':
        delete_mp3_tags(audio_file)
        mp3_tag_writer = Mp3TagWriter(audio_file)
        mp3_tag_writer.write(tag_data)
    elif file_suffix == '.flac':
        delete_flac_tags(audio_file)
        flac_tag_writer = FlacTagWriter(audio_file)
        flac_tag_writer.write(tag_data)
