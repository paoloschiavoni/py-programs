
### Programma che funge da psichiatra, digitando Quit, si interrompe

###dizionari necessari
dichiarazioni=("Continui", "Mi racconti più nel dettaglio", "Non si fermi", "Ok, e dopo cosa è successo?", "Capisco, mi racconti di più", "Perfetto... \nvada avanti", "Mhh... interessante.. \nContinui pure")
esplicazioni=("Mi racconti cosa è successo dopo che ", "E tu cosa hai pensato di fare quando ", "Sembra che tu voglia dire che ", "cosa accadde subito dopo che ", "Spiega perchè ", "quale fu il motivo del fatto che ")
sostituzionipronomi={"devo":"devi", "avevo":"avevi", "pensavo":"pensavi", "dirle":"dirmi", "confessarle":"confessarmi", "so":"sai", "penso":"pensi", "riesco":"riesci", "mangio":"mangi", "faccio":"fai", "sento":"senti", "sopporto":"sopporti", "fumo":"fumi", "vado":"vai", "ti":"mi", "io": " tu", "noi":" voi", "mio":" tuo", "nostro":" vostro", "mi":" ti", "ci":" vi", "sono":" sei", "siamo":" siete", "ho":" hai"}

### funzione main, gestisce le interazioni tra paziente e dottore. Una volta su 4 fa delle dichiarazioni.
import random
def main():
    print("Salve, \nCosa posso fare per lei?")
    while True:
        frase=str(input(">>>"))
        if frase.upper()=="QUIT":
            print("Arrivederci")
            break
        print(risposta(frase))
    

### funzione che sostituisce i pronomi
def sostpronomi(frase):
    lista=frase.split()
    frasefinale=""
    listaparolefinale=[]
    for parola in lista:
        if parola in sostituzionipronomi:
            listaparolefinale.append(sostituzionipronomi.get(parola))
        else:
            listaparolefinale.append(parola)
    return " ".join(listaparolefinale)

### funzione per la risposta
def risposta(frase):
    num=random.randint(1, 4)
    if num==1:
        return random.choice(dichiarazioni)
    else:
        return (random.choice(esplicazioni)+ sostpronomi(frase))
main()
