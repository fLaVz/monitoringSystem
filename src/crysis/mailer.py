import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

def sendMailAlert(message):

	msg = MIMEMultipart()
	msg['From'] = 'julien.flav.delvaux@gmail.com'
	msg['To'] = 'julien.flav.delvaux@gmail.com'
	msg['Subject'] = 'ServerAlert' 
	msg.attach(MIMEText(message))
	mailserver = smtplib.SMTP('smtp.gmail.com', 587)
	mailserver.ehlo()
	mailserver.starttls()
	mailserver.ehlo()
	mailserver.login('julien.flav.delvaux@gmail.com', 'JD270193')
	mailserver.sendmail('julien.flav.delvaux@gmail.com', 'julien.flav.delvaux@gmail.com', msg.as_string())
	mailserver.quit()