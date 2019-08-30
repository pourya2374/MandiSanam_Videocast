import requests

from .secrets import SESSION_ID


cookies = {
    'sessionid': SESSION_ID,
}

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
}

response = requests.get(
    'https://maktabkhooneh.org/course/%D8%B7%D8%B1%D8%A7%D8%AD%DB%8C-%D8%A7%D9%84%DA%AF%D9%88%D8%B1%DB%8C%D8%AA%D9%85-%D8%B9%D9%85%D9%84-mk582/',
    headers=headers, cookies=cookies
)
