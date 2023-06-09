import smtplib
import config
##sender_email='testingwithpython02@gmail.com'
##password='pinkpurple1234'
##
##rec_email="emilymcvey100@gmail.com"
##subject="hello"
##message="This is a message"
##
##server = smtplib.SMTP('smtp.gmail.com')
##server.ehlo()
##server.starttls()
##
##server.login(rec_email, password)
##
##print("Login success")
##
##server.sendmail(rec_email, message, sender_email)
##print("Email has been sent to ", rec_email)

subject="It worked"
msg= """my email got through
and this was on a different line"""
try:
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.ehlo()
    server.starttls()
    server.login(config.EMAIL_ADDRESS, config.PASSWORD)
    message = "Subject : {}\n\n{}".format(subject, msg)
    server.sendmail(config.EMAIL_ADDRESS, config.EMAIL_ADD, message)
    server.quit()
    print("Success: Email sent")
except:
    print("Email failed to sent")



def send_email(msg, subject):
    try:
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(config.EMAIL_ADDRESS, config.PASSWORD)
        message = "Subject : {}\n\n{}".format(subject, msg)
        server.sendmail(config.EMAIL_ADDRESS, config.EMAIL_ADD, message)
        server.quit()
        print("Success: Email sent")
    except:
        print("Email failed to sent")
