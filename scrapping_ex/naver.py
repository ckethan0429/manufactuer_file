import requests
from bs4 import BeautifulSoup
# from pprint import pprint #json이나 csv 정리되게 출력

# 1.원하는 정보가 있는 주소로 요청을 보내 , 응답을 저장
req = requests.get('https://www.naver.com/').text
#print(req)
#pprint(req.text)
#print(req.status_code)

# 2. 정보조작하기 편하게 바꾸고
soup = BeautifulSoup(req, 'html.parser')

tags = soup.select('.PM_CL_realtimeKeyword_rolling_base .ah_item .ah_k')
# 3. 바꾼정보중 원하는 것만 뽑아서, 출력한다

for tag in tags:
    print(tag.text)
