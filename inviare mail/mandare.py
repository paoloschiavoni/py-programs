import smtplib
from getpass import getpass

oggetto=str(input('oggetto: '))
contenuto=str(input('contetnuto: '))
messaggio='Subject: '+oggetto+'\n\n'+contenuto

email=smtplib.SMTP('smtp.gmail.com', 587)
email.ehlo()
email.starttls()

ind=str(input('indirizzo mail: '))
password=getpass('password: ')

email.login(ind, password)
dest=str(input('destinatario: '))
email.sendmail(ind, dest, messaggio)
email.quit()
fine=input('email inviata, invio per chiudere')