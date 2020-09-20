import smtplib

oggetto='Subject: Ciao\n\n'
contenuto='bella bro'
messaggio=oggetto+contenuto

email=smtplib.SMTP('smtp.gmail.com', 587)
email.ehlo()

email.starttls()
email.login('p3.schiavoni@gmail.com', 'PaLuNumeri73')

email.sendmail('p3.schiavoni@gmail.com', 'p3.schiavoni@gmail.com', messaggio)

email.quit()