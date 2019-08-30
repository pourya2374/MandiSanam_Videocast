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
    unit_name = soup.find('div', 'unit-content__title').text.strip()
    unit_video = None

    for item in soup.find_all('a'):
        url = item.get('href', '')
        search_result = re.search(r"https://cdn\.maktabkhooneh\.org/videos/hq\d+\.mp4", url)
        if search_result:
            unit_video = search_result.group()
            print(unit_video)
            break
    return unit_name, unit_video
