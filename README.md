# another-mutagen-wrapper

Wraps mutagen library (https://github.com/quodlibet/mutagen) to be able to load and save audio tags more easily 

* .mp3 & .flac only
* Supported tag fields:
  - Album
  - Artist
  - Comment
  - Composer
  - Genre
  - Title
  - Track number
  - Year
  - Picture 

### Loading

```
>>> import audio_tag_fetcher
>>> from audio_tag_data import AudioTagKey

>>> tag_data = audio_tag_fetcher.fetch_tag_data('beatles_yellow_submarine.mp3')

>>> tag_data.get_value_by_key(AudioTagKey.artist)
'The Beatles'

>>> tag_data.get_value_by_key(AudioTagKey.title)
'Yellow Submarine'

>>> tag_data.get_value_by_key(AudioTagKey.album)
'Revolver'

>>> tag_data.picture
<audio_tag_data.AudioTagPicture object at 0x7f60432ffa00>

>>> # Get the picture data as bytes:
>>> tag_data.picture.data
b'\xff\xd8\xff\xe0\x00\x10JFIF\x00\x01\x01\x01\x01,\x01,\x00\x00\xff\xe1\x1c0Exif\x00\x00II*\x00\x08\x00\x00\x00\x07\x00\x1a\x01\x05\x00\x01\x00\x00\x00b\x00\x00\x00\x1b\x01\x05\x00\x01\x00\x00\x00j\x00\x00\x00(\x01\x03\x00\x01\x00\x00\x00\x02\x00\x00\x001\x01\x02\x00\r\x00\x00\x00r\x00\x00\x002\x01\x02\x00\x14\x00\x00\x00\x80\x00\x00\x00\x12\x02\x03
```
Loading works with .flac files in the same way!


### Saving

```
>>> from audio_tag_data import AudioTagData, AudioTagPicture, AudioTagKey
>>> from audio_tag_writer import write_tag_data_to_file

>>> tag_data = AudioTagData()
>>> tag_data.set_key_value_pair(AudioTagKey.artist, 'Mozart')
>>> tag_data.set_key_value_pair(AudioTagKey.title, 'Symphony No. 40 in g minor, I. Molto allegro')
>>> tag_data.set_key_value_pair(AudioTagKey.album, 'Mozart: Symphony #40')

>>> with open('picture.jpeg', "rb") as f:
...     	picture_data = f.read()
...         
>>> tag_data.picture = AudioTagPicture('a nice name for the pic', picture_data)

>>> write_tag_data_to_file(tag_data, 'my_new_audio_file.flac')
```
Saving works with .mp3 files in the same way!
