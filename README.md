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
>>> import another_mutagen_wrapper as amw
>>>
>>> # Fetch the AudioTagData
>>> tag_data = amw.fetch_tag_data('beatles_yellow_submarine.mp3')
>>>
>>> # Get the stored artist:
>>> tag_data.get_value_by_key(AudioTagKey.artist)
'The Beatles'
>>>
>>> # Get the stored title:
>>> tag_data.get_value_by_key(AudioTagKey.title)
'Yellow Submarine'
>>>
>>> # Get the stored album:
>>> tag_data.get_value_by_key(AudioTagKey.album)
'Revolver'
>>>
>>> # Get other tag values as well -> see supported tag fields
>>>
>>> # Get the stored picture:
>>> tag_data.picture
<audio_tag_data.AudioTagPicture object at 0x7f60432ffa00>
>>> # Get the picture data as bytes:
>>> tag_data.picture.data
b'\xff\xd8\xff\xe0\x00\x10JFIF\x00\x01\x01\x01\x01,\x01,\x00\x00\xff\xe1\x1c0Exif\x00\x00II*\x00\x08\x00\x00\x00\x07\x00\x1a\x01\x05\x00\x01\x00\x00\x00b\x00\x00\x00\x1b\x01\x05\x00\x01\x00\x00\x00j\x00\x00\x00(\x01\x03\x00\x01\x00\x00\x00\x02\x00\x00\x001\x01\x02\x00\r\x00\x00\x00r\x00\x00\x002\x01\x02\x00\x14\x00\x00\x00\x80\x00\x00\x00\x12\x02\x03
```
Loading works with .flac files in the same way!


### Saving

```
>>> import another_mutagen_wrapper as amw
>>>
>>> # Create a new AudioTagData instance:
>>> tag_data = amw.AudioTagData()
>>>
>>> # Set the artist:
>>> tag_data.set_key_value_pair(amw.AudioTagKey.artist, 'Mozart')
>>>
>>> # Set the title:
>>> tag_data.set_key_value_pair(amw.AudioTagKey.title, 'Symphony No. 40 in g minor, I. Molto allegro')
>>>
>>> # Set the album:
>>> tag_data.set_key_value_pair(amw.AudioTagKey.album, 'Mozart: Symphony #40')
>>>
>>> # Set the track number (and the total track numbers):
>>> tag_data.set_key_value_pair(amw.AudioTagKey.track_number, '01/04')
>>>
>>> # Set values of other tag fields as well -> see supported tag fields
>>>
>>> # Set a picture:
>>> with open('your_stored_picture_of_Mozart.jpeg', "rb") as f:
...     	picture_data = f.read()
...         
>>> tag_data.picture = amw.AudioTagPicture('Mozart_Symph_40.jpg', picture_data)
>>>
>>> # Finally, write the AudioTagData to an audio file:
>>> amw.write_tag_data_to_file(tag_data, 'your_audio_file.flac')
```
Saving works with .mp3 files in the same way!
