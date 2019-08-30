import json
import os
from pathlib import Path

import wget


with open('./data/videos.txt', 'r') as inputfile:
    videos = json.load(inputfile)

base_path = Path('.') / 'data'
for video in videos:
    download_folder = base_path / video['folder']
    os.makedirs(download_folder.as_posix(), exist_ok=True)

    file_path = download_folder / video['file']
    if file_path.exists():
        os.remove(file_path.as_posix())

    print('downloading {}'.format(video['file']))
    wget.download(video['url'], file_path.as_posix())
