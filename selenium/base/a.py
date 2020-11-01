from selenium import webdriver
from selenium.webdriver.common.keys import Keys

PATH='C:\Program Files (x86)\chromedriver.exe'#il path di dove si trova chromedriver
driver=webdriver.Chrome(PATH)

#avrei potuto anche mettere così:
'''
from webdriver_manager.chrome import ChromeDriverManager
driver=webdriver.Chrome(ChromeDriverManager().install())
'''

driver.get('https://it.wikisource.org/wiki/Pagina_principale')

searchbox=driver.find_element_by_xpath('//*[@id="searchInput"]')
poesia=str(input('titolo della poesia: '))
searchbox.send_keys(poesia)
searchbox.send_keys(Keys.ENTER)
