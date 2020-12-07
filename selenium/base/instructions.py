from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#i need these to wait whenever i reasearch for an elemnt to exist
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

PATH='C:\Program Files (x86)\chromedriver.exe'#il path di dove si trova chromedriver
driver=webdriver.Chrome(PATH)
driver.get('sito')

'''#avrei potuto anche mettere così:
from webdriver_manager.chrome import ChromeDriverManager
driver=webdriver.Chrome(ChromeDriverManager().install())






#per aspettare che il nostro elemento esista (explicit wait)
driver.get('https://it.wikipedia.org/wiki/Pagina_principale')
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "myDynamicElement"))
    )
finally:
    driver.quit()





#aspettare (implicit wait)
driver.implicitly_wait(5)




#cliccare qualcosa
link=driver.find_element_by_xpath('//*[@id="n-recentchanges"]/a')
link.click()



#cercare qualcosa sulla barra di ricerca
searchbox=driver.find_element_by_xpath('//*[@id="searchInput"]')

searchbox.send_keys("ciao")
searchbox.send_keys(Keys.ENTER)



#actions
from selenium.common.webdriver.action_chains import ActionChains
actions=ActionChains(driver)
action.click()#la mette in coda
action.perform()



#selezionare più elementi:
usare driver.find_element_by_xpath(xpath/qualsiasi altra cosa)
restituisce una lista
'''



#NOTA BENE: in generale, posso scegliere se prendere l'elemento tramite xpath, id, title ecc...
#quanto faccio inspect posso o copiare l'xpath, il quale di solito c'è sempre
'https://selenium-python.readthedocs.io/api.html#module-selenium.webdriver.common.action_chains'
