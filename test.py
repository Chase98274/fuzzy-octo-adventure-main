import smtplib

personal_email = "chasewinder77@gmail.com"

server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
server.login(personal_email, "HaymanRobyn577")
server.sendmail(personal_email, "chasewinder912@gmail.com", "This is a test email")

server.quit()
