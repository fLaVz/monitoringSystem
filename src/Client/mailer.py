#-*- coding: utf-8 -*-

import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

def sendMailAlert(host, message):

	msg = MIMEMultipart()
	msg['From'] = 'julien.delvaux@alumni.univ-avignon.fr' # mail envoyé depuis
	msg['To'] = 'julien.flav.delvaux@gmail.com'			# mail envoyé a
	msg['Subject'] = host+'ServerAlert' 				# sujet du mail
	msg.attach(MIMEText(message))
	mailserver = smtplib.SMTP('smtpz.univ-avignon.fr', 465) # server smtp
	mailserver.ehlo()
	mailserver.starttls()
	mailserver.ehlo(1)
	mailserver.login('julien.delvaux@alumni.univ-avignon.fr', 'p455w0rd') #faux password car projet dispo sur github mais fonctionnel, testé avec le smtp gmail et université avignon
	mailserver.sendmail('julien.delvaux@alumni.univ-avignon.fr', 'julien.flav.delvaux@gmail.com', msg.as_string())
	mailserver.quit()