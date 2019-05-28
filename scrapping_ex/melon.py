import requests
from bs4 import BeautifulSoup
headers = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
}

res = requests.get('https://www.melon.com/chart/index.htm', headers=headers).text
soup = BeautifulSoup(res, 'html.parser')
songs = soup.select('#lst50')

with open('melon.txt', 'w', encoding='utf-8') as f:
    for song in songs:
        name = song.select_one('td:nth-child(6) .ellipsis.rank01 a').text
        rank = song.select_one('td:nth-child(2) > div > span.rank').text
        artist = song.select_one('td:nth-child(6) .ellipsis.rank02 a').text
        print(rank)
        f.write(f'{rank}위 : {name} / {artist}\n')
