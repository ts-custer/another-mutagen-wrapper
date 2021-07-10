# audio_tag_fetcher.py
from flac.flac_tag_fetcher import FlacTagFetcher
from mp3 import Mp3TagFetcher
from audio_tag_data import check_and_fetch_file_suffix, AudioTagData


def fetch_tag_data(audio_file: str) -> AudioTagData:
    file_suffix = check_and_fetch_file_suffix(audio_file)
    if file_suffix == '.mp3':
        mp3_tag_fetcher = Mp3TagFetcher(audio_file)
        mp3_tag_fetcher.fetch_mp3_tag()
        return mp3_tag_fetcher.tag_data
    elif file_suffix == '.flac':
        flac_tag_fetcher = FlacTagFetcher(audio_file)
        flac_tag_fetcher.fetch_tags()
        return flac_tag_fetcher.tag_data
