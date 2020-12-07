'''

un programma che analizza i prezzi di un determinato prodotto su amazon
Schiavoni Paolo, 07/12/2020

'''

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PATH='C:\Program Files (x86)\chromedriver.exe'
driver=webdriver.Chrome(PATH)


while 1:
    driver.get('https://www.amazon.it/')
    searchbox=driver.find_element_by_xpath('//*[@id="twotabsearchtextbox"]')
    driver.implicitly_wait(3)
    nomeprodotto=str(input('\nnome del prodotto: '))

    searchbox.send_keys(nomeprodotto)
    searchbox.send_keys(Keys.ENTER)

    lista=[]

    for el in driver.find_elements_by_class_name('a-price-whole'):
        el=el.text.replace('.', '')
        el=el.replace(' ', '')
        if el!='':
            el=float(el.replace(',', '.'))
            if el>1:
                lista.append(el)
    lista.sort()
    lista.pop(0)
    lista.pop(-1)


    max=0
    min=10000000000

    media=0
    for el in lista:
        if el>max:
            max=el
        if el<min:
            min=el
        media+=el
    media/=len(lista)

    mediana=0
    if len(lista)%2 !=0:#elementi dispari: trovo quello centrale
        mediana=lista[int((len(lista)-1)/2)]
    elif len(lista)%2==0:
        a=lista[int(len(lista)/2)]
        b=lista[int((len(lista)-2)/2)]
        mediana=(a+b)/2

    moda=0
    frequenza=0
    for i in lista:
        frequenzatmp=-1
        for j in lista:
            if j-0.7<i and j+0.7>i:
                frequenzatmp+=1
        if frequenzatmp>frequenza:
            moda=i
            frequenza=frequenzatmp


    print('\nnumero di prodotti:', len(lista), '\npiù costoso:€'+str(max)\
    , '\npiù economico: €'+str(min), '\nmedia dei prezzi: €'+str(media), \
    '\nmediana dei prezzi: €'+str(mediana))
    if frequenza>1:
        print('moda: €'+str(moda), '('+str(frequenza)+' prodotti)')
