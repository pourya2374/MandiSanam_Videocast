import json
import os
from pathlib import Path

from bs4 import BeautifulSoup as bs

from network import get_html
from utils import Video, get_unit_info


course_url = 'https://maktabkhooneh.org/course/273-%DB%8C%D8%A7%D8%AF%DA%AF%DB%8C%D8%B1%DB%8C-%D9%85%D8%A7%D8%B4%DB%8C%D9%86-mk273/'


soup = bs(get_html(course_url), 'html.parser')
videos = list()

# teaser
for video in soup.find_all('source', type="video/mp4"):
    url = video.get('src', '')
    if 'hq' in url:
        videos.append(Video('تیزر', 'مقدمه', url).serialize())
        break

# chapters
for chapter in soup.find_all('div', 'chapter'):
    chapter_name = chapter.find('div', 'chapter__title').text.strip()

    for unit in chapter.find_all('a', 'chapter__unit'):
        file_name, video_url = get_unit_info(unit.get('href'))
        if video_url is not None:
            videos.append(Video(chapter_name, file_name, video_url).serialize())


output_folder = Path('./data')
os.makedirs(output_folder.as_posix(), exist_ok=True)
with open((output_folder / 'videos.txt').as_posix(), 'w') as output:
    json.dump(videos, output, ensure_ascii=False, indent=2)
