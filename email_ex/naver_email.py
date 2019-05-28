import smtplib
from email.message import EmailMessage
from getpass import getpass

email_list = ['oops0429@gmail.com', 'ckethan0429@gmail.com', 'oops0429@hanmail.net']

password = getpass('Password : ')
msg = EmailMessage()
msg['Subject'] = '권고사직서'
msg['From'] = 'oops0429@naver.com'
msg['To'] = ','.join(email_list)
html = """
<html>
    <body>
    <img src = "http://sampleimg.com/aas.png>
    <p>HI</p>
    </body>
</html>
"""
msg.set_content('꺼졍ㅋ')

s = smtplib.SMTP_SSL('smtp.naver.com', 465) #STMP서버명, SMTP포트
s.login('oops0429', password)
s.send_message(msg)
print('이메일 전송완료!!')