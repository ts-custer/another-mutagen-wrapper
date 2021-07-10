# audio_file_utils.py

import os
from pathlib import Path
from typing import List

from audio_tag_data import AUDIO_FILE_SUFFIXES

separator: str = os.sep


def check_path_argument(path_argument: str) -> Path:
    possible_directory: Path = Path(path_argument)
    if not possible_directory.exists():
        print(f"Directory '{path_argument}' does not exist")
        exit(1)
    if not possible_directory.is_dir():
        print(f"'{path_argument}' is not a directory")
        exit(2)
    return possible_directory


def fetch_audio_files_sorted(directory: Path) -> List[str]:
    directory_name = str(directory) + separator
    audio_file_list = []
    for file_or_directory in directory.iterdir():
        if file_or_directory.is_file() and is_audio_file(file_or_directory.name):
            audio_file_list.append(directory_name + file_or_directory.name)
    return sorted(audio_file_list)


def is_audio_file(filename: str):
    filename_lower = filename.lower()
    for suffix in AUDIO_FILE_SUFFIXES:
        if filename_lower.endswith(suffix):
            return True
    return False


def check_if_file_exists(file_name: str):
    if not os.path.isfile(file_name):
        raise RuntimeError(f'File {file_name} does not exist')
