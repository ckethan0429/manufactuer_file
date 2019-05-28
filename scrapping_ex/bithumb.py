import requests
from bs4 import BeautifulSoup
# from pprint import pprint #json이나 csv 정리되게 출력

# 1.원하는 정보가 있는 주소로 요청을 보내 , 응답을 저장
req = requests.get('https://www.bithumb.com').text
#print(req)
#pprint(req.text)
#print(req.status_code)

# 2. 정보조작하기 편하게 바꾸고
soup = BeautifulSoup(req, 'html.parser')

tags = soup.select('#tableAsset > tbody > tr > td:nth-child(1) > p > a > strong')
values = soup.select('#tableAsset > tbody > tr > td:nth-child(2) > strong')
#print(tags)
# 3. 바꾼정보중 원하는 것만 뽑아서, 출력한다

bitinfos = list(zip(tags,values))
with open('bitsumb.txt', 'w', encoding = 'utf-8') as f:

    for bitinfo in bitinfos:
        print(bitinfo[0].text.split()[0],'/',bitinfo[1].text)
        f.write(f'{bitinfo[0].text.split()[0]} / {bitinfo[1].text} \n')







