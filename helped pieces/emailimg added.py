import smtplib
import config
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
import html



subject="Testing image"
msg = """Hi Dad,
hope this works
From Em"""

sender_email = config.EMAIL_ADDRESS
receiver_email = config.EMAIL_ADD

message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject
message.attach(MIMEText(msg, "plain"))
html = """\
<html>
<body>
<img src="cid:myimage">
</body>
</html>
"""
part = MIMEText(html, "html")
message.attach(part)
with open('img.jpg', 'rb') as img:
    image = MIMEImage(img.read())
image.add_header('Content-ID', '<myimage>')
message.attach(image)

server = smtplib.SMTP('smtp.gmail.com:587')
server.ehlo()
server.starttls()
server.login(config.EMAIL_ADDRESS, config.PASSWORD)
server.sendmail(sender_email, receiver_email, message.as_string())

print('Sent')
