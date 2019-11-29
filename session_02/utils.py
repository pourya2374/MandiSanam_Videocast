import re
from typing import Tuple

from bs4 import BeautifulSoup as bs

from network import get_html


class Video:
    def __init__(self, folder, file, url):
        self.folder = folder
        self.file = file
        self.url = url

    def serialize(self) -> dict:
        return {
            'folder': self.folder,
            'file': '{}.mp4'.format(self.file),
            'url': self.url
        }


def get_unit_info(relative_url: str) -> Tuple[str, str]:
    soup = bs(get_html('https://maktabkhooneh.org{}'.format(relative_url)), 'html.parser')
    unit_name = soup.find('h1', 'unit-container__top-title').text.strip()
    unit_video = None

    for item in soup.find_all('video', 'js-player'):
        url = item.get('poster', '')
        unit_video = url.replace('thumbs/', 'videos/hq').replace('jpg', 'mp4')
    return unit_name, unit_video
