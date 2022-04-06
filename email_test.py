import smtplib

recipient = input("Enter recipient's email address: ")
subject = input("Enter your subjet: ")
text = input("Enter your message: ")


personal_email = "chasewinder777@gmail.com"
message = 'Subject: {}\n\n{}'.format(subject, text)

server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
server.login(personal_email, "HaymanRobyn577")
server.sendmail(personal_email, recipient, message)

server.quit()
