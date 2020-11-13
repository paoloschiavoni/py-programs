from selenium import webdriver
from selenium.webdriver.common.keys import Keys

PATH='C:\Program Files (x86)\chromedriver.exe'#il path di dove si trova chromedriver
driver=webdriver.Chrome(PATH)

#avrei potuto anche mettere così:
'''
from webdriver_manager.chrome import ChromeDriverManager
driver=webdriver.Chrome(ChromeDriverManager().install())
'''

driver.get('https://it.wikipedia.org/wiki/Pagina_principale')

'''#cliccare qualcosa
link=driver.find_element_by_xpath('//*[@id="n-recentchanges"]/a')
link.click()
'''


'''#cercare qualcosa sulla barra di ricerca
searchbox=driver.find_element_by_xpath('//*[@id="searchInput"]')

searchbox.send_keys("ciao")
searchbox.send_keys(Keys.ENTER)
'''

#NOTA BENE: in generale, posso scegliere se prendere l'elemento tramite xpath, id, title ecc...
#quanto faccio inspect posso o copiare l'xpath, il quale di solito c'è sempre, ma
