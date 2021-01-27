print('inserire il numero decimale di cui si vuole \
trovare la frazione.\nusare il punto, non la virgola\
\nse il numero è periodico, inserire fino a 10 cifre decimali')
def find_fraction():
    try:
        num=input('\nnum: ')
        num=round(float(num), 8)
        i=0

        while True:
            i+=1
            for j in range(abs(round(i/num)-1), round(i/num)+1):
                if j!=0:
                    if str(round((i/j), 8))==str(float(num)):
                        print(str(i)+'/'+str(j))
                        return True
    except:
        print('si è verificato un errore, riprovare')
while 1:
    find_fraction()
