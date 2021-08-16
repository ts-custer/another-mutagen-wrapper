# mp3_tag_writer.py


from mutagen.easyid3 import EasyID3
from mutagen.mp3 import MP3
from mutagen.id3 import APIC
from mutagen.id3 import ID3NoHeaderError
import mutagen

import mp3
import another_mutagen_wrapper as amw


def delete_mp3_tags(mp3_full_file_name: str):
    try:
        mp3_file = EasyID3(mp3_full_file_name)
        mp3_file.delete()
        mp3_file.save()
    except mutagen.id3._util.ID3NoHeaderError:
        # mp3_file has no ID3 header -> mp3_file has no tags to delete
        pass


class Mp3TagWriter:

    def __init__(self, mp3_file: str):
        self.mp3_file = MP3(mp3_file)

    def write(self, tag_data: amw.AudioTagData):
        for key, value in tag_data.items():
            self.set_field(key, value)
        if tag_data.picture:
            self.set_picture(tag_data.picture)
        self.mp3_file.save()

    def set_field(self, key: amw.AudioTagKey, content: str):
        if self.mp3_file.tags is None:
            self.mp3_file.add_tags()
        frame_class = mp3.key_to_frame_class_mapping.get(key)
        self.mp3_file.tags.add(frame_class(encoding=3, text=content))

    def set_picture(self, new_picture: amw.AudioTagPicture):
        self.mp3_file.tags.add(APIC(encoding=3,
                                    mime='image/jpeg',
                                    type=3, desc=new_picture.name,
                                    data=new_picture.data))
