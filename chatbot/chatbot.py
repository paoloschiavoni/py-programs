#chat bot intelligente, che salva la sua memoria in un altro file nella stessa cartella
import os

print('ciao, sono tony effe, \n\nrispondo alle tue domande \
e se non so la risposta dai tu\nperchè chi ha scritto \
questo programma ha salvato di \ndefault solo ciao e come ti chiami\n')

risposte_iniziali='ciao_ciao capo\ncome ti chiami_tony effe stupida bibbi'

if not 'memoria.txt' in os.listdir():
    file=open('memoria.txt', 'w')
    file.write(risposte_iniziali)
    file=open('memoria.txt', 'r')
#creato il file se non c'era

else:
    file=open("C:\\Users\\Diego\\Desktop\\py programs\\chatbot\\memoria.txt", 'r')
#aperto il file se c'era già


risposte=file.read()
file.close()
dizio={}
lista_dr=risposte.split('\n')
for dr in lista_dr:
    lista_der=dr.split('_')
    dizio[lista_der[0]]=lista_der[1]
#aggiunto le risposte iniziali e creato il dizionario

lista_caratteri_spec=['!', '?', '.', ',', ';', ':']

def main():
    lista_caratteri_domanda=[]
    d=str(input('>>> '))
    d=d.lower()
    for el in d:
        if el not in lista_caratteri_spec:
            lista_caratteri_domanda.append(el)
    d=''.join(lista_caratteri_domanda)
    
    if d in dizio:
        print(dizio[d], '\n')
        main()
        
    print('non so cosa rispondere, dimmelo tu:')
    new_risp=str(input('>>> '))
    print('gialossssai\n')
    dizio[d]=new_risp
    file=open('memoria.txt', 'r')
    testo_tot=file.read()
    testo_tot+='\n'+d+'_'+new_risp
    file=open('memoria.txt', 'w')
    file.write(testo_tot)
    file.close()
    main()

main()